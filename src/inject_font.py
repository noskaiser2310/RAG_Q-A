import json
import os
import re
from pathlib import Path
from tqdm import tqdm


VIETNAMESE_STOPWORDS = set([
    'và', 'là', 'có', 'của', 'trong', 'được', 'cho', 'với', 'tại', 'ra', 'khi', 'thì',
    'mà', 'để', 'một', 'các', 'như', 'không', 'làm', 'đã', 'về', 'này', 'đó',
    'từ', 'cũng', 'trên', 'qua', 'hay', 'lại', 'đến', 'chỉ', 'còn', 'phải',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'hình', 'bảng', 'chương', 'phần', 'mục'
])


def filter_noisy_styles(styled_items: list[dict], min_len: int = 2) -> list[dict]:
    filtered = []
    for item in styled_items:
        text = item.get("text", "").strip()
        
        if len(text) < min_len:
            continue
            
        if re.fullmatch(r'[\\W_]+', text):
            continue
            
        if text.lower() in VIETNAMESE_STOPWORDS:
            continue
            
        filtered.append(item)
        
    return filtered


def inject_styles_smart(markdown_text: str, styled_items: list[dict]) -> str:
    if not styled_items:
        return markdown_text

    filtered_items = filter_noisy_styles(styled_items)
    
    if not filtered_items:
        return markdown_text

    sorted_items = sorted(filtered_items, key=lambda x: len(x.get('text', '')), reverse=True)

    for item in sorted_items:
        text_to_style = item.get("text")
        style = item.get("style")

        if style in ['bold', 'bold_italic']:
            styled_text = f"**{text_to_style}**"
        elif style == 'italic':
            styled_text = f"_{text_to_style}_"
        else:
            continue

        pattern = re.compile(
            r"(?<!\\w)(?<![*_])" +
            re.escape(text_to_style) +
            r"(?![_*])(?!\\w)"
        )
        
        markdown_text = pattern.sub(styled_text, markdown_text)
            
    return markdown_text


def clean_header_formatting(markdown_text: str) -> str:
    """
    Remove bold (**text**), italic (_text_) từ các dòng header.
    Multi-pass để ensure clean hoàn toàn.
    """
    lines = markdown_text.split('\\n')
    cleaned_lines = []
    
    for line in lines:
        # Kiểm tra nếu dòng là header (bắt đầu bằng # sau khoảng trắng tùy chọn)
        if re.match(r'^####+\\s', line):
            # Multi-pass cleaning - lặp cho đến khi hết formatting
            max_iterations = 5
            iteration = 0
            
            while ('**' in line or '_' in line) and iteration < max_iterations:
                # Remove bold: **text** -> text (không match * bên trong)
                line = re.sub(r'\\*\\*([^*]*)\\*\\*', r'\\1', line)
                # Remove italic: _text_ -> text (không match _ bên trong)
                line = re.sub(r'_([^_]*)_', r'\\1', line)
                iteration += 1
            
            # Fallback: nếu vẫn còn dấu (edge case), xóa hết
            if '**' in line or '_' in line:
                line = line.replace('**', '').replace('_', '')
        
        cleaned_lines.append(line)
    
    return '\\n'.join(cleaned_lines)


def batch_inject_styles(
    source_mineru_dir: Path,
    font_context_dir: Path,
    replace_original: bool = True
):
    """
    Duyệt các folder con trong source_mineru_dir, apply styling từ font context JSON.
    
    Tham số:
    - source_mineru_dir: thư mục chứa Public_001/, Public_002/, ...
    - font_context_dir: thư mục chứa *_font_context.json
    - replace_original: True -> thay thế main.md gốc
    """
    print(f"Source directory: {source_mineru_dir.resolve()}")
    print(f"Font context directory: {font_context_dir.resolve()}")
    print(f"Replace original: {replace_original}")
    
    subdirs = [d for d in source_mineru_dir.iterdir() if d.is_dir()]
    if not subdirs:
        print(f"Warning: No subdirectories found in '{source_mineru_dir}'")
        return

    print(f"Found {len(subdirs)} subdirectories to process.\\n")

    for subdir in tqdm(subdirs, desc="Processing"):
        folder_name = subdir.name
        markdown_path = subdir / "main.md"
        
        if not markdown_path.exists():
            print(f"  Warning: main.md not found in '{folder_name}'")
            continue

        font_json_path = font_context_dir / f"{folder_name}_font_context.json"
        if not font_json_path.exists():
            print(f"  Warning: Font context JSON not found for '{folder_name}'")
            continue

        try:
            markdown_text = markdown_path.read_text(encoding="utf-8")
            with open(font_json_path, 'r', encoding='utf-8') as f:
                styled_items = json.load(f)
        except Exception as e:
            print(f"  Error reading files for '{folder_name}': {e}")
            continue

        # Bước 1: Inject styles
        if styled_items:
            final_markdown = inject_styles_smart(markdown_text, styled_items)
        else:
            final_markdown = markdown_text

        # Bước 2: Clean header formatting (cuối cùng) - multi-pass
        final_markdown = clean_header_formatting(final_markdown)

        try:
            markdown_path.write_text(final_markdown, encoding="utf-8")
        except Exception as e:
            print(f"  Error writing output for '{folder_name}': {e}")

    print(f"\\n✓ Complete. Files updated in place.")


if __name__ == "__main__":
    SOURCE_MINERU_DIR = Path(r"working\\output_mineru_test")
    FONT_CONTEXT_DIR = Path(r"working\\Font_CrossBlock_Context_Filtered")

    if not SOURCE_MINERU_DIR.is_dir():
        print(f"Error: Source directory not found at '{SOURCE_MINERU_DIR}'")
    elif not FONT_CONTEXT_DIR.is_dir():
        print(f"Error: Font context directory not found at '{FONT_CONTEXT_DIR}'")
    else:
        batch_inject_styles(
            source_mineru_dir=SOURCE_MINERU_DIR,
            font_context_dir=FONT_CONTEXT_DIR,
            replace_original=True
        )