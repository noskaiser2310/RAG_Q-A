import pymupdf
import json
import os
from pathlib import Path
from tqdm import tqdm
import itertools

def _get_style(span: dict) -> str:
    """Helper function to determine the style of a text span."""
    flags = span.get("flags", 0)
    font_name = span.get("font", "").lower()
    
    is_bold = (flags & 2**4) != 0
    is_italic = (flags & 2**1) != 0 or "italic" in font_name
    
    if is_bold and is_italic: return 'bold_italic'
    if is_bold: return 'bold'
    if is_italic: return 'italic'
    return 'normal'

def _union_bbox(bboxes: list[tuple]) -> tuple | None:
    """Creates a bounding box that envelops a list of bounding boxes."""
    if not bboxes: return None
    x0 = min(b[0] for b in bboxes)
    y0 = min(b[1] for b in bboxes)
    x1 = max(b[2] for b in bboxes)
    y1 = max(b[3] for b in bboxes)
    return (x0, y0, x1, y1)

def extract_styled_text_with_cross_block_merging(pdf_path: str | Path) -> list[dict]:
    """
    Extracts styled text, intelligently merging consecutive styled content
    even across multiple lines and adjacent blocks.
    """
    all_styled_items = []

    try:
        doc = pymupdf.open(pdf_path)
    except Exception as e:
        print(f"Error: Could not open PDF '{pdf_path.name}': {e}")
        return []

    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict").get("blocks", [])
        for block_num, block in enumerate(blocks):
            if block.get("type") == 0:
                all_spans_in_block = [span for line in block.get("lines", []) for span in line.get("spans", [])]
                if not all_spans_in_block: continue

                merged_spans_in_block = []
                for style, group in itertools.groupby(all_spans_in_block, key=_get_style):
                    group_spans = list(group)
                    merged_text = " ".join(s["text"].strip() for s in group_spans if s["text"].strip())
                    merged_bbox = _union_bbox([s["bbox"] for s in group_spans])
                    
                    if merged_text:
                        merged_spans_in_block.append({"text": merged_text, "style": style, "bbox": merged_bbox})
                
                for i, span in enumerate(merged_spans_in_block):
                    if span["style"] != 'normal':
                        prefix = merged_spans_in_block[i-1]["text"].rstrip() if i > 0 and merged_spans_in_block[i-1]["style"] == 'normal' else ""
                        suffix = merged_spans_in_block[i+1]["text"].lstrip() if i < len(merged_spans_in_block) - 1 and merged_spans_in_block[i+1]["style"] == 'normal' else ""
                        
                        all_styled_items.append({
                            "prefix": prefix,
                            "text": span["text"],
                            "suffix": suffix,
                            "style": span["style"],
                            "page_num": page_num,
                            "block_num": block_num,
                            "bbox": span["bbox"]
                        })
    doc.close()

    if not all_styled_items:
        return []

    final_results = []
    i = 0
    while i < len(all_styled_items):
        current_item = all_styled_items[i]
        j = i + 1
        while j < len(all_styled_items):
            next_item = all_styled_items[j]
            if (current_item["page_num"] == next_item["page_num"] and
                current_item["style"] == next_item["style"] and
                current_item["block_num"] + 1 == next_item["block_num"] and
                not current_item["prefix"] and not current_item["suffix"] and
                not next_item["prefix"]):
                
                current_item["text"] += " " + next_item["text"]
                current_item["bbox"] = _union_bbox([current_item["bbox"], next_item["bbox"]])
                current_item["block_num"] = next_item["block_num"]
                current_item["suffix"] = next_item["suffix"]
                j += 1
            else:
                break
        final_results.append(current_item)
        i = j
        
    return final_results

