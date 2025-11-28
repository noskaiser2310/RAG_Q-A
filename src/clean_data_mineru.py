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
