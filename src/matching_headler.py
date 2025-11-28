import json
import re
from pathlib import Path

# --- NORMALIZATION AND SPACING HELPERS (SHARED) ---

def normalize_heading_text(text):
    """
    A robust function to normalize heading text from any source (MD or JSON).
    """
    if not isinstance(text, str):
        return ""
    normalized = text.strip()
    normalized = re.sub(r'^(?P<marker>[\*_]{1,2})\s*(.*?)\s*(?P=marker)$', r'\2', normalized)
    normalized = re.sub(r'^#+\s*', '', normalized)
    normalized = re.sub(r'^\d+(\.\d+)*[\.\s]*', '', normalized)
    normalized = normalized.lstrip('.- ')
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    return normalized

def ensure_heading_spacing(md_content):
    """
    Ensures every markdown heading is surrounded by exactly one blank line.
    """
    content_with_extra_newlines = re.sub(
        r'^(#+ .*)$',
        r'\n\n\1\n\n',
        md_content,
        flags=re.MULTILINE
    )
    content_with_proper_spacing = re.sub(r'\n{3,}', '\n\n', content_with_extra_newlines)
    final_content = content_with_proper_spacing.strip() + '\n'
    return final_content

# --- CORE CONVERSION LOGIC ---

def convert_headings_to_markdown(md_content, headings_metadata):
    """
    Processes headings in a two-step pipeline:
    1. Exact Match: Converts lines that are perfect matches for headings.
    2. Prefix Match: Processes remaining lines to find and split merged headings.
    """
    lines = md_content.split('\n')
    
    # --- DATA PREPARATION ---
    heading_map = {}
    for h in headings_metadata:
        normalized = normalize_heading_text(h['text'])
        if normalized and normalized not in heading_map:
            heading_map[normalized] = {'level': h['level'], 'original': normalize_heading_text(h['text'])}

    # --- PIPELINE STATE ---
    processed_lines = [None] * len(lines) # Use a list to store results
    matched_headings = set()
    skipped_in_table = []
    converted_count = 0

    # --- STEP 1: EXACT MATCH PASS ---
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if not stripped_line:
            processed_lines[i] = line
            continue

        # Skip tables
        is_in_table = '|' in stripped_line or '<td>' in stripped_line.lower() or '<th>' in stripped_line.lower()
        if is_in_table:
            processed_lines[i] = line
            # Check if it could have been a heading, for reporting
            normalized_line = normalize_heading_text(stripped_line)
            if normalized_line in heading_map and normalized_line not in matched_headings:
                 skipped_in_table.append(normalized_line)
            continue

        normalized_line = normalize_heading_text(stripped_line)
        
        if normalized_line in heading_map and normalized_line not in matched_headings:
            metadata = heading_map[normalized_line]
            level = metadata['level']
            original_clean_text = metadata['original']
            new_heading_line = f"{'#' * level} {original_clean_text}"
            
            processed_lines[i] = new_heading_line
            matched_headings.add(normalized_line)
            converted_count += 1

    # --- STEP 2: PREFIX MATCH PASS (ON REMAINING LINES) ---
    sorted_headings = sorted(
        [h for h in heading_map if h not in matched_headings], 
        key=len, 
        reverse=True
    )

    for i, line in enumerate(lines):
        # Skip if already processed in step 1 or is a table
        if processed_lines[i] is not None:
            continue

        stripped_line = line.strip()
        if not stripped_line:
            processed_lines[i] = line
            continue

        found_match = False
        for h_key in sorted_headings:
            normalized_line_lower = normalize_heading_text(stripped_line).lower()
            h_key_lower = h_key.lower()

            if normalized_line_lower.startswith(h_key_lower):
                original_h_text = heading_map[h_key]['original']
                match_obj = re.search(re.escape(original_h_text), stripped_line, re.IGNORECASE)
                
                if match_obj:
                    match_end_pos = match_obj.end()
                    is_valid_split = False
                    
                    if match_end_pos == len(stripped_line):
                        is_valid_split = True
                    elif stripped_line[match_end_pos].isspace():
                        first_content_char_index = match_end_pos + 1
                        while first_content_char_index < len(stripped_line) and stripped_line[first_content_char_index].isspace():
                            first_content_char_index += 1
                        
                        if first_content_char_index < len(stripped_line):
                            first_content_char = stripped_line[first_content_char_index]
                            if first_content_char.isupper() or not first_content_char.isalpha():
                                is_valid_split = True
                        else:
                            is_valid_split = True

                    if is_valid_split:
                        metadata = heading_map[h_key]
                        level = metadata['level']
                        heading_part = match_obj.group(0)
                        content_part = stripped_line[match_end_pos:].strip()
                        
                        new_heading_line = f"{'#' * level} {heading_part.strip()}"
                        
                        result = new_heading_line
                        if content_part:
                            result += f"\n{content_part}"
                        
                        processed_lines[i] = result
                        matched_headings.add(h_key)
                        converted_count += 1
                        found_match = True
                        break
        
        if not found_match:
            processed_lines[i] = line

    # --- FINAL ASSEMBLY AND REPORTING ---
    final_content = '\n'.join(processed_lines)
    final_content_with_spacing = ensure_heading_spacing(final_content)

    not_found = [h for h in heading_map.keys() if h not in matched_headings and h not in skipped_in_table]
    report = {
        'total_headings': len(heading_map),
        'converted': converted_count,
        'skipped_in_table': list(set(skipped_in_table)),
        'not_found': not_found,
        'matched_headings': list(matched_headings)
    }

    return final_content_with_spacing, report