def filter_redundant_bold_headings(
    styled_items: list[dict],
    headings_json_path: Path,
    log_file_path: Path
) -> list[dict]:
    """
    Filters out styled items that are 'bold' and whose text matches a heading
    found in the provided headings JSON file. Logs the removed items.
    """
    if not headings_json_path.exists():
        # If no heading file, return the original list without changes.
        return styled_items

    try:
        with open(headings_json_path, 'r', encoding='utf-8') as f:
            headings_data = json.load(f)
        # Create a set of heading texts for efficient lookup
        heading_texts = {item['text'].strip() for item in headings_data}
    except Exception as e:
        print(f"  Warning: Could not read or parse '{headings_json_path.name}': {e}. Skipping filter.")
        return styled_items

    filtered_items = []
    removed_items_log = []

    for item in styled_items:
        # Condition to remove: style is 'bold' AND text matches a heading
        is_redundant = (
            item['style'] == 'bold' and
            item['text'].strip() in heading_texts
        )

        if is_redundant:
            removed_items_log.append(item)
        else:
            filtered_items.append(item)
            
    # Write removed items to a log file if any were removed
    if removed_items_log:
        try:
            with open(log_file_path, 'a', encoding='utf-8') as log_f:
                log_f.write(f"--- Items removed from {headings_json_path.stem.replace('_headings_detailed', '')} ---\n")
                for removed in removed_items_log:
                    log_f.write(json.dumps(removed, ensure_ascii=False) + '\n')
                log_f.write("\n")
        except Exception as e:
            print(f"  Warning: Could not write to log file '{log_file_path.name}': {e}")

    return filtered_items

def batch_process_pdfs(
    input_dir: Path,
    output_parent_dir: Path,
    headings_data_dir: Path
):
    """
    Main batch processing function, now with integrated filtering.
    """
    output_dir = output_parent_dir / "Font_CrossBlock_Context_Filtered"
    log_dir = output_parent_dir / "logs"
    print(f"Initializing output directory: {output_dir.resolve()}")
    print(f"Log files will be saved in: {log_dir.resolve()}")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    # Path for the consolidated log file
    log_file_path = log_dir / "removed_bold_items.log"
    # Clear the log file at the beginning of a new run
    if log_file_path.exists():
        log_file_path.unlink()

    pdf_files = list(input_dir.glob("*.[pP][dD][fF]"))
    
    if not pdf_files:
        print(f"Warning: No PDF files found in '{input_dir}'. Aborting.")
        return

    print(f"Found {len(pdf_files)} PDF files to process.")

    for pdf_path in tqdm(pdf_files, desc="Processing PDFs (Filter & Save)"):
        pdf_stem = pdf_path.stem

        # Step 1: Extract styled text as before
        contextual_data = extract_styled_text_with_cross_block_merging(pdf_path)

        # Step 2: Define path to the corresponding headings JSON
        headings_json_path = headings_data_dir / pdf_stem / "headings_detailed.json"

        # Step 3: Filter the extracted data
        filtered_data = filter_redundant_bold_headings(
            styled_items=contextual_data,
            headings_json_path=headings_json_path,
            log_file_path=log_file_path
        )
        
        # Step 4: Save the filtered data
        output_filename = f"{pdf_stem}_font_context.json"
        output_json_path = output_dir / output_filename

        try:
            with open(output_json_path, "w", encoding="utf-8") as f:
                json.dump(filtered_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error: Failed to save JSON for '{pdf_stem}': {e}")
            
    print(f"\n✓ Processing complete. {len(pdf_files)} files handled.")
    print(f"Filtered results saved in: '{output_dir.resolve()}'")
    print(f"Details of removed items logged in: '{log_file_path.resolve()}'")


if __name__ == "__main__":
    # --- Configuration ---
    INPUT_PDF_DIR = Path(r"working/cleaned_pdfs_test") 
    OUTPUT_PARENT_DIR = Path("working")
    
    HEADINGS_DATA_DIR = Path(r"working/output_markdown_detect_test")

    # --- Execution ---
    if not INPUT_PDF_DIR.is_dir():
        print(f"Error: Input PDF directory '{INPUT_PDF_DIR}' not found.")
    elif not HEADINGS_DATA_DIR.is_dir():
        print(f"Error: Headings data directory '{HEADINGS_DATA_DIR}' not found.")
    else:
        batch_process_pdfs(
            input_dir=INPUT_PDF_DIR, 
            output_parent_dir=OUTPUT_PARENT_DIR,
            headings_data_dir=HEADINGS_DATA_DIR
        )