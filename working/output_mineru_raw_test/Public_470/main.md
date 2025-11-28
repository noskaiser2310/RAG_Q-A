# 1. Cấu trúc dữ liệu đặc tả dùng cho lưu trữ dữ liệu

Dữ liệu đặc tả dùng cho lưu trữ dữ liệu liên quan đến:

thông tinh hành chính về quá trình số hóa 3D: ngày tháng, thời gian, địa điểm, vật thể, chủng loại, cơ quan quét 3D,… các dữ liệu bao gồm các tài liệu tạo ra từ các phần mềm quét 3D, phần mềm mô hỉnh, xử lý thông tin, phân tích, xử lý đám mây điểm và hình ảnh 3D. Dữ liệu cũng có thể là tập hợp các trường dữ liệu trong một hệ thống cơ sở dữ liệu;   
tập hợp các dữ liệu bao gồm tập hợp các tệp tin (vật lý hoặc ảo), chuỗi các dữ liệu lưu trữ và hệ thống lưu trữ dữ liệu.

Các thuộc tính của dữ liệu đặc tả dùng cho lưu trữ dữ liệu với dữ liệu 3D dữ liệu được thể hiện trong bảng 1 dưới đây:

<table><tr><td colspan="1" rowspan="1">Thu@c tinh</td><td colspan="1" rowspan="1">Dói chiéu TCVN 7980:2008</td><td colspan="1" rowspan="1">Dói chiéu AGRMS</td></tr><tr><td colspan="1" rowspan="1">1. Phan loai bé mat</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Face Category</td></tr><tr><td colspan="1" rowspan="1">2. Phan loai vat thé</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Category</td></tr><tr><td colspan="1" rowspan="1">3. Dinh danh</td><td colspan="1" rowspan="1">Dinh danh (bó sung thémthu@c tinh con chuoi dinhdanh, gia tri dinh danh)</td><td colspan="1" rowspan="1">Identifier</td></tr><tr><td colspan="1" rowspan="1">4. Tieu dé</td><td colspan="1" rowspan="1">Tiéu dé (tuong thich toan|Namebo）</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">5. Tac gia</td><td colspan="1" rowspan="1">Tac gia (tuong thich toanbo）</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6. Chu dé</td><td colspan="1" rowspan="1">Chu dé (tuong thich toan|Keywordbo）</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">7. Mo ta</td><td colspan="1" rowspan="1">Mo ta (turong thich toan bo) </td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">8. Ngay</td><td colspan="1" rowspan="1">Ngay thäng (bó sung thémthu@c tinh con ngay bätdau, ngay két thuc)</td><td colspan="1" rowspan="1">Date Range</td></tr><tr><td colspan="1" rowspan="1">9. Loai bao mat</td><td colspan="2" rowspan="1">Security Classification</td></tr><tr><td colspan="1" rowspan="1">10. Quyen</td><td colspan="1" rowspan="1">Quyén (bo sung themRightsthu@c tinh con kiéu quyén,trang thai quyén)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">11. Ngon ngu</td><td colspan="1" rowspan="1">Ngon ngur (tuong thich|Languagetoan bo)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">12. Pham vi</td><td colspan="1" rowspan="1">Pham vi (bó sung thém|Coveragethu@c tinh con pham vithäm quyén, pham vi thoi gian, pham vi khong gian)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">13.Loai bó</td><td colspan="2" rowspan="1">Disposal</td></tr><tr><td colspan="1" rowspan="1">14. Dinh dang</td><td colspan="1" rowspan="1">Dinh dang (b sung thémthu@c tinh con tén dinhdang, phien ban dinh dang,tén üng dung, phién bänung dung)</td><td colspan="1" rowspan="1">Format</td></tr><tr><td colspan="1" rowspan="1">15.Do 16n</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Extent</td></tr><tr><td colspan="1" rowspan="1">16. Phuong tién lurutru</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"> Medium</td></tr><tr><td colspan="1" rowspan="1">17. Vi tri</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Location</td></tr><tr><td colspan="1" rowspan="1">18. Kieu</td><td colspan="1" rowspan="1">Kiéu (tuong thich toan bó)</td><td colspan="1" rowspan="1">Document Form</td></tr><tr><td colspan="1" rowspan="1">19. Loai may quét3D</td><td colspan="2" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">20.Chat lieu d6ituong</td><td colspan="2" rowspan="1"></td></tr></table>

![](images/b3d125e03c0e1dd3f26e5dc6cf7c0dc3e008fcb4c4183f1df684d84e4173b27d.jpg)

2. Xác định dữ liệu đặc tả

Dữ liệu đặc tả được sử dụng $\tt d \hat { e } \ m \hat { o }$ tả các đối tượng, các thông tin cần thiết để lưu trữ.

Tất cả hình ảnh được số hóa 3D nên được chỉ định dữ liệu đặc tả cho quá trình số hóa tài liệu và hỗ trợ các quy trình nghiệp vụ đang diễn ra. Các tổ chức, cơ quan có thể đưa ra các yêu cầu cụ thể và để tối đa hóa sự kế thừa các giá trị dữ liệu từ các hệ thống và thiết bị hiện có. Quy trình quản lý dữ liệu đặc tả nên tối đa hóa tự động chụp dữ liệu đặc tả, giảm thiểu việc xử lý thủ công. Bất kỳ việc sử dụng, áp dụng dữ liệu đặc tả nên được thực hiện có sự tham khảo tiêu chuẩn ISO 23081-1: 2006.

Dữ liệu đặc tả kết hợp với hình ảnh là một thành phần thiết yếu trong việc quản lý và truy vấn các hình ảnh.

Hai loại dữ liệu đặc tả nên được bắt:

dữ liệu đặc tả cụ thể cho các vật thể 3D, hình ảnh quét cụ thể và quá trình xử lý ảnh; dữ liệu đặc tả về dữ liệu 3D công việc đang được giao dịch và đại lý liên quan đến nghiệp vụ. Phần lớn các dữ liệu đặc tả này có thể được tự động sinh ra bởi các phần mềm phân tích đám mây điểm, xử lý mô hình 3D và các phần cứng như máy quét 3D được sử dụng để quản lý quá trình số hóa. Cần được giảm thiểu càng nhiều càng tốt việc xử lý thủ công.

Dữ liệu đặc tả có thể được nhúng với các nguồn tài nguyên tại thông tin tiêu đề, hoặc có thể được quản lý trong một hệ thống riêng biệt, hoặc cả hai, nhưng trong cả hai trường hợp đó phải có một mối quan hệ trực tiếp hoặc liên hệ giữa chúng; tức là khi dữ liệu đặc tả nằm trong một hệ thống riêng biệt, nó có liên kết trực tiếp đến các dữ liệu 3D. Dữ liệu đặc tả cũng có thể được đóng gói trong các định dạng hình ảnh 3D.

# 3. Tạo lập dữ liệu đặc tả

Quá trình số hóa bao gồm bảy giai đoạn mà dữ liệu đặc tả phải được áp dụng. Các giai đoạn này là:

- lên kế hoạch; chuẩn bị quét đối tượng 3D; xử lý dữ liệu 3D; dung sai số hóa dữ liệu 3D; lập chỉ mục và dữ liệu đặc tả; quản lý, lưu trữ dữ liệu.

Có hai loại thông tin đánh chỉ số: Thông tin tiểu sử và thông tin thư mục. Thông tin tiểu sử giao dịch với vòng đời của các tập tin dữ liệu 3D, các hình ảnh 3D và liên quan đến bối cảnh của các thuộc tính dữ liệu 3D và tập tin đó phải được giữ lại, đăng nhập và xác nhận trong quá trình số hóa 3D.

Các định nghĩa về nghĩa vụ trong đánh chỉ số bao gồm:

bắt buộc – thuộc tính phải có; bắt buộc nếu có - thuộc tính phải được cung cấp, nếu phù hợp với bối cảnh công việc và / hoặc các nguồn lực (đối tượng nghiệp vụ); đề nghị - nên được sử dụng nếu phù hợp với bối cảnh kinh doanh và / hoặc các nguồn lực (đối tượng kinh doanh) ;   
tùy chọn – tùy thuộc vào yêu cầu mà có lựa chọn cụ thể.

# 4. Dữ liệu đặc tả về quy luật nghiệp vụ, chính sách và ủy nhiệm tại thời điểm quét 3D

Các thông tin liên quan đến số hóa nghiệp vụ, chính sách và ủy nhiệm được mô tả trong bảng 2.

Bảng 2 – Đánh chỉ số tiểu sử   

<table><tr><td colspan="1" rowspan="1">Nghiavu</td><td colspan="1" rowspan="1">Qua trinh sóhóa 3D</td><td colspan="1" rowspan="1">Cac thu@c tinh danh chi só só hóa 3D</td></tr><tr><td colspan="1" rowspan="3">Bat buoc</td><td colspan="1" rowspan="1">3D</td><td colspan="1" rowspan="1">Quét du liéu|- Dói trong, du lieu 3D lien quan;- Ngay va thoi gian só hóa 3D (Luu y: thoi giandugc khuyén khich, nhung khong bät bu@c);- Só luong vat thé́ dugc só hóa;- Nguoi vän hanh may quét 3D va ten, nhan hiéu,quoc gia san xuat may quét 3D;- Thóng tin tham khao chéo vé du liéu 3D.</td></tr><tr><td colspan="1" rowspan="1">Quét lai (néuqua trinh nayla can thiet)</td><td colspan="1" rowspan="1"> - Dói tuong, dur lieu 3D lien quan; - Ngay va thoi gian só hóa 3D (Luu y: thoi gianduoc khuyén khich, nhung khong bät bu@c);- Só luong vat thé dugc só h6a;- Nguoi van hanh may quét 3D va ten, nhan hiéu,quoc gia san xuat may quet 3D;- Thong tin tham khao chéo vé du lieu 3D.</td></tr><tr><td colspan="1" rowspan="1">luong</td><td colspan="1" rowspan="1">Dam bao chat|- Tai liéu tham khao hang loat (bät bu@c cho hang(khi|loat dau vao);</td></tr><tr><td></td><td>hoan thanh)</td><td>- Nguoi thuc hien dam bao chat luong; - Ngay phé duyét kiém tra dam bao chat luong.</td></tr><tr><td>Bat buoc neuco3D thé</td><td>Chuyén du liéu</td><td>- Ngay chuyén - Tieu dé chuyén - Chuyén mó ta - Ly do chuyén - Tiép nhan chuyén</td></tr></table>

Một số hoặc tất cả các thông tin này có thể được lấy tự động bởi máy quét và phần mềm số hóa 3D. Trong trường hợp chuyển giao để đảm bảo lưu trữ, điều quan trọng là phải biết ngày chuyển giao để xác định bất kỳ sự chậm trễ nào đó có hợp lý không.Tổ chức cần thực hiện các thủ tục để ngăn chặn bất kỳ hình thức sửa đổi sau khi hình ảnh đã được lấy một cách phù hợp và lập chỉ mục.