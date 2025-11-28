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