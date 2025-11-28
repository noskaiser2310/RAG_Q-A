"""
RAG-based QA System - Merged Source Code
Generated automatically from multiple modules in src/
"""

# ============================================================
# add_healder.py
# ============================================================

import os
import glob

def add_public_header_to_all_folders(root_directory):
    """
    Xử lý tất cả các thư mục Public_XXX trong thư mục gốc
    """
    # Tìm tất cả thư mục con có định dạng Public_XXX
    public_folders = []
    for item in os.listdir(root_directory):
        item_path = os.path.join(root_directory, item)
        if os.path.isdir(item_path) and item.startswith('Public_'):
            public_folders.append(item_path)
    
    if not public_folders:
        print(f"Không tìm thấy thư mục Public_XXX nào trong '{root_directory}'")
        return
    
    # Xử lý từng thư mục Public_XXX
    for folder_path in public_folders:
        print(f"\nĐang xử lý thư mục: {os.path.basename(folder_path)}")
        add_public_header_to_markdown_files(folder_path)

def add_public_header_to_markdown_files(directory_path):
    """
    Thêm # Public_XXX vào đầu mỗi file markdown trong thư mục
    XXX được lấy từ tên thư mục Public_XXX
    """
    # Lấy tên thư mục
    folder_name = os.path.basename(directory_path.rstrip('/\\'))
    
    # Tạo header từ tên thư mục
    header = f"# {folder_name}\n\n"
    
    # Tìm tất cả file markdown trong thư mục
    markdown_files = glob.glob(os.path.join(directory_path, "*.md")) + \
                    glob.glob(os.path.join(directory_path, "*.markdown"))
    
    if not markdown_files:
        print(f"  Không tìm thấy file markdown nào")
        return
    
    # Xử lý từng file markdown
    for file_path in markdown_files:
        try:
            # Đọc nội dung file hiện tại
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Kiểm tra xem file đã có header Public_XXX chưa
            if content.startswith(f"# {folder_name}"):
                print(f"  File '{os.path.basename(file_path)}' đã có header, bỏ qua")
                continue
            
            # Xóa header cũ nếu nó là # Public_XXX
            lines = content.split('\n')
            if lines and lines[0].startswith('# Public_'):
                content = '\n'.join(lines[1:])
            
            # Thêm header mới vào đầu file
            new_content = header + content
            
            # Ghi nội dung mới vào file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            print(f"  ✓ Đã thêm header vào '{os.path.basename(file_path)}'")
            
        except Exception as e:
            print(f"  ✗ Lỗi với file '{os.path.basename(file_path)}': {str(e)}")

def main():
    # Thư mục gốc chứa các thư mục Public_XXX
    root_directory = r'working\output_mineru_test'
    
    # Kiểm tra thư mục gốc có tồn tại không
    if not os.path.exists(root_directory):
        print(f"Thư mục '{root_directory}' không tồn tại!")
        return
    
    # Thực hiện xử lý tất cả thư mục
    add_public_header_to_all_folders(root_directory)
    print("\nHoàn thành xử lý tất cả file!")

if __name__ == "__main__":
    main()

# ============================================================
# clean_data_mineru.py
# ============================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import os
import sys
import json
import shutil
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
from PIL import Image


# =========================
# Configuration
# =========================
INPUT_ROOT  = Path(r"working\output_mineru_raw_test")
OUTPUT_ROOT = Path(r"working\output_mineru_test")
CACHE_FILE  = INPUT_ROOT / "_processed_cache.json"
ENCODING    = "utf-8"

EMPTY_CELL_RATIO_THRESHOLD = 0.70
MIN_TABLE_TEXT_LENGTH = 20

# Image filtering rules: Xóa ảnh có width >= 1200 AND height trong [140, 160]
BANNED_IMAGE_MIN_WIDTH = 100000
BANNED_IMAGE_MIN_HEIGHT = 12000
BANNED_IMAGE_MAX_HEIGHT = 18000


# =========================
# Utils
# =========================


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode(ENCODING, errors="ignore")).hexdigest()

# =========================
# Cleaning Rules
# =========================


# =========================
# Runner
# =========================

def list_md_files(input_root: Path) -> List[Tuple[str, Path]]:
    pairs: List[Tuple[str, Path]] = []
    for d in input_root.iterdir():
        if not d.is_dir():
            continue
        if not is_public_dir(d.name):
            continue
        for md_path in d.rglob("*.md"):
            if md_path.is_file():
                pairs.append((d.name, md_path))
    return pairs

def load_cache() -> Dict[str, str]:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            return {}
    return {}


def save_cache(cache: Dict[str, str]) -> None:
    try:
        CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as e:
        print(f"[WARN] Cannot save cache: {e}", file=sys.stderr)


def is_public_dir(name: str) -> bool:
    return re.fullmatch(r"Public_\d{3}", name) is not None


def dir_to_title(dir_name: str) -> Optional[str]:
    m = re.fullmatch(r"Public(\d{3})", dir_name)
    return f"Public_{m.group(1)}" if m else None


def relpath_from(root: Path, path: Path) -> Path:
    return path.relative_to(root)


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def process_numbered_headings(content: str) -> str:
    lines = content.splitlines()
    processed_lines = []
    
    numbered_heading_pattern = re.compile(r'^(\s*)([1-8])\.\s+')
    
    for line in lines:
        stripped_line = line.lstrip()
        
        match = numbered_heading_pattern.match(line)
        if match:
            leading_spaces = match.group(1)  # Khoảng trắng đầu dòng
            number = match.group(2)          # Số (1-6)
            
            if not stripped_line.startswith('#'):
                processed_line = '\t' + line
                processed_lines.append(processed_line)
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def clean_dir_contents(p: Path) -> None:
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
        return
    
    for child in p.iterdir():
        try:
            if child.is_file() or child.is_symlink():
                child.unlink(missing_ok=True)
            elif child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
        except Exception as e:
            print(f"[WARN] Cannot remove {child}: {e}", file=sys.stderr)


def get_image_dimensions(img_path: Path) -> Optional[Tuple[int, int]]:
    try:
        with Image.open(img_path) as img:
            return img.size
    except Exception as e:
        print(f"[WARN] Cannot read image dimensions {img_path}: {e}", file=sys.stderr)
        return None


def is_banned_image(img_path: Path) -> bool:
    """
    Check if image should be filtered based on dimensions:
    - Width >= 1200 AND Height in [140, 160]
    Both conditions must be true to filter the image.
    """
    dims = get_image_dimensions(img_path)
    if dims is None:
        return False
    
    width, height = dims
    
    # Check both conditions
    width_condition = width >= BANNED_IMAGE_MIN_WIDTH
    height_condition = BANNED_IMAGE_MIN_HEIGHT <= height <= BANNED_IMAGE_MAX_HEIGHT
    
    return width_condition and height_condition


# =========================
# Image Processing
# =========================


_IMAGE_LINK_RE = re.compile(
    r"_?!\[[^\]]*]\(\s*(?P<path>(?:\.\/|\.\\)?images[\/\\][^) \t]+)(?:\s+\"[^\"]*\")?\s*\)_?",
    flags=re.I
)


def find_all_image_links(md_text: str) -> List[Tuple[str, str]]:
    results = []
    for m in _IMAGE_LINK_RE.finditer(md_text):
        full = m.group(0)
        path = m.group("path")
        path = path.replace("\\", "/")
        path = re.sub(r"^\./", "", path)
        if path.lower().startswith("images/"):
            results.append((full, path))
    return results


def filter_valid_images(src_md_dir: Path, image_links: List[Tuple[str, str]], verbose: bool = False) -> List[Tuple[str, str]]:
    valid = []
    for full_match, rel_path in image_links:
        img_path = src_md_dir / Path(rel_path)
        
        if not img_path.exists():
            if verbose:
                print(f"[SKIP] Image not found: {img_path}", file=sys.stderr)
            continue
        
        if is_banned_image(img_path):
            if verbose:
                dims = get_image_dimensions(img_path)
                print(f"[FILTER] Banned image (W×H: {dims[0]}×{dims[1]}): {img_path.name}", file=sys.stderr)
            continue
        
        valid.append((full_match, rel_path))
    
    return valid


def replace_images_with_placeholders(md_text: str, src_md_dir: Path, verbose: bool = False) -> Tuple[str, List[str]]:
    """
    Replace ![...](images/...) or _![...](images/...)_ with |<image_n>| placeholders.
    This must run BEFORE clean_markdown_pipeline.
    """
    all_links = find_all_image_links(md_text)
    valid_links = filter_valid_images(src_md_dir, all_links, verbose=verbose)
    
    valid_paths = [path for _, path in valid_links]
    
    result = md_text
    for idx, (full_match, rel_path) in enumerate(valid_links, start=1):
        placeholder = f"|<image_{idx}>|"
        result = result.replace(full_match, placeholder, 1)
    
    return result, valid_paths


def copy_and_rename_images(src_md_dir: Path, dst_md_dir: Path, valid_image_paths: List[str]) -> None:
    dst_images_root = dst_md_dir / "images"
    clean_dir_contents(dst_images_root)
    
    if not valid_image_paths:
        ensure_dir(dst_images_root)
        return
    
    ensure_dir(dst_images_root)
    
    for idx, rel_path in enumerate(valid_image_paths, start=1):
        src = src_md_dir / Path(rel_path)
        ext = src.suffix
        dst = dst_images_root / f"image_{idx}{ext}"
        
        if src.exists() and src.is_file():
            try:
                shutil.copy2(src, dst)
            except Exception as e:
                print(f"[WARN] Cannot copy image {src} → {dst}: {e}", file=sys.stderr)
        else:
            print(f"[WARN] Missing image: {src}", file=sys.stderr)


# =========================
# Cleaning Rules
# =========================


def is_near_empty_table(table_html: str) -> bool:
    all_cells = re.findall(r"<td[^>]*>(.*?)</td>", table_html, re.I | re.DOTALL)
    if not all_cells:
        return True
    
    empty_count = sum(1 for cell in all_cells if not cell.strip())
    empty_ratio = empty_count / len(all_cells)
    
    text_content = re.sub(r"<[^>]+>", "", table_html)
    text_content = re.sub(r"\s+", " ", text_content).strip()
    text_length = len(text_content)
    
    is_empty = (empty_ratio >= EMPTY_CELL_RATIO_THRESHOLD) or (text_length < MIN_TABLE_TEXT_LENGTH)
    
    return is_empty



def italicize_preface_before_first_numbered_heading(content: str) -> str:
    lines = content.splitlines()
    numbered = re.compile(r"^\s*(?:#*\s*)?\d+(?:\.\d+)*[.)]?\s+\S")
    first_idx = next((i for i, ln in enumerate(lines) if numbered.match(ln)), None)
    if first_idx is None:
        return content
    prefix = "\n".join(lines[:first_idx]).strip("\n")
    suffix = "\n".join(lines[first_idx:])
    paras = [p.strip() for p in re.split(r"\n\s*\n", prefix) if p.strip()]
    
    def should_italicize(para: str) -> bool:
        if para.startswith("_") and para.endswith("_"):
            return False
        if re.match(r"^\|<image_\d+>\|$", para.strip()):
            return False
        return True
    
    paras = [f"_{p}_" if should_italicize(p) else p for p in paras]
    new_prefix = "\n\n".join(paras)
    if new_prefix:
        return new_prefix + "\n\n" + suffix.lstrip("\n")
    return suffix


def rewrite_numbered_headings(content: str) -> str:
    lines = content.splitlines()
    
    # Pattern 1: Markdown header có số: # 1. Text
    markdown_with_num = re.compile(r"^(#+)\s*(\d+(?:\.\d+)*)(?:[.)])?\s+(.+?)\s*$")
    
    converted: List[str] = []
    
    for line in lines:
        # Case 1: # 1. Sợi chỉ thường --> # Sợi chỉ thường (bỏ số)
        m = markdown_with_num.match(line)
        if m:
            hashes = m.group(1)
            text = m.group(3).strip()
            converted.append(f"{hashes} {text}")
            continue
        
        # Case 2: Xử lý các dạng số đa cấp (1.1, 1.2, v.v.)
        # Pattern mới: bắt đầu bằng số, có thể có dấu chấm và số tiếp theo
        numbered_line = re.match(r"^\s*(\d+(?:\.\d+)*)[.)]?\s*(.+?)\s*$", line)
        if numbered_line:
            number_part = numbered_line.group(1)
            text = numbered_line.group(2).strip()
            
            # Đếm số chữ số (phần tử) trong số
            digits = re.findall(r'\d+', number_part)
            depth = len(digits)
            
            if depth == 1:
                # Single-level: thêm 2 spaces
                converted.append("  " + line)
            else:
                # Multi-level: chuyển thành heading
                converted.append("#" * depth + " " + text)
            continue
        
        converted.append(line)
    
    # Xử lý duplicate headings
    def norm(s: str) -> str:
        if s.startswith("#"):
            s = s.lstrip("#").strip()
        return re.sub(r"[\W_]+", "", s.lower())

    out: List[str] = []
    i = 0
    while i < len(converted):
        cur = converted[i]
        if i + 1 < len(converted) and cur.startswith("#") and converted[i + 1].startswith("#"):
            if norm(cur) == norm(converted[i + 1]):
                out.append(cur)
                i += 2
                continue
        out.append(cur)
        i += 1
    
    return "\n".join(out)


def normalize_references_block(content: str) -> str:
    pat = re.compile(r"^#{1,6}\s*TÀI\s*LIỆU\s*THAM\s*KHẢO\s*$", re.I | re.M)
    m = pat.search(content)
    if not m:
        return content
    start = m.end()
    nxt = re.search(r"^#{1,6}\s+", content[start:], re.M)
    end = start + (nxt.start() if nxt else len(content[start:]))
    block = content[start:end]
    block = re.sub(r"(?<!^)\s*\[(\d+)\]\s*", r"\n  \1. ", block)
    block = re.sub(r"^\s*\[(\d+)\]\s*", r"  \1. ", block, flags=re.M)
    block = re.sub(r"\n{3,}", "\n\n", block.strip())
    return content[:start] + block + content[end:]


import re

def convert_bullets(content: str) -> str:
    """
    Chuyển đổi nhiều loại bullets về format chuẩn với indentation khác nhau
    - "▪" --> "*"
    - "\no" --> "\n\t*"
    - " o " --> "\n\t*"
    - "•" --> "\t*"
    - Letter bullets (a), b), c)) -> \t1., \t2., \t3.
    """
    # ▪ --> *
    content = re.sub(r"▪", "*", content)
    
    # \no --> \n\t* (newline + o)
    content = re.sub(r"\no\s+", "\n\n  * ", content)
    
    # " o " --> "\n\t*" (space + o + space)
    content = re.sub(r"\s+o\s+", "\n\n    * ", content)
    
    # • --> \t*
    content = re.sub(r"•", "  *", content)
    content = re.sub(r"\s+•", "\n  *", content)

    
    # Chuyển đổi bullet chữ cái (a), b), c)) thành \t1., \t2., \t3.
    def letter_to_number(m): 
        letter = m.group(1).lower()
        number = ord(letter) - 96
        return f"\t{number}. "
    
    content = re.sub(r"^\s*([a-z])[\)\.]\s*", letter_to_number, content, flags=re.M)
    
    return content


def tidy_whitespace(content: str) -> str:
    content = re.sub(r"\n{3,}", "\n\n", content)
    content = re.sub(r"[ \t]+\n", "\n", content)
    return content


def keep_latex_as_is(content: str) -> str:
    """
    Strip LaTeX markup:
    - Inline $...$ → plain text
    - Display $$...$$ simple → plain text
    - Display $$...$$ complex → giữ nguyên
    """
    
    def is_simple(c):
        normalized = re.sub(r'\s+', '', c)
        patterns = [
            r'^\\(?:leftarrow|rightarrow|to|gets|xleftarrow|xrightarrow)(?:\{\})?$',
            r'^\\(?:leftarrow|rightarrow|to|gets|xleftarrow|xrightarrow)\{[^\}]*\}$',
        ]
        return any(re.match(p, normalized) for p in patterns)
    
    def process(c):
        for _ in range(5):
            c = re.sub(r'\\(?:mathrm|mathbf|text|textbf|textit|mathit|mathcal|mathbb|hat|acute|dot|breve|check|grave|bar|vec|tilde|overline|underline|circ|sqrt|frac)\s*\{\s*([^}]*?)\s*\}', r' \1 ', c)
            c = re.sub(r'\\[a-zA-Z]+\s*\{\s*([^}]*?)\s*\}', r' \1 ', c)
        c = re.sub(r'\\[a-zA-Z]+', ' ', c)
        for _ in range(5):
            c = re.sub(r'\{\s*([^}]*?)\s*\}', r' \1 ', c)
        c = re.sub(r'[\\$^_{}]', ' ', c)
        c = re.sub(r'\s+', ' ', c).strip()
        
        parts = c.split()
        merged = []
        i = 0
        while i < len(parts):
            if len(parts[i]) == 1 and parts[i].isalpha():
                letters = [parts[i]]
                j = i + 1
                while j < len(parts) and len(parts[j]) == 1 and parts[j].isalpha():
                    letters.append(parts[j])
                    j += 1
                merged.append(''.join(letters) if len(letters) >= 2 else parts[i])
                i = j
            else:
                merged.append(parts[i])
                i += 1
        c = ' '.join(merged)
        
        while re.search(r'\d\s+\d', c):
            c = re.sub(r'(\d)\s+(\d)', r'\1\2', c)
        c = re.sub(r'(\d)\s*([,.])\s*(\d)', r'\1\2\3', c)
        c = re.sub(r'\s*([=+\-*/])\s*', r'\1', c)
        return re.sub(r'\s+', ' ', c).strip()
    
    def render_arrow(c):
        c = re.sub(r'\\(?:rightarrow|to|xrightarrow)\s*(?:\{\s*\})?', '->', c)
        c = re.sub(r'\\(?:leftarrow|gets|xleftarrow)\s*(?:\{\s*\})?', '<-', c)
        c = re.sub(r'[\\{}\s]', '', c)
        return c or '->'
    
    def handle_display(m):
        return render_arrow(m.group(1)) if is_simple(m.group(1)) else m.group(0)
    
    content = re.sub(r'\$\$([^$]+?)\$\$', handle_display, content)
    content = re.sub(r'(?<!\$)\$(?!\$)([^$]+?)\$(?!\$)', lambda m: process(m.group(1)), content)
    return content  # ← ĐÃ FIX: BỎ normalize whitespace toàn bộ

def clean_markdown_pipeline(md: str, public_dir_name: str, verbose: bool = False) -> str:
    x = md
    x = rewrite_numbered_headings(x)
    x = normalize_references_block(x)
    x = convert_bullets(x)
    x = keep_latex_as_is(x)
    x = tidy_whitespace(x)
    return x


# =========================
# Runner
# =========================


def list_md_files(input_root: Path) -> List[Tuple[str, Path]]:
    pairs: List[Tuple[str, Path]] = []
    for d in input_root.iterdir():
        if not d.is_dir():
            continue
        if not is_public_dir(d.name):
            continue
        for md_path in d.rglob("*.md"):
            if md_path.is_file():
                pairs.append((d.name, md_path))
    return pairs


def main():
    if not INPUT_ROOT.exists():
        print(f"[ERROR] Input root not found: {INPUT_ROOT}", file=sys.stderr)
        sys.exit(1)
    ensure_dir(OUTPUT_ROOT)

    cache = load_cache()
    files = list_md_files(INPUT_ROOT)
    if not files:
        print("[INFO] No .md files found under PublicNNN folders.")
        return

    processed = 0
    skipped = 0
    total_images_filtered = 0

    print(f"[CONFIG] Image filter: Width >= {BANNED_IMAGE_MIN_WIDTH} AND Height in [{BANNED_IMAGE_MIN_HEIGHT}, {BANNED_IMAGE_MAX_HEIGHT}]")

    for public_dir_name, src_md_path in files:
        try:
            raw = src_md_path.read_text(encoding=ENCODING, errors="ignore")
        except Exception as e:
            print(f"[WARN] Cannot read {src_md_path}: {e}", file=sys.stderr)
            continue

        rel = relpath_from(INPUT_ROOT, src_md_path)
        dst_md_path = OUTPUT_ROOT / rel
        dst_md_dir  = dst_md_path.parent
        ensure_dir(dst_md_dir)

        sig_src = sha256_text(raw)
        cache_key = str(src_md_path.resolve())

        need_process = (cache.get(cache_key) != sig_src) or (not dst_md_path.exists())
        valid_images = []

        if need_process:
            content_with_placeholders, valid_images = replace_images_with_placeholders(
                raw, src_md_path.parent, verbose=True
            )
            
            total_before = len(find_all_image_links(raw))
            total_after = len(valid_images)
            filtered_count = total_before - total_after
            total_images_filtered += filtered_count
            
            if filtered_count > 0:
                print(f"[IMAGE FILTER] {src_md_path.name}: {filtered_count} images removed ({total_before} → {total_after})")
            
            cleaned = clean_markdown_pipeline(content_with_placeholders, public_dir_name, verbose=True)
            
            try:
                dst_md_path.write_text(cleaned, encoding=ENCODING)
            except Exception as e:
                print(f"[ERROR] Cannot write cleaned md {dst_md_path}: {e}", file=sys.stderr)
                valid_images = []
            
            copy_and_rename_images(src_md_path.parent, dst_md_dir, valid_images)
            
            cache[cache_key] = sig_src
            processed += 1
            print(f"[OK] Cleaned: {src_md_path} → {dst_md_path}")
        else:
            skipped += 1

        if not valid_images:
            ensure_dir(dst_md_dir / "images")

    save_cache(cache)
    print(f"\n[SUMMARY] processed={processed}, skipped={skipped}, total={len(files)}")
    print(f"[SUMMARY] Total images filtered: {total_images_filtered}")


if __name__ == "__main__":
    main()


# ============================================================
# clean_headler.py
# ============================================================

import os
import re
import json
import time
import argparse
import hashlib
import unicodedata
from pathlib import Path
from typing import List, Dict, Tuple

import fitz  # PyMuPDF
from tqdm import tqdm

# =============== Defaults ===============
THIN_LINE_THRESHOLD = 3       
PAD_PTS = 12                    # nở vùng redaction
VETO_THRESHOLD = 0.12        # tỉ lệ chữ trong rect vượt ngưỡng -> bỏ qua        
MIN_WIDTH_RATIO = 0.50         # bảng phải rộng tối thiểu % bề ngang trang
MAX_HEIGHT_RATIO = 0.25        # bảng phải thấp hơn ngưỡng % bề dọc trang (header thường thấp)
MERGE_PAD = 6                  # ngưỡng "gần nhau" khi gộp các rect line
IMG_REMOVE = getattr(fitz, "PDF_REDACT_IMAGE_REMOVE", 1)
IMG_NONE   = getattr(fitz, "PDF_REDACT_IMAGE_NONE", 0)
import textwrap
INPUT_DIR = Path(r'private_test\input')

state = 'test' if 'test' in str(INPUT_DIR).lower() else 'train'

WORKING_DIR = Path(r'working')
OUTPUT_DIR = WORKING_DIR / f'cleaned_pdfs_{state}'
os.makedirs(OUTPUT_DIR, exist_ok=True)
DEFAULT_KEYWORDS = [
    r"VIETTEL\s+AI\s+RACE",
    r"PUBLIC\s*\d{1,4}",
    r"LAN\s+BAN\s+HANH",   # "Lần ban hành" sau khi bỏ dấu
]

# =============== Text utils ===============
def strip_accents(s: str) -> str:
    s = unicodedata.normalize('NFD', s)
    return ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')

def norm_text(s: str) -> str:
    s = re.sub(r"\s+", " ", s.strip())
    s = strip_accents(s).upper()
    return s

def compile_patterns(keywords: List[str]) -> List[re.Pattern]:
    return [re.compile(pat) for pat in keywords]

def match_any(text: str, patterns: List[re.Pattern]) -> bool:
    for p in patterns:
        if p.search(text):
            return True
    return False

# =============== Geometry helpers ===============
def md5_bytes(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()

def _expand(r: fitz.Rect, pad=2) -> fitz.Rect:
    return fitz.Rect(r.x0 - pad, r.y0 - pad, r.x1 + pad, r.y1 + pad)

def rects_can_merge(a: fitz.Rect, b: fitz.Rect, pad=6) -> bool:
    return _expand(a, pad).intersects(_expand(b, pad))

def union_rects(rects: List[fitz.Rect], pad_for_merge=6) -> List[fitz.Rect]:
    if not rects: return []
    rects = [fitz.Rect(r) for r in rects]
    changed = True
    while changed:
        changed = False
        out: List[fitz.Rect] = []
        while rects:
            r = rects.pop()
            merged = False
            for i, rr in enumerate(out):
                if rects_can_merge(r, rr, pad_for_merge):
                    out[i] = rr | r
                    merged = True
                    changed = True
                    break
            if not merged:
                out.append(r)
        rects = out
    return rects

def is_thin_line(rect: fitz.Rect, threshold=THIN_LINE_THRESHOLD) -> bool:
    w, h = rect.width, rect.height
    return (w < threshold and h > threshold * 2) or (h < threshold and w > threshold * 2)

# =============== Table extraction ===============
def group_table_like_regions(page: fitz.Page, min_width_ratio=0.5, max_height_ratio=0.25,
                             merge_pad=6) -> List[fitz.Rect]:
    """
    Dựa vào vector line (get_drawings) để tìm các cụm line mảnh → coi là "bảng".
    Lọc theo kích thước tương đối để tránh các line lặt vặt.
    """
    w, h = page.rect.width, page.rect.height
    try:
        drawings = page.get_drawings()
    except Exception:
        drawings = []

    # Thu thập line mảnh trong trang
    line_rects: List[fitz.Rect] = []
    for dr in drawings:
        r = dr.get("rect")
        if not r: continue
        r = fitz.Rect(r)
        if is_thin_line(r, THIN_LINE_THRESHOLD):
            line_rects.append(r)

    if not line_rects:
        return []

    # Gộp line thành cụm vùng
    clusters = union_rects(line_rects, pad_for_merge=merge_pad)

    # Lọc cụm có "dáng bảng"
    tables: List[fitz.Rect] = []
    for R in clusters:
        width_ratio  = R.width / w
        height_ratio = R.height / h
        if width_ratio >= min_width_ratio and height_ratio <= max_height_ratio:
            tables.append(R)

    return tables

def extract_text_in_rect(page: fitz.Page, rect: fitz.Rect) -> str:
    """
    Lấy text 'blocks' giao với rect. Dùng text 'words' cũng được nhưng blocks đủ nhanh.
    """
    texts = []
    try:
        blocks = page.get_text("blocks") or []
    except Exception:
        blocks = []
    for b in blocks:
        if len(b) < 5: continue
        x0, y0, x1, y1, text = b[:5]
        if not isinstance(text, str): continue
        br = fitz.Rect(x0, y0, x1, y1)
        if br.intersects(rect):
            texts.append(text)
    return "\n".join(texts)

# =============== Redaction helpers ===============
def text_area_ratio(page: fitz.Page, rect: fitz.Rect) -> float:
    try:
        words = page.get_text("words") or []
    except Exception:
        return 0.0
    inter = 0.0
    for w in words:
        wr = fitz.Rect(w[0], w[1], w[2], w[3])
        if wr.intersects(rect):
            inter += (wr & rect).get_area()
    return inter / max(rect.get_area(), 1e-6)

def redact_rects(doc: fitz.Document, targets: Dict[int, List[fitz.Rect]],
                 pad_pts=6, veto_threshold=0.12, keep_debug=False, remove_images=True):
    """
    Áp redaction cho mỗi trang với danh sách rect cần xoá.
    - Nở nhẹ mỗi rect (pad_pts).
    - Nếu text_area_ratio trong rect > veto_threshold quá nhiều -> bỏ (phòng đụng nội dung thật).
    - Xóa luôn ảnh trong vùng.
    """
    for pno, rects in targets.items():
        page = doc[pno]
        for r in rects:
            rr = _expand(r, pad_pts)
            # veto "siêu an toàn": nếu tỉ lệ chữ quá cao và rect rất dày
            if text_area_ratio(page, rr) > float(veto_threshold) and (rr.height / page.rect.height) > 0.35:
                continue
            if keep_debug:
                ann = page.add_rect_annot(rr)
                ann.set_colors(stroke=(1,0,0)); ann.set_border(width=0.7); ann.update()
            page.add_redact_annot(rr, fill=(1,1,1))
        page.apply_redactions(images=(IMG_REMOVE if remove_images else IMG_NONE))

# =============== Orchestrator ===============
def process_pdf(src: Path, dst: Path, rep_dir: Path,
                keywords: List[str],
                min_width_ratio: float,
                max_height_ratio: float,
                merge_pad: int,
                pad_pts: int,
                veto_threshold: float,
                allow_text_fallback: bool,
                keep_debug: bool):
    t0 = time.time()
    doc = fitz.open(str(src))
    patterns = compile_patterns(keywords)

    removed_rects: Dict[int, List[fitz.Rect]] = {}
    debug_info: Dict[int, dict] = {}

    for pno in range(len(doc)):
        page = doc[pno]
        w, h = page.rect.width, page.rect.height

        # 1) Dò bảng bằng line mảnh
        tables = group_table_like_regions(
            page,
            min_width_ratio=min_width_ratio,
            max_height_ratio=max_height_ratio,
            merge_pad=merge_pad
        )

        page_debug = {
            "tables": [[round(r.x0,2), round(r.y0,2), round(r.x1,2), round(r.y1,2)] for r in tables],
            "hits": []
        }

        # 2) Với mỗi bảng -> trích text trong rect -> match keywords
        hits: List[fitz.Rect] = []
        for R in tables:
            raw = extract_text_in_rect(page, R)
            t = norm_text(raw)
            if not t.strip():
                continue
            if match_any(t, patterns):
                hits.append(R)
                page_debug["hits"].append({
                    "rect": [round(R.x0,2), round(R.y0,2), round(R.x1,2), round(R.y1,2)],
                    "sample_text": t[:120]
                })

        # (Tuỳ chọn) Fallback khi header là text thuần, không có line bảng
        if allow_text_fallback and not hits:
            # tìm block text lớn chứa keywords, coi block đó là "bảng" để xóa
            try:
                blocks = page.get_text("blocks") or []
            except Exception:
                blocks = []
            for b in blocks:
                if len(b) < 5: continue
                x0, y0, x1, y1, text = b[:5]
                if not isinstance(text, str): continue
                t = norm_text(text)
                if match_any(t, patterns):
                    R = fitz.Rect(x0, y0, x1, y1)
                    # lọc block quá nhỏ (caption/footnote bất chợt)
                    if (R.width / w) >= (min_width_ratio * 0.6):
                        hits.append(R)
                        page_debug.setdefault("fallback_hits", []).append({
                            "rect": [round(R.x0,2), round(R.y0,2), round(R.x1,2), round(R.y1,2)],
                            "sample_text": t[:120]
                        })

        if hits:
            # gộp hits tránh xóa chắp vá
            merged = union_rects(hits, pad_for_merge=merge_pad)
            removed_rects[pno] = merged

        debug_info[pno] = page_debug

    # 3) Redaction
    if removed_rects:
        redact_rects(
            doc, removed_rects,
            pad_pts=pad_pts,
            veto_threshold=veto_threshold,
            keep_debug=keep_debug,
            remove_images=True
        )

    # Lưu file
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(dst), deflate=True, garbage=3, clean=True)
    doc.close()

    # Báo cáo
    rep = {
        "file": src.name,
        "config": {
            "keywords": keywords,
            "min_width_ratio": min_width_ratio,
            "max_height_ratio": max_height_ratio,
            "merge_pad": merge_pad,
            "pad_pts": pad_pts,
            "veto_threshold": veto_threshold,
            "allow_text_fallback": allow_text_fallback
        },
        "targets": {
            str(p): [[round(r.x0,2), round(r.y0,2), round(r.x1,2), round(r.y1,2)] for r in rects]
            for p, rects in removed_rects.items()
        },
        "debug": debug_info,
        "metrics": {
            "processing_time_sec": round(time.time() - t0, 2),
            "pages_affected": len(removed_rects),
        }
    }
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / f"{src.stem}.tables_removed.json").write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Remove table regions containing specific keywords (v4).")
    ap.add_argument("--input",  type=Path, default=INPUT_DIR)
    ap.add_argument("--outdir", type=Path, default=OUTPUT_DIR)
    ap.add_argument("--report", type=Path, default=Path("working/reports_table_removal"))
    ap.add_argument("--keywords", type=str,
                    default=";".join(DEFAULT_KEYWORDS),
                    help="Chuỗi regex phân tách bằng ';' (đã bỏ dấu, uppercase).")
    ap.add_argument("--keywords-file", type=Path, default=None,
                    help="File txt/json chứa danh sách regex; ưu tiên hơn --keywords.")
    ap.add_argument("--min-width-ratio", type=float, default=MIN_WIDTH_RATIO,
                    help="Bảng phải rộng tối thiểu % bề ngang trang (0-1).")
    ap.add_argument("--max-height-ratio", type=float, default=MAX_HEIGHT_RATIO,
                    help="Bảng phải thấp hơn % bề dọc trang (0-1).")
    ap.add_argument("--merge-pad", type=int, default=MERGE_PAD, help="Ngưỡng gộp rect (pt).")
    ap.add_argument("--pad", type=int, default=PAD_PTS, help="Nở vùng redaction (pt).")
    ap.add_argument("--veto", type=float, default=VETO_THRESHOLD,
                    help="Nếu tỉ lệ chữ trong mask > ngưỡng & mask quá dày -> skip.")
    ap.add_argument("--allow-text-fallback", action="store_true",
                    help="Cho phép xóa theo block text nếu không phát hiện được bảng (ít dùng).")
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()

    # Tạo output dirs
    args.outdir.mkdir(parents=True, exist_ok=True)
    args.report.mkdir(parents=True, exist_ok=True)

    # Nạp keywords
    keywords: List[str]
    if args.keywords_file and args.keywords_file.exists():
        if args.keywords_file.suffix.lower() in {".json", ".jsonl"}:
            data = json.loads(args.keywords_file.read_text(encoding="utf-8"))
            if isinstance(data, list):
                keywords = [str(x) for x in data]
            else:
                raise SystemExit("keywords-file JSON phải là list regex strings.")
        else:
            # txt: mỗi dòng là một regex
            keywords = [ln.strip() for ln in args.keywords_file.read_text(encoding="utf-8").splitlines() if ln.strip()]
    else:
        keywords = [s.strip() for s in args.keywords.split(";") if s.strip()]

    # Rà PDF
    if args.input.is_file() and args.input.suffix.lower() == ".pdf":
        pdfs = [args.input]
    else:
        pdfs = sorted(args.input.rglob("*.pdf"))
        if not pdfs:
            raise SystemExit(f"Không tìm thấy PDF trong: {args.input.resolve()}")
        print(f"✓ Found {len(pdfs)} PDFs under: {args.input.resolve()}")

    # Xử lý
    for src in tqdm(pdfs, desc="Removing tables by keywords (v4)"):
        dst = args.outdir / src.name
        try:
            process_pdf(
                src, dst, args.report,
                keywords=keywords,
                min_width_ratio=args["min_width_ratio"] if isinstance(args, dict) else args.min_width_ratio,
                max_height_ratio=args["max_height_ratio"] if isinstance(args, dict) else args.max_height_ratio,
                merge_pad=args["merge_pad"] if isinstance(args, dict) else args.merge_pad,
                pad_pts=args["pad"] if isinstance(args, dict) else args.pad,
                veto_threshold=args["veto"] if isinstance(args, dict) else args.veto,
                allow_text_fallback=args.allow_text_fallback,
                keep_debug=args.debug
            )
        except Exception as e:
            print(f"⚠️ {src.name}: {e}")

if __name__ == "__main__":
    main()


# ============================================================
# combie.py
# ============================================================

import os

def extract_md_from_subfolders(root_folder):
    """
    Lấy nội dung các file .md trong các subfolder.
    Trả về dict với key là tên folder (PDF name) và value là nội dung.
    """
    extracted_contents = {}
    
    # Duyệt qua tất cả các item trong folder gốc
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        
        # Chỉ xử lý nếu là folder
        if os.path.isdir(item_path):
            # Tìm file main.md trong folder
            md_file = os.path.join(item_path, "main.md")
            
            if os.path.isfile(md_file):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        extracted_contents[item] = f.read()
                except Exception as e:
                    print(f"❌ Lỗi đọc {md_file}: {e}")
                    extracted_contents[item] = None
            else:
                # Nếu không có main.md, thử tìm file .md khác
                md_files = [f for f in os.listdir(item_path) if f.endswith('.md')]
                if md_files:
                    alt_path = os.path.join(item_path, md_files[0])
                    try:
                        with open(alt_path, 'r', encoding='utf-8') as f:
                            extracted_contents[item] = f.read()
                    except Exception as e:
                        print(f"❌ Lỗi đọc {alt_path}: {e}")
                        extracted_contents[item] = None
                else:
                    extracted_contents[item] = None
    
    return extracted_contents

# === CẤU HÌNH ===
input_folder = r"working\output_mineru_test"  # Folder chứa các subfolder
output_path = r"working\answer.md"        # File output

# === THỰC THI ===
print(f"🔍 Đang quét folder: {input_folder}")
extracted_contents = extract_md_from_subfolders(input_folder)

# === GHI FILE (đúng format bạn yêu cầu) ===
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("### TASK EXTRACT\n")
    
    for pdf_name in sorted(extracted_contents.keys()):
        content = extracted_contents[pdf_name]
        if content:
            f.write(content)
        else:
            f.write("(Extraction failed)\n")
        f.write("\n\n")
    f.write("\n")
    f.write("### TASK QA\n")
    f.write("num_correct,answers\n")
    f.write("1,A\n")  

print(f"✅ Hoàn thành! Đã xử lý {len(extracted_contents)} folder")
print(f"📁 File kết quả: {output_path}")

# ============================================================
# create_late_file.py
# ============================================================

# -*- coding: utf-8 -*-
import re
from pathlib import Path
import pandas as pd


# ======= CẤU HÌNH =======
CSV_PATH = r"test\model_Qwen3-4b_qwen.csv"  
MD_PATH  = r"working\anwser.md"                              
HEADER   = "### TASK QA"                                 
# =========================


df = pd.read_csv(CSV_PATH, dtype={"num_correct": str, "answers": str})

for col in ["num_correct", "answers"]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r"[\r\n]+", "", regex=True)
        .str.strip()
    )


VALID_CHOICES = set("ABCD")

def check_answers_valid(ans: str):
    core = ans.strip('"').strip()
    parts = list(core)
    for p in parts:
        if p not in VALID_CHOICES:
            raise ValueError(f"'{core}' không hợp lệ (chỉ A,B,C,D) trong output")

check_errors = []
for idx, ans in enumerate(df["answers"], 1):
    try:
        check_answers_valid(ans)
    except ValueError as err:
        check_errors.append((idx, str(err)))

if check_errors:
    errors_messages = '\n'.join([f"Dòng {idx}: {msg}" for idx, msg in check_errors])
    raise ValueError(f"Lỗi phát hiện trong file CSV:\n{errors_messages}")


def format_answers(ans: str) -> str:
    core = ans.strip('"').strip()
    if "," in core:
        parts = [p.strip() for p in core.split(",") if p.strip()]
        return '"' + ",".join(parts) + '"'
    else:
        parts = list(core)
        if len(parts) > 1 and all(p in VALID_CHOICES for p in parts):
            return '"' + ",".join(parts) + '"'
        return core

df["answers"] = df["answers"].apply(format_answers)

lines = [f"{nc},{ans}" for nc, ans in df[["num_correct", "answers"]].itertuples(index=False, name=None)]
qa_block = HEADER + "\n" + "num_correct,answers\n" + "\n".join(lines)


md_path = Path(MD_PATH)
old_text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""

m = re.search(r"(?m)^### TASK QA[^\n]*\n", old_text)
if m:
    new_text = old_text[:m.start()] + qa_block
else:
    if old_text and not old_text.endswith("\n"):
        old_text += "\n"
    new_text = old_text + qa_block


with open(MD_PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(new_text)


print("cập nhật file markdown:", MD_PATH)

# ============================================================
# detect_font.py
# ============================================================

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

# ============================================================
# detect_healder.py
# ============================================================

import os
import json
import re
from datetime import datetime
from pathlib import Path

# Import các hàm từ training_model_detect.py
# from training_model_detect import MLHeadingDetector, train_and_evaluate
import pymupdf
import numpy as np
import pandas as pd
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
import re
from difflib import SequenceMatcher
import lightgbm as lgb
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, classification_report, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
import joblib
import warnings
import hashlib
import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')


@dataclass
class TextLine:
    text: str
    font_size: float
    font_name: str
    is_bold: bool
    x0: float
    y0: float
    x1: float
    y1: float
    page: int
    page_height: float
    page_width: float

class ThresholdOptimizer:
    """Optimize prediction thresholds for each class to maximize F1-score"""
    
    def __init__(self):
        self.optimal_thresholds = {}
        
    def find_optimal_threshold(self, y_true: np.ndarray, y_probs: np.ndarray, class_label: int) -> float:
        """Find optimal threshold for a specific class to maximize F1-score"""
        if class_label not in np.unique(y_true):
            return 0.
            
        # Get probabilities for this class
        prob_class = y_probs[:, class_label]
        
        # Define objective function to minimize (negative F1)
        def objective(threshold):
            y_pred_class = (prob_class >= threshold).astype(int)
            true_class = (y_true == class_label).astype(int)
            
            if np.sum(y_pred_class) == 0 or np.sum(true_class) == 0:
                return 1.0  # Worst possible F1
                
            precision, recall, f1, _ = precision_recall_fscore_support(
                true_class, y_pred_class, average='binary', zero_division=0
            )
            return -f1  # Minimize negative F1
        
        # Find optimal threshold
        try:
            result = minimize_scalar(objective, bounds=(0.1, 0.9), method='bounded')
            return max(0.1, min(0.9, result.x))
        except:
            return 0.85
    
    def optimize_all_thresholds(self, y_true: np.ndarray, y_probs: np.ndarray, classes: List[int]) -> Dict[int, float]:
        """Optimize thresholds for all specified classes"""
        optimal_thresholds = {}
        
        for class_label in classes:
            if class_label > 0:  # Only optimize for heading classes (1-4)
                threshold = self.find_optimal_threshold(y_true, y_probs, class_label)
                optimal_thresholds[class_label] = threshold
                print(f"  Class {class_label}: optimal threshold = {threshold:.3f}")
        
        return optimal_thresholds
class DataValidator:
    """Validate and verify training data quality"""
    
    def __init__(self):
        self.validation_results = {}
        
    def validate_data_quality(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> Dict[str, Any]:
        """Comprehensive data quality validation"""
        validation_report = {}
        
        # Basic statistics
        validation_report['total_samples'] = len(X)
        validation_report['total_features'] = X.shape[1] if len(X) > 0 else 0
        
        # Class distribution - convert numpy types to Python native types
        unique_classes, class_counts = np.unique(y, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique_classes, class_counts):
            class_dist[int(cls)] = int(count)  # Convert to native Python types
        validation_report['class_distribution'] = class_dist
        
        # Calculate imbalance ratio only for heading classes (1-4)
        heading_counts = [count for cls, count in zip(unique_classes, class_counts) if cls > 0]
        if len(heading_counts) > 1:
            validation_report['heading_imbalance_ratio'] = float(max(heading_counts) / min(heading_counts))
        else:
            validation_report['heading_imbalance_ratio'] = 1.0
        
        # Feature statistics
        feature_stats = {}
        for i, feature_name in enumerate(feature_names):
            if len(X) > 0 and i < X.shape[1]:
                feature_data = X[:, i]
                feature_stats[feature_name] = {
                    'mean': float(np.mean(feature_data)),
                    'std': float(np.std(feature_data)),
                    'min': float(np.min(feature_data)),
                    'max': float(np.max(feature_data)),
                    'missing_values': int(np.sum(np.isnan(feature_data)))
                }
        validation_report['feature_statistics'] = feature_stats
        
        # Data quality flags - FOCUS ON HEADING CLASSES
        validation_report['quality_flags'] = {
            'has_sufficient_samples': len(X) >= 100,
            'has_multiple_heading_classes': len([cls for cls in unique_classes if cls > 0]) > 1,
            'no_missing_values': all(stats['missing_values'] == 0 for stats in feature_stats.values()),
            'reasonable_heading_imbalance': validation_report['heading_imbalance_ratio'] < 10,
            'feature_variance_adequate': all(stats['std'] > 0.01 for stats in feature_stats.values() 
                                           if feature_names[i] not in ['is_bold', 'font_differs', 'is_first', 'ends_period', 'starts_number', 'numbered_pattern', 'all_caps', 'placeholder'])
        }
        
        # Overall quality score
        quality_score = sum(validation_report['quality_flags'].values()) / len(validation_report['quality_flags'])
        validation_report['overall_quality_score'] = float(quality_score)
        
        return validation_report
    
    def cross_verify_predictions(self, detector: 'MLHeadingDetector', X: np.ndarray, y: np.ndarray, 
                               lines: List[TextLine], sample_size: int = 50) -> Dict[str, Any]:
        """Cross-verify predictions with manual inspection logic - ONLY AFTER TRAINING"""
        if len(X) == 0 or detector.model is None:
            print("  ⚠ Skipping cross-verification: Model not trained yet")
            return {}
            
        # Get predictions with optimized thresholds
        y_probs = detector.model.predict_proba(X)
        preds = detector._predict_with_thresholds(X, y_probs)
        
        verification_results = {
            'high_confidence_samples': [],
            'low_confidence_samples': [],
            'potential_misclassifications': [],
            'pattern_analysis': {}
        }
        
        # Analyze confidence scores - ONLY FOR HEADING CLASSES
        heading_indices = preds > 0
        if np.any(heading_indices):
            heading_confidences = np.max(y_probs[heading_indices], axis=1)
            high_confidence_threshold = 0.8
            low_confidence_threshold = 0.6
            
            for i, (true_label, pred_label) in enumerate(zip(y, preds)):
                if i >= sample_size:
                    break
                    
                # Only analyze heading predictions
                if pred_label > 0:
                    confidence = float(y_probs[i, pred_label])
                    
                    line_data = {
                        'text': lines[i].text if i < len(lines) else '',
                        'true_label': int(true_label),
                        'predicted_label': int(pred_label),
                        'confidence': confidence,
                        'is_correct': bool(true_label == pred_label)
                    }
                    
                    if confidence >= high_confidence_threshold:
                        verification_results['high_confidence_samples'].append(line_data)
                    elif confidence <= low_confidence_threshold:
                        verification_results['low_confidence_samples'].append(line_data)
                        
                    if true_label != pred_label and confidence > 0.7:  # High confidence but wrong
                        verification_results['potential_misclassifications'].append(line_data)
        
        # Pattern analysis for numbered headings
        numbered_patterns_analysis = self._analyze_numbered_patterns(lines, y, preds)
        verification_results['pattern_analysis'] = numbered_patterns_analysis
        
        return verification_results

    def validate_data_before_training(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> bool:
        """Quick validation before training to ensure data is usable - FOCUS ON HEADINGS"""
        if len(X) == 0:
            print("  ✗ No training data available")
            return False
            
        # Check for sufficient heading classes (at least 2 heading classes)
        heading_classes = [cls for cls in np.unique(y) if cls > 0]
        if len(heading_classes) < 2:
            print("  ✗ Need at least 2 heading classes for training")
            return False
            
        # Check for sufficient samples per heading class
        unique, counts = np.unique(y, return_counts=True)
        min_samples_per_class = 5
        for cls, count in zip(unique, counts):
            if cls > 0 and count < min_samples_per_class:  # Only check heading classes
                print(f"  ✗ Heading class {cls} has only {count} samples (min: {min_samples_per_class})")
                return False
                
        print("  ✓ Data validation passed - ready for training")
        return True
    
    def _analyze_numbered_patterns(self, lines: List[TextLine], y_true: np.ndarray, 
                                 y_pred: np.ndarray) -> Dict[str, Any]:
        """Analyze numbered pattern detection accuracy - ONLY HEADINGS"""
        analysis = {
            'true_positives': 0,
            'false_positives': 0,
            'false_negatives': 0,
            'pattern_examples': []
        }
        
        numbered_pattern = re.compile(r'^\d+(\.\d+)*\.?\s')
        
        for i, (line, true, pred) in enumerate(zip(lines, y_true, y_pred)):
            if i >= 100:  # Limit analysis to first 100 samples
                break
                
            has_numbered_pattern = bool(numbered_pattern.match(line.text.strip()))
            
            if has_numbered_pattern:
                if true > 0 and pred > 0:  # Correctly detected as heading
                    analysis['true_positives'] += 1
                elif true > 0 and pred == 0:  # Missed heading
                    analysis['false_negatives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_negative'
                    })
                elif true == 0 and pred > 0:  # False positive
                    analysis['false_positives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_positive'
                    })
        
        return analysis



class DataManager:
    """Manage training data caching and loading"""
    
    def __init__(self, cache_dir: str = "working/training_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def get_cache_key(self, input_dir: str, gt_dir: str) -> str:
        """Generate unique cache key based on input directories"""
        dir_info = f"{input_dir}_{gt_dir}"
        return hashlib.md5(dir_info.encode()).hexdigest()[:16]
    
    def save_training_data(self, cache_key: str, X: np.ndarray, y: np.ndarray, 
                         metadata: Dict[str, Any]) -> str:
        """Save training data to cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        # Save data
        np.savez(cache_file, X=X, y=y)
        
        # Convert metadata to JSON-serializable format
        serializable_metadata = self._convert_to_serializable(metadata)
        serializable_metadata['saved_at'] = datetime.now().isoformat()
        serializable_metadata['data_shape'] = X.shape if X is not None else None
        
        # Convert class distribution to serializable format
        if 'class_distribution' in serializable_metadata:
            serializable_metadata['class_distribution'] = {
                str(k): int(v) for k, v in serializable_metadata['class_distribution'].items()
            }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(serializable_metadata, f, indent=2, ensure_ascii=False)
            
        return str(cache_file)
    
    def _convert_to_serializable(self, obj: Any) -> Any:
        """Convert numpy types to Python native types for JSON serialization"""
        if isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {str(k): self._convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_to_serializable(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(self._convert_to_serializable(item) for item in obj)
        else:
            return obj
    
    def load_training_data(self, cache_key: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], Dict[str, Any]]:
        """Load training data from cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        if not cache_file.exists() or not metadata_file.exists():
            return None, None, {}
            
        try:
            # Load data
            data = np.load(cache_file)
            X, y = data['X'], data['y']
            
            # Load metadata
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                
            print(f"✓ Loaded cached training data: {X.shape[0]} samples")
            return X, y, metadata
            
        except Exception as e:
            print(f"✗ Error loading cached data: {e}")
            return None, None, {}
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get information about cached data"""
        cache_files = list(self.cache_dir.glob("*_data.npz"))
        cache_info = {
            'total_cached_datasets': len(cache_files),
            'cache_files': []
        }
        
        for cache_file in cache_files:
            metadata_file = cache_file.with_name(cache_file.stem.replace('_data', '_metadata') + '.json')
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    cache_info['cache_files'].append({
                        'file': cache_file.name,
                        'saved_at': metadata.get('saved_at', 'unknown'),
                        'data_shape': metadata.get('data_shape', 'unknown'),
                        'class_distribution': metadata.get('class_distribution', {})
                    })
                except:
                    continue
                    
        return cache_info


class FeatureExtractor:
    """Extract 22 features from each text line with ENHANCED numbered pattern detection"""

    def __init__(self):
        self.doc_stats = None
        # ENHANCED: Strict numbered patterns - chỉ tập trung vào 1., 1.1, 1.1.1, etc.
        self.numbered_patterns = [
            r'^\d+\.\s+[A-Za-zÀ-ỹ]',  # 1. Text (bắt đầu bằng số, dấu chấm, khoảng trắng, rồi chữ)
            r'^\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1 Text
            r'^\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1 Text  
            r'^\d+\.\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1.1 Text
        ]
        
        # ENHANCED: Strong exclusion patterns
        self.exclude_patterns = [
            r'^.*(hình|figure|bảng|table|biểu đồ|chart|trang|page).*\d',
            r'^.*\d+\s*[-–]\s*\d+.*',  # Number ranges like "1-2"
            r'^\d+$',  # Chỉ có số đơn thuần
            r'^.*[\.:]\d+$',  # Kết thúc bằng .số hoặc :số
        ]

    def compute_document_stats(self, lines: List[TextLine]) -> Dict:
        """Compute document-level statistics"""
        if not lines:
            self.doc_stats = {
                'median_font': 12.0, 'mean_font': 12.0, 'std_font': 1.0,
                'dominant_font': 'unknown', 'median_gap': 10.0, 
                'mean_gap': 10.0, 'std_gap': 5.0
            }
            return self.doc_stats

        font_sizes = [line.font_size for line in lines]
        font_names = [line.font_name for line in lines]

        # Compute gaps
        lines_sorted = sorted(lines, key=lambda l: (l.page, l.y0))
        gaps = []
        for i in range(1, len(lines_sorted)):
            if lines_sorted[i].page == lines_sorted[i-1].page:
                gap = lines_sorted[i].y0 - lines_sorted[i-1].y1
                if gap > 0:
                    gaps.append(gap)

        self.doc_stats = {
            'median_font': float(np.median(font_sizes)),
            'mean_font': float(np.mean(font_sizes)),
            'std_font': float(np.std(font_sizes)) if len(font_sizes) > 1 else 1.0,
            'dominant_font': max(set(font_names), key=font_names.count) if font_names else 'unknown',
            'median_gap': float(np.median(gaps)) if gaps else 10.0,
            'mean_gap': float(np.mean(gaps)) if gaps else 10.0,
            'std_gap': float(np.std(gaps)) if gaps else 5.0,
        }

        return self.doc_stats

    def is_likely_numbered_heading(self, text: str) -> bool:
        """ENHANCED: Strict detection of numbered headings while avoiding false positives"""
        text_clean = text.strip()
        
        # Check exclusion patterns first (tables, figures, etc.)
        for exclude_pattern in self.exclude_patterns:
            if re.match(exclude_pattern, text_clean, re.IGNORECASE):
                return False
        
        # Check inclusion patterns (must be at start and followed by text)
        for pattern in self.numbered_patterns:
            if re.match(pattern, text_clean):
                # EXTRA VALIDATION: text after numbers should be meaningful
                text_after_numbers = re.sub(r'^\d+(\.\d+)*\s*', '', text_clean).strip()
                if (len(text_after_numbers) >= 3 and 
                    any(c.isalpha() for c in text_after_numbers) and
                    not text_after_numbers.lower().startswith(('hình', 'bảng', 'biểu đồ', 'table', 'figure', 'chart'))):
                    return True
                    
        return False

    def extract_features(self, line: TextLine, prev_line: TextLine = None, 
                        next_line: TextLine = None) -> np.ndarray:
        """Extract 22 features from a text line with improved numbered pattern detection"""

        if self.doc_stats is None:
            raise ValueError("Call compute_document_stats first!")

        features = []
        text = line.text

        # === FONT FEATURES (5) ===
        features.append(line.font_size)  # f1: absolute font size

        font_ratio = line.font_size / self.doc_stats['median_font'] if self.doc_stats['median_font'] > 0 else 1.0
        features.append(font_ratio)  # f2: relative to median

        z_score = (line.font_size - self.doc_stats['mean_font']) / self.doc_stats['std_font'] if self.doc_stats['std_font'] > 0 else 0
        features.append(z_score)  # f3: standardized

        features.append(1.0 if line.is_bold else 0.0)  # f4: is bold

        font_differs = 1.0 if line.font_name != self.doc_stats['dominant_font'] else 0.0
        features.append(font_differs)  # f5: font differs from dominant

        # === POSITION FEATURES (6) ===
        relative_y = line.y0 / line.page_height if line.page_height > 0 else 0.5
        features.append(relative_y)  # f6: relative y position (0=top, 1=bottom)

        relative_x = line.x0 / line.page_width if line.page_width > 0 else 0.0
        features.append(relative_x)  # f7: relative x position

        features.append(line.x0)  # f8: distance from left margin (pixels)

        # Gap before
        gap_before = 0.0
        if prev_line and prev_line.page == line.page:
            gap_before = line.y0 - prev_line.y1
        features.append(gap_before)  # f9: gap before line

        # Gap after
        gap_after = 0.0
        if next_line and next_line.page == line.page:
            gap_after = next_line.y0 - line.y1
        features.append(gap_after)  # f10: gap after line

        is_first = 1.0 if (prev_line is None or prev_line.page != line.page) else 0.0
        features.append(is_first)  # f11: is first line of page

        # === TEXT FEATURES (8) ===
        features.append(len(text))  # f12: text length

        word_count = len(text.split())
        features.append(word_count)  # f13: word count

        # Capital word ratio (first letter)
        capital_words = sum(1 for word in text.split() if word and word[0].isupper())
        capital_ratio = capital_words / word_count if word_count > 0 else 0
        features.append(capital_ratio)  # f14: capital word ratio

        # NEW: Uppercase character ratio in entire text
        alpha_chars = sum(1 for c in text if c.isalpha())
        upper_chars = sum(1 for c in text if c.isupper())
        upper_ratio = upper_chars / alpha_chars if alpha_chars > 0 else 0
        features.append(upper_ratio)  # f15: uppercase character ratio

        punct_count = sum(1 for c in text if c in '.,;:!?')
        features.append(punct_count)  # f16: punctuation count

        # NEW: Period count specifically
        period_count = text.count('.')
        features.append(period_count)  # f17: period count

        ends_period = 1.0 if text.endswith('.') else 0.0
        features.append(ends_period)  # f18: ends with period

        starts_number = 1.0 if text and text[0].isdigit() else 0.0
        features.append(starts_number)  # f19: starts with number

        # === PATTERN FEATURES (3) ===
        # ENHANCED: Use strict numbered pattern detection
        matches_numbered = 1.0 if self.is_likely_numbered_heading(text) else 0.0
        features.append(matches_numbered)  # f20: numbered pattern

        is_all_caps = 1.0 if text.isupper() and len(text) > 3 else 0.0
        features.append(is_all_caps)  # f21: ALL CAPS

        # Removed keywords feature to avoid FP
        features.append(0.0)  # f22: placeholder (removed keywords)

        return np.array(features, dtype=np.float32)


class ModelManager:
    """Manage multiple model versions and save all trained models"""
    
    def __init__(self, models_dir: str = "working/models"):
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
    def save_model_version(self, detector: 'MLHeadingDetector', version_suffix: str = "", 
                         metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None) -> str:
        """Save model with versioning and metadata"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = f"heading_detector_{timestamp}"
        if version_suffix:
            version_name += f"_{version_suffix}"
            
        model_dir = self.models_dir / version_name
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Save main model
        model_path = model_dir / "model.pkl"
        joblib.dump({
            'model': detector.model,
            'feature_names': detector.feature_names,
            'feature_extractor': detector.feature_extractor
        }, model_path)
        
        # Save metadata
        metadata = {
            'version': version_name,
            'saved_at': datetime.now().isoformat(),
            'feature_count': len(detector.feature_names),
            'feature_names': detector.feature_names
        }
        
        if metrics:
            metadata['metrics'] = {k: float(v) if isinstance(v, (np.floating, float)) else v 
                                 for k, v in metrics.items()}
            
        if training_info:
            metadata['training_info'] = training_info
            
        with open(model_dir / "metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
            
        print(f"✓ Model version saved: {version_name}")
        return str(model_dir)
    
    def get_all_models(self) -> List[Dict[str, Any]]:
        """Get information about all saved models"""
        model_dirs = [d for d in self.models_dir.iterdir() if d.is_dir() and d.name.startswith("heading_detector_")]
        models_info = []
        
        for model_dir in model_dirs:
            metadata_file = model_dir / "metadata.json"
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    models_info.append({
                        'name': model_dir.name,
                        'path': str(model_dir),
                        'metadata': metadata
                    })
                except Exception as e:
                    print(f"Error loading metadata for {model_dir}: {e}")
                    
        return sorted(models_info, key=lambda x: x['metadata']['saved_at'], reverse=True)
    
    def load_latest_model(self) -> Optional[Dict]:
        """Load the most recent model"""
        all_models = self.get_all_models()
        if not all_models:
            return None
            
        latest_model = all_models[0]
        try:
            model_path = Path(latest_model['path']) / "model.pkl"
            detector_data = joblib.load(model_path)
            return {
                'detector_data': detector_data,
                'metadata': latest_model['metadata'],
                'path': latest_model['path']
            }
        except Exception as e:
            print(f"Error loading model {latest_model['name']}: {e}")
            return None
    
    def cleanup_old_models(self, keep_count: int = 5):
        """Keep only the most recent models"""
        all_models = self.get_all_models()
        if len(all_models) <= keep_count:
            return
            
        for model_info in all_models[keep_count:]:
            try:
                import shutil
                shutil.rmtree(model_info['path'])
                print(f"✓ Removed old model: {model_info['name']}")
            except Exception as e:
                print(f"✗ Error removing model {model_info['name']}: {e}")


class MLHeadingDetector:
    """ENHANCED ML-based heading detector with LightGBM (Multi-class)"""

    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.data_validator = DataValidator()
        self.data_manager = DataManager()
        self.model_manager = ModelManager()
        self.threshold_optimizer = ThresholdOptimizer()
        self.model = None
        self.feature_names = [
            'font_size', 'font_ratio', 'z_score', 'is_bold', 'font_differs',
            'y_position', 'x_position', 'left_margin', 'gap_before', 'gap_after', 'is_first',
            'text_length', 'word_count', 'capital_ratio', 'upper_ratio', 'punct_count', 
            'period_count', 'ends_period', 'starts_number', 'numbered_pattern', 
            'all_caps', 'placeholder'
        ]
        self.optimal_thresholds = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}  # Default thresholds


    def extract_lines(self, pdf_path: str) -> List[TextLine]:
        """Extract all text lines from PDF"""

        doc = pymupdf.open(pdf_path)
        all_lines = []

        for page_num, page in enumerate(doc, start=1):
            text_dict = page.get_text("dict")
            page_height = page.rect.height
            page_width = page.rect.width

            for block in text_dict["blocks"]:
                if block["type"] != 0:
                    continue

                for line in block.get("lines", []):
                    line_text = ""
                    font_sizes = []
                    font_names = []

                    for span in line.get("spans", []):
                        line_text += span["text"]
                        font_sizes.append(span["size"])
                        font_names.append(span["font"])

                    line_text = line_text.strip()
                    if not line_text:
                        continue

                    all_lines.append(TextLine(
                        text=line_text,
                        font_size=float(np.median(font_sizes)) if font_sizes else 12.0,
                        font_name=max(set(font_names), key=font_names.count) if font_names else 'unknown',
                        is_bold=any('bold' in f.lower() or 'heavy' in f.lower() for f in font_names),
                        x0=line['bbox'][0],
                        y0=line['bbox'][1],
                        x1=line['bbox'][2],
                        y1=line['bbox'][3],
                        page=page_num,
                        page_height=page_height,
                        page_width=page_width
                    ))

        doc.close()
        return all_lines

    def generate_training_data(self, pdf_path: str, gt_md_path: str) -> Tuple[np.ndarray, np.ndarray, List[TextLine]]:
        """FIXED: Generate features and labels - CHỈ gắn nhãn cho các heading markdown từ file GT"""

        # Extract lines
        lines = self.extract_lines(pdf_path)

        if not lines:
            print(f"  No lines extracted from {pdf_path}")
            return np.array([]), np.array([]), []

        # Compute document stats
        self.feature_extractor.compute_document_stats(lines)

        # Parse ground truth headings with levels - CHỈ lấy các heading markdown (#, ##, ###, ####)
        gt_headings = self._parse_markdown_with_levels(gt_md_path)
        
        if not gt_headings:
            print(f"  No markdown headings found in {gt_md_path}")
            return np.array([]), np.array([]), []

        # Extract features and labels
        X = []
        y = []

        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None

            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

            heading_level = self._fuzzy_match_with_level(line.text, gt_headings, threshold=0.8)
            y.append(heading_level)

        return np.array(X), np.array(y), lines

    def _fuzzy_match_with_level(self, text: str, gt_headings: List[Dict], threshold: float = 0.8) -> int:
        """Check if text matches any ground truth heading and return its level"""
        
        text_lower = text.lower().strip()
        best_score = 0
        best_level = 0  # Default: not a heading

        for gt_heading in gt_headings:
            gt_text = gt_heading['text'].lower().strip()
            score = SequenceMatcher(None, text_lower, gt_text).ratio()
            
            if score > best_score and score >= threshold:
                best_score = score
                best_level = gt_heading['level']

        return best_level

    def _parse_markdown_with_levels(self, md_path: str) -> List[Dict]:
        """Parse markdown to extract headings with levels (1-4) - CHỈ lấy markdown headings"""
        
        if not Path(md_path).exists():
            print(f"  Markdown file not found: {md_path}")
            return []

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            headings = []
            for line in content.split('\n'):
                line = line.strip()
                if not line:
                    continue

                # FIXED: CHỈ match markdown headings: # Heading 1, ## Heading 2, etc.
                # Bỏ qua tất cả các dòng không phải heading markdown
                match = re.match(r'^(#{1,4})\s+(.+)$', line)
                if match:
                    level = len(match.group(1))
                    text = match.group(2).strip()
                    headings.append({'text': text, 'level': level})

            print(f"  Extracted {len(headings)} markdown headings from {md_path}")
            return headings
        except Exception as e:
            print(f"  Error parsing markdown {md_path}: {e}")
            return []

    def train(self, X_train: np.ndarray, y_train: np.ndarray, X_val: np.ndarray = None, y_val: np.ndarray = None):
        """ENHANCED: Train LightGBM model with focus on heading recall and threshold optimization"""

        print(f"Training samples: {len(X_train)}")
        
        # Calculate class distribution - FOCUS ON HEADING CLASSES
        unique, counts = np.unique(y_train, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique, counts):
            class_dist[int(cls)] = int(count)
        print("Class distribution:")
        for level, count in class_dist.items():
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train)*100:.2f}%)")

        # Handle class imbalance - less aggressive merging
        y_train_adj = self._adjust_rare_classes_enhanced(y_train)
        
        # Recalculate class distribution after adjustment
        unique_adj, counts_adj = np.unique(y_train_adj, return_counts=True)
        print("\nAdjusted class distribution:")
        for level, count in zip(unique_adj, counts_adj):
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train_adj)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train_adj)*100:.2f}%)")

        # ENHANCED: Compute class weights with manual boost for headings
        class_weights = compute_class_weight(
            class_weight='balanced',
            classes=np.unique(y_train_adj),
            y=y_train_adj
        )
        
        # MANUAL BOOST: Increase weight for heading classes (1-4)
        class_weight_dict = {}
        for i, cls in enumerate(np.unique(y_train_adj)):
            base_weight = float(class_weights[i])
            if cls > 0:  # Heading classes
                boosted_weight = base_weight * 3.0  # Triple the importance
                class_weight_dict[int(cls)] = boosted_weight
            else:
                class_weight_dict[int(cls)] = base_weight
                
        print(f"Enhanced Class weights: {class_weight_dict}")

        # ENHANCED: LightGBM with focus on recall
        self.model = lgb.LGBMClassifier(
            n_estimators=300,
            max_depth=10,
            learning_rate=0.05,
            num_leaves=31,
            min_child_samples=10,
            subsample=0.7,
            colsample_bytree=0.7,
            reg_alpha=0.1,
            reg_lambda=0.1,
            class_weight=class_weight_dict,
            random_state=42,
            n_jobs=-1,
            verbose=-1,
            boosting_type='gbdt'
        )

        # Train with validation set if provided
        if X_val is not None and y_val is not None:
            self.model.fit(
                X_train, y_train_adj,
                eval_set=[(X_val, y_val)],
                eval_metric='multi_logloss',
            )
        else:
            self.model.fit(X_train, y_train_adj)

        # Optimize thresholds on validation set or training set
        if X_val is not None and y_val is not None:
            print("\nOptimizing thresholds on validation set...")
            y_val_probs = self.model.predict_proba(X_val)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_val, y_val_probs, [1, 2, 3, 4]
            )
        else:
            print("\nOptimizing thresholds on training set...")
            y_train_probs = self.model.predict_proba(X_train)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_train_adj, y_train_probs, [1, 2, 3, 4]
            )

        # Print feature importance
        print("\nTop 15 Important Features:")
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1][:15]

        for i, idx in enumerate(indices):
            print(f"  {i+1}. {self.feature_names[idx]:20s}: {importances[idx]:.4f}")

        return y_train_adj

    def _predict_with_thresholds(self, X: np.ndarray, y_probs: np.ndarray = None) -> np.ndarray:
        """Predict with optimized thresholds for heading classes"""
        if y_probs is None:
            y_probs = self.model.predict_proba(X)
        
        # Get default predictions (highest probability)
        default_preds = np.argmax(y_probs, axis=1)
        
        # Apply thresholds for heading classes
        for i in range(len(default_preds)):
            pred_class = default_preds[i]
            if pred_class in self.optimal_thresholds:
                if y_probs[i, pred_class] < self.optimal_thresholds[pred_class]:
                    # If probability below threshold, set to non-heading
                    default_preds[i] = 0
        
        return default_preds
    def _adjust_rare_classes_enhanced(self, y: np.ndarray) -> np.ndarray:
        """ENHANCED: Less aggressive class merging - preserve heading classes"""
        unique, counts = np.unique(y, return_counts=True)
        y_adj = y.copy()
        
        # Only merge extremely rare classes (less than 5 samples) - ONLY FOR HEADINGS
        for level, count in zip(unique, counts):
            if count < 5 and level > 0:  # Only merge rare heading classes
                # Find nearest heading level with sufficient samples
                possible_targets = [l for l in unique if l > 0 and np.sum(y == l) >= 10]
                if possible_targets:
                    target_level = min(possible_targets, key=lambda x: abs(x - level))
                    print(f"  Merging level {level} ({count} samples) into level {target_level}")
                    y_adj[y_adj == level] = target_level
                else:
                    # Fallback: merge into level 1
                    print(f"  Merging level {level} ({count} samples) into level 1")
                    y_adj[y_adj == level] = 1
        
        return y_adj
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Evaluate model performance - FOCUS ON HEADING CLASSES (1-4)"""

        # Adjust test labels same as training
        y_test_adj = self._adjust_rare_classes_enhanced(y_test)
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)

        # FOCUS ON HEADING CLASSES: Filter out class 0 for heading-specific metrics
        heading_indices = y_test_adj > 0
        heading_preds = preds[heading_indices]
        heading_true = y_test_adj[heading_indices]
        
        if len(heading_true) > 0:
            # Heading-specific metrics
            heading_accuracy = accuracy_score(heading_true, heading_preds)
            heading_precision, heading_recall, heading_f1, _ = precision_recall_fscore_support(
                heading_true, heading_preds, average='weighted', zero_division=0
            )
            
            # Per-class metrics for headings only
            heading_classes = sorted(np.unique(heading_true))
            per_class_metrics = precision_recall_fscore_support(
                heading_true, heading_preds, average=None, zero_division=0, labels=heading_classes
            )
            
            # Heading confusion matrix
            heading_cm = confusion_matrix(heading_true, heading_preds, labels=heading_classes)
        else:
            heading_accuracy = heading_precision = heading_recall = heading_f1 = 0.0
            per_class_metrics = ([], [], [], [])
            heading_cm = np.array([])
            heading_classes = []

        # Overall metrics (including non-headings) for reference
        overall_accuracy = accuracy_score(y_test_adj, preds)

        print("\n" + "="*70)
        print("EVALUATION RESULTS - FOCUS ON HEADING CLASSES (1-4)")
        print("="*70)
        print(f"Overall Accuracy (all classes): {overall_accuracy:.4f}")
        print(f"Heading-only Accuracy:          {heading_accuracy:.4f}")
        print(f"Heading-only Precision:         {heading_precision:.4f}")
        print(f"Heading-only Recall:            {heading_recall:.4f}")
        print(f"Heading-only F1 Score:          {heading_f1:.4f}")
        
        if heading_classes:
            print(f"\nPer-class Metrics (Headings only):")
            for i, cls in enumerate(heading_classes):
                print(f"  Level {cls}: Precision={per_class_metrics[0][i]:.4f}, "
                      f"Recall={per_class_metrics[1][i]:.4f}, F1={per_class_metrics[2][i]:.4f}")

            print(f"\nConfusion Matrix (Headings only):")
            print(heading_cm)

        # Show some misclassified heading examples
        heading_misclassified = np.where((heading_true != heading_preds) & (heading_true > 0))[0]
        if len(heading_misclassified) > 0 and len(heading_misclassified) <= 10:
            print(f"\nSample heading misclassifications ({len(heading_misclassified)} total):")
            for idx in heading_misclassified[:5]:
                print(f"  True: {heading_true[idx]}, Predicted: {heading_preds[idx]}")

        return {
            'overall_accuracy': float(overall_accuracy),
            'heading_accuracy': float(heading_accuracy),
            'heading_precision': float(heading_precision),
            'heading_recall': float(heading_recall),
            'heading_f1': float(heading_f1),
            'heading_confusion_matrix': heading_cm.tolist() if len(heading_cm) > 0 else [],
            'heading_classes': [int(cls) for cls in heading_classes],
            'per_class_metrics': [metric.tolist() for metric in per_class_metrics] if heading_classes else []
        }

    def evaluate_heading_detection(self, X_test: np.ndarray, y_test: np.ndarray, lines_test: List[TextLine]) -> Dict:
        """ENHANCED: Heading-specific evaluation metrics with threshold optimization"""
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)
        
        # FOCUS ON HEADING DETECTION (classes 1-4)
        heading_indices_true = y_test > 0
        heading_indices_pred = preds > 0
        
        total_headings = np.sum(heading_indices_true)
        detected_headings = np.sum(heading_indices_pred)
        correct_detections = np.sum(heading_indices_true & heading_indices_pred)
        
        # Calculate detection metrics
        detection_precision = correct_detections / detected_headings if detected_headings > 0 else 0
        detection_recall = correct_detections / total_headings if total_headings > 0 else 0
        detection_f1 = 2 * (detection_precision * detection_recall) / (detection_precision + detection_recall) if (detection_precision + detection_recall) > 0 else 0
        
        # Level-wise accuracy for correctly detected headings
        correctly_detected_indices = heading_indices_true & heading_indices_pred
        if np.any(correctly_detected_indices):
            level_accuracy = accuracy_score(
                y_test[correctly_detected_indices], 
                preds[correctly_detected_indices]
            )
        else:
            level_accuracy = 0.0

        print("\n" + "="*70)
        print("ENHANCED HEADING DETECTION EVALUATION")
        print("="*70)
        print(f"Detection Metrics:")
        print(f"  Precision: {detection_precision:.4f}")
        print(f"  Recall:    {detection_recall:.4f}")
        print(f"  F1-Score:  {detection_f1:.4f}")
        print(f"  Level Accuracy: {level_accuracy:.4f}")
        
        print(f"\nDetection Analysis:")
        print(f"  Total headings in test set: {total_headings}")
        print(f"  Detected as headings: {detected_headings}")
        print(f"  Correctly detected: {correct_detections}")
        print(f"  Heading Detection Rate: {detection_recall*100:.1f}%" if total_headings > 0 else "  Heading Detection Rate: N/A")
        
        # Analyze false negatives
        false_negatives = np.where(heading_indices_true & ~heading_indices_pred)[0]
        if len(false_negatives) > 0:
            print(f"\nFalse Negatives Analysis ({len(false_negatives)} missed headings):")
            for idx in false_negatives[:5]:  # Show first 5
                print(f"  Level {y_test[idx]}: {lines_test[idx].text[:80]}...")
        
        return {
            'detection_precision': float(detection_precision),
            'detection_recall': float(detection_recall),
            'detection_f1': float(detection_f1),
            'level_accuracy': float(level_accuracy),
            'total_headings': int(total_headings),
            'detected_headings': int(detected_headings),
            'correct_detections': int(correct_detections),
            'false_negatives': int(len(false_negatives))
        }
    
    def cross_validate(self, X: np.ndarray, y: np.ndarray, cv_folds: int = 5) -> Dict[str, Any]:
        """Perform cross-validation for more reliable evaluation with small data"""
        print(f"\nPerforming {cv_folds}-fold cross-validation...")
        
        # Adjust labels for consistency
        y_adj = self._adjust_rare_classes_enhanced(y)
        
        # Use stratified k-fold for imbalanced data
        skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
        
        cv_scores = {
            'accuracy': [],
            'precision': [],
            'recall': [],
            'f1': []
        }
        
        fold = 1
        for train_idx, val_idx in skf.split(X, y_adj):
            print(f"  Fold {fold}/{cv_folds}...")
            
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y_adj[train_idx], y_adj[val_idx]
            
            # Train temporary model
            temp_model = lgb.LGBMClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                verbose=-1
            )
            temp_model.fit(X_train, y_train)
            
            # Evaluate
            preds = temp_model.predict(X_val)
            cv_scores['accuracy'].append(float(accuracy_score(y_val, preds)))
            precision, recall, f1, _ = precision_recall_fscore_support(
                y_val, preds, average='weighted', zero_division=0
            )
            cv_scores['precision'].append(float(precision))
            cv_scores['recall'].append(float(recall))
            cv_scores['f1'].append(float(f1))
            
            fold += 1
        
        # Print CV results
        print(f"\nCross-Validation Results ({cv_folds}-fold):")
        for metric, scores in cv_scores.items():
            mean_score = float(np.mean(scores))
            std_score = float(np.std(scores))
            print(f"  {metric.capitalize()}: {mean_score:.4f} ± {std_score:.4f}")
        
        return cv_scores

    def predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback"""
        return self.enhanced_predict(pdf_path)

    def enhanced_predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback and minimum heading guarantee"""

        lines = self.extract_lines(pdf_path)
        if not lines:
            return []

        self.feature_extractor.compute_document_stats(lines)

        # ML Prediction
        X = []
        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None
            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

        X = np.array(X)
        preds = self.model.predict(X)
        probs = self.model.predict_proba(X)

        headings = []
        
        # RULE-BASED ENHANCEMENT: Ensure all numbered headings are detected
        for i, (line, pred, prob) in enumerate(zip(lines, preds, probs)):
            confidence = float(prob[pred])
            
            # RULE 1: If has numbered pattern but model missed it -> FORCE as heading
            if (self.feature_extractor.is_likely_numbered_heading(line.text) and 
                pred == 0 and confidence < 0.8):
                
                # Determine level based on dot count
                dot_count = line.text.strip().split(' ')[0].count('.')
                forced_level = min(4, max(1, dot_count))
                
                headings.append({
                    'text': line.text,
                    'level': forced_level,
                    'page': line.page,
                    'probability': 0.95,  # High confidence for rule-based
                    'font_size': line.font_size,
                    'detection_method': 'rule_based'
                })
                continue
                
            # RULE 2: ML prediction with lower confidence threshold
            if pred > 0 and confidence > 0.3:  # Lower threshold to catch more headings
                headings.append({
                    'text': line.text,
                    'level': int(pred),
                    'page': line.page,
                    'probability': confidence,
                    'font_size': line.font_size,
                    'detection_method': 'ml'
                })

        # RULE 3: Ensure minimum headings per document
        headings = self._ensure_minimum_headings(lines, headings)
        
        # Remove duplicates
        unique_headings = []
        seen_texts = set()
        for heading in headings:
            if heading['text'] not in seen_texts:
                unique_headings.append(heading)
                seen_texts.add(heading['text'])
        
        return unique_headings

    def _ensure_minimum_headings(self, lines: List[TextLine], headings: List[Dict]) -> List[Dict]:
        """ENHANCED: Ensure each document has at least 6 headings"""
        if len(headings) >= 6:  # Already has sufficient headings
            return headings
            
        # Find potential headings that were missed
        potential_headings = []
        
        # for i, line in enumerate(lines):
        #     # Skip if already detected
        #     if any(h['text'] == line.text for h in headings):
        #         continue
                
        #     # Characteristics of actual headings
        #     is_likely_heading = (
        #         self.feature_extractor.is_likely_numbered_heading(line.text) or
        #         (line.font_size > self.feature_extractor.doc_stats['median_font'] * 1.1 and 
        #          len(line.text.split()) <= 15 and  # Headings are usually short
        #          any(c.isupper() for c in line.text) and  # Has uppercase letters
        #          not line.text.endswith('.') and  # Doesn't end with period
        #          not line.text[-1].isdigit())  # Doesn't end with digit
        #     )
            
        #     if is_likely_heading:
        #         dot_count = line.text.strip().split(' ')[0].count('.')
        #         level = min(4, max(1, dot_count + 1))
                
        #         potential_headings.append({
        #             'text': line.text,
        #             'level': level,
        #             'page': line.page,
        #             'probability': 0.7,
        #             'font_size': line.font_size,
        #             'detection_method': 'fallback'
        #         })
        
        # Add potential headings if current count is too low
        if len(headings) < 6 and potential_headings:
            needed = min(6 - len(headings), len(potential_headings))
            headings.extend(potential_headings[:needed])
        
        return headings

    def save_all_models(self, metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None):
        """Save all model versions with metadata"""
        # Save main model
        main_model_path = self.model_manager.save_model_version(
            self, "main", metrics, training_info
        )
        
        # Also save a simplified version for quick loading
        simple_model_path = self.model_manager.save_model_version(
            self, "simple", metrics, training_info
        )
        
        print(f"✓ All model versions saved:")
        print(f"  - Main model: {main_model_path}")
        print(f"  - Simple model: {simple_model_path}")
        
        # Clean up old models (keep only 5 most recent)
        self.model_manager.cleanup_old_models(keep_count=5)
        
        return main_model_path

    def load_latest_model(self):
        """Load the most recent model"""
        model_data = self.model_manager.load_latest_model()
        if model_data is None:
            print("✗ No trained model found")
            return False
            
        try:
            detector_data = model_data['detector_data']
            self.model = detector_data['model']
            self.feature_names = detector_data['feature_names']
            self.feature_extractor = detector_data['feature_extractor']
            print(f"✓ Loaded model: {model_data['metadata']['version']}")
            return True
        except Exception as e:
            print(f"✗ Error loading model: {e}")
            return False


# ============================================================
# ENHANCED TRAINING PIPELINE - LIGHTGBM VERSION
# ============================================================

def train_and_evaluate(
    input_dir: str = r'input',
    gt_dir: str = r'output',
    output_dir: str = 'working/ml_heading_model_lgb',
    train_ratio: float = 0.75,  # Reduced to have more validation data
    val_ratio: float = 0.15,   # Added validation split
    use_cached_data: bool = True,
    enable_cross_validation: bool = True,
    enable_data_validation: bool = True,
    optimize_thresholds: bool = True  # New parameter for threshold optimization
):
    """Enhanced training pipeline with threshold optimization"""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    detector = MLHeadingDetector()
    
    # Check cache first
    cache_key = detector.data_manager.get_cache_key(input_dir, gt_dir)
    X_all, y_all, metadata = None, None, {}
    
    if use_cached_data:
        X_all, y_all, metadata = detector.data_manager.load_training_data(cache_key)
    
    # If no cached data or not using cache, generate new data
    if X_all is None or y_all is None:
        print("Generating new training data...")
        
        # Load dataset with proper path handling
        input_path = Path(input_dir)
        gt_path = Path(gt_dir)

        pdf_files = sorted(input_path.glob('*.pdf'))
        print(f"Found {len(pdf_files)} PDF files")

        # Generate training data with error handling
        print("\nGenerating training data...")
        X_all_parts = []
        y_all_parts = []
        all_lines = []
        processed_count = 0

        for i, pdf_file in enumerate(pdf_files):
            doc_id = pdf_file.stem
            
            # Look for markdown file
            possible_md_locations = [
                gt_path / f"{doc_id}.md",
                gt_path / doc_id / "main.md", 
                gt_path / doc_id / f"{doc_id}.md",
                gt_path / f"{doc_id}" / "main.md"
            ]
            
            gt_md_path = None
            for location in possible_md_locations:
                if location.exists():
                    gt_md_path = location
                    break
            
            if gt_md_path is None:
                print(f"  Skipping {doc_id}: No markdown file found")
                continue

            try:
                X_batch, y_batch, lines_batch = detector.generate_training_data(str(pdf_file), str(gt_md_path))
                
                if len(X_batch) > 0:
                    X_all_parts.append(X_batch)
                    y_all_parts.append(y_batch)
                    all_lines.extend(lines_batch)
                    processed_count += 1
                    print(f"  ✓ Processed {doc_id}: {len(X_batch)} samples")
                else:
                    print(f"  ⚠ No samples from {doc_id}")
                    
            except Exception as e:
                print(f"  ✗ Error with {doc_id}: {e}")
                continue

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(pdf_files)} files")

        # Check if we have any data
        if not X_all_parts:
            print("\n❌ ERROR: No training data generated!")
            return None, None

        # Combine all data
        try:
            X_all = np.vstack(X_all_parts)
            y_all = np.hstack(y_all_parts)
            
            # Save to cache for future use
            metadata = {
                'source_files': len(pdf_files),
                'processed_files': processed_count,
                'generated_at': datetime.now().isoformat()
            }
            detector.data_manager.save_training_data(cache_key, X_all, y_all, metadata)
            print(f"✓ Training data cached with key: {cache_key}")
            
        except ValueError as e:
            print(f"\n❌ ERROR combining data: {e}")
            return None, None

        print(f"\n✅ Successfully processed {processed_count}/{len(pdf_files)} files")
        print(f"Total samples: {len(X_all)}")
    else:
        print("✓ Using cached training data")
        all_lines = []  # Lines not available from cache

    # Show class distribution - FOCUS ON HEADINGS
    unique, counts = np.unique(y_all, return_counts=True)
    print("\nFinal Class Distribution:")
    total_samples = len(y_all)
    for level, count in zip(unique, counts):
        if level == 0:
            print(f"  Level {level} (Not heading): {count} samples ({count/total_samples*100:.2f}%)")
        else:
            print(f"  Level {level}: {count} samples ({count/total_samples*100:.2f}%)")
    
    heading_samples = np.sum(y_all > 0)
    print(f"Total heading samples: {heading_samples}/{total_samples} ({heading_samples/total_samples*100:.2f}%)")

    # Data Validation and Quality Check - FOCUS ON HEADINGS
    if enable_data_validation and len(X_all) > 0:
        print("\n" + "="*70)
        print("DATA QUALITY VALIDATION - HEADING FOCUS")
        print("="*70)
        
        validation_report = detector.data_validator.validate_data_quality(
            X_all, y_all, detector.feature_names
        )
        
        print(f"Overall Quality Score: {validation_report['overall_quality_score']:.2f}/1.00")
        print("\nQuality Flags (Heading Focus):")
        for flag, value in validation_report['quality_flags'].items():
            status = "✓" if value else "✗"
            print(f"  {status} {flag}: {value}")
        
        # Quick validation to ensure data is trainable - FOCUS ON HEADINGS
        is_data_ready = detector.data_validator.validate_data_before_training(X_all, y_all, detector.feature_names)
        if not is_data_ready:
            print("\n❌ Data validation failed - cannot proceed with training")
            return None, None
        
        # Save validation report
        with open(output_path / 'data_validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, indent=2, ensure_ascii=False)

    # Split train/val/test with indices
    indices = np.arange(len(X_all))
    
    # First split: train + temp vs test
    X_train_val, X_test, y_train_val, y_test, indices_train_val, indices_test = train_test_split(
        X_all, y_all, indices, test_size=1-train_ratio-val_ratio, random_state=42, stratify=y_all
    )
    
    # Second split: train vs val
    X_train, X_val, y_train, y_val, indices_train, indices_val = train_test_split(
        X_train_val, y_train_val, indices_train_val, test_size=val_ratio/(train_ratio+val_ratio), 
        random_state=42, stratify=y_train_val
    )

    print(f"\nDataset split:")
    print(f"  Training:   {len(X_train)} samples")
    print(f"  Validation: {len(X_val)} samples (for threshold optimization)")
    print(f"  Testing:    {len(X_test)} samples")

    # Cross-Validation for small datasets
    cv_results = {}
    if enable_cross_validation and len(X_train) > 0:
        cv_results = detector.cross_validate(X_train, y_train, cv_folds=min(5, len(X_train)//10))
        
        # Save CV results
        with open(output_path / 'cross_validation_results.json', 'w', encoding='utf-8') as f:
            json.dump(cv_results, f, indent=2, ensure_ascii=False)

    # Train model with validation set for threshold optimization
    print("\n" + "="*70)
    print("TRAINING LIGHTGBM WITH THRESHOLD OPTIMIZATION")
    print("="*70)

    if optimize_thresholds:
        y_train_adj = detector.train(X_train, y_train, X_val, y_val)
    else:
        y_train_adj = detector.train(X_train, y_train)

    # Evaluate
    print("\n" + "="*70)
    print("EVALUATION ON TEST SET - HEADING FOCUS")
    print("="*70)

    # Standard evaluation - FOCUS ON HEADINGS
    metrics = detector.evaluate(X_test, y_test)
    
    # ENHANCED: Heading-specific evaluation
    if len(X_test) > 0 and all_lines:  # Only if we have lines data
        # Get test lines for enhanced evaluation using precomputed indices_test
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            heading_metrics = detector.evaluate_heading_detection(X_test, y_test, test_lines)
            metrics['heading_detection'] = heading_metrics

    # POST-TRAINING CROSS-VERIFICATION (only after model is trained)
    if enable_data_validation and len(X_test) > 0 and all_lines:
        print("\n" + "="*70)
        print("POST-TRAINING CROSS-VERIFICATION - HEADING FOCUS")
        print("="*70)
        
        # Use the precomputed indices_test to get test lines
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            verification_results = detector.data_validator.cross_verify_predictions(
                detector, X_test, y_test, test_lines
            )
            
            print(f"High confidence heading samples: {len(verification_results.get('high_confidence_samples', []))}")
            print(f"Low confidence heading samples: {len(verification_results.get('low_confidence_samples', []))}")
            print(f"Potential heading misclassifications: {len(verification_results.get('potential_misclassifications', []))}")
            
            # Save verification results
            with open(output_path / 'cross_verification_report.json', 'w', encoding='utf-8') as f:
                json.dump(verification_results, f, indent=2, ensure_ascii=False)
        else:
            print("  ⚠ No test lines available for cross-verification")

    # Save all model versions and training info
    training_info = {
        'training_date': datetime.now().isoformat(),
        'dataset_info': {
            'total_samples': len(X_all),
            'training_samples': len(X_train),
            'validation_samples': len(X_val),
            'test_samples': len(X_test),
            'class_distribution': {str(k): int(v) for k, v in zip(unique, counts)},
            'optimal_thresholds': detector.optimal_thresholds
        },
        'model_metrics': metrics,
        'cross_validation_results': cv_results,
        'cache_key': cache_key,
        'data_validation': {
            'overall_quality_score': validation_report.get('overall_quality_score', 0) if enable_data_validation else 'not_performed'
        }
    }
    
    # Save all model versions
    main_model_path = detector.save_all_models(metrics, training_info)

    # Save training info separately
    with open(output_path / 'training_info.json', 'w', encoding='utf-8') as f:
        json.dump(training_info, f, indent=2, ensure_ascii=False)

    # Save metrics as CSV - FOCUS ON HEADING METRICS
    metrics_df = pd.DataFrame([{
        'overall_accuracy': metrics['overall_accuracy'],
        'heading_accuracy': metrics['heading_accuracy'],
        'heading_precision': metrics['heading_precision'],
        'heading_recall': metrics['heading_recall'],
        'heading_f1': metrics['heading_f1']
    }])
    metrics_df.to_csv(output_path / 'metrics_lgb.csv', index=False)

    # Print optimal thresholds
    print(f"\nOptimal Thresholds for Heading Classes:")
    for level, threshold in detector.optimal_thresholds.items():
        print(f"  Level {level}: {threshold:.3f}")

    print("\n✅ Enhanced Training with Threshold Optimization complete!")

    return detector, metrics

def apply_rule_based_filtering(headings):
    """Áp dụng các quy tắc lọc để loại bỏ heading không mong muốn"""
    
    filtered_headings = []
    removal_patterns = [
        r'^Hình\s*\d+[\.\d]*[\.:]?.*$',
        r'^Hình\s*\d+[\.\d]*[\.:]?.*$',
        r'^Figure\s*\d+[\.\d]*[\.:]?.*$',
        r'^Image\s*\d+[\.\d]*[\.:]?.*$',
        r'^Bảng\s*\d+[\.\d]*[\.:]?.*$',
        r'^Table\s*\d+[\.\d]*[\.:]?.*$',
        r'^Phụ lục\s*[A-Z\d][\.:]?.*$',
        r'^Appendix\s*[A-Z\d][\.:]?.*$',
        r'^Trang bìa$',
        r'^Mục lục$',
        r'^Table of Contents$',
        r'^Cover page$',
        r'^Contents$',
        r'^\d+$',
        r'^\.+$',
        r'^…+$',
        r'^\*+$',
        r'^[\d\s\.…\-_]+$',
    ]
    
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in removal_patterns]
    
    removal_keywords = [
        'hình', 'figure', 'image', 'bảng', 'table', 
        'phụ lục', 'appendix', 'biểu đồ', 'chart',
        'đồ thị', 'graph'
    ]
    
    for heading in headings:
        text = heading['text'].strip()
        should_keep = True
        
        for pattern in compiled_patterns:
            if pattern.match(text):
                should_keep = False
                break
        
        if should_keep:
            text_lower = text.lower()
            for keyword in removal_keywords:
                if text_lower.startswith(keyword + ' ') and has_number_after_keyword(text, keyword):
                    should_keep = False
                    break
        
        if should_keep:
            if len(text) < 3 and not is_roman_numeral(text):
                should_keep = False
            elif re.match(r'^[^\w\sÀ-ỹ]+$', text):
                should_keep = False
            elif heading.get('probability', 1.0) < 0.3:
                should_keep = False
        
        if should_keep:
            filtered_headings.append(heading)
    
    return filtered_headings

def has_number_after_keyword(text, keyword):
    """Kiểm tra xem sau keyword có số không"""
    pattern = r'^{}\s*\d+'.format(re.escape(keyword))
    return re.search(pattern, text, re.IGNORECASE) is not None

def is_roman_numeral(text):
    """Kiểm tra xem text có phải là số La Mã không"""
    roman_pattern = r'^[IVXLCDM]+$'
    return re.match(roman_pattern, text.upper()) is not None

def clean_heading_text(headings):
    """Làm sạch text của heading"""
    for heading in headings:
        text = heading['text']
        
        text = re.sub(r'\s*\.+\s*\d+$', '', text)
        text = re.sub(r'\s*…+\s*\d+$', '', text)
        text = re.sub(r'\s*-\s*\d+$', '', text)
        
        text = re.sub(r'^[\.…\s\-_]+', '', text)
        text = re.sub(r'[\.…\s\-_]+$', '', text)
        
        text = re.sub(r'\s+', ' ', text).strip()
        
        heading['text_original'] = heading['text']
        heading['text'] = text
    
    return headings

def process_pdf_file(pdf_file, detector, OUTPUT_DIR):
    """Xử lý một file PDF và lưu kết quả"""
    print(f" Processing: {pdf_file}")
    
    pdf_name = os.path.splitext(os.path.basename(pdf_file))[0]
    pdf_output_dir = os.path.join(OUTPUT_DIR, pdf_name)
    os.makedirs(pdf_output_dir, exist_ok=True)
    
    # Dự đoán headings
    raw_headings = detector.enhanced_predict(pdf_file)
    
    # Áp dụng rule-based filtering
    filtered_headings = apply_rule_based_filtering(raw_headings)
    
    # Làm sạch text heading
    cleaned_headings = clean_heading_text(filtered_headings)
    
    # Chỉ lưu headings_detailed.json
    output_json = os.path.join(pdf_output_dir, "headings_detailed.json")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(cleaned_headings, f, indent=2, ensure_ascii=False)
    
    print(f"Results saved to: {output_json}")
    print(f"Raw headings: {len(raw_headings)} → Filtered: {len(cleaned_headings)}")
    
    return {
        "file_name": pdf_name,
        "raw_headings": len(raw_headings),
        "filtered_headings": len(cleaned_headings)
    }

def main():
    # Tạo thư mục output nếu chưa tồn tại
    INPUT_DIR = Path(r'working\cleaned_pdfs_test')
    
    state = 'test' if 'test' in str(INPUT_DIR).lower() else 'train'
    WORKING_DIR = Path(r'working')
    OUTPUT_DIR = WORKING_DIR / f'output_markdown_detect_{state}'
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 1. Huấn luyện hoặc load model
    training_info = {}
    if not os.path.exists("working/models"):
        print("Training new model...")
        detector, metrics = train_and_evaluate( 
            input_dir='input',
            gt_dir='output',
            use_cached_data=True,
            optimize_thresholds=True
        )
        training_info = {
            "training_date": datetime.now().isoformat(),
            "metrics": metrics,
            "status": "newly_trained"
        }
    else:
        detector = MLHeadingDetector()
        if not detector.load_latest_model():
            print("No trained model found. Please train first.")
            return
        training_info = {
            "training_date": "previously_trained",
            "status": "loaded_existing"
        }
    
    # Lưu thông tin training
    with open(os.path.join(OUTPUT_DIR, "training_info.json"), "w", encoding="utf-8") as f:
        json.dump(training_info, f, indent=2, ensure_ascii=False)
    
    # 2. Xác định thư mục đầu vào
    if not os.path.exists(INPUT_DIR):
        print(f"Input folder '{INPUT_DIR}' not found!")
        return
    
    # 3. Tìm tất cả file PDF trong thư mục
    pdf_files = []
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(INPUT_DIR, file))
    
    if not pdf_files:
        print(f" No PDF files found in '{INPUT_DIR}'")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process")
    
    # 4. Xử lý từng file PDF
    results = []
    for pdf_file in pdf_files:
        try:
            result = process_pdf_file(pdf_file, detector, OUTPUT_DIR)
            results.append(result)
        except Exception as e:
            print(f"Error processing {pdf_file}: {str(e)}")
    
    # 5. In tổng kết
    print(f"\nPROCESSING SUMMARY")
    print(f"====================")
    print(f"Total PDF files processed: {len(results)}")
    for result in results:
        print(f"  - {result['file_name']}: {result['filtered_headings']} headings (from {result['raw_headings']})")

if __name__ == "__main__":
    main()

# ============================================================
# ensemble_model.py
# ============================================================

import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
import warnings
warnings.filterwarnings('ignore')
from lightgbm import LGBMClassifier

# ============================================================================
# PART 1: DATA LOADING (CORRECTED)
# ============================================================================

def load_ground_truth(gt_csv: str) -> pd.DataFrame:
    """
    Load ground truth (only num_correct and answers)
    
    Format:
        num_correct,answers
        1,A
        1,C
        2,AB
    """
    df = pd.read_csv(gt_csv)
    
    # Validate columns
    if 'num_correct' not in df.columns or 'answers' not in df.columns:
        raise ValueError("Ground truth must have 'num_correct' and 'answers' columns")
    
    # Add question_id if not present
    if 'question_id' not in df.columns:
        df.insert(0, 'question_id', range(len(df)))
    
    print(f"✓ Loaded ground truth: {len(df)} questions")
    return df


def load_model_predictions(csv_path: str, model_name: str, n_questions: int) -> pd.DataFrame:
    """
    Load model predictions with probabilities
    
    Format:
        question_id,num_correct,answers,prob_A,prob_B,prob_C,prob_D
        0,1,B,0.0190,0.0370,0.0325,0.0294
    """
    try:
        df = pd.read_csv(csv_path)
        
        # Validate required columns
        required = ['prob_A', 'prob_B', 'prob_C', 'prob_D']
        if not all(col in df.columns for col in required):
            print(f"  [WARN] {model_name}: Missing probability columns, using uniform")
            return create_uniform_predictions(n_questions, model_name)
        
        # Ensure question_id exists
        if 'question_id' not in df.columns:
            df.insert(0, 'question_id', range(len(df)))
        
        # Validate size
        if len(df) != n_questions:
            print(f"  [WARN] {model_name}: Size mismatch ({len(df)} vs {n_questions})")
            if len(df) < n_questions:
                # Pad with uniform
                missing = n_questions - len(df)
                uniform_df = create_uniform_predictions(missing, model_name)
                uniform_df['question_id'] = range(len(df), n_questions)
                df = pd.concat([df, uniform_df], ignore_index=True)
            else:
                df = df.iloc[:n_questions]
        
        print(f"  ✓ {model_name}: Loaded {len(df)} predictions")
        return df
        
    except FileNotFoundError:
        print(f"  [ERROR] {model_name}: File not found, using uniform fallback")
        return create_uniform_predictions(n_questions, model_name)
    except Exception as e:
        print(f"  [ERROR] {model_name}: {str(e)}, using uniform fallback")
        return create_uniform_predictions(n_questions, model_name)


def create_uniform_predictions(n_questions: int, model_name: str) -> pd.DataFrame:
    """Create uniform probability predictions (fallback for crashed models)"""
    print(f"  [INFO] Creating uniform predictions for {model_name}")
    return pd.DataFrame({
        'question_id': range(n_questions),
        'num_correct': [1] * n_questions,
        'answers': ['A'] * n_questions,
        'prob_A': [0.25] * n_questions,
        'prob_B': [0.25] * n_questions,
        'prob_C': [0.25] * n_questions,
        'prob_D': [0.25] * n_questions,
    })


def load_all_models(csv_files: List[Dict[str, str]], n_questions: int) -> List[pd.DataFrame]:
    """
    Load all model predictions with robust error handling
    
    Args:
        csv_files: [{'name': 'model1', 'path': 'model1.csv'}, ...]
        n_questions: Expected number of questions
    """
    print(f"\n{'='*80}")
    print(f"LOADING {len(csv_files)} MODEL PREDICTIONS")
    print(f"{'='*80}")
    
    dfs = []
    for cfg in csv_files:
        df = load_model_predictions(cfg['path'], cfg['name'], n_questions)
        dfs.append(df)
    
    print(f"✓ Loaded {len(dfs)} models\n")
    return dfs

from sklearn.linear_model import LogisticRegression

# ============================================================================
# PART 2: META-MODEL (CORRECTED)
# ============================================================================
from sklearn.neural_network import MLPClassifier

class HalvesOptimizedMetaEnsemble:
    """
    Two-stage meta-ensemble for halves scoring
    
    Training:
    - Features: Model probabilities (prob_A, prob_B, prob_C, prob_D from each model)
    - Labels: Ground truth (num_correct, answers)
    
    Inference:
    - Stage 1: Predict num_correct
    - Stage 2: Predict which options are correct
    - Stage 3: Select answers with halves-aware strategy
    """
    
    def __init__(self):
        # Stage 1: Predict num_correct (1, 2, or 3)


        # Stage 1: Dự đoán số câu đúng
        self.num_correct_model = MLPClassifier(
            hidden_layer_sizes=(8, 4),
            activation='relu',
            alpha=1e-3,
            learning_rate_init=1e-3,
            max_iter=2000,
            early_stopping=True,
            n_iter_no_change=20,
            random_state=42
        )

        # Stage 2: Bộ phân loại nhị phân cho từng lựa chọn
        self.option_models = {
            'A': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42),
            'B': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42),
            'C': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42),
            'D': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42)
        }

        
        self.scaler_num = StandardScaler()
        self.scaler_opt = StandardScaler()
        self.trained = False
    
    def extract_num_correct_features(self, dfs: List[pd.DataFrame], idx: int) -> np.ndarray:
        """
        Extract features for predicting num_correct
        
        Uses ONLY model probabilities (no ground truth info)
        """
        features = []
        n_models = len(dfs)
        
        # Collect all probabilities from all models
        all_probs = []
        for df in dfs:
            row = df.iloc[idx]
            probs = [row['prob_A'], row['prob_B'], row['prob_C'], row['prob_D']]
            all_probs.append(probs)
        
        all_probs = np.array(all_probs)  # Shape: (n_models, 4)
        
        # Feature 1: Raw probabilities from each model (flattened)
        features.extend(all_probs.flatten())
        
        # Feature 2: Per-model statistics
        max_per_model = all_probs.max(axis=1)
        features.extend([
            max_per_model.mean(),
            max_per_model.std(),
            max_per_model.max(),
            max_per_model.min()
        ])
        
        # Feature 3: Confidence gap (top-1 vs top-2) per model
        gaps = []
        for probs in all_probs:
            sorted_probs = np.sort(probs)[::-1]
            gap = sorted_probs[0] - sorted_probs[1] if len(sorted_probs) > 1 else sorted_probs[0]
            gaps.append(gap)
        
        features.extend([
            np.mean(gaps),
            np.std(gaps),
            np.max(gaps),
            np.min(gaps)
        ])
        
        # Feature 4: High-confidence counts
        for threshold in [0.4, 0.5, 0.6, 0.7]:
            high_conf = (all_probs > threshold).sum()
            features.append(high_conf / (n_models * 4))
        
        # Feature 5: Per-option aggregated stats (cross-model)
        for opt_idx in range(4):
            opt_probs = all_probs[:, opt_idx]
            features.extend([
                opt_probs.mean(),
                opt_probs.std(),
                opt_probs.max(),
                opt_probs.min(),
                (opt_probs > 0.5).sum() / n_models
            ])
        
        # Feature 6: Distribution statistics
        avg_probs = all_probs.mean(axis=0)
        avg_probs_norm = avg_probs / (avg_probs.sum() + 1e-10)
        entropy = -np.sum(avg_probs_norm * np.log(avg_probs_norm + 1e-10))
        features.append(entropy)
        
        # Feature 7: Model agreement
        if n_models > 1:
            corrs = []
            for i in range(n_models):
                for j in range(i+1, n_models):
                    corr = np.corrcoef(all_probs[i], all_probs[j])[0, 1]
                    corrs.append(corr if not np.isnan(corr) else 0.0)
            features.extend([
                np.mean(corrs),
                np.std(corrs)
            ])
        else:
            features.extend([0.0, 0.0])
        
        return np.array(features)
    
    def extract_option_features(self, dfs: List[pd.DataFrame], idx: int, option: str) -> np.ndarray:
        """
        Extract features for predicting if specific option is correct
        
        Uses ONLY model probabilities
        """
        features = []
        n_models = len(dfs)
        
        # Raw probabilities for this option from all models
        opt_probs = [df.iloc[idx][f'prob_{option}'] for df in dfs]
        features.extend(opt_probs)
        
        # Statistics
        features.extend([
            np.mean(opt_probs),
            np.std(opt_probs),
            np.max(opt_probs),
            np.min(opt_probs),
            np.median(opt_probs)
        ])
        
        # Agreement
        for threshold in [0.4, 0.5, 0.6]:
            features.append(sum([1 for p in opt_probs if p > threshold]) / n_models)
        
        # Relative ranking
        rankings = []
        for df in dfs:
            row = df.iloc[idx]
            probs = [row['prob_A'], row['prob_B'], row['prob_C'], row['prob_D']]
            rank = sorted(range(4), key=lambda i: probs[i], reverse=True).index(ord(option) - ord('A'))
            rankings.append(rank)
        
        features.extend([
            np.mean(rankings),
            np.std(rankings),
            (np.array(rankings) == 0).sum() / n_models,  # Top-1 rate
            (np.array(rankings) <= 1).sum() / n_models   # Top-2 rate
        ])
        
        # Comparative features (vs other options)
        all_probs = []
        for df in dfs:
            row = df.iloc[idx]
            all_probs.append([row['prob_A'], row['prob_B'], row['prob_C'], row['prob_D']])
        
        all_probs = np.array(all_probs)
        opt_idx = ord(option) - ord('A')
        
        # Gaps to other options
        gaps_to_others = []
        for other_idx in range(4):
            if other_idx != opt_idx:
                gap = (all_probs[:, opt_idx] - all_probs[:, other_idx]).mean()
                gaps_to_others.append(gap)
        
        features.extend([
            np.mean(gaps_to_others),
            np.max(gaps_to_others),
            np.min(gaps_to_others)
        ])
        
        return np.array(features)
    
    def train(self, dfs_train: List[pd.DataFrame], gt_df: pd.DataFrame):
        """
        Train meta-model
        
        Args:
            dfs_train: Model predictions (with probabilities)
            gt_df: Ground truth (only num_correct and answers)
        """
        print(f"\n{'='*80}")
        print("TRAINING HALVES-OPTIMIZED META-ENSEMBLE")
        print(f"{'='*80}")
        
        n_questions = len(gt_df)
        
        # Validate alignment
        if len(dfs_train[0]) != n_questions:
            raise ValueError(f"Size mismatch: models={len(dfs_train[0])}, gt={n_questions}")
        
        # ===== STAGE 1: Train num_correct predictor =====
        print("\n[Stage 1] Training num_correct predictor...")
        
        X_num = []
        y_num = []
        
        for i in range(n_questions):
            features = self.extract_num_correct_features(dfs_train, i)
            X_num.append(features)
            
            # Label from ground truth
            y_num.append(int(gt_df.iloc[i]['num_correct']))
        
        X_num = np.array(X_num)
        y_num = np.array(y_num)
        
        # Normalize
        X_num = self.scaler_num.fit_transform(X_num)
        
        # Train
        self.num_correct_model.fit(X_num, y_num)
        
        # Evaluate
        y_num_pred = self.num_correct_model.predict(X_num)
        acc = accuracy_score(y_num, y_num_pred)
        print(f"  ✓ num_correct train accuracy: {acc:.4f}")
        
        # Distribution
        unique, counts = np.unique(y_num, return_counts=True)
        print(f"  True distribution: {dict(zip(unique, counts))}")
        unique_pred, counts_pred = np.unique(y_num_pred, return_counts=True)
        print(f"  Pred distribution: {dict(zip(unique_pred, counts_pred))}")
        
        # ===== STAGE 2: Train per-option models =====
        print("\n[Stage 2] Training per-option models...")
        
        for option in ['A', 'B', 'C', 'D']:
            X_opt = []
            y_opt = []
            
            for i in range(n_questions):
                features = self.extract_option_features(dfs_train, i, option)
                X_opt.append(features)
                
                # Label: 1 if option is in ground truth answers, 0 otherwise
                gt_answers = str(gt_df.iloc[i]['answers']).upper()
                y_opt.append(1 if option in gt_answers else 0)
            
            X_opt = np.array(X_opt)
            y_opt = np.array(y_opt)
            
            # Normalize
            X_opt = self.scaler_opt.fit_transform(X_opt)
            
            # Train
            self.option_models[option].fit(X_opt, y_opt)
            
            # Evaluate
            y_opt_pred = self.option_models[option].predict(X_opt)
            acc = accuracy_score(y_opt, y_opt_pred)
            f1 = f1_score(y_opt, y_opt_pred, zero_division=0)
            pos_rate = y_opt.mean()
            
            print(f"  ✓ Option {option}: acc={acc:.4f}, f1={f1:.4f}, pos_rate={pos_rate:.3f}")
        
        self.trained = True
        print(f"\n✓ Meta-model training complete\n")
    
    def predict_with_halves_optimization(self, dfs_test: List[pd.DataFrame], 
                                        conservative_factor: float = 0.15) -> pd.DataFrame:
        """
        Predict with halves-aware strategy
        """
        if not self.trained:
            raise RuntimeError("Model not trained. Call train() first.")
        
        n_questions = len(dfs_test[0])
        results = []
        
        for i in range(n_questions):
            # Stage 1: Predict num_correct
            features_num = self.extract_num_correct_features(dfs_test, i)
            features_num = self.scaler_num.transform([features_num])
            
            predicted_num = self.num_correct_model.predict(features_num)[0]
            num_correct_probs = self.num_correct_model.predict_proba(features_num)[0]
            
            # Stage 2: Get option probabilities
            option_probs = {}
            for option in ['A', 'B', 'C', 'D']:
                features_opt = self.extract_option_features(dfs_test, i, option)
                features_opt = self.scaler_opt.transform([features_opt])
                prob = self.option_models[option].predict_proba(features_opt)[0][1]
                option_probs[option] = float(prob)
            
            # Stage 3: Halves-optimized selection
            sorted_options = sorted(option_probs.items(), key=lambda x: x[1], reverse=True)
            
            # Strategy: Evaluate expected halves score for k=1,2,3
            best_selection = []
            best_score = -1
            
            for k in range(1, 4):  # Try 1, 2, or 3 options
                selected = [opt for opt, _ in sorted_options[:k]]
                selected_probs = [option_probs[opt] for opt in selected]
                
                # Expected metrics
                expected_correct = sum(selected_probs)
                expected_wrong = k - expected_correct
                
                # Penalty for mismatch with predicted_num
                num_penalty = abs(k - predicted_num) * 0.3
                
                # Expected halves score
                expected_error = num_penalty + expected_wrong
                
                if expected_error < 0.7:
                    score = 1.0 - conservative_factor * (k - 1)
                elif expected_error < 1.5:
                    score = 0.5 - conservative_factor * (k - 1)
                else:
                    score = 0.0 - conservative_factor * k
                
                if score > best_score:
                    best_score = score
                    best_selection = selected
            
            # Fallback
            if not best_selection:
                best_selection = [sorted_options[0][0]]
            
            # Cap at 3 answers
            if len(best_selection) > 3:
                best_selection = best_selection[:3]
            
            results.append({
                'question_id': i,
                'num_correct': len(best_selection),
                'answers': ''.join(sorted(best_selection)),
                'prob_A': option_probs['A'],
                'prob_B': option_probs['B'],
                'prob_C': option_probs['C'],
                'prob_D': option_probs['D']
            })
        
        return pd.DataFrame(results)


# ============================================================================
# COMPLETE PIPELINE WITH EVALUATION
# ============================================================================

def run_meta_ensemble_with_evaluation(
    csv_files: List[Dict[str, str]],
    gt_csv: str,
    output_csv: str,
    conservative_factor: float = 0.15
):
    """
    Complete pipeline: Train → Predict → Evaluate
    """
    print(f"\n{'='*80}")
    print("META-ENSEMBLE PIPELINE WITH EVALUATION")
    print(f"{'='*80}")
    
    # Load ground truth
    gt_df = load_ground_truth(gt_csv)
    n_questions = len(gt_df)
    
    # Load model predictions
    dfs = load_all_models(csv_files, n_questions)
    
    # Train meta-ensemble
    ensemble = HalvesOptimizedMetaEnsemble()
    ensemble.train(dfs, gt_df)
    
    # Predict
    result_df = ensemble.predict_with_halves_optimization(
        dfs, 
        conservative_factor=conservative_factor
    )
    
    # Save
    result_df.to_csv(output_csv, index=False)
    print(f"✓ Saved predictions to: {output_csv}\n")
    
    # Evaluate
    per_q_df, by_k_df, summary, n = evaluate_halves_optimized(gt_csv, output_csv)
    print_evaluation_report(summary, by_k_df)
    
    # Save evaluation results
    per_q_df.to_csv(output_csv.replace('.csv', '_per_question.csv'), index=False)
    wrong_df = per_q_df[per_q_df['halves_score'] < 1.0]
    wrong_df.to_csv(output_csv.replace('.csv', '_wrong.csv'), index=False)
    
    return ensemble, result_df, summary


def tune_conservative_factor(
    ensemble: HalvesOptimizedMetaEnsemble,
    dfs: List[pd.DataFrame],
    gt_csv: str,
    output_dir: str = '.'
):
    """
    Grid search for best conservative_factor
    """
    print(f"\n{'='*80}")
    print("TUNING CONSERVATIVE FACTOR")
    print(f"{'='*80}")
    
    results = []
    
    for cf in [0.0,0.3,0.6,0.9]:
        # Predict with this factor
        pred_df = ensemble.predict_with_halves_optimization(dfs, conservative_factor=cf)
        pred_path = f'{output_dir}/pred_cf_{cf:.2f}.csv'
        pred_df.to_csv(pred_path, index=False)
        
        # Evaluate
        _, _, summary, _ = evaluate_halves_optimized(gt_csv, pred_path)
        
        results.append({
            'conservative_factor': cf,
            'halves_score': summary['official_halves_mean'],
            'exact_match': summary['exact_match_accuracy'],
            'one_error': summary['one_error_rate'],
            'two_plus_error': summary['two_plus_error_rate']
        })
        
        print(f"CF={cf:.2f}: Halves={summary['official_halves_mean']:.4f}, "
              f"Exact={summary['exact_match_accuracy']:.4f}, "
              f"e≥2={summary['two_plus_error_rate']:.4f}")
    
    # Find best
    results_df = pd.DataFrame(results)
    best_idx = results_df['halves_score'].idxmax()
    best_cf = results_df.iloc[best_idx]['conservative_factor']
    best_score = results_df.iloc[best_idx]['halves_score']
    
    print(f"\n✓ Best conservative_factor: {best_cf:.2f} (score: {best_score:.4f})")
    
    # Save tuning results
    results_df.to_csv(f'{output_dir}/tuning_results.csv', index=False)
    
    return best_cf, results_df


import pandas as pd
import numpy as np
import pickle
from typing import List, Dict , Optional
from pathlib import Path


# ============================================================================
# PART 1: SAVE/LOAD TRAINED MODEL
# ============================================================================

def save_trained_ensemble(ensemble, save_path: str):
    """
    Save trained meta-ensemble to disk
    
    Args:
        ensemble: Trained HalvesOptimizedMetaEnsemble or AdvancedHalvesMetaEnsemble
        save_path: Path to save (e.g., 'trained_models/ensemble.pkl')
    """
    if not ensemble.trained:
        raise RuntimeError("Cannot save untrained model")
    
    # Create directory if not exists
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Save entire object
    with open(save_path, 'wb') as f:
        pickle.dump(ensemble, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    print(f"✓ Saved trained ensemble to: {save_path}")
    print(f"  Model type: {type(ensemble).__name__}")
    print(f"  File size: {Path(save_path).stat().st_size / 1024:.2f} KB")


def load_trained_ensemble(load_path: str):
    """
    Load trained meta-ensemble from disk
    
    Args:
        load_path: Path to saved model
    
    Returns:
        Trained ensemble object
    """
    if not Path(load_path).exists():
        raise FileNotFoundError(f"Model file not found: {load_path}")
    
    with open(load_path, 'rb') as f:
        ensemble = pickle.load(f)
    
    if not ensemble.trained:
        raise RuntimeError("Loaded model is not trained")
    
    print(f"✓ Loaded trained ensemble from: {load_path}")
    print(f"  Model type: {type(ensemble).__name__}")
    
    return ensemble


# ============================================================================
# PART 2: INFERENCE ON TEST SET (NO GROUND TRUTH)
# ============================================================================

def inference_on_test_set(
    ensemble,
    test_csv_files: List[Dict[str, str]],
    output_csv: str,
    conservative_factor: float = 0.10,
    n_questions: Optional[int] = None
):
    """
    Inference on test set using trained ensemble
    
    Args:
        ensemble: Trained meta-ensemble (loaded or just trained)
        test_csv_files: [{'name': 'model1', 'path': 'test/model1.csv'}, ...]
        output_csv: Output predictions path
        conservative_factor: Conservative factor (from tuning)
        n_questions: Number of questions (auto-detect if None)
    
    Returns:
        DataFrame with predictions
    """
    print(f"\n{'='*80}")
    print("INFERENCE ON TEST SET")
    print(f"{'='*80}")
    
    # Auto-detect n_questions from first valid file
    if n_questions is None:
        for cfg in test_csv_files:
            try:
                df_temp = pd.read_csv(cfg['path'])
                n_questions = len(df_temp)
                print(f"Auto-detected {n_questions} questions from {cfg['name']}")
                break
            except:
                continue
        
        if n_questions is None:
            raise ValueError("Cannot auto-detect n_questions. Please provide manually.")
    
    # Load test predictions
    print(f"\nLoading {len(test_csv_files)} test model predictions...")
    test_dfs = load_all_models(test_csv_files, n_questions)
    
    # Predict
    print(f"\nRunning inference with CF={conservative_factor:.2f}...")
    
    # Choose prediction method based on ensemble type
    if hasattr(ensemble, 'predict_with_adaptive_strategy'):
        # AdvancedHalvesMetaEnsemble
        result_df = ensemble.predict_with_adaptive_strategy(
            test_dfs, 
            conservative_factor=conservative_factor
        )
    else:
        # HalvesOptimizedMetaEnsemble
        result_df = ensemble.predict_with_halves_optimization(
            test_dfs,
            conservative_factor=conservative_factor
        )
    
    # Save
    result_df.to_csv(output_csv, index=False)
    print(f"\n✓ Saved test predictions to: {output_csv}")
    print(f"  Total questions: {len(result_df)}")
    
    # Distribution analysis
    num_correct_dist = result_df['num_correct'].value_counts().sort_index()
    print(f"\nPredicted num_correct distribution:")
    for k, count in num_correct_dist.items():
        print(f"  k={k}: {count} questions ({count/len(result_df)*100:.1f}%)")
    
    return result_df


# ============================================================================
# PART 3: COMPLETE WORKFLOW
# ============================================================================

def train_and_save_workflow(
    train_csv_files: List[Dict[str, str]],
    gt_csv: str,
    model_save_path: str = 'trained_models/ensemble.pkl',
    tune_cf: bool = True
):
    """
    Complete training workflow:
    1. Train on validation set
    2. Tune conservative_factor
    3. Save trained model
    4. Return best CF
    """
    print(f"\n{'='*80}")
    print("TRAINING WORKFLOW")
    print(f"{'='*80}")
    
    # Load data
    gt_df = load_ground_truth(gt_csv)
    train_dfs = load_all_models(train_csv_files, len(gt_df))
    
    # Train
    print("\n[Step 1/3] Training meta-ensemble...")
    ensemble = HalvesOptimizedMetaEnsemble()  # or AdvancedHalvesMetaEnsemble()
    ensemble.train(train_dfs, gt_df)
    
    # Tune CF
    best_cf = 0.10  # Default
    if tune_cf:
        print("\n[Step 2/3] Tuning conservative_factor...")
        best_cf, _ = tune_conservative_factor(
            ensemble=ensemble,
            dfs=train_dfs,
            gt_csv=gt_csv,
            output_dir='tuning'
        )
    
    # Save
    print("\n[Step 3/3] Saving trained model...")
    save_trained_ensemble(ensemble, model_save_path)
    
    print(f"\n{'='*80}")
    print("TRAINING COMPLETE")
    print(f"{'='*80}")
    print(f"Model saved to: {model_save_path}")
    print(f"Best conservative_factor: {best_cf:.2f}")
    
    return ensemble, best_cf


def inference_workflow(
    model_path: str,
    test_csv_files: List[Dict[str, str]],
    output_csv: str,
    conservative_factor: float = 0.10
):
    """
    Complete inference workflow:
    1. Load trained model
    2. Run inference on test set
    3. Save predictions
    """
    print(f"\n{'='*80}")
    print("INFERENCE WORKFLOW")
    print(f"{'='*80}")
    
    # Load trained model
    print("[Step 1/2] Loading trained model...")
    ensemble = load_trained_ensemble(model_path)
    
    # Inference
    print("\n[Step 2/2] Running inference...")
    result_df = inference_on_test_set(
        ensemble=ensemble,
        test_csv_files=test_csv_files,
        output_csv=output_csv,
        conservative_factor=conservative_factor
    )
    
    print(f"\n{'='*80}")
    print("INFERENCE COMPLETE")
    print(f"{'='*80}")
    print(f"Predictions saved to: {output_csv}")
    
    return result_df


# ============================================================================
# MAIN USAGE - TWO SCENARIOS
# ============================================================================

if __name__ == "__main__":

    val_csv_files = [
        {'name': 'model1', 'path': 'val/model_Qwen3-4b_results_vn.csv'},
        {'name': 'model2', 'path': 'val/Qwen2.5-3B.csv'},
        {'name': 'model3', 'path': 'val/model_Qwen3-4b_results.csv'},
    ]
    
    # Train and save
    trained_ensemble, best_cf = train_and_save_workflow(
        train_csv_files=val_csv_files,
        gt_csv='ground_truth.csv',
        model_save_path='trained_models/meta_ensemble.pkl',
        tune_cf=True  # Tune conservative_factor
    )
    # ========================================================================
    # SCENARIO 2: INFERENCE PHASE (PRODUCTION)
    # ========================================================================
    
    print("\n" + "="*80)
    print("SCENARIO 2: INFERENCE PHASE")
    print("="*80)
    
# Test set predictions (KHÔNG có ground truth)
test_csv_files = [
    {'name': 'model1', 'path': 'test/model_Qwen3-4b_results_vn.csv'},
    {'name': 'model2', 'path': 'test/Qwen2.5-3B.csv'},
    {'name': 'model3', 'path': 'test/model_Qwen3-4b_results.csv'}
]

# Load trained model and inference
test_predictions = inference_workflow(
    model_path='trained_models/meta_ensemble.pkl',
    test_csv_files=test_csv_files,
    output_csv='test_predictions.csv',
    conservative_factor=best_cf  # Use best CF from training
)

print("\n✓ ALL DONE!")
print(f"\nFiles created:")
print(f"  - trained_models/meta_ensemble.pkl (trained model)")
print(f"  - test_predictions.csv (final submission)")


# ============================================================
# inject_font.py
# ============================================================

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

# ============================================================
# inject_table.py
# ============================================================

import re
import json
import os
from typing import List, Dict, Optional
import pymupdf
import html
from bs4 import BeautifulSoup

# ==============================================================================
# HELPER: PHÁT HIỆN BẢNG TRIVIAL 
# ==============================================================================

def is_trivial_table_html(table_html: str) -> bool:
    soup = BeautifulSoup(table_html, 'html.parser')
    cells = [cell.get_text(strip=True) for cell in soup.find_all('td')]
    
    if not cells or all(cell == "" for cell in cells):
        return True
    
    numeric_only = all(re.match(r'^[\d.,\s-]*$', cell) or cell == "" for cell in cells)
    if numeric_only:
        return True
    
    rows = soup.find_all('tr')
    if rows and all(len(row.find_all('td')) <= 1 for row in rows):
        return True
    
    return False

import re
from typing import List

def is_trivial_pdf_table(table_data: List[List[str]]) -> bool:
    """Phát hiện bảng trivial TRONG PDF (dùng cùng logic với HTML)"""
    if not table_data:
        return True
    
    # Check for empty table
    if all(not row for row in table_data):
        return True
    
    all_cells = [cell for row in table_data for cell in row]
    non_empty = [cell for cell in all_cells if cell.strip() != ""]
    
    if not non_empty:
        return True
    
    # Check if all non-empty cells contain only numbers and basic punctuation
    numeric_only = all(re.match(r'^[\d.,\s-]*$', cell.strip()) for cell in non_empty)
    if numeric_only:
        return True
    
    # Check if all rows have only 0 or 1 columns (not really a table)
    if all(len(row) <= 1 for row in table_data):
        return True
    
    return False

# ==============================================================================
# PHASE 1: TRÍCH XUẤT BẢNG TỪ PDF (GIỮ NGUYÊN THỨ TỰ)
# ==============================================================================

def extract_raw_tables_from_pdf(pdf_path: str) -> List[List[List[str]]]:
    doc = pymupdf.open(pdf_path)
    all_tables = []
    
    print(f"📄 Đang trích xuất bảng thô từ PDF: {pdf_path}")
    
    for page_num, page in enumerate(doc, 1):
        tables = page.find_tables()
        if not tables:
            continue
        
        for i, table in enumerate(tables):
            raw_data = table.extract()
            clean_data = [
                [str(cell) if cell is not None else "" for cell in row]
                for row in raw_data
            ]
            all_tables.append(clean_data)
            print(f"  - Trang {page_num}, Bảng {i+1}: {len(clean_data)} hàng, {max(len(r) for r in clean_data) if clean_data else 0} cột")
    
    doc.close()
    print(f"\n✅ Tổng cộng: {len(all_tables)} bảng thô từ PDF (chưa lọc).")
    return all_tables

# ==============================================================================
# PHASE 2: PHÂN TÍCH MARKDOWN - GIỮ NGUYÊN THỨ TỰ VỊ TRÍ
# ==============================================================================

def extract_table_positions_from_raw_md(md_content: str) -> List[Dict]:
    """Trích xuất vị trí bảng TRONG FILE GỐC THEO THỨ TỰ XUẤT HIỆN"""
    patterns = [
        r'(<table\b[^<]*(?:(?!</table>)<[^<]*)*</table>)',  # HTML table
        r'(\|.*\|(?:\n\|[-: ]+\|)+\n(?:\|.*\|\n*)+)'        # Markdown table syntax
    ]
    
    positions = []
    current_index = 0
    
    while current_index < len(md_content):
        earliest_match = None
        
        for pattern in patterns:
            regex = re.compile(pattern, re.DOTALL)
            match = regex.search(md_content, current_index)
            if match and (earliest_match is None or match.start() < earliest_match.start()):
                earliest_match = match
        
        if earliest_match is None:
            break
        
        start_pos = earliest_match.start()
        end_pos = earliest_match.end()
        table_content = earliest_match.group(0)
        is_html = table_content.startswith("<table")
        
        positions.append({
            "start_pos": start_pos,
            "end_pos": end_pos,
            "content": table_content,
            "is_html": is_html,
            "is_trivial": is_trivial_table_html(table_content) if is_html else False
        })
        
        current_index = end_pos
    
    return positions

# ==============================================================================
# PHASE 3: GHÉP BẢNG PDF THEO THỨ TỰ TUYỆT ĐỐI
# ==============================================================================

def merge_pdf_tables_in_order(
    pdf_tables: List[List[List[str]]],
    num_target_tables: int
) -> List[List[List[str]]]:
    """Ghép bảng PDF GIỮ NGUYÊN THỨ TỰ XUẤT HIỆN"""
    non_trivial_pdf_tables = [t for t in pdf_tables if not is_trivial_pdf_table(t)]
    if not non_trivial_pdf_tables:
        return []
    
    num_pdf_tables = len(non_trivial_pdf_tables)
    if num_target_tables <= 0:
        return []
    
    merged_groups = []
    tables_per_group = max(1, num_pdf_tables // num_target_tables)
    start_idx = 0
    
    for i in range(num_target_tables):
        end_idx = min(start_idx + tables_per_group, num_pdf_tables)
        group_tables = non_trivial_pdf_tables[start_idx:end_idx]
        
        if group_tables:
            merged_table = []
            for table_idx, table in enumerate(group_tables):
                for row_idx, row in enumerate(table):
                    if table_idx > 0 and row_idx == 0 and is_header_like(row, merged_table[0] if merged_table else []):
                        continue
                    merged_table.append(row)
            merged_groups.append(merged_table)
        else:
            merged_groups.append([])
        
        start_idx = end_idx
    
    return merged_groups

def is_header_like(row: List[str], reference_header: List[str]) -> bool:
    if not reference_header or len(row) < len(reference_header):
        return False
    
    matches = 0
    for i, ref_cell in enumerate(reference_header):
        if i >= len(row):
            break
        cell = row[i].strip().lower()
        ref = ref_cell.strip().lower()
        if cell and ref and (cell == ref or ref in cell or cell in ref):
            matches += 1
    
    return matches >= len(reference_header) * 0.7

# ==============================================================================
# PHASE 4: THAY THẾ BẢNG THEO ĐÚNG VỊ TRÍ (KHÔNG ĐẢO THỨ TỰ)
# ==============================================================================

import html
from typing import List

def render_pdf_table_as_html(table_data: List[List[str]], has_header: bool = False) -> str:
    """Render bảng PDF thành HTML với đầy đủ tính năng"""
    if not table_data:
        return "<table></table>"
    
    num_cols = max(len(row) for row in table_data)
    html_lines = ['<table style="width:100%;">', "<colgroup>"]
    html_lines.extend(["<col/>"] * num_cols)
    html_lines.append("</colgroup>")
    
    # Xử lý header nếu có
    if has_header and table_data:
        html_lines.append("<thead>")
        header_row = table_data[0]
        html_lines.append("<tr>")
        for i in range(num_cols):
            cell = header_row[i] if i < len(header_row) else ""
            cell_content = html.escape(cell.strip()) if cell.strip() else "&nbsp;"
            html_lines.append(f'<th><strong>{cell_content}</strong></th>')
        html_lines.append("</tr>")
        html_lines.append("</thead>")
        table_data = table_data[1:]  # Bỏ header row
    
    # Xử lý body
    html_lines.append("<tbody>")
    for row in table_data:
        html_lines.append("<tr>")
        for i in range(num_cols):
            cell = row[i] if i < len(row) else ""
            cell_content = html.escape(cell.strip()) if cell.strip() else "&nbsp;"
            html_lines.append(f"<td>{cell_content}</td>")
        html_lines.append("</tr>")
    
    html_lines.append("</tbody></table>")
    return "\n".join(html_lines)

def replace_tables_in_correct_order(
    md_content: str,
    table_positions: List[Dict],
    merged_tables: List[List[List[str]]]
) -> str:
    """
    THAY THẾ BẢNG THEO ĐÚNG THỨ TỰ TỪ TRÊN XUỐNG DƯỚI:
    1. Chuẩn bị danh sách replacement trước
    2. Thay thế TỪ CUỐI LÊN ĐẦU để tránh lệch index
    3. Đảm bảo thứ tự bảng không đổi
    """
    # Bước 1: Chuẩn bị replacement cho từng vị trí bảng
    replacements = []
    merged_idx = 0
    
    for pos in table_positions:
        if pos["is_trivial"]:
            replacements.append("")  # Xóa bảng trivial
        else:
            if merged_idx < len(merged_tables):
                replacements.append(render_pdf_table_as_html(merged_tables[merged_idx]))
                merged_idx += 1
            else:
                replacements.append(pos["content"])  # Giữ nguyên nếu không đủ bảng PDF
    
    # Bước 2: Thay thế từ cuối lên đầu (để không lệch index)
    result = md_content
    for i in range(len(table_positions) - 1, -1, -1):
        pos = table_positions[i]
        replacement = replacements[i]
        result = result[:pos["start_pos"]] + replacement + result[pos["end_pos"]:]
    
    return result

# ==============================================================================
# MAIN PIPELINE (ĐẢM BẢO THỨ TỰ TUYỆT ĐỐI)
# ==============================================================================

def process_document(
    md_path: str,
    pdf_path: str,
    output_md_path: str,
    audit_path: Optional[str] = None
):
    """Pipeline chính - ĐẢM BẢO THỨ TỰ TỪ TRÊN XUỐNG DƯỚI"""
    # Bước 1: Đọc file Markdown GỐC
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Bước 2: Trích xuất vị trí bảng THEO THỨ TỰ XUẤT HIỆN
    table_positions = extract_table_positions_from_raw_md(md_content)
    
    if not table_positions:
        print("❗ Không tìm thấy bảng. Giữ nguyên file gốc.")
        os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return
    
    # Bước 3: Đếm số bảng KHÔNG TRIVIAL
    non_trivial_positions = [pos for pos in table_positions if not pos["is_trivial"]]
    num_target_tables = len(non_trivial_positions)
    
    # Bước 4: Xử lý trường hợp tất cả bảng đều trivial
    if num_target_tables == 0:
        print("❗ Tất cả bảng đều trivial. Xóa toàn bộ bảng.")
        final_content = replace_tables_in_correct_order(md_content, table_positions, [])
        os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        return
    
    # Bước 5: Trích xuất bảng từ PDF
    pdf_tables = extract_raw_tables_from_pdf(pdf_path)
    if not pdf_tables:
        print("❗ Không có bảng trong PDF. Giữ nguyên file gốc.")
        os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return
    
    # Bước 6: Ghép bảng PDF THEO THỨ TỰ
    merged_tables = merge_pdf_tables_in_order(pdf_tables, num_target_tables)
    if not merged_tables:
        print("❗ Không có bảng hợp lệ sau khi ghép. Giữ nguyên file gốc.")
        os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return
    
    # Bước 7: Thay thế vào file gốc THEO ĐÚNG VỊ TRÍ
    final_content = replace_tables_in_correct_order(md_content, table_positions, merged_tables)
    
    # Bước 8: Lưu kết quả
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    
    # Bước 9: Audit log
    if audit_path:
        audit_data = {
            "total_md_tables": len(table_positions),
            "trivial_md_tables": len(table_positions) - num_target_tables,
            "non_trivial_md_tables": num_target_tables,
            "total_pdf_tables": len(pdf_tables),
            "merged_tables_count": len(merged_tables),
            "table_mapping": [
                {
                    "md_position": i+1,
                    "start": pos["start_pos"],
                    "end": pos["end_pos"],
                    "is_trivial": pos["is_trivial"],
                    "used_pdf_table": bool(not pos["is_trivial"] and i < len(merged_tables))
                }
                for i, pos in enumerate(table_positions)
            ]
        }
        os.makedirs(os.path.dirname(audit_path), exist_ok=True)
        with open(audit_path, "w", encoding="utf-8") as f:
            json.dump(audit_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ HOÀN TẤT! Kết quả đã giữ nguyên thứ tự từ trên xuống dưới.")
    print(f"📁 File kết quả: {output_md_path}")

def process_single_document(md_path: str, pdf_path: str, audit_path: Optional[str] = None):
    """Xử lý một tài liệu duy nhất - DÙNG ĐỂ GHI ĐÈ FILE GỐC"""
    try:
        # Bước 1: Đọc file Markdown gốc
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        # Bước 2: Trích xuất vị trí bảng
        table_positions = extract_table_positions_from_raw_md(md_content)
        if not table_positions:
            print(f"ℹ️  Bỏ qua {os.path.basename(md_path)}: Không có bảng")
            return False
        
        # Bước 3: Xử lý bảng trivial
        non_trivial_positions = [pos for pos in table_positions if not pos["is_trivial"]]
        num_target_tables = len(non_trivial_positions)
        
        if num_target_tables == 0:
            print(f"ℹ️  Bỏ qua {os.path.basename(md_path)}: Tất cả bảng đều trivial")
            # Xóa toàn bộ bảng trivial
            final_content = replace_tables_in_correct_order(md_content, table_positions, [])
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(final_content)
            return True
        
        # Bước 4: Trích xuất bảng từ PDF
        if not os.path.exists(pdf_path):
            print(f"⚠️  Bỏ qua {os.path.basename(md_path)}: File PDF không tồn tại: {pdf_path}")
            return False
        
        pdf_tables = extract_raw_tables_from_pdf(pdf_path)
        if not pdf_tables:
            print(f"⚠️  Bỏ qua {os.path.basename(md_path)}: PDF không có bảng")
            return False
        
        # Bước 5: Ghép bảng theo thứ tự
        merged_tables = merge_pdf_tables_in_order(pdf_tables, num_target_tables)
        if not merged_tables:
            print(f"⚠️  Bỏ qua {os.path.basename(md_path)}: Không tạo được bảng hợp lệ")
            return False
        
        # Bước 6: Thay thế vào file gốc
        final_content = replace_tables_in_correct_order(md_content, table_positions, merged_tables)
        
        # Bước 7: GHI ĐÈ TRỰC TIẾP VÀO FILE GỐC
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        
        # Bước 8: Audit log
        if audit_path:
            os.makedirs(os.path.dirname(audit_path), exist_ok=True)
            audit_data = {
                "source_md": md_path,
                "source_pdf": pdf_path,
                "total_tables": len(table_positions),
                "trivial_tables": len(table_positions) - num_target_tables,
                "processed_tables": num_target_tables,
                "pdf_tables_used": len(merged_tables),
                "processing_time": os.path.getmtime(md_path)
            }
            with open(audit_path, "w", encoding="utf-8") as f:
                json.dump(audit_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Hoàn tất: {os.path.basename(md_path)}")
        return True
    
    except Exception as e:
        print(f"❌ Lỗi xử lý {md_path}: {str(e)}")
        return False
    
def process_all_folders(
    md_base_dir: str,
    pdf_base_dir: str,
    audit_base_dir: Optional[str] = None
):
    """
    XỬ LÝ TỰ ĐỘNG TẤT CẢ THƯ MỤC:
    - Duyệt tất cả thư mục trong md_base_dir
    - Tự động ánh xạ với file PDF tương ứng
    - Ghi đè kết quả trực tiếp vào main.md gốc
    """
    print(f"\n{'='*50}")
    print(f"🚀 BẮT ĐẦU XỬ LÝ TOÀN BỘ THƯ MỤC")
    print(f"📁 Thư mục Markdown: {md_base_dir}")
    print(f"📁 Thư mục PDF: {pdf_base_dir}")
    print(f"📁 Thư mục Audit: {audit_base_dir or 'Không lưu'}")
    print(f"{'='*50}\n")
    
    # Lấy danh sách tất cả thư mục con
    all_folders = [
        d for d in os.listdir(md_base_dir)
        if os.path.isdir(os.path.join(md_base_dir, d))
    ]
    
    if not all_folders:
        print("❗ Không tìm thấy thư mục nào để xử lý")
        return
    
    print(f"📂 Tổng số thư mục: {len(all_folders)}")
    print(f"Danh sách: {', '.join(all_folders[:5])}{'...' if len(all_folders) > 5 else ''}\n")
    
    success_count = 0
    total_count = 0
    
    for folder_name in sorted(all_folders):
        total_count += 1
        print(f"\n{'-'*40}")
        print(f"🔄 Xử lý thư mục: {folder_name} ({total_count}/{len(all_folders)})")
        
        # Đường dẫn file
        md_path = os.path.join(md_base_dir, folder_name, "main.md")
        pdf_path = os.path.join(pdf_base_dir, f"{folder_name}.pdf")
        audit_path = os.path.join(audit_base_dir, folder_name, "audit.json") if audit_base_dir else None
        
        # Kiểm tra tồn tại file
        if not os.path.exists(md_path):
            print(f"❌ Bỏ qua: File main.md không tồn tại tại {md_path}")
            continue
        
        # Xử lý từng tài liệu
        if process_single_document(md_path, pdf_path, audit_path):
            success_count += 1
    
    # Báo cáo tổng kết
    print(f"\n{'='*50}")
    print(f"📊 BÁO CÁO TỔNG KẾT")
    print(f"Tổng số thư mục: {total_count}")
    print(f"✅ Xử lý thành công: {success_count}")
    print(f"❌ Xử lý thất bại: {total_count - success_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    BASE_DIR = "working"
    MD_BASE_DIR = f"{BASE_DIR}/output_mineru_test"    # Thư mục chứa tất cả thư mục Public_XXX
    PDF_BASE_DIR = f"{BASE_DIR}/cleaned_pdfs_test"     # Thư mục chứa tất cả file PDF
    AUDIT_BASE_DIR = f"{BASE_DIR}/audit_logs"           # Thư mục lưu audit logs (tùy chọn)
    
    # Tạo thư mục audit nếu cần
    if AUDIT_BASE_DIR:
        os.makedirs(AUDIT_BASE_DIR, exist_ok=True)
        print(f"📁 Đã tạo thư mục audit: {AUDIT_BASE_DIR}")
    
    # CHẠY TOÀN BỘ QUY TRÌNH
    process_all_folders(
        md_base_dir=MD_BASE_DIR,
        pdf_base_dir=PDF_BASE_DIR,
        audit_base_dir=AUDIT_BASE_DIR
    )
    
    print("\n✨ HOÀN TẤT TOÀN BỘ QUY TRÌNH XỬ LÝ!")

# ============================================================
# load_and_index_task.py
# ============================================================

import os
import sys
import pickle
from pathlib import Path
from rag_system import AdvancedRAG

def load_extracted_contents_from_output(output_dir):
    output_path = Path(output_dir)
    extracted_contents = {}
    
    for subdir in output_path.iterdir():
        if subdir.is_dir():
            pdf_name = subdir.name
            main_md = subdir / 'main.md'
            if main_md.exists():
                try:
                    with open(main_md, 'r', encoding='utf-8') as f:
                        content = f.read()
                    extracted_contents[pdf_name] = content
                except Exception as e:
                    print(f"Lỗi khi đọc file {main_md}: {e}")
            else:
                print(f"Cảnh báo: Không tìm thấy file {main_md} cho {pdf_name}")
    
    return extracted_contents

def main():
    OUTPUT_DIR = Path(os.getenv('OUTPUT_DIR', 'working/output_mineru_test'))
    
    print("=" * 50)
    print("TASK: LOAD EXTRACTED CONTENTS AND BUILD RAG INDEX")
    print("=" * 50)
    
    contents_file = OUTPUT_DIR / 'extracted_contents.pkl'
    if contents_file.exists():
        print("Đã tìm thấy extracted_contents.pkl. Đang tải...")
        with open(contents_file, 'rb') as f:
            extracted_contents = pickle.load(f)
    else:
        print("Đang tải nội dung từ các file Markdown...")
        extracted_contents = load_extracted_contents_from_output(OUTPUT_DIR)
        if not extracted_contents:
            print("Không có nội dung nào được tải. Thoát.")
            sys.exit(1)
        # Lưu extracted_contents vào file pickle
        with open(contents_file, 'wb') as f:
            pickle.dump(extracted_contents, f)
        print(f"✓ Đã lưu extracted_contents.pkl với {len(extracted_contents)} tài liệu")
    
    # Xây dựng RAG index
    print("\n--- Đang xây dựng RAG Index ---")
    rag_system = AdvancedRAG(extracted_contents)
    
    if not rag_system.ready:
        print("\n✗ Khởi tạo RAG system thất bại. Thoát.")
        sys.exit(1)
    
    # Lưu trạng thái RAG
    rag_state = {
        'chunks': rag_system.chunks,
        'chunk_to_doc': rag_system.chunk_to_doc,
        'chunk_embeddings': rag_system.chunk_embeddings,
        'bm25_corpus': [chunk.lower().split() for chunk in rag_system.chunks],
        'corpus': rag_system.corpus,
        'doc_names': rag_system.doc_names
    }
    
    rag_state_file = OUTPUT_DIR / 'rag_state.pkl'
    with open(rag_state_file, 'wb') as f:
        pickle.dump(rag_state, f)
    print(f"✓ Đã lưu: {rag_state_file}")
    
    print("\n" + "=" * 50)
    print("✓ HOÀN THÀNH LOAD VÀ INDEX")
    print("=" * 50)
    print(f"Đã tải: {len(extracted_contents)} tài liệu")
    print(f"Đã index: {len(rag_system.chunks)} chunks")

if __name__ == "__main__":
    main()

# ============================================================
# matching_headler.py
# ============================================================

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

# ============================================================
# model_headling_detect.py
# ============================================================

import pymupdf
import numpy as np
import pandas as pd
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
import re
from difflib import SequenceMatcher
import lightgbm as lgb
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, classification_report, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
import joblib
import warnings
import hashlib
import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')


@dataclass
class TextLine:
    text: str
    font_size: float
    font_name: str
    is_bold: bool
    x0: float
    y0: float
    x1: float
    y1: float
    page: int
    page_height: float
    page_width: float

class ThresholdOptimizer:
    """Optimize prediction thresholds for each class to maximize F1-score"""
    
    def __init__(self):
        self.optimal_thresholds = {}
        
    def find_optimal_threshold(self, y_true: np.ndarray, y_probs: np.ndarray, class_label: int) -> float:
        """Find optimal threshold for a specific class to maximize F1-score"""
        if class_label not in np.unique(y_true):
            return 0.
            
        # Get probabilities for this class
        prob_class = y_probs[:, class_label]
        
        # Define objective function to minimize (negative F1)
        def objective(threshold):
            y_pred_class = (prob_class >= threshold).astype(int)
            true_class = (y_true == class_label).astype(int)
            
            if np.sum(y_pred_class) == 0 or np.sum(true_class) == 0:
                return 1.0  # Worst possible F1
                
            precision, recall, f1, _ = precision_recall_fscore_support(
                true_class, y_pred_class, average='binary', zero_division=0
            )
            return -f1  # Minimize negative F1
        
        # Find optimal threshold
        try:
            result = minimize_scalar(objective, bounds=(0.1, 0.9), method='bounded')
            return max(0.1, min(0.9, result.x))
        except:
            return 0.5
    
    def optimize_all_thresholds(self, y_true: np.ndarray, y_probs: np.ndarray, classes: List[int]) -> Dict[int, float]:
        """Optimize thresholds for all specified classes"""
        optimal_thresholds = {}
        
        for class_label in classes:
            if class_label > 0:  # Only optimize for heading classes (1-4)
                threshold = self.find_optimal_threshold(y_true, y_probs, class_label)
                optimal_thresholds[class_label] = threshold
                print(f"  Class {class_label}: optimal threshold = {threshold:.3f}")
        
        return optimal_thresholds
class DataValidator:
    """Validate and verify training data quality"""
    
    def __init__(self):
        self.validation_results = {}
        
    def validate_data_quality(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> Dict[str, Any]:
        """Comprehensive data quality validation"""
        validation_report = {}
        
        # Basic statistics
        validation_report['total_samples'] = len(X)
        validation_report['total_features'] = X.shape[1] if len(X) > 0 else 0
        
        # Class distribution - convert numpy types to Python native types
        unique_classes, class_counts = np.unique(y, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique_classes, class_counts):
            class_dist[int(cls)] = int(count)  # Convert to native Python types
        validation_report['class_distribution'] = class_dist
        
        # Calculate imbalance ratio only for heading classes (1-4)
        heading_counts = [count for cls, count in zip(unique_classes, class_counts) if cls > 0]
        if len(heading_counts) > 1:
            validation_report['heading_imbalance_ratio'] = float(max(heading_counts) / min(heading_counts))
        else:
            validation_report['heading_imbalance_ratio'] = 1.0
        
        # Feature statistics
        feature_stats = {}
        for i, feature_name in enumerate(feature_names):
            if len(X) > 0 and i < X.shape[1]:
                feature_data = X[:, i]
                feature_stats[feature_name] = {
                    'mean': float(np.mean(feature_data)),
                    'std': float(np.std(feature_data)),
                    'min': float(np.min(feature_data)),
                    'max': float(np.max(feature_data)),
                    'missing_values': int(np.sum(np.isnan(feature_data)))
                }
        validation_report['feature_statistics'] = feature_stats
        
        # Data quality flags - FOCUS ON HEADING CLASSES
        validation_report['quality_flags'] = {
            'has_sufficient_samples': len(X) >= 100,
            'has_multiple_heading_classes': len([cls for cls in unique_classes if cls > 0]) > 1,
            'no_missing_values': all(stats['missing_values'] == 0 for stats in feature_stats.values()),
            'reasonable_heading_imbalance': validation_report['heading_imbalance_ratio'] < 10,
            'feature_variance_adequate': all(stats['std'] > 0.01 for stats in feature_stats.values() 
                                           if feature_names[i] not in ['is_bold', 'font_differs', 'is_first', 'ends_period', 'starts_number', 'numbered_pattern', 'all_caps', 'placeholder'])
        }
        
        # Overall quality score
        quality_score = sum(validation_report['quality_flags'].values()) / len(validation_report['quality_flags'])
        validation_report['overall_quality_score'] = float(quality_score)
        
        return validation_report
    
    def cross_verify_predictions(self, detector: 'MLHeadingDetector', X: np.ndarray, y: np.ndarray, 
                               lines: List[TextLine], sample_size: int = 50) -> Dict[str, Any]:
        """Cross-verify predictions with manual inspection logic - ONLY AFTER TRAINING"""
        if len(X) == 0 or detector.model is None:
            print("  ⚠ Skipping cross-verification: Model not trained yet")
            return {}
            
        # Get predictions with optimized thresholds
        y_probs = detector.model.predict_proba(X)
        preds = detector._predict_with_thresholds(X, y_probs)
        
        verification_results = {
            'high_confidence_samples': [],
            'low_confidence_samples': [],
            'potential_misclassifications': [],
            'pattern_analysis': {}
        }
        
        # Analyze confidence scores - ONLY FOR HEADING CLASSES
        heading_indices = preds > 0
        if np.any(heading_indices):
            heading_confidences = np.max(y_probs[heading_indices], axis=1)
            high_confidence_threshold = 0.8
            low_confidence_threshold = 0.6
            
            for i, (true_label, pred_label) in enumerate(zip(y, preds)):
                if i >= sample_size:
                    break
                    
                # Only analyze heading predictions
                if pred_label > 0:
                    confidence = float(y_probs[i, pred_label])
                    
                    line_data = {
                        'text': lines[i].text if i < len(lines) else '',
                        'true_label': int(true_label),
                        'predicted_label': int(pred_label),
                        'confidence': confidence,
                        'is_correct': bool(true_label == pred_label)
                    }
                    
                    if confidence >= high_confidence_threshold:
                        verification_results['high_confidence_samples'].append(line_data)
                    elif confidence <= low_confidence_threshold:
                        verification_results['low_confidence_samples'].append(line_data)
                        
                    if true_label != pred_label and confidence > 0.7:  # High confidence but wrong
                        verification_results['potential_misclassifications'].append(line_data)
        
        # Pattern analysis for numbered headings
        numbered_patterns_analysis = self._analyze_numbered_patterns(lines, y, preds)
        verification_results['pattern_analysis'] = numbered_patterns_analysis
        
        return verification_results

    def validate_data_before_training(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> bool:
        """Quick validation before training to ensure data is usable - FOCUS ON HEADINGS"""
        if len(X) == 0:
            print("  ✗ No training data available")
            return False
            
        # Check for sufficient heading classes (at least 2 heading classes)
        heading_classes = [cls for cls in np.unique(y) if cls > 0]
        if len(heading_classes) < 2:
            print("  ✗ Need at least 2 heading classes for training")
            return False
            
        # Check for sufficient samples per heading class
        unique, counts = np.unique(y, return_counts=True)
        min_samples_per_class = 5
        for cls, count in zip(unique, counts):
            if cls > 0 and count < min_samples_per_class:  # Only check heading classes
                print(f"  ✗ Heading class {cls} has only {count} samples (min: {min_samples_per_class})")
                return False
                
        print("  ✓ Data validation passed - ready for training")
        return True
    
    def _analyze_numbered_patterns(self, lines: List[TextLine], y_true: np.ndarray, 
                                 y_pred: np.ndarray) -> Dict[str, Any]:
        """Analyze numbered pattern detection accuracy - ONLY HEADINGS"""
        analysis = {
            'true_positives': 0,
            'false_positives': 0,
            'false_negatives': 0,
            'pattern_examples': []
        }
        
        numbered_pattern = re.compile(r'^\d+(\.\d+)*\.?\s')
        
        for i, (line, true, pred) in enumerate(zip(lines, y_true, y_pred)):
            if i >= 100:  # Limit analysis to first 100 samples
                break
                
            has_numbered_pattern = bool(numbered_pattern.match(line.text.strip()))
            
            if has_numbered_pattern:
                if true > 0 and pred > 0:  # Correctly detected as heading
                    analysis['true_positives'] += 1
                elif true > 0 and pred == 0:  # Missed heading
                    analysis['false_negatives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_negative'
                    })
                elif true == 0 and pred > 0:  # False positive
                    analysis['false_positives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_positive'
                    })
        
        return analysis



class DataManager:
    """Manage training data caching and loading"""
    
    def __init__(self, cache_dir: str = "working/training_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def get_cache_key(self, input_dir: str, gt_dir: str) -> str:
        """Generate unique cache key based on input directories"""
        dir_info = f"{input_dir}_{gt_dir}"
        return hashlib.md5(dir_info.encode()).hexdigest()[:16]
    
    def save_training_data(self, cache_key: str, X: np.ndarray, y: np.ndarray, 
                         metadata: Dict[str, Any]) -> str:
        """Save training data to cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        # Save data
        np.savez(cache_file, X=X, y=y)
        
        # Convert metadata to JSON-serializable format
        serializable_metadata = self._convert_to_serializable(metadata)
        serializable_metadata['saved_at'] = datetime.now().isoformat()
        serializable_metadata['data_shape'] = X.shape if X is not None else None
        
        # Convert class distribution to serializable format
        if 'class_distribution' in serializable_metadata:
            serializable_metadata['class_distribution'] = {
                str(k): int(v) for k, v in serializable_metadata['class_distribution'].items()
            }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(serializable_metadata, f, indent=2, ensure_ascii=False)
            
        return str(cache_file)
    
    def _convert_to_serializable(self, obj: Any) -> Any:
        """Convert numpy types to Python native types for JSON serialization"""
        if isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {str(k): self._convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_to_serializable(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(self._convert_to_serializable(item) for item in obj)
        else:
            return obj
    
    def load_training_data(self, cache_key: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], Dict[str, Any]]:
        """Load training data from cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        if not cache_file.exists() or not metadata_file.exists():
            return None, None, {}
            
        try:
            # Load data
            data = np.load(cache_file)
            X, y = data['X'], data['y']
            
            # Load metadata
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                
            print(f"✓ Loaded cached training data: {X.shape[0]} samples")
            return X, y, metadata
            
        except Exception as e:
            print(f"✗ Error loading cached data: {e}")
            return None, None, {}
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get information about cached data"""
        cache_files = list(self.cache_dir.glob("*_data.npz"))
        cache_info = {
            'total_cached_datasets': len(cache_files),
            'cache_files': []
        }
        
        for cache_file in cache_files:
            metadata_file = cache_file.with_name(cache_file.stem.replace('_data', '_metadata') + '.json')
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    cache_info['cache_files'].append({
                        'file': cache_file.name,
                        'saved_at': metadata.get('saved_at', 'unknown'),
                        'data_shape': metadata.get('data_shape', 'unknown'),
                        'class_distribution': metadata.get('class_distribution', {})
                    })
                except:
                    continue
                    
        return cache_info


class FeatureExtractor:
    """Extract 22 features from each text line with ENHANCED numbered pattern detection"""

    def __init__(self):
        self.doc_stats = None
        # ENHANCED: Strict numbered patterns - chỉ tập trung vào 1., 1.1, 1.1.1, etc.
        self.numbered_patterns = [
            r'^\d+\.\s+[A-Za-zÀ-ỹ]',  # 1. Text (bắt đầu bằng số, dấu chấm, khoảng trắng, rồi chữ)
            r'^\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1 Text
            r'^\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1 Text  
            r'^\d+\.\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1.1 Text
        ]
        
        # ENHANCED: Strong exclusion patterns
        self.exclude_patterns = [
            r'^.*(hình|figure|bảng|table|biểu đồ|chart|trang|page).*\d',
            r'^.*\d+\s*[-–]\s*\d+.*',  # Number ranges like "1-2"
            r'^\d+$',  # Chỉ có số đơn thuần
            r'^.*[\.:]\d+$',  # Kết thúc bằng .số hoặc :số
        ]

    def compute_document_stats(self, lines: List[TextLine]) -> Dict:
        """Compute document-level statistics"""
        if not lines:
            self.doc_stats = {
                'median_font': 12.0, 'mean_font': 12.0, 'std_font': 1.0,
                'dominant_font': 'unknown', 'median_gap': 10.0, 
                'mean_gap': 10.0, 'std_gap': 5.0
            }
            return self.doc_stats

        font_sizes = [line.font_size for line in lines]
        font_names = [line.font_name for line in lines]

        # Compute gaps
        lines_sorted = sorted(lines, key=lambda l: (l.page, l.y0))
        gaps = []
        for i in range(1, len(lines_sorted)):
            if lines_sorted[i].page == lines_sorted[i-1].page:
                gap = lines_sorted[i].y0 - lines_sorted[i-1].y1
                if gap > 0:
                    gaps.append(gap)

        self.doc_stats = {
            'median_font': float(np.median(font_sizes)),
            'mean_font': float(np.mean(font_sizes)),
            'std_font': float(np.std(font_sizes)) if len(font_sizes) > 1 else 1.0,
            'dominant_font': max(set(font_names), key=font_names.count) if font_names else 'unknown',
            'median_gap': float(np.median(gaps)) if gaps else 10.0,
            'mean_gap': float(np.mean(gaps)) if gaps else 10.0,
            'std_gap': float(np.std(gaps)) if gaps else 5.0,
        }

        return self.doc_stats

    def is_likely_numbered_heading(self, text: str) -> bool:
        """ENHANCED: Strict detection of numbered headings while avoiding false positives"""
        text_clean = text.strip()
        
        # Check exclusion patterns first (tables, figures, etc.)
        for exclude_pattern in self.exclude_patterns:
            if re.match(exclude_pattern, text_clean, re.IGNORECASE):
                return False
        
        # Check inclusion patterns (must be at start and followed by text)
        for pattern in self.numbered_patterns:
            if re.match(pattern, text_clean):
                # EXTRA VALIDATION: text after numbers should be meaningful
                text_after_numbers = re.sub(r'^\d+(\.\d+)*\s*', '', text_clean).strip()
                if (len(text_after_numbers) >= 3 and 
                    any(c.isalpha() for c in text_after_numbers) and
                    not text_after_numbers.lower().startswith(('hình', 'bảng', 'biểu đồ', 'table', 'figure', 'chart'))):
                    return True
                    
        return False

    def extract_features(self, line: TextLine, prev_line: TextLine = None, 
                        next_line: TextLine = None) -> np.ndarray:
        """Extract 22 features from a text line with improved numbered pattern detection"""

        if self.doc_stats is None:
            raise ValueError("Call compute_document_stats first!")

        features = []
        text = line.text

        # === FONT FEATURES (5) ===
        features.append(line.font_size)  # f1: absolute font size

        font_ratio = line.font_size / self.doc_stats['median_font'] if self.doc_stats['median_font'] > 0 else 1.0
        features.append(font_ratio)  # f2: relative to median

        z_score = (line.font_size - self.doc_stats['mean_font']) / self.doc_stats['std_font'] if self.doc_stats['std_font'] > 0 else 0
        features.append(z_score)  # f3: standardized

        features.append(1.0 if line.is_bold else 0.0)  # f4: is bold

        font_differs = 1.0 if line.font_name != self.doc_stats['dominant_font'] else 0.0
        features.append(font_differs)  # f5: font differs from dominant

        # === POSITION FEATURES (6) ===
        relative_y = line.y0 / line.page_height if line.page_height > 0 else 0.5
        features.append(relative_y)  # f6: relative y position (0=top, 1=bottom)

        relative_x = line.x0 / line.page_width if line.page_width > 0 else 0.0
        features.append(relative_x)  # f7: relative x position

        features.append(line.x0)  # f8: distance from left margin (pixels)

        # Gap before
        gap_before = 0.0
        if prev_line and prev_line.page == line.page:
            gap_before = line.y0 - prev_line.y1
        features.append(gap_before)  # f9: gap before line

        # Gap after
        gap_after = 0.0
        if next_line and next_line.page == line.page:
            gap_after = next_line.y0 - line.y1
        features.append(gap_after)  # f10: gap after line

        is_first = 1.0 if (prev_line is None or prev_line.page != line.page) else 0.0
        features.append(is_first)  # f11: is first line of page

        # === TEXT FEATURES (8) ===
        features.append(len(text))  # f12: text length

        word_count = len(text.split())
        features.append(word_count)  # f13: word count

        # Capital word ratio (first letter)
        capital_words = sum(1 for word in text.split() if word and word[0].isupper())
        capital_ratio = capital_words / word_count if word_count > 0 else 0
        features.append(capital_ratio)  # f14: capital word ratio

        # NEW: Uppercase character ratio in entire text
        alpha_chars = sum(1 for c in text if c.isalpha())
        upper_chars = sum(1 for c in text if c.isupper())
        upper_ratio = upper_chars / alpha_chars if alpha_chars > 0 else 0
        features.append(upper_ratio)  # f15: uppercase character ratio

        punct_count = sum(1 for c in text if c in '.,;:!?')
        features.append(punct_count)  # f16: punctuation count

        # NEW: Period count specifically
        period_count = text.count('.')
        features.append(period_count)  # f17: period count

        ends_period = 1.0 if text.endswith('.') else 0.0
        features.append(ends_period)  # f18: ends with period

        starts_number = 1.0 if text and text[0].isdigit() else 0.0
        features.append(starts_number)  # f19: starts with number

        # === PATTERN FEATURES (3) ===
        # ENHANCED: Use strict numbered pattern detection
        matches_numbered = 1.0 if self.is_likely_numbered_heading(text) else 0.0
        features.append(matches_numbered)  # f20: numbered pattern

        is_all_caps = 1.0 if text.isupper() and len(text) > 3 else 0.0
        features.append(is_all_caps)  # f21: ALL CAPS

        # Removed keywords feature to avoid FP
        features.append(0.0)  # f22: placeholder (removed keywords)

        return np.array(features, dtype=np.float32)


class ModelManager:
    """Manage multiple model versions and save all trained models"""
    
    def __init__(self, models_dir: str = "working/models"):
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
    def save_model_version(self, detector: 'MLHeadingDetector', version_suffix: str = "", 
                         metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None) -> str:
        """Save model with versioning and metadata"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = f"heading_detector_{timestamp}"
        if version_suffix:
            version_name += f"_{version_suffix}"
            
        model_dir = self.models_dir / version_name
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Save main model
        model_path = model_dir / "model.pkl"
        joblib.dump({
            'model': detector.model,
            'feature_names': detector.feature_names,
            'feature_extractor': detector.feature_extractor
        }, model_path)
        
        # Save metadata
        metadata = {
            'version': version_name,
            'saved_at': datetime.now().isoformat(),
            'feature_count': len(detector.feature_names),
            'feature_names': detector.feature_names
        }
        
        if metrics:
            metadata['metrics'] = {k: float(v) if isinstance(v, (np.floating, float)) else v 
                                 for k, v in metrics.items()}
            
        if training_info:
            metadata['training_info'] = training_info
            
        with open(model_dir / "metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
            
        print(f"✓ Model version saved: {version_name}")
        return str(model_dir)
    
    def get_all_models(self) -> List[Dict[str, Any]]:
        """Get information about all saved models"""
        model_dirs = [d for d in self.models_dir.iterdir() if d.is_dir() and d.name.startswith("heading_detector_")]
        models_info = []
        
        for model_dir in model_dirs:
            metadata_file = model_dir / "metadata.json"
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    models_info.append({
                        'name': model_dir.name,
                        'path': str(model_dir),
                        'metadata': metadata
                    })
                except Exception as e:
                    print(f"Error loading metadata for {model_dir}: {e}")
                    
        return sorted(models_info, key=lambda x: x['metadata']['saved_at'], reverse=True)
    
    def load_latest_model(self) -> Optional[Dict]:
        """Load the most recent model"""
        all_models = self.get_all_models()
        if not all_models:
            return None
            
        latest_model = all_models[0]
        try:
            model_path = Path(latest_model['path']) / "model.pkl"
            detector_data = joblib.load(model_path)
            return {
                'detector_data': detector_data,
                'metadata': latest_model['metadata'],
                'path': latest_model['path']
            }
        except Exception as e:
            print(f"Error loading model {latest_model['name']}: {e}")
            return None
    
    def cleanup_old_models(self, keep_count: int = 5):
        """Keep only the most recent models"""
        all_models = self.get_all_models()
        if len(all_models) <= keep_count:
            return
            
        for model_info in all_models[keep_count:]:
            try:
                import shutil
                shutil.rmtree(model_info['path'])
                print(f"✓ Removed old model: {model_info['name']}")
            except Exception as e:
                print(f"✗ Error removing model {model_info['name']}: {e}")


class MLHeadingDetector:
    """ENHANCED ML-based heading detector with LightGBM (Multi-class)"""

    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.data_validator = DataValidator()
        self.data_manager = DataManager()
        self.model_manager = ModelManager()
        self.threshold_optimizer = ThresholdOptimizer()
        self.model = None
        self.feature_names = [
            'font_size', 'font_ratio', 'z_score', 'is_bold', 'font_differs',
            'y_position', 'x_position', 'left_margin', 'gap_before', 'gap_after', 'is_first',
            'text_length', 'word_count', 'capital_ratio', 'upper_ratio', 'punct_count', 
            'period_count', 'ends_period', 'starts_number', 'numbered_pattern', 
            'all_caps', 'placeholder'
        ]
        self.optimal_thresholds = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}  # Default thresholds


    def extract_lines(self, pdf_path: str) -> List[TextLine]:
        """Extract all text lines from PDF"""

        doc = pymupdf.open(pdf_path)
        all_lines = []

        for page_num, page in enumerate(doc, start=1):
            text_dict = page.get_text("dict")
            page_height = page.rect.height
            page_width = page.rect.width

            for block in text_dict["blocks"]:
                if block["type"] != 0:
                    continue

                for line in block.get("lines", []):
                    line_text = ""
                    font_sizes = []
                    font_names = []

                    for span in line.get("spans", []):
                        line_text += span["text"]
                        font_sizes.append(span["size"])
                        font_names.append(span["font"])

                    line_text = line_text.strip()
                    if not line_text:
                        continue

                    all_lines.append(TextLine(
                        text=line_text,
                        font_size=float(np.median(font_sizes)) if font_sizes else 12.0,
                        font_name=max(set(font_names), key=font_names.count) if font_names else 'unknown',
                        is_bold=any('bold' in f.lower() or 'heavy' in f.lower() for f in font_names),
                        x0=line['bbox'][0],
                        y0=line['bbox'][1],
                        x1=line['bbox'][2],
                        y1=line['bbox'][3],
                        page=page_num,
                        page_height=page_height,
                        page_width=page_width
                    ))

        doc.close()
        return all_lines

    def generate_training_data(self, pdf_path: str, gt_md_path: str) -> Tuple[np.ndarray, np.ndarray, List[TextLine]]:
        """FIXED: Generate features and labels - CHỈ gắn nhãn cho các heading markdown từ file GT"""

        # Extract lines
        lines = self.extract_lines(pdf_path)

        if not lines:
            print(f"  No lines extracted from {pdf_path}")
            return np.array([]), np.array([]), []

        # Compute document stats
        self.feature_extractor.compute_document_stats(lines)

        # Parse ground truth headings with levels - CHỈ lấy các heading markdown (#, ##, ###, ####)
        gt_headings = self._parse_markdown_with_levels(gt_md_path)
        
        if not gt_headings:
            print(f"  No markdown headings found in {gt_md_path}")
            return np.array([]), np.array([]), []

        # Extract features and labels
        X = []
        y = []

        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None

            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

            # FIXED: CHỈ sử dụng fuzzy matching với các heading markdown từ GT
            # Tất cả các dòng khác đều là level 0 (không phải heading)
            heading_level = self._fuzzy_match_with_level(line.text, gt_headings, threshold=0.8)
            y.append(heading_level)

        return np.array(X), np.array(y), lines

    def _fuzzy_match_with_level(self, text: str, gt_headings: List[Dict], threshold: float = 0.8) -> int:
        """Check if text matches any ground truth heading and return its level"""
        
        text_lower = text.lower().strip()
        best_score = 0
        best_level = 0  # Default: not a heading

        for gt_heading in gt_headings:
            gt_text = gt_heading['text'].lower().strip()
            score = SequenceMatcher(None, text_lower, gt_text).ratio()
            
            if score > best_score and score >= threshold:
                best_score = score
                best_level = gt_heading['level']

        return best_level

    def _parse_markdown_with_levels(self, md_path: str) -> List[Dict]:
        """Parse markdown to extract headings with levels (1-4) - CHỈ lấy markdown headings"""
        
        if not Path(md_path).exists():
            print(f"  Markdown file not found: {md_path}")
            return []

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            headings = []
            for line in content.split('\n'):
                line = line.strip()
                if not line:
                    continue

                # FIXED: CHỈ match markdown headings: # Heading 1, ## Heading 2, etc.
                # Bỏ qua tất cả các dòng không phải heading markdown
                match = re.match(r'^(#{1,4})\s+(.+)$', line)
                if match:
                    level = len(match.group(1))
                    text = match.group(2).strip()
                    headings.append({'text': text, 'level': level})

            print(f"  Extracted {len(headings)} markdown headings from {md_path}")
            return headings
        except Exception as e:
            print(f"  Error parsing markdown {md_path}: {e}")
            return []

    def train(self, X_train: np.ndarray, y_train: np.ndarray, X_val: np.ndarray = None, y_val: np.ndarray = None):
        """ENHANCED: Train LightGBM model with focus on heading recall and threshold optimization"""

        print(f"Training samples: {len(X_train)}")
        
        # Calculate class distribution - FOCUS ON HEADING CLASSES
        unique, counts = np.unique(y_train, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique, counts):
            class_dist[int(cls)] = int(count)
        print("Class distribution:")
        for level, count in class_dist.items():
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train)*100:.2f}%)")

        # Handle class imbalance - less aggressive merging
        y_train_adj = self._adjust_rare_classes_enhanced(y_train)
        
        # Recalculate class distribution after adjustment
        unique_adj, counts_adj = np.unique(y_train_adj, return_counts=True)
        print("\nAdjusted class distribution:")
        for level, count in zip(unique_adj, counts_adj):
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train_adj)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train_adj)*100:.2f}%)")

        # ENHANCED: Compute class weights with manual boost for headings
        class_weights = compute_class_weight(
            class_weight='balanced',
            classes=np.unique(y_train_adj),
            y=y_train_adj
        )
        
        # MANUAL BOOST: Increase weight for heading classes (1-4)
        class_weight_dict = {}
        for i, cls in enumerate(np.unique(y_train_adj)):
            base_weight = float(class_weights[i])
            if cls > 0:  # Heading classes
                boosted_weight = base_weight * 3.0  # Triple the importance
                class_weight_dict[int(cls)] = boosted_weight
            else:
                class_weight_dict[int(cls)] = base_weight
                
        print(f"Enhanced Class weights: {class_weight_dict}")

        # ENHANCED: LightGBM with focus on recall
        self.model = lgb.LGBMClassifier(
            n_estimators=300,
            max_depth=10,
            learning_rate=0.05,
            num_leaves=31,
            min_child_samples=10,
            subsample=0.7,
            colsample_bytree=0.7,
            reg_alpha=0.1,
            reg_lambda=0.1,
            class_weight=class_weight_dict,
            random_state=42,
            n_jobs=-1,
            verbose=-1,
            boosting_type='gbdt'
        )

        # Train with validation set if provided
        if X_val is not None and y_val is not None:
            self.model.fit(
                X_train, y_train_adj,
                eval_set=[(X_val, y_val)],
                eval_metric='multi_logloss',
            )
        else:
            self.model.fit(X_train, y_train_adj)

        # Optimize thresholds on validation set or training set
        if X_val is not None and y_val is not None:
            print("\nOptimizing thresholds on validation set...")
            y_val_probs = self.model.predict_proba(X_val)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_val, y_val_probs, [1, 2, 3, 4]
            )
        else:
            print("\nOptimizing thresholds on training set...")
            y_train_probs = self.model.predict_proba(X_train)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_train_adj, y_train_probs, [1, 2, 3, 4]
            )

        # Print feature importance
        print("\nTop 15 Important Features:")
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1][:15]

        for i, idx in enumerate(indices):
            print(f"  {i+1}. {self.feature_names[idx]:20s}: {importances[idx]:.4f}")

        return y_train_adj

    def _predict_with_thresholds(self, X: np.ndarray, y_probs: np.ndarray = None) -> np.ndarray:
        """Predict with optimized thresholds for heading classes"""
        if y_probs is None:
            y_probs = self.model.predict_proba(X)
        
        # Get default predictions (highest probability)
        default_preds = np.argmax(y_probs, axis=1)
        
        # Apply thresholds for heading classes
        for i in range(len(default_preds)):
            pred_class = default_preds[i]
            if pred_class in self.optimal_thresholds:
                if y_probs[i, pred_class] < self.optimal_thresholds[pred_class]:
                    # If probability below threshold, set to non-heading
                    default_preds[i] = 0
        
        return default_preds
    def _adjust_rare_classes_enhanced(self, y: np.ndarray) -> np.ndarray:
        """ENHANCED: Less aggressive class merging - preserve heading classes"""
        unique, counts = np.unique(y, return_counts=True)
        y_adj = y.copy()
        
        # Only merge extremely rare classes (less than 5 samples) - ONLY FOR HEADINGS
        for level, count in zip(unique, counts):
            if count < 5 and level > 0:  # Only merge rare heading classes
                # Find nearest heading level with sufficient samples
                possible_targets = [l for l in unique if l > 0 and np.sum(y == l) >= 10]
                if possible_targets:
                    target_level = min(possible_targets, key=lambda x: abs(x - level))
                    print(f"  Merging level {level} ({count} samples) into level {target_level}")
                    y_adj[y_adj == level] = target_level
                else:
                    # Fallback: merge into level 1
                    print(f"  Merging level {level} ({count} samples) into level 1")
                    y_adj[y_adj == level] = 1
        
        return y_adj
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Evaluate model performance - FOCUS ON HEADING CLASSES (1-4)"""

        # Adjust test labels same as training
        y_test_adj = self._adjust_rare_classes_enhanced(y_test)
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)

        # FOCUS ON HEADING CLASSES: Filter out class 0 for heading-specific metrics
        heading_indices = y_test_adj > 0
        heading_preds = preds[heading_indices]
        heading_true = y_test_adj[heading_indices]
        
        if len(heading_true) > 0:
            # Heading-specific metrics
            heading_accuracy = accuracy_score(heading_true, heading_preds)
            heading_precision, heading_recall, heading_f1, _ = precision_recall_fscore_support(
                heading_true, heading_preds, average='weighted', zero_division=0
            )
            
            # Per-class metrics for headings only
            heading_classes = sorted(np.unique(heading_true))
            per_class_metrics = precision_recall_fscore_support(
                heading_true, heading_preds, average=None, zero_division=0, labels=heading_classes
            )
            
            # Heading confusion matrix
            heading_cm = confusion_matrix(heading_true, heading_preds, labels=heading_classes)
        else:
            heading_accuracy = heading_precision = heading_recall = heading_f1 = 0.0
            per_class_metrics = ([], [], [], [])
            heading_cm = np.array([])
            heading_classes = []

        # Overall metrics (including non-headings) for reference
        overall_accuracy = accuracy_score(y_test_adj, preds)

        print("\n" + "="*70)
        print("EVALUATION RESULTS - FOCUS ON HEADING CLASSES (1-4)")
        print("="*70)
        print(f"Overall Accuracy (all classes): {overall_accuracy:.4f}")
        print(f"Heading-only Accuracy:          {heading_accuracy:.4f}")
        print(f"Heading-only Precision:         {heading_precision:.4f}")
        print(f"Heading-only Recall:            {heading_recall:.4f}")
        print(f"Heading-only F1 Score:          {heading_f1:.4f}")
        
        if heading_classes:
            print(f"\nPer-class Metrics (Headings only):")
            for i, cls in enumerate(heading_classes):
                print(f"  Level {cls}: Precision={per_class_metrics[0][i]:.4f}, "
                      f"Recall={per_class_metrics[1][i]:.4f}, F1={per_class_metrics[2][i]:.4f}")

            print(f"\nConfusion Matrix (Headings only):")
            print(heading_cm)

        # Show some misclassified heading examples
        heading_misclassified = np.where((heading_true != heading_preds) & (heading_true > 0))[0]
        if len(heading_misclassified) > 0 and len(heading_misclassified) <= 10:
            print(f"\nSample heading misclassifications ({len(heading_misclassified)} total):")
            for idx in heading_misclassified[:5]:
                print(f"  True: {heading_true[idx]}, Predicted: {heading_preds[idx]}")

        return {
            'overall_accuracy': float(overall_accuracy),
            'heading_accuracy': float(heading_accuracy),
            'heading_precision': float(heading_precision),
            'heading_recall': float(heading_recall),
            'heading_f1': float(heading_f1),
            'heading_confusion_matrix': heading_cm.tolist() if len(heading_cm) > 0 else [],
            'heading_classes': [int(cls) for cls in heading_classes],
            'per_class_metrics': [metric.tolist() for metric in per_class_metrics] if heading_classes else []
        }

    def evaluate_heading_detection(self, X_test: np.ndarray, y_test: np.ndarray, lines_test: List[TextLine]) -> Dict:
        """ENHANCED: Heading-specific evaluation metrics with threshold optimization"""
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)
        
        # FOCUS ON HEADING DETECTION (classes 1-4)
        heading_indices_true = y_test > 0
        heading_indices_pred = preds > 0
        
        total_headings = np.sum(heading_indices_true)
        detected_headings = np.sum(heading_indices_pred)
        correct_detections = np.sum(heading_indices_true & heading_indices_pred)
        
        # Calculate detection metrics
        detection_precision = correct_detections / detected_headings if detected_headings > 0 else 0
        detection_recall = correct_detections / total_headings if total_headings > 0 else 0
        detection_f1 = 2 * (detection_precision * detection_recall) / (detection_precision + detection_recall) if (detection_precision + detection_recall) > 0 else 0
        
        # Level-wise accuracy for correctly detected headings
        correctly_detected_indices = heading_indices_true & heading_indices_pred
        if np.any(correctly_detected_indices):
            level_accuracy = accuracy_score(
                y_test[correctly_detected_indices], 
                preds[correctly_detected_indices]
            )
        else:
            level_accuracy = 0.0

        print("\n" + "="*70)
        print("ENHANCED HEADING DETECTION EVALUATION")
        print("="*70)
        print(f"Detection Metrics:")
        print(f"  Precision: {detection_precision:.4f}")
        print(f"  Recall:    {detection_recall:.4f}")
        print(f"  F1-Score:  {detection_f1:.4f}")
        print(f"  Level Accuracy: {level_accuracy:.4f}")
        
        print(f"\nDetection Analysis:")
        print(f"  Total headings in test set: {total_headings}")
        print(f"  Detected as headings: {detected_headings}")
        print(f"  Correctly detected: {correct_detections}")
        print(f"  Heading Detection Rate: {detection_recall*100:.1f}%" if total_headings > 0 else "  Heading Detection Rate: N/A")
        
        # Analyze false negatives
        false_negatives = np.where(heading_indices_true & ~heading_indices_pred)[0]
        if len(false_negatives) > 0:
            print(f"\nFalse Negatives Analysis ({len(false_negatives)} missed headings):")
            for idx in false_negatives[:5]:  # Show first 5
                print(f"  Level {y_test[idx]}: {lines_test[idx].text[:80]}...")
        
        return {
            'detection_precision': float(detection_precision),
            'detection_recall': float(detection_recall),
            'detection_f1': float(detection_f1),
            'level_accuracy': float(level_accuracy),
            'total_headings': int(total_headings),
            'detected_headings': int(detected_headings),
            'correct_detections': int(correct_detections),
            'false_negatives': int(len(false_negatives))
        }
    
    def cross_validate(self, X: np.ndarray, y: np.ndarray, cv_folds: int = 5) -> Dict[str, Any]:
        """Perform cross-validation for more reliable evaluation with small data"""
        print(f"\nPerforming {cv_folds}-fold cross-validation...")
        
        # Adjust labels for consistency
        y_adj = self._adjust_rare_classes_enhanced(y)
        
        # Use stratified k-fold for imbalanced data
        skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
        
        cv_scores = {
            'accuracy': [],
            'precision': [],
            'recall': [],
            'f1': []
        }
        
        fold = 1
        for train_idx, val_idx in skf.split(X, y_adj):
            print(f"  Fold {fold}/{cv_folds}...")
            
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y_adj[train_idx], y_adj[val_idx]
            
            # Train temporary model
            temp_model = lgb.LGBMClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                verbose=-1
            )
            temp_model.fit(X_train, y_train)
            
            # Evaluate
            preds = temp_model.predict(X_val)
            cv_scores['accuracy'].append(float(accuracy_score(y_val, preds)))
            precision, recall, f1, _ = precision_recall_fscore_support(
                y_val, preds, average='weighted', zero_division=0
            )
            cv_scores['precision'].append(float(precision))
            cv_scores['recall'].append(float(recall))
            cv_scores['f1'].append(float(f1))
            
            fold += 1
        
        # Print CV results
        print(f"\nCross-Validation Results ({cv_folds}-fold):")
        for metric, scores in cv_scores.items():
            mean_score = float(np.mean(scores))
            std_score = float(np.std(scores))
            print(f"  {metric.capitalize()}: {mean_score:.4f} ± {std_score:.4f}")
        
        return cv_scores

    def predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback"""
        return self.enhanced_predict(pdf_path)

    def enhanced_predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback and minimum heading guarantee"""

        lines = self.extract_lines(pdf_path)
        if not lines:
            return []

        self.feature_extractor.compute_document_stats(lines)

        # ML Prediction
        X = []
        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None
            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

        X = np.array(X)
        preds = self.model.predict(X)
        probs = self.model.predict_proba(X)

        headings = []
        
        # RULE-BASED ENHANCEMENT: Ensure all numbered headings are detected
        for i, (line, pred, prob) in enumerate(zip(lines, preds, probs)):
            confidence = float(prob[pred])
            
            # RULE 1: If has numbered pattern but model missed it -> FORCE as heading
            if (self.feature_extractor.is_likely_numbered_heading(line.text) and 
                pred == 0 and confidence < 0.8):
                
                # Determine level based on dot count
                dot_count = line.text.strip().split(' ')[0].count('.')
                forced_level = min(4, max(1, dot_count))
                
                headings.append({
                    'text': line.text,
                    'level': forced_level,
                    'page': line.page,
                    'probability': 0.95,  # High confidence for rule-based
                    'font_size': line.font_size,
                    'detection_method': 'rule_based'
                })
                continue
                
            # RULE 2: ML prediction with lower confidence threshold
            if pred > 0 and confidence > 0.3:  # Lower threshold to catch more headings
                headings.append({
                    'text': line.text,
                    'level': int(pred),
                    'page': line.page,
                    'probability': confidence,
                    'font_size': line.font_size,
                    'detection_method': 'ml'
                })

        # RULE 3: Ensure minimum headings per document
        headings = self._ensure_minimum_headings(lines, headings)
        
        # Remove duplicates
        unique_headings = []
        seen_texts = set()
        for heading in headings:
            if heading['text'] not in seen_texts:
                unique_headings.append(heading)
                seen_texts.add(heading['text'])
        
        return unique_headings

    def _ensure_minimum_headings(self, lines: List[TextLine], headings: List[Dict]) -> List[Dict]:
        """ENHANCED: Ensure each document has at least 6 headings"""
        if len(headings) >= 6:  # Already has sufficient headings
            return headings
            
        # Find potential headings that were missed
        potential_headings = []
        
        for i, line in enumerate(lines):
            # Skip if already detected
            if any(h['text'] == line.text for h in headings):
                continue
                
            # Characteristics of actual headings
            is_likely_heading = (
                self.feature_extractor.is_likely_numbered_heading(line.text) or
                (line.font_size > self.feature_extractor.doc_stats['median_font'] * 1.1 and 
                 len(line.text.split()) <= 15 and  # Headings are usually short
                 any(c.isupper() for c in line.text) and  # Has uppercase letters
                 not line.text.endswith('.') and  # Doesn't end with period
                 not line.text[-1].isdigit())  # Doesn't end with digit
            )
            
            if is_likely_heading:
                dot_count = line.text.strip().split(' ')[0].count('.')
                level = min(4, max(1, dot_count + 1))
                
                potential_headings.append({
                    'text': line.text,
                    'level': level,
                    'page': line.page,
                    'probability': 0.7,
                    'font_size': line.font_size,
                    'detection_method': 'fallback'
                })
        
        # Add potential headings if current count is too low
        if len(headings) < 6 and potential_headings:
            needed = min(6 - len(headings), len(potential_headings))
            headings.extend(potential_headings[:needed])
        
        return headings

    def save_all_models(self, metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None):
        """Save all model versions with metadata"""
        # Save main model
        main_model_path = self.model_manager.save_model_version(
            self, "main", metrics, training_info
        )
        
        # Also save a simplified version for quick loading
        simple_model_path = self.model_manager.save_model_version(
            self, "simple", metrics, training_info
        )
        
        print(f"✓ All model versions saved:")
        print(f"  - Main model: {main_model_path}")
        print(f"  - Simple model: {simple_model_path}")
        
        # Clean up old models (keep only 5 most recent)
        self.model_manager.cleanup_old_models(keep_count=5)
        
        return main_model_path

    def load_latest_model(self):
        """Load the most recent model"""
        model_data = self.model_manager.load_latest_model()
        if model_data is None:
            print("✗ No trained model found")
            return False
            
        try:
            detector_data = model_data['detector_data']
            self.model = detector_data['model']
            self.feature_names = detector_data['feature_names']
            self.feature_extractor = detector_data['feature_extractor']
            print(f"✓ Loaded model: {model_data['metadata']['version']}")
            return True
        except Exception as e:
            print(f"✗ Error loading model: {e}")
            return False


# ============================================================
# ENHANCED TRAINING PIPELINE - LIGHTGBM VERSION
# ============================================================

def train_and_evaluate(
    input_dir: str = r'D:\Viettel_Race_Ai\rag\training_input',
    gt_dir: str = r'D:\Viettel_Race_Ai\rag\training_output',
    output_dir: str = 'working/ml_heading_model_lgb',
    train_ratio: float = 0.75,  # Reduced to have more validation data
    val_ratio: float = 0.15,   # Added validation split
    use_cached_data: bool = True,
    enable_cross_validation: bool = True,
    enable_data_validation: bool = True,
    optimize_thresholds: bool = True  # New parameter for threshold optimization
):
    """Enhanced training pipeline with threshold optimization"""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    detector = MLHeadingDetector()
    
    # Check cache first
    cache_key = detector.data_manager.get_cache_key(input_dir, gt_dir)
    X_all, y_all, metadata = None, None, {}
    
    if use_cached_data:
        X_all, y_all, metadata = detector.data_manager.load_training_data(cache_key)
    
    # If no cached data or not using cache, generate new data
    if X_all is None or y_all is None:
        print("Generating new training data...")
        
        # Load dataset with proper path handling
        input_path = Path(input_dir)
        gt_path = Path(gt_dir)

        pdf_files = sorted(input_path.glob('*.pdf'))
        print(f"Found {len(pdf_files)} PDF files")

        # Generate training data with error handling
        print("\nGenerating training data...")
        X_all_parts = []
        y_all_parts = []
        all_lines = []
        processed_count = 0

        for i, pdf_file in enumerate(pdf_files):
            doc_id = pdf_file.stem
            
            # Look for markdown file
            possible_md_locations = [
                gt_path / f"{doc_id}.md",
                gt_path / doc_id / "main.md", 
                gt_path / doc_id / f"{doc_id}.md",
                gt_path / f"{doc_id}" / "main.md"
            ]
            
            gt_md_path = None
            for location in possible_md_locations:
                if location.exists():
                    gt_md_path = location
                    break
            
            if gt_md_path is None:
                print(f"  Skipping {doc_id}: No markdown file found")
                continue

            try:
                X_batch, y_batch, lines_batch = detector.generate_training_data(str(pdf_file), str(gt_md_path))
                
                if len(X_batch) > 0:
                    X_all_parts.append(X_batch)
                    y_all_parts.append(y_batch)
                    all_lines.extend(lines_batch)
                    processed_count += 1
                    print(f"  ✓ Processed {doc_id}: {len(X_batch)} samples")
                else:
                    print(f"  ⚠ No samples from {doc_id}")
                    
            except Exception as e:
                print(f"  ✗ Error with {doc_id}: {e}")
                continue

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(pdf_files)} files")

        # Check if we have any data
        if not X_all_parts:
            print("\n❌ ERROR: No training data generated!")
            return None, None

        # Combine all data
        try:
            X_all = np.vstack(X_all_parts)
            y_all = np.hstack(y_all_parts)
            
            # Save to cache for future use
            metadata = {
                'source_files': len(pdf_files),
                'processed_files': processed_count,
                'generated_at': datetime.now().isoformat()
            }
            detector.data_manager.save_training_data(cache_key, X_all, y_all, metadata)
            print(f"✓ Training data cached with key: {cache_key}")
            
        except ValueError as e:
            print(f"\n❌ ERROR combining data: {e}")
            return None, None

        print(f"\n✅ Successfully processed {processed_count}/{len(pdf_files)} files")
        print(f"Total samples: {len(X_all)}")
    else:
        print("✓ Using cached training data")
        all_lines = []  # Lines not available from cache

    # Show class distribution - FOCUS ON HEADINGS
    unique, counts = np.unique(y_all, return_counts=True)
    print("\nFinal Class Distribution:")
    total_samples = len(y_all)
    for level, count in zip(unique, counts):
        if level == 0:
            print(f"  Level {level} (Not heading): {count} samples ({count/total_samples*100:.2f}%)")
        else:
            print(f"  Level {level}: {count} samples ({count/total_samples*100:.2f}%)")
    
    heading_samples = np.sum(y_all > 0)
    print(f"Total heading samples: {heading_samples}/{total_samples} ({heading_samples/total_samples*100:.2f}%)")

    # Data Validation and Quality Check - FOCUS ON HEADINGS
    if enable_data_validation and len(X_all) > 0:
        print("\n" + "="*70)
        print("DATA QUALITY VALIDATION - HEADING FOCUS")
        print("="*70)
        
        validation_report = detector.data_validator.validate_data_quality(
            X_all, y_all, detector.feature_names
        )
        
        print(f"Overall Quality Score: {validation_report['overall_quality_score']:.2f}/1.00")
        print("\nQuality Flags (Heading Focus):")
        for flag, value in validation_report['quality_flags'].items():
            status = "✓" if value else "✗"
            print(f"  {status} {flag}: {value}")
        
        # Quick validation to ensure data is trainable - FOCUS ON HEADINGS
        is_data_ready = detector.data_validator.validate_data_before_training(X_all, y_all, detector.feature_names)
        if not is_data_ready:
            print("\n❌ Data validation failed - cannot proceed with training")
            return None, None
        
        # Save validation report
        with open(output_path / 'data_validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, indent=2, ensure_ascii=False)

    # Split train/val/test with indices
    indices = np.arange(len(X_all))
    
    # First split: train + temp vs test
    X_train_val, X_test, y_train_val, y_test, indices_train_val, indices_test = train_test_split(
        X_all, y_all, indices, test_size=1-train_ratio-val_ratio, random_state=42, stratify=y_all
    )
    
    # Second split: train vs val
    X_train, X_val, y_train, y_val, indices_train, indices_val = train_test_split(
        X_train_val, y_train_val, indices_train_val, test_size=val_ratio/(train_ratio+val_ratio), 
        random_state=42, stratify=y_train_val
    )

    print(f"\nDataset split:")
    print(f"  Training:   {len(X_train)} samples")
    print(f"  Validation: {len(X_val)} samples (for threshold optimization)")
    print(f"  Testing:    {len(X_test)} samples")

    # Cross-Validation for small datasets
    cv_results = {}
    if enable_cross_validation and len(X_train) > 0:
        cv_results = detector.cross_validate(X_train, y_train, cv_folds=min(5, len(X_train)//10))
        
        # Save CV results
        with open(output_path / 'cross_validation_results.json', 'w', encoding='utf-8') as f:
            json.dump(cv_results, f, indent=2, ensure_ascii=False)

    # Train model with validation set for threshold optimization
    print("\n" + "="*70)
    print("TRAINING LIGHTGBM WITH THRESHOLD OPTIMIZATION")
    print("="*70)

    if optimize_thresholds:
        y_train_adj = detector.train(X_train, y_train, X_val, y_val)
    else:
        y_train_adj = detector.train(X_train, y_train)

    # Evaluate
    print("\n" + "="*70)
    print("EVALUATION ON TEST SET - HEADING FOCUS")
    print("="*70)

    # Standard evaluation - FOCUS ON HEADINGS
    metrics = detector.evaluate(X_test, y_test)
    
    # ENHANCED: Heading-specific evaluation
    if len(X_test) > 0 and all_lines:  # Only if we have lines data
        # Get test lines for enhanced evaluation using precomputed indices_test
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            heading_metrics = detector.evaluate_heading_detection(X_test, y_test, test_lines)
            metrics['heading_detection'] = heading_metrics

    # POST-TRAINING CROSS-VERIFICATION (only after model is trained)
    if enable_data_validation and len(X_test) > 0 and all_lines:
        print("\n" + "="*70)
        print("POST-TRAINING CROSS-VERIFICATION - HEADING FOCUS")
        print("="*70)
        
        # Use the precomputed indices_test to get test lines
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            verification_results = detector.data_validator.cross_verify_predictions(
                detector, X_test, y_test, test_lines
            )
            
            print(f"High confidence heading samples: {len(verification_results.get('high_confidence_samples', []))}")
            print(f"Low confidence heading samples: {len(verification_results.get('low_confidence_samples', []))}")
            print(f"Potential heading misclassifications: {len(verification_results.get('potential_misclassifications', []))}")
            
            # Save verification results
            with open(output_path / 'cross_verification_report.json', 'w', encoding='utf-8') as f:
                json.dump(verification_results, f, indent=2, ensure_ascii=False)
        else:
            print("  ⚠ No test lines available for cross-verification")

    # Save all model versions and training info
    training_info = {
        'training_date': datetime.now().isoformat(),
        'dataset_info': {
            'total_samples': len(X_all),
            'training_samples': len(X_train),
            'validation_samples': len(X_val),
            'test_samples': len(X_test),
            'class_distribution': {str(k): int(v) for k, v in zip(unique, counts)},
            'optimal_thresholds': detector.optimal_thresholds
        },
        'model_metrics': metrics,
        'cross_validation_results': cv_results,
        'cache_key': cache_key,
        'data_validation': {
            'overall_quality_score': validation_report.get('overall_quality_score', 0) if enable_data_validation else 'not_performed'
        }
    }
    
    # Save all model versions
    main_model_path = detector.save_all_models(metrics, training_info)

    # Save training info separately
    with open(output_path / 'training_info.json', 'w', encoding='utf-8') as f:
        json.dump(training_info, f, indent=2, ensure_ascii=False)

    # Save metrics as CSV - FOCUS ON HEADING METRICS
    metrics_df = pd.DataFrame([{
        'overall_accuracy': metrics['overall_accuracy'],
        'heading_accuracy': metrics['heading_accuracy'],
        'heading_precision': metrics['heading_precision'],
        'heading_recall': metrics['heading_recall'],
        'heading_f1': metrics['heading_f1']
    }])
    metrics_df.to_csv(output_path / 'metrics_lgb.csv', index=False)

    # Print optimal thresholds
    print(f"\nOptimal Thresholds for Heading Classes:")
    for level, threshold in detector.optimal_thresholds.items():
        print(f"  Level {level}: {threshold:.3f}")

    print("\n✅ Enhanced Training with Threshold Optimization complete!")

    return detector, metrics


if __name__ == "__main__":
    try:
        # Enhanced training with threshold optimization
        detector, metrics = train_and_evaluate(
            use_cached_data=True,
            enable_cross_validation=True,
            enable_data_validation=True,
            optimize_thresholds=True  # Enable threshold optimization
        )
        if detector is None:
            print("\nTraining failed - no data processed")
    except Exception as e:
        print(f"❌ Training failed: {e}")
        import traceback
        traceback.print_exc()

# ============================================================
# pdf_extractor_mineru.py
# ============================================================

import subprocess
import shutil
from pathlib import Path
from tqdm import tqdm
import os
import time

INPUT_DIR = Path(r'working/cleaned_pdfs_test')
state = 'test' if 'test' in str(INPUT_DIR).lower() else 'train'
WORKING_DIR = Path(r'working')
OUTPUT_DIR = WORKING_DIR / f'output_mineru_raw_{state}'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def find_pdf_directory(base_dir):
    pdf_dirs = []
    for root, dirs, files in os.walk(base_dir):
        pdf_files = [f for f in files if f.lower().endswith('.pdf')]
        if pdf_files:
            pdf_dirs.append((Path(root), pdf_files))
    
    if pdf_dirs:
        pdf_dirs.sort(key=lambda x: len(x[1]), reverse=True)
        return pdf_dirs[0]
    return None, []


class PDFExtractorBatch:
    
    def __init__(self, batch_size=10):
        """
        Xử lý theo batch thay vì từng file
        - 1 lần init models phục vụ nhiều PDFs
        - Giảm overhead từ 28.7s/PDF xuống 28.7s/batch
        """
        self.batch_size = batch_size
    
    def extract_batch(self, pdf_paths, output_dir):
        """Xử lý 1 batch PDFs"""
        # Tạo temp dir cho batch
        batch_temp_dir = output_dir / f"batch_temp_{int(time.time())}"
        batch_temp_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy PDFs vào temp dir
        temp_pdfs = []
        for pdf_path in pdf_paths:
            temp_pdf = batch_temp_dir / pdf_path.name
            shutil.copy2(pdf_path, temp_pdf)
            temp_pdfs.append(temp_pdf)
        
        # Chạy mineru cho toàn bộ batch
        mineru_output = output_dir / f"batch_output_{int(time.time())}"
        
        env = os.environ.copy()
        env['MINERU_DEVICE_MODE'] = 'cuda'
        # env['MINERU_FORMULA_ENABLE'] = 'false'  # ← Thêm dòng này

        
        cmd = [
            "mineru",
            "-p", str(batch_temp_dir),  # Process entire directory
            "-o", str(mineru_output),
            "--method","txt",
            "--format", "markdown",
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=3600)
            
            if result.returncode != 0:
                print(f"Batch failed: {result.stderr[:200]}")
                return {}
            
            # Move results to final locations
            results = {}
            for pdf_path in pdf_paths:
                pdf_name = pdf_path.stem
                
                # Find output for this PDF
                source_dir = mineru_output / pdf_name / "txt"
                if not source_dir.exists():
                    results[pdf_name] = "Failed: No output"
                    continue
                
                # Create final output dir
                final_dir = output_dir / pdf_name
                final_dir.mkdir(parents=True, exist_ok=True)
                
                # Move markdown
                md_file = source_dir / f"{pdf_name}.md"
                if md_file.exists():
                    final_md = final_dir / "main.md"
                    shutil.copy2(md_file, final_md)
                    results[pdf_name] = final_md.read_text(encoding='utf-8')
                else:
                    results[pdf_name] = "Failed: No markdown"
                
                # Move images
                images_source = source_dir / "images"
                if images_source.exists():
                    images_dest = final_dir / "images"
                    if images_dest.exists():
                        shutil.rmtree(images_dest)
                    shutil.copytree(images_source, images_dest)
            
            # Cleanup
            shutil.rmtree(batch_temp_dir, ignore_errors=True)
            shutil.rmtree(mineru_output, ignore_errors=True)
            
            return results
            
        except Exception as e:
            print(f"Batch error: {e}")
            return {}
    
    def extract_all(self, pdf_dir: Path, output_dir: Path) -> dict:
        pdf_files = sorted(Path(pdf_dir).glob("*.pdf"))
        all_results = {}
        
        # Split into batches
        batches = [pdf_files[i:i + self.batch_size] 
                  for i in range(0, len(pdf_files), self.batch_size)]
        
        print(f"\n🚀 Processing {len(pdf_files)} PDFs in {len(batches)} batches")
        print(f"   Batch size: {self.batch_size}")
        print(f"   Expected init overhead: {len(batches)} × 28.7s = {len(batches) * 28.7:.1f}s")
        
        start_time = time.time()
        
        for batch_idx, batch in enumerate(batches, 1):
            print(f"\n📦 Batch {batch_idx}/{len(batches)} ({len(batch)} PDFs)")
            batch_start = time.time()
            
            batch_results = self.extract_batch(batch, output_dir)
            all_results.update(batch_results)
            
            batch_elapsed = time.time() - batch_start
            print(f"   ⏱️  Batch time: {batch_elapsed:.1f}s ({batch_elapsed/len(batch):.1f}s per PDF)")
            
            # Progress
            processed = sum(len(b) for b in batches[:batch_idx])
            remaining_batches = len(batches) - batch_idx
            eta = remaining_batches * batch_elapsed
            print(f"   Progress: {processed}/{len(pdf_files)} | ETA: {eta/60:.1f} min")
        
        total_elapsed = time.time() - start_time
        avg_per_pdf = total_elapsed / len(pdf_files)
        
        print(f"\n⏱️  Total time: {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")
        print(f"📊 Avg per PDF: {avg_per_pdf:.1f}s")
        print(f"🚀 Speedup vs sequential: {109/avg_per_pdf:.2f}x")
        
        return all_results


# Main execution
pdf_dir, pdf_files = find_pdf_directory(INPUT_DIR)

if pdf_dir:
    print("\n" + "="*50)
    print("TASK 1: PDF EXTRACTION (BATCH MODE)")
    print("="*50)
    
    # Batch size tuning:
    # - Small (5-10): More overhead, better memory control
    # - Medium (10-20): Balance
    # - Large (20-50): Less overhead, risk OOM
    extractor = PDFExtractorBatch(batch_size=20)
    
    extracted_contents = extractor.extract_all(pdf_dir, OUTPUT_DIR)
    
    print("\n=== EXTRACTION SUMMARY ===")
    success = sum(1 for c in extracted_contents.values() if not c.startswith("Failed"))
    failed = len(extracted_contents) - success
    
    print(f"✓ Success: {success}/{len(extracted_contents)}")
    if failed > 0:
        print(f"✗ Failed: {failed}")
else:
    print("\n✗ Cannot proceed without PDF files")


# ============================================================
# qa_system.py
# ============================================================

import os
import re
import gc
import csv
import time
import warnings
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any, Set

import numpy as np
import pandas as pd
import torch
import faiss

from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

from rag_system import AdvancedRAGSystem, auto_generate_data
# ===========================================================================
# PART 2: OPTIMIZED QA SYSTEM (SEQUENTIAL + BATCH + MEMORY CLEANUP)
# ============================================================================

class OptimizedQASystem:
    """
    Optimized QA with:
    - Batch processing
    - Soft probabilities
    - Conservative selection
    - Memory cleanup
    """

    def __init__(self, model_name: str, device="cuda"):
        self.model_name = model_name
        self.device = device
        self.model = None
        self.tokenizer = None
        self.pipe = None

    def load_model(self):
        """Load model into memory"""
        print(f"\n[QA] Loading {self.model_name}...")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True
        )

        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=100,
            temperature=0.1,
            do_sample=False,
            return_full_text=False
        )

        print(f"✓ Model loaded: {self.model_name}")

    def unload_model(self):
        """Unload model and free memory"""
        print(f"\n[QA] Unloading {self.model_name}...")

        if self.model is not None:
            del self.model
        if self.tokenizer is not None:
            del self.tokenizer
        if self.pipe is not None:
            del self.pipe

        self.model = None
        self.tokenizer = None
        self.pipe = None

        # Clean GPU memory
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        # Clean system memory
        gc.collect()

        print("✓ Model unloaded, memory cleaned")

    def _detect_question_complexity(self, question: str, context: str) -> str:
        """
        Detect question type and return reasoning complexity
        
        Returns: 'simple', 'calculation', 'comparison', 'inference'
        """
        q = question.lower()
        # Từ khóa cho các loại câu hỏi
        calculation_keywords = ['tính', 'bao nhiêu', 'phần trăm', 'số', 'đếm', 'tổng']
        comparison_keywords = ['so sánh', 'khác nhau', 'giống nhau', 'hơn', 'thấp hơn', 'cao hơn']
        inference_keywords = ['suy ra', 'kết luận', 'có thể', 'dẫn đến', 'vì vậy', 'do đó']
        
        if any(kw in q for kw in calculation_keywords):
            return 'calculation'
        if any(kw in q for kw in comparison_keywords):
            return 'comparison'
        if any(kw in q for kw in inference_keywords):
            return 'inference'
        return 'simple'


    def _get_reasoning_steps(self, complexity: str) -> str:
        """
        Return reasoning steps string based on the complexity type
        """
        steps = {
            'simple': (
                "1. Tìm thông tin liên quan trong bối cảnh.\n"
                "2. So sánh với đáp án cần đánh giá.\n"
                "3. Kết luận đáp án đúng (Y) hay sai (N)."
            ),
            'calculation': (
                "1. Xác định các số liệu liên quan trong bối cảnh.\n"
                "2. Xác định phép tính cần thực hiện.\n"
                "3. Tính toán và kiểm tra kết quả.\n"
                "4. So sánh với đáp án.\n"
                "5. Kết luận đáp án đúng (Y) hay sai (N)."
            ),
            'comparison': (
                "1. Xác định các đối tượng cần so sánh.\n"
                "2. Liệt kê đặc điểm, số liệu của các đối tượng.\n"
                "3. Phân tích điểm giống và khác.\n"
                "4. So sánh với đáp án.\n"
                "5. Kết luận đáp án đúng (Y) hay sai (N)."
            ),
            'inference': (
                "1. Xác định các tiền đề trong bối cảnh.\n"
                "2. Áp dụng quy luật logic hoặc sự kiện liên quan.\n"
                "3. Thực hiện các bước suy diễn logic.\n"
                "4. So sánh với đáp án.\n"
                "5. Kết luận đáp án đúng (Y) hay sai (N)."
            )
        }
        return steps.get(complexity, steps['simple'])
    
    
    def evaluate_single_option(self, question: str, option_letter: str,
                               option_text: str, context: str = "") -> float:
        """
        Adaptive reasoning evaluation with dynamic prompt structure
        
        Returns: confidence score float in [0,1]
        """
        try:
            complexity = self._detect_question_complexity(question, context)
            reasoning_steps = self._get_reasoning_steps(complexity)
    
            prompt = f"""Bạn là chuyên gia phân tích đáp án trắc nghiệm tiếng việt, có khả năng đánh giá chính xác từng lựa chọn dựa trên câu hỏi, ngữ cảnh và hướng dẫn suy luận. Nhiệm vụ của bạn là xác định liệu đáp án được đưa ra là đúng (Y) hay sai (N) — không cần giải thích lý do.

##Nguyên tắc đánh giá:
- Tập trung tuyệt đối vào phần “CÂU HỎI” để xác định yêu cầu chính của đề bài.
- Ngữ cảnh đầu vào có thể chứa thông tin nhiễu, nên chỉ sử dụng các chi tiết thật sự liên quan đến câu hỏi.
- Đối chiếu đáp án với câu hỏi và hướng dẫn suy luận để xác định tính đúng/sai.
- Phân tích thật kỹ trước khi đưa ra câu trả lời cho câu hỏi và phải xác minh thật chuẩn và chính xác 
- Chỉ đưa ra kết quả cuối cùng là đúng(Y) hoặc sai(N) thôi không kèm theo gì cái gì khác 
## BỐI CẢNH
{context[:2500]}

## CÂU HỎI 
{question}

## ĐÁP ÁN CẦN ĐÁNH GIÁ 
{option_letter}. {option_text}

=== HƯỚNG DẪN ĐÁNH GIÁ (Loại câu hỏi: {complexity.upper()}) ===
{reasoning_steps}

Chỉ trả lời cuối cùng: Y (đúng) hoặc N (sai)

Trả lời:"""
    
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
    
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=1,
                    output_scores=True,
                    return_dict_in_generate=True,
                    temperature=0.7,
                    do_sample=False,
                    pad_token_id=self.tokenizer.eos_token_id
                )
    
            if not hasattr(outputs, 'scores') or len(outputs.scores) == 0:
                return 0.5
    
            first_token_logits = outputs.scores[0][0]
    
            y_tokens, n_tokens = [], []
    
            for y_var in ["Y", "y", " Y", " y"]:
                ids = self.tokenizer.encode(y_var, add_special_tokens=False)
                if len(ids) > 0:
                    y_tokens.append(ids[0])
    
            for n_var in ["N", "n", " N", " n"]:
                ids = self.tokenizer.encode(n_var, add_special_tokens=False)
                if len(ids) > 0:
                    n_tokens.append(ids[0])
    
            y_tokens = list(set(y_tokens))
            n_tokens = list(set(n_tokens))
    
            if not y_tokens or not n_tokens:
                return 0.5
    
            probs = torch.softmax(first_token_logits, dim=-1)
    
            y_prob = max([probs[tid].item() for tid in y_tokens])
            n_prob = max([probs[tid].item() for tid in n_tokens])
    
            total = y_prob + n_prob
            confidence = y_prob / total if total > 0 else 0.5
    
            confidence = max(0.0, min(1.0, confidence))
    
            return confidence
    
        except Exception as e:
            print(f"    [WARN] Logit extraction failed for {option_letter}: {str(e)[:80]}")
    
            try:
                response = self.pipe(
                    prompt,
                    max_new_tokens=1,
                    temperature=0.7
                )[0]['generated_text'].strip().upper()
    
                if response.startswith('Y'):
                    return 0.75
                elif response.startswith('N'):
                    return 0.25
                else:
                    return 0.5
            except:
                return 0.5


    def process_batch(self, questions: List[dict], rag: AdvancedRAGSystem,
                     batch_size: int = 5) -> List[dict]:
        """
        Process batch of questions

        Args:
            questions: List of {question, options_dict}
            rag: RAG system for context retrieval
            batch_size: Number of questions to process together

        Returns:
            List of results with soft probabilities
        """

        if self.model is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")

        results = []
        total = len(questions)

        print(f"\n[QA] Processing {total} questions in batches of {batch_size}...")

        for start_idx in range(0, total, batch_size):
            end_idx = min(start_idx + batch_size, total)
            batch = questions[start_idx:end_idx]

            # Process batch
            for i, q_data in enumerate(batch):
                question = q_data['question']
                options = q_data['options']

                # Get context from RAG
                try:
                    retrieved = rag.retrieve(question, top_k=3)
                    context = "\n\n".join([r.chunk for r in retrieved])
                except:
                    context = ""

                # Evaluate each option
                option_scores = {}
                for opt_letter, opt_text in options.items():
                    score = self.evaluate_single_option(
                        question, opt_letter, opt_text, context
                    )
                    option_scores[opt_letter] = score

                # Conservative selection
                selected = self._select_conservative(option_scores, threshold=0.65)

                results.append({
                    'question_id': q_data['question_id'],
                    'question': question,
                    'option_scores': option_scores,
                    'selected_answers': selected,
                    'num_correct': len(selected),
                    'answers': ''.join(sorted(selected))
                })

                if (start_idx + i + 1) % 50 == 0:
                    print(f"  ✓ Processed {start_idx + i + 1}/{total}")

        print(f"  ✓ Batch processing complete: {len(results)} results")

        return results

    def _select_conservative(self, scores: Dict[str, float],
                            threshold: float = 0.65) -> List[str]:
        """
        Conservative answer selection

        Strategy:
        - High threshold to avoid penalty
        - Max 2 answers
        - Prefer fewer over many wrong
        """

        sorted_opts = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        selected = []
        for opt, score in sorted_opts:
            if score >= threshold:
                selected.append(opt)

        # Safety: at least 1 answer
        if not selected:
            selected = [sorted_opts[0][0]]

        # Safety: max 2 answers
        if len(selected) > 2:
            selected = selected[:2]

        return sorted(selected)


# ============================================================================
# PART 3: SEQUENTIAL ENSEMBLE PIPELINE
# ============================================================================

def run_single_model(model_name: str, questions: List[dict], rag: AdvancedRAGSystem,
                     output_csv: str, batch_size: int = 5):
    """
    Run single model on all questions

    Pipeline:
    1. Load model
    2. Process all questions in batches
    3. Save results to CSV
    4. Unload model and clean memory
    """

    print(f"\n{'='*80}")
    print(f"RUNNING MODEL: {model_name}")
    print(f"{'='*80}")

    # Initialize QA system
    qa = OptimizedQASystem(model_name, device="cuda")

    # Load model
    qa.load_model()

    # Process all questions
    results = qa.process_batch(questions, rag, batch_size=batch_size)

    # Save to CSV with soft probabilities
    save_results_with_probabilities(results, output_csv)

    # Unload and cleanup
    qa.unload_model()

    print(f"\n✓ Model {model_name} complete")
    print(f"✓ Results saved to: {output_csv}")

    return results


def save_results_with_probabilities(results: List[dict], output_path: str):
    """Save results with soft probabilities"""

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Header
        writer.writerow([
            'question_id', 'num_correct', 'answers',
            'prob_A', 'prob_B', 'prob_C', 'prob_D'
        ])

        # Data
        for r in results:
            scores = r['option_scores']
            writer.writerow([
                r['question_id'],
                r['num_correct'],
                r['answers'],
                f"{scores['A']:.4f}",
                f"{scores['B']:.4f}",
                f"{scores['C']:.4f}",
                f"{scores['D']:.4f}"
            ])

    print(f"  ✓ Saved {len(results)} results to {output_path}")


def ensemble_multiple_csvs(csv_files: List[str], 
                          output_csv: str,
                          threshold: float = 0.70,
                          weights: Optional[List[float]] = None):
    
    print(f"\n{'='*80}")
    print(f"FINAL ENSEMBLE FROM {len(csv_files)} MODELS")
    print(f"{'='*80}")
    
    # Validate and normalize weights
    if weights is None:
        weights = [1.0 / len(csv_files)] * len(csv_files)
        print(f"Using equal weights: {weights}")
    else:
        assert len(weights) == len(csv_files), \
            f"Weights length ({len(weights)}) != Models count ({len(csv_files)})"
        
        # Normalize
        total = sum(weights)
        weights = [w / total for w in weights]
        print(f"Normalized weights: {[f'{w:.4f}' for w in weights]}")
    
    # Load all predictions
    dfs = [pd.read_csv(f) for f in csv_files]
    
    final_results = []
    
    for idx in range(len(dfs[0])):
        # Weighted aggregation
        all_probs = {'A': [], 'B': [], 'C': [], 'D': []}
        
        for df in dfs:
            row = df.iloc[idx]
            all_probs['A'].append(float(row['prob_A']))
            all_probs['B'].append(float(row['prob_B']))
            all_probs['C'].append(float(row['prob_C']))
            all_probs['D'].append(float(row['prob_D']))
        
        # Weighted average
        final_probs = {}
        for opt in ['A', 'B', 'C', 'D']:
            final_probs[opt] = sum(w * p for w, p in zip(weights, all_probs[opt]))
        
        # Select answers
        sorted_opts = sorted(final_probs.items(), key=lambda x: x[1], reverse=True)
        
        selected = []
        for opt, prob in sorted_opts:
            if prob >= threshold:
                selected.append(opt)
        
        if not selected:
            selected = [sorted_opts[0][0]]
        
        if len(selected) > 2:
            selected = selected[:2]
        
        final_results.append({
            'question_id': idx,
            'num_correct': len(selected),
            'answers': ''.join(sorted(selected))
        })
    
    # Save
    pd.DataFrame(final_results).to_csv(output_csv, index=False)
    print(f"\n✓ Saved to: {output_csv}")

# ============================================================
# qa_task.py
# ============================================================

import os
import re
import gc
import csv
import time
import warnings
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any, Set

import numpy as np
import pandas as pd
import torch
import faiss

from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

from rag_system import AdvancedRAGSystem, auto_generate_data
from qa_system import run_single_model, ensemble_multiple_csvs
warnings.filterwarnings("ignore")


extracted_contents = auto_generate_data("working/output_mineru_test")

rag_system = AdvancedRAGSystem(
    extracted_contents=extracted_contents,
    embedding_model="AITeamVN/Vietnamese_Embedding_v2"
)

# Step 2: Load questions
print("\n[STEP 2] Loading questions...")

df = pd.read_csv('private_test/input/question.csv')

questions = []
for idx, row in df.iterrows():
    questions.append({
        'question_id': idx,
        'question': row['Question'],
        'options': {
            'A': row['A'],
            'B': row['B'],
            'C': row['C'],
            'D': row['D']
        }
    })

print(f"✓ Loaded {len(questions)} questions")

# Step 3: Run models sequentially
model_configs = [
    {
        'name':  'Qwen/Qwen3-4B-Instruct-2507',  
        'output': 'test\model_Qwen3-4b_qwen.csv'
    },
]

csv_files = []

for i, config in enumerate(model_configs, 1):
    print(f"\n[STEP {3+i-1}] Running Model {i}/{len(model_configs)}...")

    run_single_model(
        model_name=config['name'],
        questions=questions,
        rag=rag_system,
        output_csv=config['output'],
        batch_size=10  # Adjust based on GPU memory
    )

    csv_files.append(config['output'])

# # Step 4: Final ensemble
# weights = [1]

# ensemble_multiple_csvs(
#     csv_files=csv_files,
#     output_csv='submission.csv',
#     threshold=0.70 ,
#     weights=weights
# )

print("\n" + "="*80)
print("✓ PIPELINE COMPLETE")

# ============================================================
# rag_system.py
# ============================================================

import os
import re
import torch
import warnings
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
from sentence_transformers import CrossEncoder
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import re
import time
import numpy as np
import faiss
import torch
import pandas as pd
from typing import List, Dict, Optional, Tuple, Any, Set
from collections import defaultdict
from dataclasses import dataclass, field
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.text_splitter import RecursiveCharacterTextSplitter

warnings.filterwarnings("ignore")


class DocumentLoader:
    """Load documents từ cấu trúc folder Public_XXX/main.md"""
    
    def __init__(self, root_folder: str):
        self.root_folder = Path(root_folder)
        self.encodings = ['utf-8', 'latin1', 'cp1252', 'utf-16']
    
    def load_all(self) -> Tuple[Dict[str, str], Dict[str, str]]:
        """
        Load tất cả documents từ folder
        
        Returns:
            (extracted_contents, file_id_mapping)
            extracted_contents: {full_path: content}
            file_id_mapping: {file_id: full_path}
        """
        if not self.root_folder.exists():
            raise FileNotFoundError(f"Folder không tồn tại: {self.root_folder}")
        
        extracted_contents = {}
        file_id_mapping = {}
        
        for folder in self.root_folder.iterdir():
            if not folder.is_dir():
                continue
            
            if not self._is_valid_folder(folder.name):
                continue
            
            content = self._read_document(folder)
            if content:
                file_id = self._extract_file_id(folder.name)
                file_path = str(folder / "main.md")
                extracted_contents[file_path] = content
                file_id_mapping[file_id] = file_path
        
        return extracted_contents, file_id_mapping
    
    def _is_valid_folder(self, folder_name: str) -> bool:
        """Kiểm tra folder có đúng format Public_XXX hoặc Private_XXX"""
        return bool(re.match(r'^(Public|Private)_\d+', folder_name, re.IGNORECASE))
    
    def _extract_file_id(self, folder_name: str) -> str:
        """Chuẩn hóa file_id: Public_001, Private_002"""
        match = re.search(r'(Public|Private)_(\d+)', folder_name, re.IGNORECASE)
        if match:
            prefix = match.group(1).capitalize()
            number = match.group(2)
            return f"{prefix}_{number}"
        return folder_name
    
    def _read_document(self, folder: Path) -> Optional[str]:
        """Đọc nội dung file main.md với fallback encoding"""
        main_md = folder / "main.md"
        
        if not main_md.exists():
            return None
        
        for encoding in self.encodings:
            try:
                return main_md.read_text(encoding=encoding)
            except UnicodeDecodeError:
                continue
        
        # Fallback cuối cùng: ignore errors
        return main_md.read_text(encoding='utf-8', errors='ignore')


def auto_generate_data(root_folder: str, device: str = None) -> Tuple[Dict[str, str], Dict[str, str]]:
    loader = DocumentLoader(root_folder)
    raw_contents, file_mapping = loader.load_all()
    
    extracted_contents = {}
    
    for file_id, file_path in file_mapping.items():
        content = raw_contents[file_path]
        output_key = f"{file_id}.md"
        extracted_contents[output_key] = content
    
    # Trả về dict rỗng cho document_types để tương thích
    return extracted_contents

@dataclass
class ChunkMetadata:
    """Metadata for each chunk"""
    file_id: str
    file_path: str
    global_idx: int
    chunk_idx_in_file: int
    heading_level: int
    heading_text: str
    parent_headings: List[str]
    content_type: str  # 'heading', 'content', 'nested', 'child_content', 'parent_chunk'
    section_type: Optional[str] = None

@dataclass
class SearchResult:
    """Search result with rich metadata"""
    chunk: str
    score: float
    file_id: str
    chunk_idx: int
    heading_level: int
    heading_text: str
    parent_headings: List[str]
    search_mode: str
    retrieval_score: float
    rerank_score: float
    section_type: Optional[str] = None

@dataclass
class DocumentNode:
    """Class to store parent-child chunk relationship"""
    parent_chunk: str
    parent_metadata: ChunkMetadata
    child_chunks: List[str]
    child_metadata: List[ChunkMetadata]

import re
import json
import torch
from typing import List
from transformers import AutoTokenizer, AutoModelForCausalLM

class LLMQueryExpander:
    def __init__(self, model_path: str = "Qwen/Qwen2.5-3B-Instruct"):
        print(f"Khởi tạo LLM Query Expander với model: {model_path}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="cuda",
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        self.model.eval()
        
        self.expansion_patterns = {
            'là gì': ['nghĩa là gì', 'định nghĩa', 'khái niệm', 'giải thích'],
            'là bao nhiêu': ['bằng bao nhiêu', 'giá trị', 'cụ thể là'],
            'như thế nào': ['ra sao', 'thế nào', 'cách nào'],
            'có độ phức tạp': ['độ phức tạp thuật toán', 'phức tạp thời gian'],
            'cách': ['làm thế nào để', 'phương pháp', 'hướng dẫn']
        }
    
    def expand_query(self, query: str, max_expansions: int = 2) -> List[str]:
        try:
            llm_variants = self._llm_expand(query, max_expansions)
            
            if llm_variants:
                final_results = [query] if query not in llm_variants else []
                final_results.extend([v for v in llm_variants if v != query])
                return final_results[:max_expansions + 1]
            
            rule_variants = self._rule_based_expand(query, max_expansions)
            final_results = [query]
            final_results.extend([v for v in rule_variants if v != query])
            return final_results[:max_expansions + 1]
            
        except Exception:
            return [query]
    
    def _llm_expand(self, query: str, max_expansions: int) -> List[str]:
        try:
            prompt = f"""Bạn là trợ lý NLP chuyên viết lại câu hỏi để cải thiện tìm kiếm.

NHIỆM VỤ:
- Từ câu hỏi đầu vào (gọi là "câu gốc"), hãy viết lại CHÍNH XÁC {max_expansions} phiên bản khác nhau nhưng GIỮ NGUYÊN Ý NGHĨA.
- Chỉ sử dụng TIẾNG VIỆT THUẦN (không pha ngôn ngữ khác, không phiên âm, không ký hiệu lạ/emoji).

BẢO TOÀN NGHIĨA & CHỦ THỂ (INVARIANTS) — BẮT BUỘC:
1) GIỮ NGUYÊN CHỦ THỂ/TRỌNG TÂM của câu gốc (người/vật/thực thể/chủ đề chính). Không thay thế, không đổi hướng.
2) GIỮ NGUYÊN CÁC THỰC THỂ ĐẶC THÙ: tên riêng (người/tổ chức/thuật toán/mẫu/phiên bản/ký hiệu), chính tả và hoa-thường.
3) GIỮ CÁC RÀNG BUỘC NGỮ CẢNH: thời gian (năm/tháng/ngày), miền/phạm vi, đơn vị đo (Hz, MHz, ms, %, kg, km…), điều kiện/giới hạn (≤, ≥, >, <), ngôn ngữ/khung (ví dụ: “trong Python”, “trên Windows”, “ở Việt Nam”).
4) GIỮ CỰC TÍNH/PHỦ ĐỊNH: không đổi khẳng định ↔ phủ định, so sánh ↔ không so sánh.
5) KHÔNG thêm/bỏ thực thể, con số, đơn vị, điều kiện; KHÔNG khái quát hoá hay cụ thể hoá hơn câu gốc.
6) KHÔNG đổi loại câu hỏi và lưu ý đầu ra luôn là câu hỏi tuyệt đối không tra lời nó(định nghĩa ↔ so sánh ↔ giải thích ↔ cách làm…); giữ mục đích hỏi giống nhau.

ĐA DẠNG DIỄN ĐẠT:
- Đa dạng cấu trúc/cụm từ, nhưng không đổi nội dung cốt lõi.
- Dùng từ phổ thông, rõ ràng; giữ dạng câu hỏi (dấu “?” khi phù hợp).
- Mỗi biến thể 3–20 từ, ≤150 ký tự, không xuống dòng, không markdown/HTML.

CẤM TUYỆT ĐỐI:
- Không in ra lời giải thích, tiêu đề, chú thích, “ví dụ”, “candidates”, “explanation”, thẻ như <think>, hoặc khối ```…```.
- Không trả về placeholder (A1, B2, …), không viết “dan” thay “và”, không chèn tiếng Anh/Trung hay ký tự điều khiển.
- Không lặp lại gần như y hệt; mỗi biến thể phải có khác biệt ngôn ngữ hữu ích cho tìm kiếm.

ĐẦU RA DUY NHẤT HỢP LỆ:
- CHỈ một JSON array gồm CHÍNH XÁC {max_expansions} chuỗi tiếng Việt.
- Không được in kèm bất cứ ký tự nào ngoài JSON.

QUY TRÌNH (thực hiện nội bộ, KHÔNG in ra):
1) Trích xuất các bất biến: chủ thể chính; tên riêng/thuật ngữ; ràng buộc thời gian/phạm vi/đơn vị/điều kiện; cực tính; loại câu hỏi.
2) Sinh nhiều bản nháp diễn đạt khác nhau.
3) TỰ KIỂM (self-check) từng biến thể: có giữ đủ bất biến không? có thêm/bớt gì không? tiếng Việt thuần? độ dài hợp lệ? kết thúc bằng “?” khi cần?
4) Loại bản vi phạm; khử trùng lặp; nếu thiếu số lượng, sinh bổ sung rồi kiểm tra lại.

CÂU GỐC:
"{query}"

HÃY TRẢ VỀ NGAY MỘT JSON ARRAY CHỨA CHÍNH XÁC {max_expansions} CHUỖI TIẾNG VIỆT, KHÔNG THÊM GÌ KHÁC.
Ví dụ định dạng (chỉ là minh hoạ về cấu trúc, KHÔNG dùng nội dung sau):
["biến thể 1", "biến thể 2"]
"""
            
            messages = [{"role": "user", "content": prompt}]
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=526,
                    temperature=0.3,
                    top_p=0.75,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.2
                )
            
            response = self.tokenizer.decode(
                outputs[0][inputs.input_ids.shape[1]:],
                skip_special_tokens=True
            ).strip()
            
            variants = self._parse_json_response(response, query, max_expansions)
            vietnamese_variants = [v for v in variants if self._is_vietnamese(v)]
            
            return vietnamese_variants
            
        except Exception:
            return []
    
    def _is_vietnamese(self, text: str) -> bool:
        if not text or len(text) < 3:
            return False
        
        if re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text):
            return False
        
        vietnamese_chars = r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]'
        has_vietnamese_chars = bool(re.search(vietnamese_chars, text.lower()))
        
        vietnamese_keywords = [
            'là', 'của', 'và', 'có', 'trong', 'được', 'cho', 'với', 'để',
            'thuật toán', 'độ phức tạp', 'cách', 'phương pháp', 'gì', 'nào',
            'như thế nào', 'bao nhiêu', 'thế nào'
        ]
        has_vietnamese_words = any(keyword in text.lower() for keyword in vietnamese_keywords)
        
        english_keywords = [
            'how to', 'what is', 'steps for', 'method for', 'algorithm',
            'the', 'a ', 'an ', 'is ', 'are ', 'for ', 'of '
        ]
        has_english_keywords = any(keyword in text.lower() for keyword in english_keywords)
        
        if has_english_keywords and not has_vietnamese_chars:
            return False
        
        return has_vietnamese_chars or has_vietnamese_words
    
    def _parse_json_response(self, response: str, original_query: str, expected_count: int) -> List[str]:
        response = re.sub(r'</?think>.*?(?=\n|$)', '', response, flags=re.DOTALL).strip()
        
        try:
            data = json.loads(response)
            if isinstance(data, list):
                variants = [str(item).strip() for item in data if isinstance(item, str)]
                variants = [v for v in variants if 8 <= len(v) <= 150 and v != original_query]
                return variants[:expected_count]
        except json.JSONDecodeError:
            pass
        
        json_match = re.search(r'\[([^\[\]]+)\]', response)
        if json_match:
            try:
                json_str = json_match.group(0)
                data = json.loads(json_str)
                if isinstance(data, list):
                    variants = [str(item).strip() for item in data if isinstance(item, str)]
                    variants = [v for v in variants if 8 <= len(v) <= 150 and v != original_query]
                    return variants[:expected_count]
            except json.JSONDecodeError:
                pass
        
        return self._extract_variants_freetext(response, original_query, expected_count)
    
    def _extract_variants_freetext(self, response: str, original_query: str, max_variants: int) -> List[str]:
        if not response or len(response) < 5:
            return []
        
        noise_patterns = [
            r'^(Đây là|Dưới đây là|Tôi đã viết|Có thể viết lại|Các cách viết).*?:\s*',
            r'(Hay còn nói cách khác|Nhớ rằng|Lưu ý|Chú ý).*$',
        ]
        
        cleaned_response = response
        for pattern in noise_patterns:
            cleaned_response = re.sub(pattern, '', cleaned_response, flags=re.IGNORECASE | re.MULTILINE)
        
        lines = cleaned_response.split('\n')
        variants = []
        
        for line in lines:
            line = line.strip()
            if not line or len(line) < 8:
                continue
            
            cleaned = re.sub(r'^(Cách\s*\d+[\:\.\)]?\s*|[\d]+[\.\)\:]\s*|[-•*]\s*)', '', line, flags=re.IGNORECASE)
            cleaned = cleaned.strip(' "\'')
            
            if 8 <= len(cleaned) <= 150:
                if not re.search(r'(là\s+O\(|bằng\s+\d|độ phức tạp.*(là|bằng)\s+\w+\()', cleaned):
                    if cleaned != original_query and cleaned not in variants:
                        variants.append(cleaned)
            
            if len(variants) >= max_variants:
                break
        
        return variants
    
    def _rule_based_expand(self, query: str, max_expansions: int) -> List[str]:
        variants = []
        query_lower = query.lower()
        
        for pattern, replacements in self.expansion_patterns.items():
            if pattern in query_lower:
                for replacement in replacements[:max_expansions]:
                    variant = re.sub(
                        re.escape(pattern),
                        replacement,
                        query,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    if variant != query and variant not in variants:
                        variants.append(variant)
                    
                    if len(variants) >= max_expansions:
                        break
                break
        
        if not variants:
            synonyms = {
                'thuật toán': 'algorithm',
                'độ phức tạp': 'complexity',
                'cách': 'phương pháp',
                'là gì': 'nghĩa là gì'
            }
            
            for original, synonym in synonyms.items():
                if original in query_lower:
                    variant = re.sub(
                        re.escape(original),
                        synonym,
                        query,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    if variant != query:
                        variants.append(variant)
                        break
        
        return variants[:max_expansions]


class HierarchicalChunker:
    """
    Smart chunking that respects hierarchical heading structure
    Strategy:
    - H1 (title): Skip or use as document title
    - H2 (section): Create chunks per section
    - H3 (subsection): Group content under subsection
    - Content: Chunk by size but keep heading context
    - Special handling for tables, formulas, and long text
    """
    def __init__(self, 
                 parent_chunk_size: int = 1024,  # Kích thước chunk cha
                 child_chunk_size: int = 256,    # Kích thước chunk con
                 overlap_size: int = 50,         # Overlap cho chunk con
                 min_chunk_size: int = 50):
        self.parent_chunk_size = parent_chunk_size
        self.child_chunk_size = child_chunk_size
        self.overlap_size = overlap_size
        self.min_chunk_size = min_chunk_size
        self.heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        self.list_pattern = re.compile(r'^[ \s]*[-*+]\s+', re.MULTILINE)
        # Khởi tạo text splitter cho child chunks
        self.child_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.child_chunk_size,
            chunk_overlap=self.overlap_size,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def _extract_tables(self, text: str) -> List[str]:
        """
        Trích xuất các bảng từ văn bản HTML/Markdown
        Giữ nguyên vẹn từng bảng để tránh chia cắt không hợp lý
        """
        tables = []
        # Pattern 1: Bảng HTML (<table>...</table>)
        table_pattern = r'<table[^>]*>.*?</table>'
        html_tables = re.findall(table_pattern, text, re.DOTALL | re.IGNORECASE)
        tables.extend(html_tables)
        # Pattern 2: Bảng Markdown (|-|-| và |-|-|-|)
        markdown_pattern = r'(\|[^\\n]+\|[^\\n]*\n(\|[^\\n]+\|[^\\n]*\n)+)'
        markdown_tables = re.findall(markdown_pattern, text)
        for match in markdown_tables:
            if isinstance(match, tuple):
                tables.append(match[0])
            else:
                tables.append(match)
        # Pattern 3: Bảng được định dạng bằng dấu gạch ngang và dấu pipe
        ascii_pattern = r'((?:.*?\|.*?\n){2,}(?:-+\|[-+\s]+\n)(?:.*?\|.*?\n)+)'
        ascii_tables = re.findall(ascii_pattern, text)
        tables.extend(ascii_tables)
        # Loại bỏ các bảng trùng lặp
        unique_tables = []
        for table in tables:
            if table not in unique_tables:
                unique_tables.append(table)
        return unique_tables
    
    def _chunk_section_content(self, 
                              content: str, 
                              section_header: str,
                              section_type: str,
                              context_prefix: str,
                              file_id: str,
                              base_size: int,
                              overlap: int) -> List[Tuple[str, ChunkMetadata]]:
        """Chunk nội dung của một section với kích thước lớn hơn"""
        lines = content.split('\n')
        chunks = []
        current_chunk = []
        current_size = 0
        chunk_counter = 0
        
        # Các mẫu để xác định điểm phân chia tự nhiên
        natural_break_patterns = [
            r'^\s*[-•*]\s',           # Danh sách
            r'^\d+\.\s',              # Danh sách đánh số
            r'^\s*[A-Z][a-z]+\s*:\s', # Định nghĩa
            r'\.\s*$',                # Cuối câu
        ]
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            
            words = stripped.split()
            current_chunk.append(line)
            current_size += len(words)
            
            # Điểm phân chia tự nhiên
            is_natural_break = (
                (current_size >= base_size and 
                 any(re.search(pattern, line) for pattern in natural_break_patterns)) or
                (current_size >= base_size * 1.2)  # Giới hạn cứng
            )
            
            if is_natural_break:
                chunk_text = '\n'.join(current_chunk)
                meta = ChunkMetadata(
                    file_id=file_id,
                    file_path=f"chunk_{chunk_counter}",
                    global_idx=-1,
                    chunk_idx_in_file=chunk_counter,
                    heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                    heading_text=section_header,
                    parent_headings=[section_header],
                    content_type='content',
                    section_type=section_type,
                )
                chunks.append((context_prefix + chunk_text, meta))
                chunk_counter += 1
                
                # Keep overlap - giữ lại phần cuối để context
                overlap_lines = current_chunk[-(overlap // 8):]
                current_chunk = overlap_lines
                current_size = sum(len(l.split()) for l in overlap_lines)
        
        # Last chunk
        if current_chunk:
            chunk_text = '\n'.join(current_chunk)
            meta = ChunkMetadata(
                file_id=file_id,
                file_path=f"chunk_{chunk_counter}",
                global_idx=-1,
                chunk_idx_in_file=chunk_counter,
                heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                heading_text=section_header,
                parent_headings=[section_header],
                content_type='content',
                section_type=section_type,
            )
            chunks.append((context_prefix + chunk_text, meta))
        
        return chunks
    
    def _split_by_structure(self, text: str, struct_info: Dict[str, Any]) -> List[Dict]:
        """
        Chia văn bản thành các phần dựa trên cấu trúc tài liệu
        """
        sections = []
        

        section_pattern = r'(?:#\s+(.*?)(?:\n|$))|(?:##\s+(.*?)(?:\n|$))|(?:###\s+(.*?)(?:\n|$))'
        
        # Tìm các section trong văn bản
        current_section = {
            'header': 'Introduction',
            'content': '',
            'type': 'introduction'
        }
        
        lines = text.split('\n')
        in_section = False
        current_header = ''
        
        for line in lines:
            header_match = re.match(r'^(#{1,3})\s+(.+)$', line.strip())
            if header_match:
                # Lưu section hiện tại nếu có nội dung
                if current_section['content'].strip():
                    sections.append(current_section.copy())
                
                # Bắt đầu section mới
                level = len(header_match.group(1))
                header_text = header_match.group(2)
                current_header = header_text
                
                section_type = 'main_section' if level == 1 else 'subsection'
                if 'bảng' in header_text.lower() or 'table' in header_text.lower():
                    section_type = 'table_section'
                elif 'công thức' in header_text.lower() or 'formula' in header_text.lower():
                    section_type = 'formula_section'
                
                current_section = {
                    'header': header_text,
                    'content': '',
                    'type': section_type
                }
                in_section = True
            else:
                if in_section:
                    current_section['content'] += line + '\n'
                else:
                    current_section['content'] += line + '\n'
        
        # Thêm section cuối cùng
        if current_section['content'].strip():
            sections.append(current_section)
        
        return sections
    
    def _generate_document_summary(self, content: str) -> str:
        """
        Generate robust document summary based on structure and content patterns
        
        Strategy:
        1. Identify first substantial paragraph after structural elements
        2. Skip headings, lists, tables, and technical artifacts
        3. Extract meaningful sentences with proper truncation
        4. Multiple fallbacks for different document structures
        """
        # Chuẩn bị lines và loại bỏ dòng trống
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Các mẫu cấu trúc cần bỏ qua
        structural_patterns = [
            r'^#{1,6}\s',       # Markdown headings (# đến ######)
            r'^[-*+]\s',        # Danh sách bullet
            r'^\d+\.\s',        # Danh sách đánh số
            r'^\|',             # Bảng Markdown
            r'^```',            # Code blocks
            r'^<table',         # Bảng HTML
            r'^<div',           # HTML containers
            r'^>',              # Blockquotes
            r'^!\[',            # Hình ảnh
            r'^\[',             # Liên kết/tham chiếu
            r'^[\*\_]{3,}',     # Đường phân cách
            r'^\s*$',           # Dòng trống
        ]
        
        # Bước 1: Tìm đoạn văn bản thực sự đầu tiên
        main_content = []
        capture_started = False
        
        for line in lines:
            # Kiểm tra xem dòng có phải là phần cấu trúc không
            is_structural = any(re.match(pattern, line, re.IGNORECASE) for pattern in structural_patterns)
            
            # Bắt đầu capture khi gặp dòng nội dung thực sự đầu tiên
            if not capture_started and not is_structural and len(line.split()) >= 8:
                capture_started = True
            
            # Thu thập nội dung sau khi bắt đầu capture
            if capture_started and not is_structural:
                # Bỏ qua các dòng quá ngắn hoặc có tính chất metadata
                if len(line.split()) >= 5 and not re.match(r'^(Ngày|Date|Version|Tác giả|Author):', line, re.IGNORECASE):
                    main_content.append(line)
            
            # Dừng khi đã có đủ nội dung
            if len(main_content) >= 4 or (main_content and len(' '.join(main_content)) > 400):
                break
        
        # Bước 2: Xử lý và tạo tóm tắt từ nội dung thu thập được
        if main_content:
            text = ' '.join(main_content)
            
            # Tách thành các câu và lấy 1-2 câu đầu tiên
            sentences = re.split(r'(?<=[.!?])\s+', text.strip())
            meaningful_sentences = []
            
            for sent in sentences:
                # Lọc các câu có ý nghĩa (tránh câu quá ngắn hoặc fragment)
                if len(sent.split()) >= 6 and not re.match(r'^\W*$', sent):
                    meaningful_sentences.append(sent.strip())
                if len(meaningful_sentences) >= 2:
                    break
            
            if meaningful_sentences:
                summary = ' '.join(meaningful_sentences[:2])
                
                # Cắt gọn ở ranh giới câu nếu quá dài
                if len(summary) > 350:
                    # Tìm điểm kết thúc câu gần nhất trước vị trí 300
                    safe_point = max(
                        summary[:300].rfind('.'),
                        summary[:300].rfind('!'),
                        summary[:300].rfind('?')
                    )
                    if safe_point > 100:  # Đảm bảo phần tóm tắt có ý nghĩa
                        summary = summary[:safe_point+1] + '...'
                    else:
                        summary = summary[:300] + '...'
                return summary.strip()
        
        # Fallback 1: Lấy 2-3 dòng đầu tiên không phải cấu trúc
        fallback_lines = []
        for line in lines:
            if not any(re.match(pattern, line, re.IGNORECASE) for pattern in structural_patterns):
                if len(line.split()) >= 4 and not re.match(r'^(File|Document|ID):', line, re.IGNORECASE):
                    fallback_lines.append(line)
            if len(fallback_lines) >= 3:
                break
        
        if fallback_lines:
            summary = ' '.join(fallback_lines[:2])
            return summary[:350] + '...' if len(summary) > 350 else summary
        
        # Fallback 2: Sử dụng metadata hoặc mô tả mặc định
        return "Tài liệu kỹ thuật không có phần giới thiệu rõ ràng. Vui lòng tham khảo các section cụ thể để tìm thông tin chi tiết."
        
    def chunk_document_to_nodes(self, 
                               text: str, 
                               file_id: str,
                               struct_info: Optional[Dict[str, Any]] = None) -> List[DocumentNode]:
        """
        Tạo ra các node tài liệu, mỗi node chứa chunk cha và các chunk con.
        Strategy Small-to-Large:
        - Chunk cha (parent): 1024 tokens - để trả về làm context
        - Chunk con (child): 256 tokens - để tìm kiếm
        """

        
        doc_summary = self._generate_document_summary(text)  # Dùng hàm mới
        
        # Prefix context cho tất cả chunk
        file_context = f"[TÀI LIỆU: {file_id}] "
        
        nodes = []
        global_parent_idx = 0
        global_child_idx = 0
        
        # Bước 1: Xử lý bảng trước - giữ nguyên vẹn từng bảng
        tables = self._extract_tables(text)
        for i, table in enumerate(tables):
            if len(table) > 50:  # Chỉ xử lý bảng có nội dung đáng kể
                # Tạo parent chunk cho bảng (nguyên vẹn)
                parent_meta = ChunkMetadata(
                    file_id=file_id,
                    file_path=f"table_{i}",
                    global_idx=global_parent_idx,
                    chunk_idx_in_file=i,
                    heading_level=3,
                    heading_text=f"Bảng {i+1}",
                    parent_headings=[],
                    content_type='parent_chunk',
                    section_type='table_data',
                )
                parent_chunk = file_context + f"[BẢNG {i+1}] {table}"
                
                # Chia bảng thành các child chunks nhỏ hơn nếu cần
                child_chunks = self.child_splitter.split_text(parent_chunk)
                child_metadata = []
                
                for j, child_text in enumerate(child_chunks):
                    child_meta = ChunkMetadata(
                        file_id=file_id,
                        file_path=f"table_{i}_child_{j}",
                        global_idx=global_child_idx,
                        chunk_idx_in_file=j,
                        heading_level=3,
                        heading_text=f"Bảng {i+1} - Phần {j+1}",
                        parent_headings=[f"Bảng {i+1}"],
                        content_type='child_content',
                        section_type='table_data',
                    )
                    child_metadata.append(child_meta)
                    global_child_idx += 1
                
                # Tạo node và thêm vào danh sách
                node = DocumentNode(
                    parent_chunk=parent_chunk,
                    parent_metadata=parent_meta,
                    child_chunks=child_chunks,
                    child_metadata=child_metadata
                )
                nodes.append(node)
                global_parent_idx += 1
        
        
        # Bước 3: Chia text thành các phần lớn dựa trên cấu trúc
        sections = self._split_by_structure(text, struct_info)
        
        # Bước 4: Tạo parent và child chunks cho từng section
        for section in sections:
            section_header = section['header']
            section_content = section['content']
            section_type = section['type']
            
            # Tạo context string cho section
            section_context = f"[PHẦN: {section_header}] [LOẠI: {section_type}] "
            
            # Tạo parent chunk từ toàn bộ section
            parent_content = section_context + section_content
            parent_chunk = file_context + parent_content
            
            parent_meta = ChunkMetadata(
                file_id=file_id,
                file_path=f"section_{global_parent_idx}",
                global_idx=global_parent_idx,
                chunk_idx_in_file=global_parent_idx,
                heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                heading_text=section_header,
                parent_headings=[section_header],
                content_type='parent_chunk',
                section_type=section_type,
            )
            
            # Chia thành các child chunks
            child_chunks = self.child_splitter.split_text(parent_chunk)
            child_metadata = []
            
            for j, child_text in enumerate(child_chunks):
                child_meta = ChunkMetadata(
                    file_id=file_id,
                    file_path=f"section_{global_parent_idx}_child_{j}",
                    global_idx=global_child_idx,
                    chunk_idx_in_file=j,
                    heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                    heading_text=f"{section_header} - Phần {j+1}",
                    parent_headings=[section_header],
                    content_type='child_content',
                    section_type=section_type,
                )
                child_metadata.append(child_meta)
                global_child_idx += 1
            
            node = DocumentNode(
                parent_chunk=parent_chunk,
                parent_metadata=parent_meta,
                child_chunks=child_chunks,
                child_metadata=child_metadata
            )
            nodes.append(node)
            global_parent_idx += 1
        
        return nodes

class AdvancedRAGSystem:
    """
    Advanced RAG system with:
    - Parent Document Retriever (Small-to-Large strategy)
    - Optimized reranking logic (prioritizing cross-encoder scores)
    - LLM-based query expansion
    - Hierarchical document chunking with table handling
    - Adaptive retrieval strategies
    - Document type aware processing
    - Integration with LLM for QA
    """
    def __init__(self, 
                 extracted_contents: Dict[str, str],
                 embedding_model: str = "AITeamVN/Vietnamese_Embedding_v2",
                 reranker_model: str = "namdp-ptit/ViRanker",
                 llm_model_path: str = "Qwen/Qwen2.5-3B-Instruct",
                 embedding_dim: int = 728,
                 device: str = "cuda" if torch.cuda.is_available() else "cpu"):
        """
        Initialize Advanced RAG System
        Args:
            extracted_contents: {file_path: markdown_content}
            embedding_model: Qwen model to use
            reranker_model: Cross-encoder for reranking
            llm_model_path: Path to LLM model for query expansion and QA
            embedding_dim: Output dimension for embeddings
            device: 'cuda' or 'cpu'
        """
        self.device = device
        self.embedding_dim = embedding_dim
        self.ready = False
        
        print("\n" + "="*100)
        print("INITIALIZING ADVANCED RAG SYSTEM WITH PARENT DOCUMENT RETRIEVER")
        print("="*100)
        
        if not extracted_contents:
            print("❌ No documents provided")
            return
        
        # Initialize query expander
        print(f"\n[0/6] Loading LLM Query Expander...")
        self.query_expander = LLMQueryExpander(model_path=llm_model_path)
        print("  ✓ LLM Query Expander ready")
        
        print(f"\n[1/6] Loading embedding model: {embedding_model}")
        self.embedding_model = SentenceTransformer(embedding_model, device=device)
        print(f"  ✓ Loaded on device: {device}")
        
        print(f"\n[2/6] Processing documents with hierarchical chunking (Parent-Child strategy)...")
        self._process_documents_hierarchically(extracted_contents)
        
        print(f"\n[3/6] Building dense index (FAISS) for child chunks...")
        self._build_dense_index()
        
        print(f"\n[4/6] Building sparse index (BM25) for child chunks...")
        self._build_sparse_index()
        
        print(f"\n[5/6] Loading reranker: {reranker_model}")
        self.reranker = CrossEncoder(reranker_model, device=device)
        print(f"  ✓ Reranker ready")
        
        print(f"\n[6/6] System ready for queries")
        self.ready = True
        self._print_stats()
    
    def _extract_file_id(self, file_path: str) -> str:
        """Extract file ID from path (Public_XXX, Private_XXX, etc)"""
        match = re.search(r'(Public_\d+|Private_\d+)', file_path, re.IGNORECASE)
        if match:
            return match.group(1)
        # Fallback: use folder name
        parts = file_path.replace('\\', '/').split('/')
        if len(parts) >= 2:
            return parts[-2]
        return file_path.split('/')[-1].replace('.md', '')
    
    
    def _process_documents_hierarchically(self, extracted_contents: Dict[str, str]):
        """Process documents into parent-child chunk hierarchy"""
        # Structures for parent-child relationship
        self.parent_chunks_store = {}  # parent_idx -> parent_chunk_text
        self.parent_metadata_store = {}  # parent_idx -> parent_metadata
        self.child_to_parent_map = {}  # child_global_idx -> parent_idx
        self.child_chunks = []  # List of all child chunks for indexing
        self.child_metadata_list = []  # Metadata for each child chunk
        
        self.file_id_to_chunks = defaultdict(list)  # file_id -> list of child indices
        self.file_metadata = {}  # file_id -> metadata
        
        chunker = HierarchicalChunker(
            parent_chunk_size=768,  # Kích thước chunk cha
            child_chunk_size=256,    # Kích thước chunk con
            overlap_size=64,         # Overlap cho chunk con
            min_chunk_size=64
        )
        
        global_parent_idx_counter = 0
        
        for file_path, content in extracted_contents.items():
            if not content or not content.strip():
                continue
            
            file_id = self._extract_file_id(file_path)            
            # Prepare structure info for smart chunking
            struct_info = {
                'metadata': {
                    'document_summary': self._generate_document_summary(content)
                }
            }
            
            # Chunk with hierarchical awareness and structure handling
            document_nodes = chunker.chunk_document_to_nodes(content, file_id, struct_info)
            
            file_child_indices = []
            
            # Process each document node (parent-child relationship)
            for node in document_nodes:
                parent_idx = global_parent_idx_counter
                
                # Store parent chunk and metadata
                self.parent_chunks_store[parent_idx] = node.parent_chunk
                self.parent_metadata_store[parent_idx] = node.parent_metadata
                
                # Process child chunks
                for child_idx_in_node, (child_text, child_meta) in enumerate(zip(node.child_chunks, node.child_metadata)):
                    global_child_idx = len(self.child_chunks)
                    
                    # Set proper indices
                    child_meta.global_idx = global_child_idx
                    child_meta.chunk_idx_in_file = child_idx_in_node
                    
                    # Store child chunk and metadata
                    self.child_chunks.append(child_text)
                    self.child_metadata_list.append(child_meta)
                    
                    # Map child to parent
                    self.child_to_parent_map[global_child_idx] = parent_idx
                    
                    # Track file-specific chunks
                    file_child_indices.append(global_child_idx)
                
                global_parent_idx_counter += 1
            
            # Store file metadata
            self.file_id_to_chunks[file_id] = file_child_indices
            self.file_metadata[file_id] = {
                'path': file_path,
                'num_parents': len(document_nodes),
                'num_children': len(file_child_indices)
            }
        
        # Set chunks to child chunks for indexing
        self.chunks = self.child_chunks
        self.chunk_metadata_list = self.child_metadata_list
        
        print(f"  ✓ Processed {len(self.file_metadata)} files")
        print(f"  ✓ Total parent chunks: {len(self.parent_chunks_store)}")
        print(f"  ✓ Total child chunks (for indexing): {len(self.chunks)}")
        
        # Show distribution
        if self.file_metadata:
            parent_counts = [meta['num_parents'] for meta in self.file_metadata.values()]
            child_counts = [meta['num_children'] for meta in self.file_metadata.values()]
            
            print(f"  • Min parents/file: {min(parent_counts)}")
            print(f"  • Max parents/file: {max(parent_counts)}")
            print(f"  • Avg parents/file: {np.mean(parent_counts):.1f}")
            
            print(f"  • Min children/file: {min(child_counts)}")
            print(f"  • Max children/file: {max(child_counts)}")
            print(f"  • Avg children/file: {np.mean(child_counts):.1f}")
    
    def _generate_document_summary(self, content: str) -> str:
        """
        Tóm tắt thông minh không phụ thuộc document type:
        1. Lấy nội dung sau heading đầu tiên
        2. Giới hạn 2-3 câu đầu tiên
        3. Loại bỏ bảng/formula phức tạp
        """
        # Bước 1: Tách phần giới thiệu sau title
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Bỏ qua các heading (#, ##) và metadata
        body_lines = []
        in_body = False
        
        for line in lines:
            if line.startswith('#'):
                continue
            if re.match(r'^\s*[-*]\s|^\d+\.', line):  # Danh sách
                continue
            if '|' in line and '-' in line:  # Bảng Markdown
                continue
            if line.startswith('<table') or line.startswith('</table'):  # HTML table
                continue
                
            if len(line.split()) > 5:  # Chỉ lấy dòng có nội dung thực
                body_lines.append(line)
            
            if len(body_lines) >= 5:  # Giới hạn 5 dòng đầu
                break
        
        # Bước 2: Ghép thành đoạn và xử lý
        summary = ' '.join(body_lines[:3])  # Chỉ lấy 3 dòng đầu
        
        # Xử lý độ dài
        summary = summary[:400]  # Giới hạn 400 ký tự
        if len(summary) > 380:
            summary = summary[:summary.rfind(' ', 0, 380)] + '...'
        
        # Fallback nếu không có nội dung
        if len(summary.strip()) < 20:
            return "Tài liệu kỹ thuật không có phần giới thiệu."
        
        return summary
    
    def _match_by_document_type(self, query: str) -> Optional[str]:
        """Match file dựa trên loại tài liệu được đề cập trong query"""
        return None
    
    def _build_dense_index(self):
        """Build FAISS index for dense retrieval (on child chunks)"""
        # Add instruction prefix for better Vietnamese understanding
        instruction = "Represent this passage for retrieval: "
        chunks_with_instruction = [instruction + chunk for chunk in self.chunks]
        
        print(f"  Encoding {len(chunks_with_instruction)} child chunks...")
        self.chunk_embeddings = self.embedding_model.encode(
            chunks_with_instruction,
            show_progress_bar=True,
            batch_size=32,
            normalize_embeddings=True,
            convert_to_numpy=True,
            device=self.device
        )
        print(f"  ✓ Embeddings shape: {self.chunk_embeddings.shape}")
        
        # Build FAISS index
        dimension = self.chunk_embeddings.shape[1]
        self.faiss_index = faiss.IndexFlatIP(dimension)
        self.faiss_index.add(self.chunk_embeddings.astype('float32'))
        print(f"  ✓ FAISS index: {self.faiss_index.ntotal} vectors, dim={dimension}")
    
    def _build_sparse_index(self):
        """Build BM25 index for keyword search (on child chunks)"""
        tokenized_chunks = [chunk.lower().split() for chunk in self.chunks]
        self.bm25 = BM25Okapi(tokenized_chunks)
        print(f"  ✓ BM25 index: {len(tokenized_chunks)} documents")
    
    def _detect_file_id_from_query(self, query: str) -> Optional[str]:
        """
        Detect file ID from query with TD651 → Public_651 mapping
        Only maps TD prefix to Public_ (not other prefixes)
        """
        query_lower = query.lower()
        
        # Strategy 1: Look for TD + numbers pattern (only TD maps to Public_)
        td_match = re.search(r'\btd\s*(\d+)\b', query_lower)
        if td_match:
            number = td_match.group(1)
            candidate_id = f"Public_{number}"
            if candidate_id in self.file_metadata:
                return candidate_id
        
        # Strategy 2: Look for explicit Public_XXX patterns
        public_match = re.search(r'\b(public[_\s]*\d+)\b', query_lower)
        if public_match:
            raw_id = public_match.group(1)
            # Normalize format to Public_XXX
            number = re.search(r'\d+', raw_id).group(0)
            candidate_id = f"Public_{number}"
            if candidate_id in self.file_metadata:
                return candidate_id
        
        return None

    def _expand_query(self, query: str, max_expansions: int = 2) -> List[str]:
        """
        Enhanced query expansion with LLM
        Falls back to rule-based expansion if LLM fails
        """
        # Try LLM-based expansion first
        expanded_queries = self.query_expander.expand_query(query, max_expansions=max_expansions)
        
        # Fallback to rule-based if LLM fails
        if len(expanded_queries) <= 1:
            return self._rule_based_query_expansion(query, max_expansions)
        
        return expanded_queries
    
    def _rule_based_query_expansion(self, query: str, max_expansions: int = 2) -> List[str]:
        """Fallback rule-based query expansion with Vietnamese synonyms"""
        expanded = [query]
        synonyms = {
            'bao nhiêu': ['số lượng', 'giá trị'],
            'là gì': ['định nghĩa', 'khái niệm', 'ý nghĩa'],
            'nào': ['những', 'các'],
            'khi nào': ['điều kiện', 'thời điểm'],
            'nguyên nhân': ['lý do', 'tại sao'],
            'phân loại': ['loại', 'nhóm'],
            'độ phức tạp': ['thời gian chạy', 'độ khó'],
            'bài toán': ['vấn đề', 'nhiệm vụ'],
            'phương pháp': ['cách thức', 'giải pháp'],
            'tối ưu': ['hiệu quả', 'cải tiến']
        }
        
        query_lower = query.lower()
        for term, syns in synonyms.items():
            if term in query_lower:
                for syn in syns[:1]:  # Only take first synonym
                    if len(expanded) < max_expansions + 1:
                        new_query = query_lower.replace(term, syn)
                        expanded.append(new_query)
        
        return expanded[:max_expansions + 1]
    
    # Hàm _get_adaptive_alpha - chỉ dựa trên query
    def _get_adaptive_alpha(self, query: str, file_id: Optional[str] = None) -> float:
        """Loại bỏ logic dựa trên document type"""
        query_lower = query.lower()
        keyword_patterns = ['năm', 'ngày', 'số', 'bao nhiêu', 'mã', 'giá trị', 'kích thước']
        if any(kw in query_lower for kw in keyword_patterns):
            return 0.3  # Ưu tiên BM25 cho truy vấn số
        
        semantic_patterns = ['là gì', 'định nghĩa', 'tại sao', 'như thế nào', 'giải thích']
        if any(kw in query_lower for kw in semantic_patterns):
            return 0.8  # Ưu tiên dense vector
        
        return 0.6  # Cân bằng
    
    def retrieve(self,
                 query: str,
                 top_k: int = 10,
                 rerank_candidates: int = 25,
                 use_instruction: bool = True,
                 alpha: Optional[float] = None,
                 verbose: bool = True) -> List[SearchResult]:
        """
        Retrieve relevant chunks using Parent Document Retriever strategy
        Enhanced with optimized reranking (prioritizing cross-encoder scores)
        """
        if not self.ready:
            return []
        
        start_time = time.time()
        
        # PHASE 1: Detect search mode
        target_file_id = self._detect_file_id_from_query(query)
        if target_file_id:
            search_indices = self.file_id_to_chunks[target_file_id]
            search_mode = "FILE-SPECIFIC"
            effective_top_k = min(top_k * 2, len(search_indices))
            effective_rerank = min(rerank_candidates * 2, len(search_indices))
        else:
            search_indices = list(range(len(self.chunks)))
            search_mode = "GLOBAL"
            effective_top_k = top_k
            effective_rerank = rerank_candidates
        
        if verbose:
            print(f"\n{'='*80}")
            print(f"🔍 RETRIEVAL: {search_mode} MODE")
            print(f"{'='*80}")
            if target_file_id:
                print(f"Target file: {target_file_id}")
                print(f"Search space: {len(search_indices)} child chunks")
            else:
                print(f"Search space: {len(search_indices)} child chunks (global)")
        
        # PHASE 2: Expand query using LLM
        queries = self._expand_query(query, max_expansions=2)
        if verbose and len(queries) > 1:
            print(f"Query expansions ({len(queries)}):")
            for i, q in enumerate(queries):
                print(f"  {i+1}. {q}")
        
        # PHASE 3: Hybrid retrieval (on child chunks)
        all_candidates = {}
        
        for q in queries:
            # Add instruction for consistency (Qwen3 uses last-token pooling)
            q_with_instruction = f"Represent this query for retrieval: {q}" if use_instruction else q
            
            # Dense search
            q_embedding = self.embedding_model.encode(
                [q_with_instruction],
                normalize_embeddings=True,
                convert_to_numpy=True,
                device=self.device
            )
            
            if search_mode == "FILE-SPECIFIC":
                dense_scores = []
                for idx in search_indices:
                    score = float(np.dot(q_embedding[0], self.chunk_embeddings[idx]))
                    dense_scores.append((idx, score))
                dense_scores.sort(key=lambda x: x[1], reverse=True)
                top_dense = dense_scores[:effective_top_k * 3]
            else:
                scores, indices = self.faiss_index.search(
                    q_embedding.astype('float32'),
                    effective_top_k * 3
                )
                top_dense = [(int(idx), float(score)) 
                             for idx, score in zip(indices[0], scores[0])]
            
            for idx, score in top_dense:
                if idx not in all_candidates:
                    all_candidates[idx] = {'dense': 0.0, 'bm25': 0.0}
                all_candidates[idx]['dense'] = max(all_candidates[idx]['dense'], score)
            
            # Sparse (BM25) search
            tokenized_q = q.lower().split()
            bm25_scores = self.bm25.get_scores(tokenized_q)
            
            if search_mode == "FILE-SPECIFIC":
                file_bm25 = [(idx, float(bm25_scores[idx])) for idx in search_indices]
                file_bm25.sort(key=lambda x: x[1], reverse=True)
                top_bm25 = file_bm25[:effective_top_k * 3]
            else:
                top_bm25_indices = np.argsort(bm25_scores)[-(effective_top_k * 3):][::-1]
                top_bm25 = [(int(idx), float(bm25_scores[idx])) for idx in top_bm25_indices]
            
            for idx, score in top_bm25:
                if idx not in all_candidates:
                    all_candidates[idx] = {'dense': 0.0, 'bm25': 0.0}
                all_candidates[idx]['bm25'] = max(all_candidates[idx]['bm25'], score)
        
        if not all_candidates:
            return []
        
        # PHASE 4: Score fusion
        max_dense = max((c['dense'] for c in all_candidates.values()), default=1.0)
        max_bm25 = max((c['bm25'] for c in all_candidates.values()), default=1.0)
        
        if max_dense > 0:
            for idx in all_candidates:
                all_candidates[idx]['dense'] /= max_dense
        
        if max_bm25 > 0:
            for idx in all_candidates:
                all_candidates[idx]['bm25'] /= max_bm25
        
        # Adaptive weighting
        if alpha is None:
            alpha = self._get_adaptive_alpha(query, target_file_id)
        
        combined = [
            (idx, alpha * scores['dense'] + (1 - alpha) * scores['bm25'])
            for idx, scores in all_candidates.items()
        ]
        combined.sort(key=lambda x: x[1], reverse=True)
        top_candidates = combined[:effective_rerank]
        
        if verbose:
            print(f"Candidates after fusion: {len(top_candidates)}")
            print(f"Dense/Sparse weight: {alpha:.2f}/{1-alpha:.2f}")
        
        # PHASE 5: Reranking - CẢI TIẾN QUAN TRỌNG: ƯU TIÊN ĐIỂM CỦA RERANKER
        if not top_candidates:
            return []
        
        pairs = [[query, self.chunks[idx]] for idx, _ in top_candidates]
        rerank_scores = self.reranker.predict(pairs, batch_size=32)
        
        # Gắn điểm rerank vào các ứng viên ban đầu
        reranked_candidates = [
            (top_candidates[i][0], rerank_scores[i])  
            for i in range(len(top_candidates))
        ]
        
        # Sắp xếp lại danh sách ứng viên chỉ dựa trên rerank_score
        reranked_candidates.sort(key=lambda x: x[1], reverse=True)
        # =============================================================
        
        if verbose:
            print(f"Reranked candidates: {len(reranked_candidates)} (sorted by reranker score only)")
        
        # PHASE 6: Parent Chunk Expansion
        final_parent_chunks = {}  # parent_idx -> {chunk, max_score, metadata}
        seen_hashes = set()
        
        for child_idx, score in reranked_candidates:
            # Lấy parent index từ map
            parent_idx = self.child_to_parent_map.get(child_idx)
            
            if parent_idx is not None and parent_idx in self.parent_chunks_store:
                # Tạo hash để kiểm tra trùng lặp
                parent_hash = hash(self.parent_chunks_store[parent_idx][:200])
                
                if parent_hash not in seen_hashes:
                    seen_hashes.add(parent_hash)
                    
                    # Lấy metadata của parent
                    parent_meta = self.parent_metadata_store[parent_idx]
                    
                    # Lưu trữ parent chunk với điểm số cao nhất
                    if parent_idx not in final_parent_chunks or score > final_parent_chunks[parent_idx]["score"]:
                        final_parent_chunks[parent_idx] = {
                            "chunk": self.parent_chunks_store[parent_idx],
                            "score": score,
                            "metadata": parent_meta
                        }
            
            # Dừng khi đã đủ số lượng kết quả
            if len(final_parent_chunks) >= top_k:
                break
        
        if verbose:
            print(f"Unique parent chunks after expansion: {len(final_parent_chunks)}")
        
        # Format kết quả cuối cùng
        results = []
        sorted_parents = sorted(final_parent_chunks.items(), key=lambda x: x[1]["score"], reverse=True)
        
        for parent_idx, parent_data in sorted_parents[:top_k]:
            meta = parent_data["metadata"]
            
            # Truy xuất điểm retrieval gốc của child chunks tương ứng
            retrieval_score = 0.0
            for child_idx, score in top_candidates:
                if self.child_to_parent_map.get(child_idx) == parent_idx:
                    retrieval_score = score
                    break
            
            result = SearchResult(
                chunk=parent_data["chunk"],
                score=float(parent_data["score"]),
                file_id=meta.file_id,
                chunk_idx=meta.chunk_idx_in_file,
                heading_level=meta.heading_level,
                heading_text=meta.heading_text,
                parent_headings=meta.parent_headings,
                search_mode=search_mode,
                retrieval_score=float(retrieval_score),
                rerank_score=float(parent_data["score"]),
                section_type=meta.section_type
            )
            results.append(result)
        
        elapsed = time.time() - start_time
        if verbose:
            print(f"\nResults: {len(results)} parent chunks (in {elapsed:.2f}s)")
            if results:
                print(f"Top score: {results[0].score:.4f}")
                print(f"Top chunk section type: {results[0].section_type}")
                print(f"Top chunk heading: {results[0].heading_text}")
        
        return results
    
    def _print_stats(self):
        """Print system statistics"""
        print(f"\n{'='*100}")
        print("SYSTEM READY ✓")
        print(f"{'='*100}")
        print(f"\nSystem Configuration:")
        print(f"  Model: Qwen3-Embedding-0.6B")
        print(f"  Device: {self.device}")
        print(f"  Embedding Dim: {self.embedding_dim}")
        print(f"  Files: {len(self.file_metadata)}")
        print(f"  Parent Chunks: {len(self.parent_chunks_store)}")
        print(f"  Child Chunks: {len(self.chunks)}")
        print(f"  Dense Index: FAISS (IP)")
        print(f"  Sparse Index: BM25")
        
        if self.file_metadata:
            parent_counts = [m['num_parents'] for m in self.file_metadata.values()]
            child_counts = [m['num_children'] for m in self.file_metadata.values()]
            
            print(f"\nParent Chunk Distribution:")
            print(f"  Min: {min(parent_counts)}")
            print(f"  Max: {max(parent_counts)}")
            print(f"  Avg: {np.mean(parent_counts):.1f}")
            print(f"  Total: {sum(parent_counts)}")
            
            print(f"\nChild Chunk Distribution:")
            print(f"  Min: {min(child_counts)}")
            print(f"  Max: {max(child_counts)}")
            print(f"  Avg: {np.mean(child_counts):.1f}")
            print(f"  Total: {sum(child_counts)}")
            

# ============================================================
# table_clean_final.py
# ============================================================

from bs4 import BeautifulSoup
import re
from pathlib import Path
from collections import Counter


class AdvancedTableProcessor:
    def __init__(self, html_string, verbose=True):
        self.html = html_string
        self.verbose = verbose
        self.raw_matrix = []
        self.cleaned_matrix = []
            
    def parse_raw_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        table = soup.find('table')
        if not table:
            raise ValueError("No table found in HTML")

        # 🔴 HARD FILTER: remove hardcoded Viettel AI Race header block (2 rows)
        # Build raw HTML string of the entire table for direct pattern matching
        table_html = str(table)
        
        # Pattern: 2 consecutive <tr> with the exact structure (flexible whitespace, &nbsp;)
        pattern = r'''
            <tr\s*>[^<]*(?:<td[^>]*>&nbsp;</td>\s*){3}
            <td[^>]*>VIETTEL\s+AI\s+RACE</td>
            (?:\s*<td[^>]*>&nbsp;</td>){4}
            <td[^>]*>TD441</td>
            (?:\s*<td[^>]*>&nbsp;</td>){3}\s*</tr>\s*
            <tr\s*>[^<]*(?:<td[^>]*>&nbsp;</td>\s*){3}
            <td[^>]*>BỘ\s+CHỈ\s+TIÊU\s+KỸ\s+THUẬT\s+CHO\s+HỆ\s+THỐNG\s+vCOC</td>
            (?:\s*<td[^>]*>&nbsp;</td>){4}
            <td[^>]*>Lần\s+ban\s+hành:\s*1</td>
            (?:\s*<td[^>]*>&nbsp;</td>){3}\s*</tr>
        '''
        new_table_html = re.sub(pattern, '', table_html, flags=re.IGNORECASE | re.DOTALL | re.VERBOSE)
        
        # Parse the cleaned table
        new_soup = BeautifulSoup(new_table_html, 'html.parser')
        clean_table = new_soup.find('table')
        if not clean_table:
            clean_table = soup.new_tag('table')  # empty table if all removed

        # Now parse rows normally (without the hardcoded block)
        for tr in clean_table.find_all('tr'):
            cells = tr.find_all(['td', 'th'])
            # Skip empty rows
            if all(not td.get_text(strip=True).replace('\xa0', '').strip() for td in cells):
                continue
            row = []
            for td in cells:
                text = td.get_text(strip=True).replace('\xa0', ' ').strip()
                if not text:
                    text = '&nbsp;'
                is_bold = bool(td.find('strong') or td.find('b'))
                has_br = bool(td.find('br'))
                rowspan = int(td.get('rowspan', 1))
                colspan = int(td.get('colspan', 1))
                row.append({
                    'text': text,
                    'is_bold': is_bold,
                    'has_br': has_br,
                    'rowspan': rowspan,
                    'colspan': colspan
                })
            self.raw_matrix.append(row)
        return self
    
    def detect_complex_header(self):
        if not self.raw_matrix:
            return 0
        if len(self.raw_matrix) > 0 and any(
            "YÊU CẦU" in cell['text'] or "STT" in cell['text'].upper()
            for cell in self.raw_matrix[0]
        ):
            return 1
        return 0
    
    def clean_and_merge_complex(self):
        if not self.raw_matrix:
            raise ValueError("Run parse_raw_html() first")
        self.cleaned_matrix = self.raw_matrix
        return self
    
    def generate_clean_html(self):
        if not self.cleaned_matrix:
            raise ValueError("Run clean_and_merge_complex() first")
        html_parts = ['<table>']
        html_parts.append('<tbody>')
        for row in self.cleaned_matrix:
            html_parts.append('<tr>')
            for cell in row:
                if cell.get('rowspan', 1) == 0 or cell.get('colspan', 1) == 0:
                    continue
                attrs = []
                if cell.get('rowspan', 1) > 1:
                    attrs.append(f'rowspan="{cell["rowspan"]}"')
                if cell.get('colspan', 1) > 1:
                    attrs.append(f'colspan="{cell["colspan"]}"')
                attr_str = ' ' + ' '.join(attrs) if attrs else ''
                content = cell['text']
                if cell['is_bold']:
                    content = f'<strong>{content}</strong>'
                html_parts.append(f'<td{attr_str}>{content}</td>')
            html_parts.append('</tr>')
        html_parts.append('</tbody>')
        html_parts.append('</table>')
        return '\n'.join(html_parts)


def is_empty(cell):
    if cell is None:
        return True
    text = cell.get('text', '') if isinstance(cell, dict) else str(cell)
    return not text or not text.strip() or text.strip() == '&nbsp;'


def shift_left_compress_header(matrix, verbose=False):
    if not matrix or not matrix[0]:
        return matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    iteration = 0
    while True:
        changed = False
        iteration += 1
        if verbose:
            print(f"\n{'='*70}\nITERATION {iteration}\n{'='*70}")
        for j in range(num_cols - 1):
            header_current = matrix[0][j]
            header_next = matrix[0][j + 1]
            if is_empty(header_current) and not is_empty(header_next):
                if verbose:
                    print(f"\n📍 [HEADER] Column {j}→{j+1}: empty → value")
                for i in range(num_rows):
                    if is_empty(matrix[i][j]) and not is_empty(matrix[i][j + 1]):
                        val = matrix[i][j + 1].get('text', '') if isinstance(matrix[i][j + 1], dict) else str(matrix[i][j + 1])
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = {'text': '&nbsp;', 'is_bold': False, 'has_br': False, 'rowspan': 1, 'colspan': 1}
                        changed = True
                        if verbose:
                            print(f"  ✓ Row {i}: '{val}' ({i},{j+1}) → ({i},{j})")
            elif is_empty(header_next):
                data_moved = False
                for i in range(1, num_rows):
                    if is_empty(matrix[i][j]) and not is_empty(matrix[i][j + 1]):
                        if verbose and not data_moved:
                            print(f"\n📍 [DATA] Column {j}→{j+1}: source header empty")
                            data_moved = True
                        val = matrix[i][j + 1].get('text', '') if isinstance(matrix[i][j + 1], dict) else str(matrix[i][j + 1])
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = {'text': '&nbsp;', 'is_bold': False, 'has_br': False, 'rowspan': 1, 'colspan': 1}
                        changed = True
                        if verbose:
                            print(f"  ✓ Row {i}: '{val}' ({i},{j+1}) → ({i},{j})")
        if not changed:
            if verbose:
                print(f"\n✅ No changes. Stopping.")
            break
    last_col = num_cols - 1
    while last_col >= 0:
        all_empty = True
        for i in range(num_rows):
            if not is_empty(matrix[i][last_col]):
                all_empty = False
                break
        if all_empty:
            last_col -= 1
        else:
            break
    if last_col >= 0:
        for i in range(num_rows):
            matrix[i] = matrix[i][:last_col + 1]
    if verbose:
        print(f"\n✂️ Trimmed to {last_col + 1} columns")
    return matrix


def merge_and_pad_tables(html_content, verbose=True):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    if verbose:
        print(f"\n📊 Found {len(tables)} tables")
    parsed_tables = []
    for i, table in enumerate(tables):
        proc = AdvancedTableProcessor(str(table), verbose=False)
        proc.parse_raw_html()
        proc.clean_and_merge_complex()
        parsed_tables.append({
            'index': i,
            'processor': proc,
            'html': str(table)
        })
    all_col_counts = []
    has_stt_list = []
    for tbl in parsed_tables:
        proc = tbl['processor']
        header_rows = proc.detect_complex_header()
        data = proc.cleaned_matrix[header_rows:]
        for row in data:
            if row:
                all_col_counts.append(len(row))
        first_row = proc.cleaned_matrix[0] if proc.cleaned_matrix else []
        has_stt_list.append(first_row and first_row[0]['text'].strip().isdigit())
    if all_col_counts:
        counter = Counter(all_col_counts)
        standard_cols = counter.most_common()[0][0]
        if verbose:
            print(f"📐 Column distribution: {dict(counter)}")
            print(f"📊 Standard columns: {standard_cols}")
    else:
        standard_cols = 5
        if verbose:
            print(f"📐 Using fallback: {standard_cols} cols")
    master_has_stt = any(has_stt_list)
    if parsed_tables:
        first_proc = parsed_tables[0]['processor']
        first_cols = len(first_proc.cleaned_matrix[0]) if first_proc.cleaned_matrix else 0
        if first_cols != standard_cols:
            if has_special_technical_header(first_proc.cleaned_matrix):
                if verbose:
                    print(f"\n⚠️ [SKIP] First table has special technical header — skip shift_left_compress_header")
            else:
                if verbose:
                    print(f"\n🔧 [NORMALIZE 1] First table has {first_cols} cols != standard {standard_cols}")
                    print(f"   → Applying shift_left_compress_header...")
                first_proc.cleaned_matrix = shift_left_compress_header(first_proc.cleaned_matrix, verbose=verbose)
            if verbose:
                new_cols = len(first_proc.cleaned_matrix[0]) if first_proc.cleaned_matrix else 0
                print(f"   ✅ Normalized to {new_cols} cols")
    current_stt = 1
    for i, tbl in enumerate(parsed_tables):
        proc = tbl['processor']
        curr_has_stt = has_stt_list[i]
        if i == 0:
            for row in reversed(proc.cleaned_matrix):
                if row and row[0]['text'].strip().isdigit():
                    current_stt = int(row[0]['text'].strip()) + 1
                    break
            continue
        new_matrix = []
        for row in proc.cleaned_matrix:
            if not row:
                continue
            original_data = [cell.copy() for cell in row]
            original_col_count = len(original_data)
            stt_added = 1 if (master_has_stt and not curr_has_stt) else 0
            cols_after_stt = original_col_count + stt_added
            padding_needed = max(0, standard_cols - cols_after_stt)
            new_row = []
            if master_has_stt and not curr_has_stt:
                new_row.append({
                    'text': str(current_stt),
                    'is_bold': False,
                    'has_br': False,
                    'rowspan': 1,
                    'colspan': 1
                })
                current_stt += 1
            for _ in range(padding_needed):
                new_row.append({
                    'text': '&nbsp;',
                    'is_bold': False,
                    'has_br': False,
                    'rowspan': 1,
                    'colspan': 1
                })
            new_row.extend(original_data)
            new_matrix.append(new_row)
        proc.cleaned_matrix = new_matrix
        if verbose:
            print(f"✅ Table {i}: Padded to {standard_cols} cols")
    result_parts = []
    for tbl in parsed_tables:
        result_parts.append(tbl['processor'].generate_clean_html())
    result_html = '\n\n'.join(result_parts)
    result_html = clean_redundant_table_tags(result_html)
    return result_html


def clean_redundant_table_tags(html_content):
    def should_remove_gap(gap_content):
        if not gap_content.strip():
            return True
        cleaned = re.sub(r'<!--.*?-->', '', gap_content, flags=re.DOTALL)
        cleaned = re.sub(r'\s*\|<image_\d+>\|\s*', '', cleaned)
        cleaned = cleaned.strip()
        if not cleaned:
            return True
        return bool(re.fullmatch(r'[\s\-_=*#+\n]{1,50}', cleaned))
    def replace_pair(match):
        full_match = match.group(0)
        gap_content = match.group(2)
        if should_remove_gap(gap_content):
            return ''
        return full_match
    pattern_table = r'(</table>)([^<]*?)(<table[^>]*>)'
    html_content = re.sub(pattern_table, replace_pair, html_content, flags=re.DOTALL)
    pattern_tbody = r'(</tbody>)(\s*)(<tbody>)'
    html_content = re.sub(
        pattern_tbody,
        lambda m: '' if not m.group(2).strip() or should_remove_gap(m.group(2)) else m.group(0),
        html_content,
        flags=re.DOTALL
    )
    return html_content


def parse_html_to_matrix(html_string):
    proc = AdvancedTableProcessor(html_string, verbose=False)
    proc.parse_raw_html()
    proc.clean_and_merge_complex()
    return proc.cleaned_matrix


def matrix_to_html(matrix):
    html_parts = ['<table>']
    html_parts.append('<tbody>')
    for row in matrix:
        html_parts.append('<tr>')
        for cell in row:
            attrs = []
            if cell.get('rowspan', 1) > 1:
                attrs.append(f'rowspan="{cell["rowspan"]}"')
            if cell.get('colspan', 1) > 1:
                attrs.append(f'colspan="{cell["colspan"]}"')
            attr_str = ' ' + ' '.join(attrs) if attrs else ''
            content = cell['text']
            if cell.get('is_bold', False):
                content = f'<strong>{content}</strong>'
            html_parts.append(f'<td{attr_str}>{content}</td>')
        html_parts.append('</tr>')
    html_parts.append('</tbody>')
    html_parts.append('</table>')
    return '\n'.join(html_parts)


def merge_row_with_previous(matrix, stt_col=0, join_with='\n', verbose=False):
    def is_empty(cell):
        if cell is None:
            return True
        text = cell.get('text', '') if isinstance(cell, dict) else str(cell)
        return not text or not text.strip() or text.strip() == '&nbsp;'
    def is_number(cell):
        try:
            text = cell.get('text', '') if isinstance(cell, dict) else str(cell)
            return text.isdigit()
        except:
            return False
    merged_matrix = []
    i = 0
    while i < len(matrix):
        if i > 0 and is_empty(matrix[i][stt_col]) and is_number(matrix[i-1][stt_col]):
            next_is_number = (i + 1 < len(matrix) and is_number(matrix[i+1][stt_col]))
            prev_number = int(matrix[i-1][stt_col].get('text', '') if isinstance(matrix[i-1][stt_col], dict) else str(matrix[i-1][stt_col]))
            next_number = int(matrix[i+1][stt_col].get('text', '') if isinstance(matrix[i+1][stt_col], dict) else str(matrix[i+1][stt_col])) if next_is_number else None
            if next_is_number and next_number == prev_number + 1:
                if verbose:
                    print(f"🟧 Merging row {i} into row {i-1} (STT: {prev_number})")
                for j in range(1, len(matrix[i])):
                    c_prev = matrix[i-1][j]
                    c_cur = matrix[i][j]
                    if not is_empty(c_cur):
                        if isinstance(c_prev, dict):
                            c_prev['text'] += join_with + (c_cur.get('text', '') if isinstance(c_cur, dict) else str(c_cur))
                i += 1
                continue
        merged_matrix.append(matrix[i])
        i += 1
    return merged_matrix
    
def has_special_technical_header(matrix):
    if not matrix or len(matrix) < 1:
        return False
    first_row = matrix[0]
    if len(first_row) < 2:
        return False
    texts = [cell.get('text', '').strip().upper() for cell in first_row]
    if texts[0] == 'STT':
        for t in texts[1:]:
            if 'CẤU HÌNH' in t and 'THÔNG SỐ' in t and 'KỸ THUẬT' in t:
                return True
    return False

def compress_tables_in_file(input_file, output_file=None, verbose=True):
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.parent / f"{input_path.stem}_compressed{input_path.suffix}"
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    if verbose:
        print(f"\n📖 Reading: {input_file}")
    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table')
    if verbose:
        print(f"📊 Found {len(tables)} tables")
        print(f"\n🔧 [NORMALIZE 2] Post-merge normalization...")
    processed_tables = []
    for i, table in enumerate(tables):
        if verbose:
            print(f"\n{'='*70}\nTABLE {i+1}/{len(tables)}\n{'='*70}")
        try:
            # Trong compress_tables_in_file, trong vòng for xử lý từng table:
            matrix = parse_html_to_matrix(str(table))
            if verbose:
                print(f"📐 Original: {len(matrix)} rows × {len(matrix[0]) if matrix else 0} cols")

            matrix = merge_row_with_previous(matrix, verbose=verbose)

            # → Sửa ở đây:
            if has_special_technical_header(matrix):
                if verbose:
                    print("⚠️ Skip shift_left_compress_header (special technical header)")
                compressed_matrix = matrix
            else:
                compressed_matrix = shift_left_compress_header(matrix, verbose=verbose)
            compressed_html = matrix_to_html(compressed_matrix)
            processed_tables.append(compressed_html)
            if verbose:
                print(f"✅ Final: {len(compressed_matrix)} rows × {len(compressed_matrix[0]) if compressed_matrix else 0} cols")
        except Exception as e:
            if verbose:
                print(f"❌ Error: {e}")
            processed_tables.append(str(table))
    pattern = r'<table[^>]*>.*?</table>'
    sections = []
    last_end = 0
    for match in re.finditer(pattern, content, re.DOTALL):
        if match.start() > last_end:
            sections.append(('text', content[last_end:match.start()]))
        sections.append(('table', None))
        last_end = match.end()
    if last_end < len(content):
        sections.append(('text', content[last_end:]))
    table_idx = 0
    result_parts = []
    for section_type, section_content in sections:
        if section_type == 'text':
            result_parts.append(section_content)
        else:
            result_parts.append(processed_tables[table_idx])
            table_idx += 1
    result = ''.join(result_parts)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    if verbose:
        print(f"\n{'='*70}\n✅ DONE\n📁 Output: {output_file}\n{'='*70}")
    return result


def process_markdown_file_complete(input_file_path, output_file_path=None, verbose=True):
    if output_file_path is None:
        input_path = Path(input_file_path)
        output_file_path = input_path.parent / f"{input_path.stem}_final{input_path.suffix}"
    temp_file = Path(input_file_path).parent / "temp_merged.md"
    
    # BƯỚC 1: Merge & Pad (normalize lần 1)
    with open(input_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if verbose:
        print(f"📖 Reading: {input_file_path}\n")
    
    pattern = r'(<table[^>]*>.*?</table>)'
    sections = []
    last_end = 0
    for match in re.finditer(pattern, content, re.DOTALL):
        if match.start() > last_end:
            sections.append(('text', content[last_end:match.start()]))
        sections.append(('table', match.group(1)))
        last_end = match.end()
    if last_end < len(content):
        sections.append(('text', content[last_end:]))
    processed = []
    i = 0
    while i < len(sections):
        if sections[i][0] == 'text':
            processed.append(sections[i][1])
            i += 1
        else:
            table_group = [sections[i][1]]
            j = i + 1
            while j < len(sections):
                if sections[j][0] == 'table':
                    table_group.append(sections[j][1])
                    j += 1
                elif sections[j][0] == 'text':
                    if sections[j][1].strip():
                        break
                    j += 1
                else:
                    break
            combined = '\n\n'.join(table_group)
            merged = merge_and_pad_tables(combined, verbose=verbose)
            processed.append(merged)
            i = j
    temp_content = ''.join(processed)
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(temp_content)
    if verbose:
        print(f"\n💾 Temp saved: {temp_file}")
    
    compress_tables_in_file(temp_file, output_file_path, verbose=verbose)
    
    temp_file.unlink()
    return output_file_path
import os
from pathlib import Path

def process_folder(base_dir: str, pattern: str = "Public_*/main.md", verbose: bool = True):
    base_path = Path(base_dir)
    md_files = list(base_path.glob(pattern))
    
    if not md_files:
        return

    for i, md_file in enumerate(md_files, 1):
        try:
            if verbose:
                print(f"[{i}/{len(md_files)}] {md_file.relative_to(base_path)}")
            process_markdown_file_complete(str(md_file), str(md_file), verbose=verbose)
        except Exception as e:
            print(f"❌ {md_file}: {e}")

if __name__ == "__main__":
    process_folder(r"working\output_mineru_test", verbose=False)


# ============================================================
# training_model_detect.py
# ============================================================

import pymupdf
import numpy as np
import pandas as pd
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
import re
from difflib import SequenceMatcher
import lightgbm as lgb
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, classification_report, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
import joblib
import warnings
import hashlib
import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')


@dataclass
class TextLine:
    text: str
    font_size: float
    font_name: str
    is_bold: bool
    x0: float
    y0: float
    x1: float
    y1: float
    page: int
    page_height: float
    page_width: float

class ThresholdOptimizer:
    """Optimize prediction thresholds for each class to maximize F1-score"""
    
    def __init__(self):
        self.optimal_thresholds = {}
        
    def find_optimal_threshold(self, y_true: np.ndarray, y_probs: np.ndarray, class_label: int) -> float:
        """Find optimal threshold for a specific class to maximize F1-score"""
        if class_label not in np.unique(y_true):
            return 0.
            
        # Get probabilities for this class
        prob_class = y_probs[:, class_label]
        
        # Define objective function to minimize (negative F1)
        def objective(threshold):
            y_pred_class = (prob_class >= threshold).astype(int)
            true_class = (y_true == class_label).astype(int)
            
            if np.sum(y_pred_class) == 0 or np.sum(true_class) == 0:
                return 1.0  # Worst possible F1
                
            precision, recall, f1, _ = precision_recall_fscore_support(
                true_class, y_pred_class, average='binary', zero_division=0
            )
            return -f1  # Minimize negative F1
        
        # Find optimal threshold
        try:
            result = minimize_scalar(objective, bounds=(0.1, 0.9), method='bounded')
            return max(0.1, min(0.9, result.x))
        except:
            return 0.85
    
    def optimize_all_thresholds(self, y_true: np.ndarray, y_probs: np.ndarray, classes: List[int]) -> Dict[int, float]:
        """Optimize thresholds for all specified classes"""
        optimal_thresholds = {}
        
        for class_label in classes:
            if class_label > 0:  # Only optimize for heading classes (1-4)
                threshold = self.find_optimal_threshold(y_true, y_probs, class_label)
                optimal_thresholds[class_label] = threshold
                print(f"  Class {class_label}: optimal threshold = {threshold:.3f}")
        
        return optimal_thresholds
class DataValidator:
    """Validate and verify training data quality"""
    
    def __init__(self):
        self.validation_results = {}
        
    def validate_data_quality(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> Dict[str, Any]:
        """Comprehensive data quality validation"""
        validation_report = {}
        
        # Basic statistics
        validation_report['total_samples'] = len(X)
        validation_report['total_features'] = X.shape[1] if len(X) > 0 else 0
        
        # Class distribution - convert numpy types to Python native types
        unique_classes, class_counts = np.unique(y, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique_classes, class_counts):
            class_dist[int(cls)] = int(count)  # Convert to native Python types
        validation_report['class_distribution'] = class_dist
        
        # Calculate imbalance ratio only for heading classes (1-4)
        heading_counts = [count for cls, count in zip(unique_classes, class_counts) if cls > 0]
        if len(heading_counts) > 1:
            validation_report['heading_imbalance_ratio'] = float(max(heading_counts) / min(heading_counts))
        else:
            validation_report['heading_imbalance_ratio'] = 1.0
        
        # Feature statistics
        feature_stats = {}
        for i, feature_name in enumerate(feature_names):
            if len(X) > 0 and i < X.shape[1]:
                feature_data = X[:, i]
                feature_stats[feature_name] = {
                    'mean': float(np.mean(feature_data)),
                    'std': float(np.std(feature_data)),
                    'min': float(np.min(feature_data)),
                    'max': float(np.max(feature_data)),
                    'missing_values': int(np.sum(np.isnan(feature_data)))
                }
        validation_report['feature_statistics'] = feature_stats
        
        # Data quality flags - FOCUS ON HEADING CLASSES
        validation_report['quality_flags'] = {
            'has_sufficient_samples': len(X) >= 100,
            'has_multiple_heading_classes': len([cls for cls in unique_classes if cls > 0]) > 1,
            'no_missing_values': all(stats['missing_values'] == 0 for stats in feature_stats.values()),
            'reasonable_heading_imbalance': validation_report['heading_imbalance_ratio'] < 10,
            'feature_variance_adequate': all(stats['std'] > 0.01 for stats in feature_stats.values() 
                                           if feature_names[i] not in ['is_bold', 'font_differs', 'is_first', 'ends_period', 'starts_number', 'numbered_pattern', 'all_caps', 'placeholder'])
        }
        
        # Overall quality score
        quality_score = sum(validation_report['quality_flags'].values()) / len(validation_report['quality_flags'])
        validation_report['overall_quality_score'] = float(quality_score)
        
        return validation_report
    
    def cross_verify_predictions(self, detector: 'MLHeadingDetector', X: np.ndarray, y: np.ndarray, 
                               lines: List[TextLine], sample_size: int = 50) -> Dict[str, Any]:
        """Cross-verify predictions with manual inspection logic - ONLY AFTER TRAINING"""
        if len(X) == 0 or detector.model is None:
            print("  ⚠ Skipping cross-verification: Model not trained yet")
            return {}
            
        # Get predictions with optimized thresholds
        y_probs = detector.model.predict_proba(X)
        preds = detector._predict_with_thresholds(X, y_probs)
        
        verification_results = {
            'high_confidence_samples': [],
            'low_confidence_samples': [],
            'potential_misclassifications': [],
            'pattern_analysis': {}
        }
        
        # Analyze confidence scores - ONLY FOR HEADING CLASSES
        heading_indices = preds > 0
        if np.any(heading_indices):
            heading_confidences = np.max(y_probs[heading_indices], axis=1)
            high_confidence_threshold = 0.8
            low_confidence_threshold = 0.6
            
            for i, (true_label, pred_label) in enumerate(zip(y, preds)):
                if i >= sample_size:
                    break
                    
                # Only analyze heading predictions
                if pred_label > 0:
                    confidence = float(y_probs[i, pred_label])
                    
                    line_data = {
                        'text': lines[i].text if i < len(lines) else '',
                        'true_label': int(true_label),
                        'predicted_label': int(pred_label),
                        'confidence': confidence,
                        'is_correct': bool(true_label == pred_label)
                    }
                    
                    if confidence >= high_confidence_threshold:
                        verification_results['high_confidence_samples'].append(line_data)
                    elif confidence <= low_confidence_threshold:
                        verification_results['low_confidence_samples'].append(line_data)
                        
                    if true_label != pred_label and confidence > 0.7:  # High confidence but wrong
                        verification_results['potential_misclassifications'].append(line_data)
        
        # Pattern analysis for numbered headings
        numbered_patterns_analysis = self._analyze_numbered_patterns(lines, y, preds)
        verification_results['pattern_analysis'] = numbered_patterns_analysis
        
        return verification_results

    def validate_data_before_training(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> bool:
        """Quick validation before training to ensure data is usable - FOCUS ON HEADINGS"""
        if len(X) == 0:
            print("  ✗ No training data available")
            return False
            
        # Check for sufficient heading classes (at least 2 heading classes)
        heading_classes = [cls for cls in np.unique(y) if cls > 0]
        if len(heading_classes) < 2:
            print("  ✗ Need at least 2 heading classes for training")
            return False
            
        # Check for sufficient samples per heading class
        unique, counts = np.unique(y, return_counts=True)
        min_samples_per_class = 5
        for cls, count in zip(unique, counts):
            if cls > 0 and count < min_samples_per_class:  # Only check heading classes
                print(f"  ✗ Heading class {cls} has only {count} samples (min: {min_samples_per_class})")
                return False
                
        print("  ✓ Data validation passed - ready for training")
        return True
    
    def _analyze_numbered_patterns(self, lines: List[TextLine], y_true: np.ndarray, 
                                 y_pred: np.ndarray) -> Dict[str, Any]:
        """Analyze numbered pattern detection accuracy - ONLY HEADINGS"""
        analysis = {
            'true_positives': 0,
            'false_positives': 0,
            'false_negatives': 0,
            'pattern_examples': []
        }
        
        numbered_pattern = re.compile(r'^\d+(\.\d+)*\.?\s')
        
        for i, (line, true, pred) in enumerate(zip(lines, y_true, y_pred)):
            if i >= 100:  # Limit analysis to first 100 samples
                break
                
            has_numbered_pattern = bool(numbered_pattern.match(line.text.strip()))
            
            if has_numbered_pattern:
                if true > 0 and pred > 0:  # Correctly detected as heading
                    analysis['true_positives'] += 1
                elif true > 0 and pred == 0:  # Missed heading
                    analysis['false_negatives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_negative'
                    })
                elif true == 0 and pred > 0:  # False positive
                    analysis['false_positives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_positive'
                    })
        
        return analysis



class DataManager:
    """Manage training data caching and loading"""
    
    def __init__(self, cache_dir: str = "working/training_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def get_cache_key(self, input_dir: str, gt_dir: str) -> str:
        """Generate unique cache key based on input directories"""
        dir_info = f"{input_dir}_{gt_dir}"
        return hashlib.md5(dir_info.encode()).hexdigest()[:16]
    
    def save_training_data(self, cache_key: str, X: np.ndarray, y: np.ndarray, 
                         metadata: Dict[str, Any]) -> str:
        """Save training data to cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        # Save data
        np.savez(cache_file, X=X, y=y)
        
        # Convert metadata to JSON-serializable format
        serializable_metadata = self._convert_to_serializable(metadata)
        serializable_metadata['saved_at'] = datetime.now().isoformat()
        serializable_metadata['data_shape'] = X.shape if X is not None else None
        
        # Convert class distribution to serializable format
        if 'class_distribution' in serializable_metadata:
            serializable_metadata['class_distribution'] = {
                str(k): int(v) for k, v in serializable_metadata['class_distribution'].items()
            }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(serializable_metadata, f, indent=2, ensure_ascii=False)
            
        return str(cache_file)
    
    def _convert_to_serializable(self, obj: Any) -> Any:
        """Convert numpy types to Python native types for JSON serialization"""
        if isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {str(k): self._convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_to_serializable(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(self._convert_to_serializable(item) for item in obj)
        else:
            return obj
    
    def load_training_data(self, cache_key: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], Dict[str, Any]]:
        """Load training data from cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        if not cache_file.exists() or not metadata_file.exists():
            return None, None, {}
            
        try:
            # Load data
            data = np.load(cache_file)
            X, y = data['X'], data['y']
            
            # Load metadata
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                
            print(f"✓ Loaded cached training data: {X.shape[0]} samples")
            return X, y, metadata
            
        except Exception as e:
            print(f"✗ Error loading cached data: {e}")
            return None, None, {}
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get information about cached data"""
        cache_files = list(self.cache_dir.glob("*_data.npz"))
        cache_info = {
            'total_cached_datasets': len(cache_files),
            'cache_files': []
        }
        
        for cache_file in cache_files:
            metadata_file = cache_file.with_name(cache_file.stem.replace('_data', '_metadata') + '.json')
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    cache_info['cache_files'].append({
                        'file': cache_file.name,
                        'saved_at': metadata.get('saved_at', 'unknown'),
                        'data_shape': metadata.get('data_shape', 'unknown'),
                        'class_distribution': metadata.get('class_distribution', {})
                    })
                except:
                    continue
                    
        return cache_info


class FeatureExtractor:
    """Extract 22 features from each text line with ENHANCED numbered pattern detection"""

    def __init__(self):
        self.doc_stats = None
        # ENHANCED: Strict numbered patterns - chỉ tập trung vào 1., 1.1, 1.1.1, etc.
        self.numbered_patterns = [
            r'^\d+\.\s+[A-Za-zÀ-ỹ]',  # 1. Text (bắt đầu bằng số, dấu chấm, khoảng trắng, rồi chữ)
            r'^\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1 Text
            r'^\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1 Text  
            r'^\d+\.\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1.1 Text
        ]
        
        # ENHANCED: Strong exclusion patterns
        self.exclude_patterns = [
            r'^.*(hình|figure|bảng|table|biểu đồ|chart|trang|page).*\d',
            r'^.*\d+\s*[-–]\s*\d+.*',  # Number ranges like "1-2"
            r'^\d+$',  # Chỉ có số đơn thuần
            r'^.*[\.:]\d+$',  # Kết thúc bằng .số hoặc :số
        ]

    def compute_document_stats(self, lines: List[TextLine]) -> Dict:
        """Compute document-level statistics"""
        if not lines:
            self.doc_stats = {
                'median_font': 12.0, 'mean_font': 12.0, 'std_font': 1.0,
                'dominant_font': 'unknown', 'median_gap': 10.0, 
                'mean_gap': 10.0, 'std_gap': 5.0
            }
            return self.doc_stats

        font_sizes = [line.font_size for line in lines]
        font_names = [line.font_name for line in lines]

        # Compute gaps
        lines_sorted = sorted(lines, key=lambda l: (l.page, l.y0))
        gaps = []
        for i in range(1, len(lines_sorted)):
            if lines_sorted[i].page == lines_sorted[i-1].page:
                gap = lines_sorted[i].y0 - lines_sorted[i-1].y1
                if gap > 0:
                    gaps.append(gap)

        self.doc_stats = {
            'median_font': float(np.median(font_sizes)),
            'mean_font': float(np.mean(font_sizes)),
            'std_font': float(np.std(font_sizes)) if len(font_sizes) > 1 else 1.0,
            'dominant_font': max(set(font_names), key=font_names.count) if font_names else 'unknown',
            'median_gap': float(np.median(gaps)) if gaps else 10.0,
            'mean_gap': float(np.mean(gaps)) if gaps else 10.0,
            'std_gap': float(np.std(gaps)) if gaps else 5.0,
        }

        return self.doc_stats

    def is_likely_numbered_heading(self, text: str) -> bool:
        """ENHANCED: Strict detection of numbered headings while avoiding false positives"""
        text_clean = text.strip()
        
        # Check exclusion patterns first (tables, figures, etc.)
        for exclude_pattern in self.exclude_patterns:
            if re.match(exclude_pattern, text_clean, re.IGNORECASE):
                return False
        
        # Check inclusion patterns (must be at start and followed by text)
        for pattern in self.numbered_patterns:
            if re.match(pattern, text_clean):
                # EXTRA VALIDATION: text after numbers should be meaningful
                text_after_numbers = re.sub(r'^\d+(\.\d+)*\s*', '', text_clean).strip()
                if (len(text_after_numbers) >= 3 and 
                    any(c.isalpha() for c in text_after_numbers) and
                    not text_after_numbers.lower().startswith(('hình', 'bảng', 'biểu đồ', 'table', 'figure', 'chart'))):
                    return True
                    
        return False

    def extract_features(self, line: TextLine, prev_line: TextLine = None, 
                        next_line: TextLine = None) -> np.ndarray:
        """Extract 22 features from a text line with improved numbered pattern detection"""

        if self.doc_stats is None:
            raise ValueError("Call compute_document_stats first!")

        features = []
        text = line.text

        # === FONT FEATURES (5) ===
        features.append(line.font_size)  # f1: absolute font size

        font_ratio = line.font_size / self.doc_stats['median_font'] if self.doc_stats['median_font'] > 0 else 1.0
        features.append(font_ratio)  # f2: relative to median

        z_score = (line.font_size - self.doc_stats['mean_font']) / self.doc_stats['std_font'] if self.doc_stats['std_font'] > 0 else 0
        features.append(z_score)  # f3: standardized

        features.append(1.0 if line.is_bold else 0.0)  # f4: is bold

        font_differs = 1.0 if line.font_name != self.doc_stats['dominant_font'] else 0.0
        features.append(font_differs)  # f5: font differs from dominant

        # === POSITION FEATURES (6) ===
        relative_y = line.y0 / line.page_height if line.page_height > 0 else 0.5
        features.append(relative_y)  # f6: relative y position (0=top, 1=bottom)

        relative_x = line.x0 / line.page_width if line.page_width > 0 else 0.0
        features.append(relative_x)  # f7: relative x position

        features.append(line.x0)  # f8: distance from left margin (pixels)

        # Gap before
        gap_before = 0.0
        if prev_line and prev_line.page == line.page:
            gap_before = line.y0 - prev_line.y1
        features.append(gap_before)  # f9: gap before line

        # Gap after
        gap_after = 0.0
        if next_line and next_line.page == line.page:
            gap_after = next_line.y0 - line.y1
        features.append(gap_after)  # f10: gap after line

        is_first = 1.0 if (prev_line is None or prev_line.page != line.page) else 0.0
        features.append(is_first)  # f11: is first line of page

        # === TEXT FEATURES (8) ===
        features.append(len(text))  # f12: text length

        word_count = len(text.split())
        features.append(word_count)  # f13: word count

        # Capital word ratio (first letter)
        capital_words = sum(1 for word in text.split() if word and word[0].isupper())
        capital_ratio = capital_words / word_count if word_count > 0 else 0
        features.append(capital_ratio)  # f14: capital word ratio

        # NEW: Uppercase character ratio in entire text
        alpha_chars = sum(1 for c in text if c.isalpha())
        upper_chars = sum(1 for c in text if c.isupper())
        upper_ratio = upper_chars / alpha_chars if alpha_chars > 0 else 0
        features.append(upper_ratio)  # f15: uppercase character ratio

        punct_count = sum(1 for c in text if c in '.,;:!?')
        features.append(punct_count)  # f16: punctuation count

        # NEW: Period count specifically
        period_count = text.count('.')
        features.append(period_count)  # f17: period count

        ends_period = 1.0 if text.endswith('.') else 0.0
        features.append(ends_period)  # f18: ends with period

        starts_number = 1.0 if text and text[0].isdigit() else 0.0
        features.append(starts_number)  # f19: starts with number

        # === PATTERN FEATURES (3) ===
        # ENHANCED: Use strict numbered pattern detection
        matches_numbered = 1.0 if self.is_likely_numbered_heading(text) else 0.0
        features.append(matches_numbered)  # f20: numbered pattern

        is_all_caps = 1.0 if text.isupper() and len(text) > 3 else 0.0
        features.append(is_all_caps)  # f21: ALL CAPS

        # Removed keywords feature to avoid FP
        features.append(0.0)  # f22: placeholder (removed keywords)

        return np.array(features, dtype=np.float32)


class ModelManager:
    """Manage multiple model versions and save all trained models"""
    
    def __init__(self, models_dir: str = "working/models"):
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
    def save_model_version(self, detector: 'MLHeadingDetector', version_suffix: str = "", 
                         metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None) -> str:
        """Save model with versioning and metadata"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = f"heading_detector_{timestamp}"
        if version_suffix:
            version_name += f"_{version_suffix}"
            
        model_dir = self.models_dir / version_name
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Save main model
        model_path = model_dir / "model.pkl"
        joblib.dump({
            'model': detector.model,
            'feature_names': detector.feature_names,
            'feature_extractor': detector.feature_extractor
        }, model_path)
        
        # Save metadata
        metadata = {
            'version': version_name,
            'saved_at': datetime.now().isoformat(),
            'feature_count': len(detector.feature_names),
            'feature_names': detector.feature_names
        }
        
        if metrics:
            metadata['metrics'] = {k: float(v) if isinstance(v, (np.floating, float)) else v 
                                 for k, v in metrics.items()}
            
        if training_info:
            metadata['training_info'] = training_info
            
        with open(model_dir / "metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
            
        print(f"✓ Model version saved: {version_name}")
        return str(model_dir)
    
    def get_all_models(self) -> List[Dict[str, Any]]:
        """Get information about all saved models"""
        model_dirs = [d for d in self.models_dir.iterdir() if d.is_dir() and d.name.startswith("heading_detector_")]
        models_info = []
        
        for model_dir in model_dirs:
            metadata_file = model_dir / "metadata.json"
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    models_info.append({
                        'name': model_dir.name,
                        'path': str(model_dir),
                        'metadata': metadata
                    })
                except Exception as e:
                    print(f"Error loading metadata for {model_dir}: {e}")
                    
        return sorted(models_info, key=lambda x: x['metadata']['saved_at'], reverse=True)
    
    def load_latest_model(self) -> Optional[Dict]:
        """Load the most recent model"""
        all_models = self.get_all_models()
        if not all_models:
            return None
            
        latest_model = all_models[0]
        try:
            model_path = Path(latest_model['path']) / "model.pkl"
            detector_data = joblib.load(model_path)
            return {
                'detector_data': detector_data,
                'metadata': latest_model['metadata'],
                'path': latest_model['path']
            }
        except Exception as e:
            print(f"Error loading model {latest_model['name']}: {e}")
            return None
    
    def cleanup_old_models(self, keep_count: int = 5):
        """Keep only the most recent models"""
        all_models = self.get_all_models()
        if len(all_models) <= keep_count:
            return
            
        for model_info in all_models[keep_count:]:
            try:
                import shutil
                shutil.rmtree(model_info['path'])
                print(f"✓ Removed old model: {model_info['name']}")
            except Exception as e:
                print(f"✗ Error removing model {model_info['name']}: {e}")


class MLHeadingDetector:
    """ENHANCED ML-based heading detector with LightGBM (Multi-class)"""

    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.data_validator = DataValidator()
        self.data_manager = DataManager()
        self.model_manager = ModelManager()
        self.threshold_optimizer = ThresholdOptimizer()
        self.model = None
        self.feature_names = [
            'font_size', 'font_ratio', 'z_score', 'is_bold', 'font_differs',
            'y_position', 'x_position', 'left_margin', 'gap_before', 'gap_after', 'is_first',
            'text_length', 'word_count', 'capital_ratio', 'upper_ratio', 'punct_count', 
            'period_count', 'ends_period', 'starts_number', 'numbered_pattern', 
            'all_caps', 'placeholder'
        ]
        self.optimal_thresholds = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}  # Default thresholds


    def extract_lines(self, pdf_path: str) -> List[TextLine]:
        """Extract all text lines from PDF"""

        doc = pymupdf.open(pdf_path)
        all_lines = []

        for page_num, page in enumerate(doc, start=1):
            text_dict = page.get_text("dict")
            page_height = page.rect.height
            page_width = page.rect.width

            for block in text_dict["blocks"]:
                if block["type"] != 0:
                    continue

                for line in block.get("lines", []):
                    line_text = ""
                    font_sizes = []
                    font_names = []

                    for span in line.get("spans", []):
                        line_text += span["text"]
                        font_sizes.append(span["size"])
                        font_names.append(span["font"])

                    line_text = line_text.strip()
                    if not line_text:
                        continue

                    all_lines.append(TextLine(
                        text=line_text,
                        font_size=float(np.median(font_sizes)) if font_sizes else 12.0,
                        font_name=max(set(font_names), key=font_names.count) if font_names else 'unknown',
                        is_bold=any('bold' in f.lower() or 'heavy' in f.lower() for f in font_names),
                        x0=line['bbox'][0],
                        y0=line['bbox'][1],
                        x1=line['bbox'][2],
                        y1=line['bbox'][3],
                        page=page_num,
                        page_height=page_height,
                        page_width=page_width
                    ))

        doc.close()
        return all_lines

    def generate_training_data(self, pdf_path: str, gt_md_path: str) -> Tuple[np.ndarray, np.ndarray, List[TextLine]]:
        """FIXED: Generate features and labels - CHỈ gắn nhãn cho các heading markdown từ file GT"""

        # Extract lines
        lines = self.extract_lines(pdf_path)

        if not lines:
            print(f"  No lines extracted from {pdf_path}")
            return np.array([]), np.array([]), []

        # Compute document stats
        self.feature_extractor.compute_document_stats(lines)

        # Parse ground truth headings with levels - CHỈ lấy các heading markdown (#, ##, ###, ####)
        gt_headings = self._parse_markdown_with_levels(gt_md_path)
        
        if not gt_headings:
            print(f"  No markdown headings found in {gt_md_path}")
            return np.array([]), np.array([]), []

        # Extract features and labels
        X = []
        y = []

        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None

            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

            heading_level = self._fuzzy_match_with_level(line.text, gt_headings, threshold=0.8)
            y.append(heading_level)

        return np.array(X), np.array(y), lines

    def _fuzzy_match_with_level(self, text: str, gt_headings: List[Dict], threshold: float = 0.8) -> int:
        """Check if text matches any ground truth heading and return its level"""
        
        text_lower = text.lower().strip()
        best_score = 0
        best_level = 0  # Default: not a heading

        for gt_heading in gt_headings:
            gt_text = gt_heading['text'].lower().strip()
            score = SequenceMatcher(None, text_lower, gt_text).ratio()
            
            if score > best_score and score >= threshold:
                best_score = score
                best_level = gt_heading['level']

        return best_level

    def _parse_markdown_with_levels(self, md_path: str) -> List[Dict]:
        """Parse markdown to extract headings with levels (1-4) - CHỈ lấy markdown headings"""
        
        if not Path(md_path).exists():
            print(f"  Markdown file not found: {md_path}")
            return []

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            headings = []
            for line in content.split('\n'):
                line = line.strip()
                if not line:
                    continue

                # FIXED: CHỈ match markdown headings: # Heading 1, ## Heading 2, etc.
                # Bỏ qua tất cả các dòng không phải heading markdown
                match = re.match(r'^(#{1,4})\s+(.+)$', line)
                if match:
                    level = len(match.group(1))
                    text = match.group(2).strip()
                    headings.append({'text': text, 'level': level})

            print(f"  Extracted {len(headings)} markdown headings from {md_path}")
            return headings
        except Exception as e:
            print(f"  Error parsing markdown {md_path}: {e}")
            return []

    def train(self, X_train: np.ndarray, y_train: np.ndarray, X_val: np.ndarray = None, y_val: np.ndarray = None):
        """ENHANCED: Train LightGBM model with focus on heading recall and threshold optimization"""

        print(f"Training samples: {len(X_train)}")
        
        # Calculate class distribution - FOCUS ON HEADING CLASSES
        unique, counts = np.unique(y_train, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique, counts):
            class_dist[int(cls)] = int(count)
        print("Class distribution:")
        for level, count in class_dist.items():
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train)*100:.2f}%)")

        # Handle class imbalance - less aggressive merging
        y_train_adj = self._adjust_rare_classes_enhanced(y_train)
        
        # Recalculate class distribution after adjustment
        unique_adj, counts_adj = np.unique(y_train_adj, return_counts=True)
        print("\nAdjusted class distribution:")
        for level, count in zip(unique_adj, counts_adj):
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train_adj)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train_adj)*100:.2f}%)")

        # ENHANCED: Compute class weights with manual boost for headings
        class_weights = compute_class_weight(
            class_weight='balanced',
            classes=np.unique(y_train_adj),
            y=y_train_adj
        )
        
        # MANUAL BOOST: Increase weight for heading classes (1-4)
        class_weight_dict = {}
        for i, cls in enumerate(np.unique(y_train_adj)):
            base_weight = float(class_weights[i])
            if cls > 0:  # Heading classes
                boosted_weight = base_weight * 3.0  # Triple the importance
                class_weight_dict[int(cls)] = boosted_weight
            else:
                class_weight_dict[int(cls)] = base_weight
                
        print(f"Enhanced Class weights: {class_weight_dict}")

        # ENHANCED: LightGBM with focus on recall
        self.model = lgb.LGBMClassifier(
            n_estimators=300,
            max_depth=10,
            learning_rate=0.05,
            num_leaves=31,
            min_child_samples=10,
            subsample=0.7,
            colsample_bytree=0.7,
            reg_alpha=0.1,
            reg_lambda=0.1,
            class_weight=class_weight_dict,
            random_state=42,
            n_jobs=-1,
            verbose=-1,
            boosting_type='gbdt'
        )

        # Train with validation set if provided
        if X_val is not None and y_val is not None:
            self.model.fit(
                X_train, y_train_adj,
                eval_set=[(X_val, y_val)],
                eval_metric='multi_logloss',
            )
        else:
            self.model.fit(X_train, y_train_adj)

        # Optimize thresholds on validation set or training set
        if X_val is not None and y_val is not None:
            print("\nOptimizing thresholds on validation set...")
            y_val_probs = self.model.predict_proba(X_val)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_val, y_val_probs, [1, 2, 3, 4]
            )
        else:
            print("\nOptimizing thresholds on training set...")
            y_train_probs = self.model.predict_proba(X_train)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_train_adj, y_train_probs, [1, 2, 3, 4]
            )

        # Print feature importance
        print("\nTop 15 Important Features:")
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1][:15]

        for i, idx in enumerate(indices):
            print(f"  {i+1}. {self.feature_names[idx]:20s}: {importances[idx]:.4f}")

        return y_train_adj

    def _predict_with_thresholds(self, X: np.ndarray, y_probs: np.ndarray = None) -> np.ndarray:
        """Predict with optimized thresholds for heading classes"""
        if y_probs is None:
            y_probs = self.model.predict_proba(X)
        
        # Get default predictions (highest probability)
        default_preds = np.argmax(y_probs, axis=1)
        
        # Apply thresholds for heading classes
        for i in range(len(default_preds)):
            pred_class = default_preds[i]
            if pred_class in self.optimal_thresholds:
                if y_probs[i, pred_class] < self.optimal_thresholds[pred_class]:
                    # If probability below threshold, set to non-heading
                    default_preds[i] = 0
        
        return default_preds
    def _adjust_rare_classes_enhanced(self, y: np.ndarray) -> np.ndarray:
        """ENHANCED: Less aggressive class merging - preserve heading classes"""
        unique, counts = np.unique(y, return_counts=True)
        y_adj = y.copy()
        
        # Only merge extremely rare classes (less than 5 samples) - ONLY FOR HEADINGS
        for level, count in zip(unique, counts):
            if count < 5 and level > 0:  # Only merge rare heading classes
                # Find nearest heading level with sufficient samples
                possible_targets = [l for l in unique if l > 0 and np.sum(y == l) >= 10]
                if possible_targets:
                    target_level = min(possible_targets, key=lambda x: abs(x - level))
                    print(f"  Merging level {level} ({count} samples) into level {target_level}")
                    y_adj[y_adj == level] = target_level
                else:
                    # Fallback: merge into level 1
                    print(f"  Merging level {level} ({count} samples) into level 1")
                    y_adj[y_adj == level] = 1
        
        return y_adj
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Evaluate model performance - FOCUS ON HEADING CLASSES (1-4)"""

        # Adjust test labels same as training
        y_test_adj = self._adjust_rare_classes_enhanced(y_test)
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)

        # FOCUS ON HEADING CLASSES: Filter out class 0 for heading-specific metrics
        heading_indices = y_test_adj > 0
        heading_preds = preds[heading_indices]
        heading_true = y_test_adj[heading_indices]
        
        if len(heading_true) > 0:
            # Heading-specific metrics
            heading_accuracy = accuracy_score(heading_true, heading_preds)
            heading_precision, heading_recall, heading_f1, _ = precision_recall_fscore_support(
                heading_true, heading_preds, average='weighted', zero_division=0
            )
            
            # Per-class metrics for headings only
            heading_classes = sorted(np.unique(heading_true))
            per_class_metrics = precision_recall_fscore_support(
                heading_true, heading_preds, average=None, zero_division=0, labels=heading_classes
            )
            
            # Heading confusion matrix
            heading_cm = confusion_matrix(heading_true, heading_preds, labels=heading_classes)
        else:
            heading_accuracy = heading_precision = heading_recall = heading_f1 = 0.0
            per_class_metrics = ([], [], [], [])
            heading_cm = np.array([])
            heading_classes = []

        # Overall metrics (including non-headings) for reference
        overall_accuracy = accuracy_score(y_test_adj, preds)

        print("\n" + "="*70)
        print("EVALUATION RESULTS - FOCUS ON HEADING CLASSES (1-4)")
        print("="*70)
        print(f"Overall Accuracy (all classes): {overall_accuracy:.4f}")
        print(f"Heading-only Accuracy:          {heading_accuracy:.4f}")
        print(f"Heading-only Precision:         {heading_precision:.4f}")
        print(f"Heading-only Recall:            {heading_recall:.4f}")
        print(f"Heading-only F1 Score:          {heading_f1:.4f}")
        
        if heading_classes:
            print(f"\nPer-class Metrics (Headings only):")
            for i, cls in enumerate(heading_classes):
                print(f"  Level {cls}: Precision={per_class_metrics[0][i]:.4f}, "
                      f"Recall={per_class_metrics[1][i]:.4f}, F1={per_class_metrics[2][i]:.4f}")

            print(f"\nConfusion Matrix (Headings only):")
            print(heading_cm)

        # Show some misclassified heading examples
        heading_misclassified = np.where((heading_true != heading_preds) & (heading_true > 0))[0]
        if len(heading_misclassified) > 0 and len(heading_misclassified) <= 10:
            print(f"\nSample heading misclassifications ({len(heading_misclassified)} total):")
            for idx in heading_misclassified[:5]:
                print(f"  True: {heading_true[idx]}, Predicted: {heading_preds[idx]}")

        return {
            'overall_accuracy': float(overall_accuracy),
            'heading_accuracy': float(heading_accuracy),
            'heading_precision': float(heading_precision),
            'heading_recall': float(heading_recall),
            'heading_f1': float(heading_f1),
            'heading_confusion_matrix': heading_cm.tolist() if len(heading_cm) > 0 else [],
            'heading_classes': [int(cls) for cls in heading_classes],
            'per_class_metrics': [metric.tolist() for metric in per_class_metrics] if heading_classes else []
        }

    def evaluate_heading_detection(self, X_test: np.ndarray, y_test: np.ndarray, lines_test: List[TextLine]) -> Dict:
        """ENHANCED: Heading-specific evaluation metrics with threshold optimization"""
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)
        
        # FOCUS ON HEADING DETECTION (classes 1-4)
        heading_indices_true = y_test > 0
        heading_indices_pred = preds > 0
        
        total_headings = np.sum(heading_indices_true)
        detected_headings = np.sum(heading_indices_pred)
        correct_detections = np.sum(heading_indices_true & heading_indices_pred)
        
        # Calculate detection metrics
        detection_precision = correct_detections / detected_headings if detected_headings > 0 else 0
        detection_recall = correct_detections / total_headings if total_headings > 0 else 0
        detection_f1 = 2 * (detection_precision * detection_recall) / (detection_precision + detection_recall) if (detection_precision + detection_recall) > 0 else 0
        
        # Level-wise accuracy for correctly detected headings
        correctly_detected_indices = heading_indices_true & heading_indices_pred
        if np.any(correctly_detected_indices):
            level_accuracy = accuracy_score(
                y_test[correctly_detected_indices], 
                preds[correctly_detected_indices]
            )
        else:
            level_accuracy = 0.0

        print("\n" + "="*70)
        print("ENHANCED HEADING DETECTION EVALUATION")
        print("="*70)
        print(f"Detection Metrics:")
        print(f"  Precision: {detection_precision:.4f}")
        print(f"  Recall:    {detection_recall:.4f}")
        print(f"  F1-Score:  {detection_f1:.4f}")
        print(f"  Level Accuracy: {level_accuracy:.4f}")
        
        print(f"\nDetection Analysis:")
        print(f"  Total headings in test set: {total_headings}")
        print(f"  Detected as headings: {detected_headings}")
        print(f"  Correctly detected: {correct_detections}")
        print(f"  Heading Detection Rate: {detection_recall*100:.1f}%" if total_headings > 0 else "  Heading Detection Rate: N/A")
        
        # Analyze false negatives
        false_negatives = np.where(heading_indices_true & ~heading_indices_pred)[0]
        if len(false_negatives) > 0:
            print(f"\nFalse Negatives Analysis ({len(false_negatives)} missed headings):")
            for idx in false_negatives[:5]:  # Show first 5
                print(f"  Level {y_test[idx]}: {lines_test[idx].text[:80]}...")
        
        return {
            'detection_precision': float(detection_precision),
            'detection_recall': float(detection_recall),
            'detection_f1': float(detection_f1),
            'level_accuracy': float(level_accuracy),
            'total_headings': int(total_headings),
            'detected_headings': int(detected_headings),
            'correct_detections': int(correct_detections),
            'false_negatives': int(len(false_negatives))
        }
    
    def cross_validate(self, X: np.ndarray, y: np.ndarray, cv_folds: int = 5) -> Dict[str, Any]:
        """Perform cross-validation for more reliable evaluation with small data"""
        print(f"\nPerforming {cv_folds}-fold cross-validation...")
        
        # Adjust labels for consistency
        y_adj = self._adjust_rare_classes_enhanced(y)
        
        # Use stratified k-fold for imbalanced data
        skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
        
        cv_scores = {
            'accuracy': [],
            'precision': [],
            'recall': [],
            'f1': []
        }
        
        fold = 1
        for train_idx, val_idx in skf.split(X, y_adj):
            print(f"  Fold {fold}/{cv_folds}...")
            
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y_adj[train_idx], y_adj[val_idx]
            
            # Train temporary model
            temp_model = lgb.LGBMClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                verbose=-1
            )
            temp_model.fit(X_train, y_train)
            
            # Evaluate
            preds = temp_model.predict(X_val)
            cv_scores['accuracy'].append(float(accuracy_score(y_val, preds)))
            precision, recall, f1, _ = precision_recall_fscore_support(
                y_val, preds, average='weighted', zero_division=0
            )
            cv_scores['precision'].append(float(precision))
            cv_scores['recall'].append(float(recall))
            cv_scores['f1'].append(float(f1))
            
            fold += 1
        
        # Print CV results
        print(f"\nCross-Validation Results ({cv_folds}-fold):")
        for metric, scores in cv_scores.items():
            mean_score = float(np.mean(scores))
            std_score = float(np.std(scores))
            print(f"  {metric.capitalize()}: {mean_score:.4f} ± {std_score:.4f}")
        
        return cv_scores

    def predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback"""
        return self.enhanced_predict(pdf_path)

    def enhanced_predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback and minimum heading guarantee"""

        lines = self.extract_lines(pdf_path)
        if not lines:
            return []

        self.feature_extractor.compute_document_stats(lines)

        # ML Prediction
        X = []
        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None
            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

        X = np.array(X)
        preds = self.model.predict(X)
        probs = self.model.predict_proba(X)

        headings = []
        
        # RULE-BASED ENHANCEMENT: Ensure all numbered headings are detected
        for i, (line, pred, prob) in enumerate(zip(lines, preds, probs)):
            confidence = float(prob[pred])
            
            # RULE 1: If has numbered pattern but model missed it -> FORCE as heading
            if (self.feature_extractor.is_likely_numbered_heading(line.text) and 
                pred == 0 and confidence < 0.8):
                
                # Determine level based on dot count
                dot_count = line.text.strip().split(' ')[0].count('.')
                forced_level = min(4, max(1, dot_count))
                
                headings.append({
                    'text': line.text,
                    'level': forced_level,
                    'page': line.page,
                    'probability': 0.95,  # High confidence for rule-based
                    'font_size': line.font_size,
                    'detection_method': 'rule_based'
                })
                continue
                
            # RULE 2: ML prediction with lower confidence threshold
            if pred > 0 and confidence > 0.3:  # Lower threshold to catch more headings
                headings.append({
                    'text': line.text,
                    'level': int(pred),
                    'page': line.page,
                    'probability': confidence,
                    'font_size': line.font_size,
                    'detection_method': 'ml'
                })

        # RULE 3: Ensure minimum headings per document
        headings = self._ensure_minimum_headings(lines, headings)
        
        # Remove duplicates
        unique_headings = []
        seen_texts = set()
        for heading in headings:
            if heading['text'] not in seen_texts:
                unique_headings.append(heading)
                seen_texts.add(heading['text'])
        
        return unique_headings

    def _ensure_minimum_headings(self, lines: List[TextLine], headings: List[Dict]) -> List[Dict]:
        """ENHANCED: Ensure each document has at least 6 headings"""
        if len(headings) >= 6:  # Already has sufficient headings
            return headings
            
        # Find potential headings that were missed
        potential_headings = []
        
        # for i, line in enumerate(lines):
        #     # Skip if already detected
        #     if any(h['text'] == line.text for h in headings):
        #         continue
                
        #     # Characteristics of actual headings
        #     is_likely_heading = (
        #         self.feature_extractor.is_likely_numbered_heading(line.text) or
        #         (line.font_size > self.feature_extractor.doc_stats['median_font'] * 1.1 and 
        #          len(line.text.split()) <= 15 and  # Headings are usually short
        #          any(c.isupper() for c in line.text) and  # Has uppercase letters
        #          not line.text.endswith('.') and  # Doesn't end with period
        #          not line.text[-1].isdigit())  # Doesn't end with digit
        #     )
            
        #     if is_likely_heading:
        #         dot_count = line.text.strip().split(' ')[0].count('.')
        #         level = min(4, max(1, dot_count + 1))
                
        #         potential_headings.append({
        #             'text': line.text,
        #             'level': level,
        #             'page': line.page,
        #             'probability': 0.7,
        #             'font_size': line.font_size,
        #             'detection_method': 'fallback'
        #         })
        
        # Add potential headings if current count is too low
        if len(headings) < 6 and potential_headings:
            needed = min(6 - len(headings), len(potential_headings))
            headings.extend(potential_headings[:needed])
        
        return headings

    def save_all_models(self, metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None):
        """Save all model versions with metadata"""
        # Save main model
        main_model_path = self.model_manager.save_model_version(
            self, "main", metrics, training_info
        )
        
        # Also save a simplified version for quick loading
        simple_model_path = self.model_manager.save_model_version(
            self, "simple", metrics, training_info
        )
        
        print(f"✓ All model versions saved:")
        print(f"  - Main model: {main_model_path}")
        print(f"  - Simple model: {simple_model_path}")
        
        # Clean up old models (keep only 5 most recent)
        self.model_manager.cleanup_old_models(keep_count=5)
        
        return main_model_path

    def load_latest_model(self):
        """Load the most recent model"""
        model_data = self.model_manager.load_latest_model()
        if model_data is None:
            print("✗ No trained model found")
            return False
            
        try:
            detector_data = model_data['detector_data']
            self.model = detector_data['model']
            self.feature_names = detector_data['feature_names']
            self.feature_extractor = detector_data['feature_extractor']
            print(f"✓ Loaded model: {model_data['metadata']['version']}")
            return True
        except Exception as e:
            print(f"✗ Error loading model: {e}")
            return False


# ============================================================
# ENHANCED TRAINING PIPELINE - LIGHTGBM VERSION
# ============================================================

def train_and_evaluate(
    input_dir: str = r'input',
    gt_dir: str = r'output',
    output_dir: str = 'working/ml_heading_model_lgb',
    train_ratio: float = 0.75,  # Reduced to have more validation data
    val_ratio: float = 0.15,   # Added validation split
    use_cached_data: bool = True,
    enable_cross_validation: bool = True,
    enable_data_validation: bool = True,
    optimize_thresholds: bool = True  # New parameter for threshold optimization
):
    """Enhanced training pipeline with threshold optimization"""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    detector = MLHeadingDetector()
    
    # Check cache first
    cache_key = detector.data_manager.get_cache_key(input_dir, gt_dir)
    X_all, y_all, metadata = None, None, {}
    
    if use_cached_data:
        X_all, y_all, metadata = detector.data_manager.load_training_data(cache_key)
    
    # If no cached data or not using cache, generate new data
    if X_all is None or y_all is None:
        print("Generating new training data...")
        
        # Load dataset with proper path handling
        input_path = Path(input_dir)
        gt_path = Path(gt_dir)

        pdf_files = sorted(input_path.glob('*.pdf'))
        print(f"Found {len(pdf_files)} PDF files")

        # Generate training data with error handling
        print("\nGenerating training data...")
        X_all_parts = []
        y_all_parts = []
        all_lines = []
        processed_count = 0

        for i, pdf_file in enumerate(pdf_files):
            doc_id = pdf_file.stem
            
            # Look for markdown file
            possible_md_locations = [
                gt_path / f"{doc_id}.md",
                gt_path / doc_id / "main.md", 
                gt_path / doc_id / f"{doc_id}.md",
                gt_path / f"{doc_id}" / "main.md"
            ]
            
            gt_md_path = None
            for location in possible_md_locations:
                if location.exists():
                    gt_md_path = location
                    break
            
            if gt_md_path is None:
                print(f"  Skipping {doc_id}: No markdown file found")
                continue

            try:
                X_batch, y_batch, lines_batch = detector.generate_training_data(str(pdf_file), str(gt_md_path))
                
                if len(X_batch) > 0:
                    X_all_parts.append(X_batch)
                    y_all_parts.append(y_batch)
                    all_lines.extend(lines_batch)
                    processed_count += 1
                    print(f"  ✓ Processed {doc_id}: {len(X_batch)} samples")
                else:
                    print(f"  ⚠ No samples from {doc_id}")
                    
            except Exception as e:
                print(f"  ✗ Error with {doc_id}: {e}")
                continue

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(pdf_files)} files")

        # Check if we have any data
        if not X_all_parts:
            print("\n❌ ERROR: No training data generated!")
            return None, None

        # Combine all data
        try:
            X_all = np.vstack(X_all_parts)
            y_all = np.hstack(y_all_parts)
            
            # Save to cache for future use
            metadata = {
                'source_files': len(pdf_files),
                'processed_files': processed_count,
                'generated_at': datetime.now().isoformat()
            }
            detector.data_manager.save_training_data(cache_key, X_all, y_all, metadata)
            print(f"✓ Training data cached with key: {cache_key}")
            
        except ValueError as e:
            print(f"\n❌ ERROR combining data: {e}")
            return None, None

        print(f"\n✅ Successfully processed {processed_count}/{len(pdf_files)} files")
        print(f"Total samples: {len(X_all)}")
    else:
        print("✓ Using cached training data")
        all_lines = []  # Lines not available from cache

    # Show class distribution - FOCUS ON HEADINGS
    unique, counts = np.unique(y_all, return_counts=True)
    print("\nFinal Class Distribution:")
    total_samples = len(y_all)
    for level, count in zip(unique, counts):
        if level == 0:
            print(f"  Level {level} (Not heading): {count} samples ({count/total_samples*100:.2f}%)")
        else:
            print(f"  Level {level}: {count} samples ({count/total_samples*100:.2f}%)")
    
    heading_samples = np.sum(y_all > 0)
    print(f"Total heading samples: {heading_samples}/{total_samples} ({heading_samples/total_samples*100:.2f}%)")

    # Data Validation and Quality Check - FOCUS ON HEADINGS
    if enable_data_validation and len(X_all) > 0:
        print("\n" + "="*70)
        print("DATA QUALITY VALIDATION - HEADING FOCUS")
        print("="*70)
        
        validation_report = detector.data_validator.validate_data_quality(
            X_all, y_all, detector.feature_names
        )
        
        print(f"Overall Quality Score: {validation_report['overall_quality_score']:.2f}/1.00")
        print("\nQuality Flags (Heading Focus):")
        for flag, value in validation_report['quality_flags'].items():
            status = "✓" if value else "✗"
            print(f"  {status} {flag}: {value}")
        
        # Quick validation to ensure data is trainable - FOCUS ON HEADINGS
        is_data_ready = detector.data_validator.validate_data_before_training(X_all, y_all, detector.feature_names)
        if not is_data_ready:
            print("\n❌ Data validation failed - cannot proceed with training")
            return None, None
        
        # Save validation report
        with open(output_path / 'data_validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, indent=2, ensure_ascii=False)

    # Split train/val/test with indices
    indices = np.arange(len(X_all))
    
    # First split: train + temp vs test
    X_train_val, X_test, y_train_val, y_test, indices_train_val, indices_test = train_test_split(
        X_all, y_all, indices, test_size=1-train_ratio-val_ratio, random_state=42, stratify=y_all
    )
    
    # Second split: train vs val
    X_train, X_val, y_train, y_val, indices_train, indices_val = train_test_split(
        X_train_val, y_train_val, indices_train_val, test_size=val_ratio/(train_ratio+val_ratio), 
        random_state=42, stratify=y_train_val
    )

    print(f"\nDataset split:")
    print(f"  Training:   {len(X_train)} samples")
    print(f"  Validation: {len(X_val)} samples (for threshold optimization)")
    print(f"  Testing:    {len(X_test)} samples")

    # Cross-Validation for small datasets
    cv_results = {}
    if enable_cross_validation and len(X_train) > 0:
        cv_results = detector.cross_validate(X_train, y_train, cv_folds=min(5, len(X_train)//10))
        
        # Save CV results
        with open(output_path / 'cross_validation_results.json', 'w', encoding='utf-8') as f:
            json.dump(cv_results, f, indent=2, ensure_ascii=False)

    # Train model with validation set for threshold optimization
    print("\n" + "="*70)
    print("TRAINING LIGHTGBM WITH THRESHOLD OPTIMIZATION")
    print("="*70)

    if optimize_thresholds:
        y_train_adj = detector.train(X_train, y_train, X_val, y_val)
    else:
        y_train_adj = detector.train(X_train, y_train)

    # Evaluate
    print("\n" + "="*70)
    print("EVALUATION ON TEST SET - HEADING FOCUS")
    print("="*70)

    # Standard evaluation - FOCUS ON HEADINGS
    metrics = detector.evaluate(X_test, y_test)
    
    # ENHANCED: Heading-specific evaluation
    if len(X_test) > 0 and all_lines:  # Only if we have lines data
        # Get test lines for enhanced evaluation using precomputed indices_test
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            heading_metrics = detector.evaluate_heading_detection(X_test, y_test, test_lines)
            metrics['heading_detection'] = heading_metrics

    # POST-TRAINING CROSS-VERIFICATION (only after model is trained)
    if enable_data_validation and len(X_test) > 0 and all_lines:
        print("\n" + "="*70)
        print("POST-TRAINING CROSS-VERIFICATION - HEADING FOCUS")
        print("="*70)
        
        # Use the precomputed indices_test to get test lines
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            verification_results = detector.data_validator.cross_verify_predictions(
                detector, X_test, y_test, test_lines
            )
            
            print(f"High confidence heading samples: {len(verification_results.get('high_confidence_samples', []))}")
            print(f"Low confidence heading samples: {len(verification_results.get('low_confidence_samples', []))}")
            print(f"Potential heading misclassifications: {len(verification_results.get('potential_misclassifications', []))}")
            
            # Save verification results
            with open(output_path / 'cross_verification_report.json', 'w', encoding='utf-8') as f:
                json.dump(verification_results, f, indent=2, ensure_ascii=False)
        else:
            print("  ⚠ No test lines available for cross-verification")

    # Save all model versions and training info
    training_info = {
        'training_date': datetime.now().isoformat(),
        'dataset_info': {
            'total_samples': len(X_all),
            'training_samples': len(X_train),
            'validation_samples': len(X_val),
            'test_samples': len(X_test),
            'class_distribution': {str(k): int(v) for k, v in zip(unique, counts)},
            'optimal_thresholds': detector.optimal_thresholds
        },
        'model_metrics': metrics,
        'cross_validation_results': cv_results,
        'cache_key': cache_key,
        'data_validation': {
            'overall_quality_score': validation_report.get('overall_quality_score', 0) if enable_data_validation else 'not_performed'
        }
    }
    
    # Save all model versions
    main_model_path = detector.save_all_models(metrics, training_info)

    # Save training info separately
    with open(output_path / 'training_info.json', 'w', encoding='utf-8') as f:
        json.dump(training_info, f, indent=2, ensure_ascii=False)

    # Save metrics as CSV - FOCUS ON HEADING METRICS
    metrics_df = pd.DataFrame([{
        'overall_accuracy': metrics['overall_accuracy'],
        'heading_accuracy': metrics['heading_accuracy'],
        'heading_precision': metrics['heading_precision'],
        'heading_recall': metrics['heading_recall'],
        'heading_f1': metrics['heading_f1']
    }])
    metrics_df.to_csv(output_path / 'metrics_lgb.csv', index=False)

    # Print optimal thresholds
    print(f"\nOptimal Thresholds for Heading Classes:")
    for level, threshold in detector.optimal_thresholds.items():
        print(f"  Level {level}: {threshold:.3f}")

    print("\n✅ Enhanced Training with Threshold Optimization complete!")

    return detector, metrics


if __name__ == "__main__":
    try:
        # Enhanced training with threshold optimization
        detector, metrics = train_and_evaluate(
            use_cached_data=True,
            enable_cross_validation=True,
            enable_data_validation=True,
            optimize_thresholds=True  # Enable threshold optimization
        )
        if detector is None:
            print("\nTraining failed - no data processed")
    except Exception as e:
        print(f"❌ Training failed: {e}")
        import traceback
        traceback.print_exc()

# ============================================================
# zip.py
# ============================================================

import os
import sys
import zipfile
from pathlib import Path

def merge_python_files():
    """Merge all Python files from src/ (recursively) into main.py"""
    SRC_DIR = Path("src")

    if not SRC_DIR.exists():
        print("✗ src/ directory not found")
        return False

    print("\n--- Merging Python source files ---")

    python_files = sorted([
        f for f in SRC_DIR.rglob("*.py")
        if f.is_file() and "__pycache__" not in f.parts
    ])

    if not python_files:
        print("✗ No Python files found in src/")
        return False

    main_py_content = [
        '"""',
        "RAG-based QA System - Merged Source Code",
        "Generated automatically from multiple modules in src/",
        '"""',
        "",
    ]

    for file_path in python_files:
        rel_path = file_path.relative_to(SRC_DIR)
        print(f"  ✓ Adding {rel_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        main_py_content.append(f"# {'='*60}")
        main_py_content.append(f"# {rel_path.as_posix()}")
        main_py_content.append(f"# {'='*60}")
        main_py_content.append("")
        main_py_content.append(content)
        main_py_content.append("")

    output_path = Path("main.py")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(main_py_content))

    print(f"\n✓ Created main.py ({output_path.stat().st_size / 1024:.2f} KB)")
    return True


def package_submission():
    WORKING_DIR = Path.cwd()
    OUTPUT_DIR = Path(os.getenv('OUTPUT_DIR', 'working/output_mineru_test'))
    ANSWER_FILE = Path("working/answer.md")

    if not OUTPUT_DIR.exists():
        print(f"✗ Output directory not found: {OUTPUT_DIR}")
        print("  Run Task 1 and Task 2 first!")
        return False

    print("\n" + "="*50)
    print("PACKAGING SUBMISSION")
    print("="*50)

    output_zip = WORKING_DIR / 'submission_output.zip'

    print(f"\nPacking files from: {OUTPUT_DIR}")
    print(f"Creating ZIP: {output_zip}")

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        file_count = 0
        skipped_count = 0

        for file_path in OUTPUT_DIR.rglob('*'):
            if file_path.is_file():
                if file_path.suffix == '.pkl':
                    skipped_count += 1
                    continue
                if '__pycache__' in file_path.parts:
                    continue
                arcname = file_path.relative_to(OUTPUT_DIR)
                zipf.write(file_path, arcname)
                file_count += 1

        # ====================================================
        # FIX: place answer.md directly in root of ZIP
        # ====================================================
        if ANSWER_FILE.exists():
            zipf.write(ANSWER_FILE, "answer.md")  # <-- FIXED
            file_count += 1
            print(f"  ✓ Added answer.md to ZIP root")
        else:
            print("  ⚠ Missing working/answer.md — please ensure it exists before submission!")

        # Add merged main.py
        main_py = Path("main.py")
        if main_py.exists():
            zipf.write(main_py, "main.py")
            file_count += 1
            print(f"  ✓ Added main.py")

        print(f"\n  Added: {file_count} files")
        print(f"  Skipped: {skipped_count} .pkl files")

    print(f"\n✓ Created: {output_zip}")
    print(f"  Size: {output_zip.stat().st_size / 1024 / 1024:.2f} MB")

    # Validation
    print("\n--- Validation ---")
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        files = zipf.namelist()

        has_main = 'main.py' in files
        has_answer = 'answer.md' in files  # MUST be root
        has_pkl = any(f.endswith('.pkl') for f in files)

        print(f"{'✓' if has_main else '✗'} main.py")
        print(f"{'✓' if has_answer else '✗'} answer.md (root)")
        print(f"{'✓' if not has_pkl else '✗'} No .pkl files (correct)")

    return True


def main():
    print("="*50)
    print("SUBMISSION PACKAGING TOOL")
    print("="*50)

    if not merge_python_files():
        sys.exit(1)

    if not package_submission():
        sys.exit(1)


if __name__ == "__main__":
    main()

