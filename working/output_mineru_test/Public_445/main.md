# Public_445

<table>
<tbody>
<tr>
<td>Nghiệp vụ</td>
<td>Loại chỉ
tiêu</td>
<td>Hành
động</td>
<td>API/Action</td>
<td>Mô tả chi tiết</td>
<td>Phương</td>
<td>Kết quả</td>
<td>Ghi chú</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>pháp</td>
<td>mong</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đo</td>
<td>muốn</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>trước khi
tải.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/contact/update</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/lead/add</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>ứng
99.99%.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>xác thực
hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/opportunity/delete</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,</td>
<td>Kiểm
thử</td>
<td>Cảnh báo
nếu thiếu
trường</td>
<td>Dữ liệu được
backup hàng ngày,</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/opportunity/delete</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/opportunity/delete</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/opportunity/delete</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/campaign/import</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/contact/update</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu</td>
<td>Kiểm
thử</td>
<td>Thành
công với
thời gian
xử lý <</td>
<td>Dữ liệu được
backup hàng ngày,</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/contact/update</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu</td>
<td>Kiểm
thử</td>
<td>Thành
công với
thời gian
xử lý <</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>chức
năng</td>
<td>1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/opportunity/delete</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/opportunity/delete</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/contact/update</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/lead/add</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>ứng
99.99%.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm</td>
<td>Kiểm
thử</td>
<td>Xuất báo
cáo chi
tiết dưới</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>chức
năng</td>
<td>dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Contact</td>
<td>Kiểm
thử</td>
<td>Cảnh báo
nếu thiếu</td>
<td>Dữ liệu được
backup hàng ngày,</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/contact/update</td>
<td>Import dữ liệu
Lead trong</td>
<td>Kiểm
thử</td>
<td>Cảnh báo
nếu thiếu</td>
<td>Dữ liệu được
backup hàng ngày,</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>ứng
99.99%.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/opportunity/delete</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/campaign/import</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/opportunity/delete</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/lead/add</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/opportunity/delete</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/contact/update</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>xác thực
hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/opportunity/delete</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/opportunity/delete</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/campaign/import</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/campaign/import</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/lead/export</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,</td>
<td>Kiểm
thử</td>
<td>Đồng bộ
dữ liệu
sang</td>
<td>Yêu cầu tích hợp
với hệ thống RPA</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>ứng
99.99%.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/export</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/contact/update</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/contact/update</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/contact/update</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/campaign/import</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/contact/update</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/add</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>rollback
giao dịch.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/add</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm</td>
<td>Kiểm
thử</td>
<td>Không
lỗi, log
đầy đủ
trong</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Cập
nhật</td>
<td>/crm/contact/update</td>
<td>Cập nhật dữ
liệu Contact
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Campaign
trong CRM,
bao gồm</td>
<td>Kiểm
thử</td>
<td>Đồng bộ
dữ liệu
sang
DataLake</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/lead/add</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Cập
nhật</td>
<td>/crm/lead/add</td>
<td>Cập nhật dữ
liệu Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/contact/update</td>
<td>Xóa dữ liệu
Contact trong</td>
<td>Kiểm
thử</td>
<td>Cảnh báo
nếu thiếu</td>
<td>Kết quả được gửi
mail và SMS cho</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>hiệu
năng</td>
<td>trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Import</td>
<td>/crm/opportunity/delete</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/add</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/lead/export</td>
<td>Gắn thẻ dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/campaign/import</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/campaign/import</td>
<td>Xóa dữ liệu
Opportunity
trong CRM,
bao gồm</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake</td>
<td>Kết quả được gửi
mail và SMS cho</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có
xác thực
hai lớp
trước khi
tải.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/contact/update</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Chuyển
đổi</td>
<td>/crm/lead/export</td>
<td>Chuyển đổi dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/add</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm</td>
<td>Kiểm
thử</td>
<td>Đồng bộ
dữ liệu
sang
DataLake</td>
<td>Kết quả được gửi
mail và SMS cho</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>chức
năng</td>
<td>trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Export</td>
<td>/crm/contact/update</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Phải kiểm thử với ≥
10.000 bản ghi để
đảm bảo hiệu năng.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Import</td>
<td>/crm/campaign/import</td>
<td>Import dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong
vòng 5s,
tự động
retry khi
lỗi.</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/lead/export</td>
<td>Export dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Xuất báo
cáo chi
tiết dưới
dạng
CSV, có</td>
<td>Yêu cầu tích hợp
với hệ thống RPA
để tự động hóa quy
trình.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>xác thực
hai lớp
trước khi
tải.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Gắn
thẻ</td>
<td>/crm/contact/update</td>
<td>Gắn thẻ dữ liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Import</td>
<td>/crm/lead/export</td>
<td>Import dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử bảo
mật</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Contact</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Xóa</td>
<td>/crm/opportunity/delete</td>
<td>Xóa dữ liệu
Contact trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Cảnh báo
nếu thiếu
trường
bắt buộc,
hệ thống
rollback
giao dịch.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/opportunity/delete</td>
<td>Thêm mới dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu</td>
<td>Kiểm
thử
hiệu
năng</td>
<td>Đồng bộ
dữ liệu
sang
DataLake
trong</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>&nbsp;</td>
<td>vòng 5s,
tự động
retry khi
lỗi.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Opportunity</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Thêm
mới</td>
<td>/crm/lead/export</td>
<td>Thêm mới dữ
liệu
Opportunity
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang
hệ thống
Billing.</td>
<td>Dữ liệu được
backup hàng ngày,
lưu giữ tối thiểu 30
ngày.</td>
</tr>
<tr>
<td>Lead</td>
<td>Chỉ tiêu
hiệu năng</td>
<td>Export</td>
<td>/crm/opportunity/delete</td>
<td>Export dữ liệu
Lead trong
CRM, bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Thành
công với
thời gian
xử lý <
1s, dữ
liệu đồng
bộ sang</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>hệ thống
Billing.</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
bảo mật</td>
<td>Xóa</td>
<td>/crm/lead/add</td>
<td>Xóa dữ liệu
Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Kết quả được gửi
mail và SMS cho
quản trị viên phụ
trách.</td>
</tr>
<tr>
<td>Campaign</td>
<td>Chỉ tiêu
chức
năng</td>
<td>Chuyển
đổi</td>
<td>/crm/opportunity/delete</td>
<td>Chuyển đổi dữ
liệu Campaign
trong CRM,
bao gồm
validate dữ liệu
đầu vào, xử lý
logic nghiệp vụ
và ghi log đầy
đủ.</td>
<td>Kiểm
thử
chức
năng</td>
<td>Không
lỗi, log
đầy đủ
trong
AuditLog,
SLA đáp
ứng
99.99%.</td>
<td>Theo chuẩn ISO
27001 và quy định
bảo mật Viettel.</td>
</tr>
</tbody>
</table>
