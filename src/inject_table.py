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