# --- Các hàm process_single_document và batch_process_documents không thay đổi ---
# (Giữ nguyên các hàm này như trong các phiên bản trước)
def process_single_document(json_path, md_path, output_path=None):
    """Process single document"""
    if output_path is None:
        output_path = md_path

    with open(json_path, 'r', encoding='utf-8') as f:
        headings_metadata = json.load(f)

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    converted_md, report = convert_headings_to_markdown(md_content, headings_metadata)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted_md)

    return report

def batch_process_documents(base_json_dir, base_md_dir, output_base_dir=None, verbose=True):
    """Batch process multiple Public_XXX folders"""
    base_json_path = Path(base_json_dir)
    base_md_path = Path(base_md_dir)

    if output_base_dir:
        output_base = Path(output_base_dir)
        output_base.mkdir(parents=True, exist_ok=True)
    else:
        output_base = base_md_path

    public_folders = sorted([d for d in base_json_path.iterdir()
                            if d.is_dir() and d.name.startswith('Public_')])

    if verbose:
        print(f"Found {len(public_folders)} Public_XXX folders")
        print("=" * 80)

    all_reports = {}

    for public_folder in public_folders:
        folder_name = public_folder.name

        if verbose:
            print(f"\n📁 Processing {folder_name}...")

        json_file = public_folder / 'headings_detailed.json'
        md_file = base_md_path / folder_name / 'main.md'
        output_file = output_base / folder_name / 'main.md'

        if not json_file.exists():
            if verbose:
                print(f"  ⚠️  JSON not found: {json_file}")
            all_reports[folder_name] = {'error': 'JSON not found'}
            continue

        if not md_file.exists():
            if verbose:
                print(f"  ⚠️  MD not found: {md_file}")
            all_reports[folder_name] = {'error': 'MD not found'}
            continue

        output_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            report = process_single_document(json_file, md_file, output_file)
            all_reports[folder_name] = report

            if verbose:
                print(f"  ✓ Converted {report['converted']}/{report['total_headings']} headings")
                if report.get('skipped_in_table'):
                    print(f"  ↪️  Skipped in table: {len(report['skipped_in_table'])} headings")
                if report['not_found']:
                    print(f"  ⚠️  Not found: {report['not_found']}")

        except Exception as e:
            if verbose:
                print(f"  ❌ Error: {e}")
            all_reports[folder_name] = {'error': str(e)}

    if verbose:
        print("\n" * 2 + "=" * 80)
        print("BATCH PROCESSING SUMMARY")
        print("=" * 80)

        success_count = sum(1 for r in all_reports.values() if 'error' not in r)
        total_converted = sum(r.get('converted', 0) for r in all_reports.values())
        total_skipped = sum(len(r.get('skipped_in_table', [])) for r in all_reports.values())
        total_headings = sum(r.get('total_headings', 0) for r in all_reports.values())

        print(f"✓ Successfully processed: {success_count}/{len(all_reports)} documents")
        print(f"✓ Total headings converted: {total_converted}/{total_headings}")
        print(f"↪️  Total headings skipped in tables: {total_skipped}")

        failures = {k: v for k, v in all_reports.items() if 'error' in v}
        if failures:
            print(f"\n❌ Failed documents:")
            for doc, error in failures.items():
                print(f"  - {doc}: {error['error']}")

    return all_reports


if __name__ == '__main__':
    # CONFIGURATION
    BASE_JSON_DIR = r'working/output_markdown_detect_test'
    BASE_MD_DIR = r'working/output_mineru_test'
    OUTPUT_DIR = None

    # RUN
    reports = batch_process_documents(
        base_json_dir=BASE_JSON_DIR,
        base_md_dir=BASE_MD_DIR,
        output_base_dir=OUTPUT_DIR,
        verbose=True
    )

    # Save report to JSON
    output_report_path = Path(BASE_MD_DIR) / 'conversion_report.json'
    with open(output_report_path, 'w', encoding='utf-8') as f:
        json.dump(reports, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Detailed report saved to: {output_report_path}")