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