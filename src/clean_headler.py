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
