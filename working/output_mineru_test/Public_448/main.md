# Public_448

<table>
<tbody>
<tr>
<td>API</td>
<td>Phương</td>
<td>Hành</td>
<td>Mô tả chi tiết</td>
<td>Kết quả</td>
<td>Ghi chú</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>thức</td>
<td>động</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /customer/update
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API /ivr/callflow sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức GET
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Thêm
bản</td>
<td>API /ivr/callflow sử
dụng phương thức PUT</td>
<td>Log đầy</td>
<td>Tích hợp
với API</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>ghi</td>
<td>để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>đủ</td>
<td>Gateway</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Thêm bản</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Kiểm
tra
trạng</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>thái</td>
<td>OAuth2 và log giao
dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/customer/update</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PUT</td>
<td>Export</td>
<td>API</td>
<td>Rollback</td>
<td>Tích hợp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>dữ
liệu</td>
<td>/security/firewall/config
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>khi lỗi</td>
<td>với API
Gateway</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API
/security/firewall/config
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Xóa
thông</td>
<td>API /invoice/export sử
dụng phương thức GET</td>
<td>Rollback</td>
<td>Giới hạn
rate-limit</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>tin</td>
<td>để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>khi lỗi</td>
<td>1000
req/min</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Cập
nhật
cấu</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>hình</td>
<td>OAuth2 và log giao
dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API
/security/firewall/config
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /customer/update
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/customer/update</td>
<td>DELETE</td>
<td>Xóa
thông</td>
<td>API /customer/update
sử dụng phương thức
DELETE để Xóa thông</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>tin</td>
<td>tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>req/min</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức GET
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Cập
nhật
cấu</td>
<td>API
/network/qos/monitor
sử dụng phương thức</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>hình</td>
<td>GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Gateway</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /customer/update
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức GET
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /customer/update
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/customer/update</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /customer/update
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức GET
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Thêm</td>
<td>API /crm/lead/import</td>
<td>Thông</td>
<td>Theo</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>bản
ghi</td>
<td>sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>báo sự
kiện qua
Kafka</td>
<td>chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Cập
nhật</td>
<td>API /crm/lead/import
sử dụng phương thức</td>
<td>Rollback</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>cấu
hình</td>
<td>PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>khi lỗi</td>
<td>RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Kiểm
tra
trạng</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Kiểm tra</td>
<td>Thành
công</td>
<td>Giới hạn
rate-limit
1000</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>thái</td>
<td>trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td><1s</td>
<td>req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/security/firewall/config
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Cập
nhật
cấu</td>
<td>API
/network/qos/monitor
sử dụng phương thức</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>hình</td>
<td>GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>&nbsp;</td>
<td>Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Xóa
thông</td>
<td>API
/security/firewall/config</td>
<td>Retry tối</td>
<td>Hỗ trợ
JSON và</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>tin</td>
<td>sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>đa 3 lần</td>
<td>XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Xóa
thông</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Xóa thông tin,</td>
<td>Thành
công</td>
<td>Tích hợp
với API</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>tin</td>
<td>có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td><1s</td>
<td>Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API /ivr/callflow sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Xóa thông tin, có
xác thực OAuth2 và log</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Kiểm
tra
trạng</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Kiểm tra trạng thái,</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>thái</td>
<td>có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức GET
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/customer/update</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API
/security/firewall/config
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Xóa
thông</td>
<td>API /crm/lead/import
sử dụng phương thức</td>
<td>Thông
báo sự</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>tin</td>
<td>PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>kiện qua
Kafka</td>
<td>RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/security/firewall/config
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/customer/update</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức GET
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Export</td>
<td>API /ivr/callflow sử</td>
<td>Thông</td>
<td>Hỗ trợ</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dữ
liệu</td>
<td>dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>báo sự
kiện qua
Kafka</td>
<td>JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>POST</td>
<td>Xóa
thông
tin</td>
<td>API /rpa/task/execute
sử dụng phương thức
POST để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/security/firewall/config
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Cập
nhật
cấu</td>
<td>API /invoice/export sử
dụng phương thức
POST để Cập nhật cấu</td>
<td>Thông
báo sự
kiện qua</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>hình</td>
<td>hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Kafka</td>
<td>RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API
/security/firewall/config
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
GET để Export dữ liệu,</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
GET để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức GET
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Xóa
thông</td>
<td>API /invoice/export sử
dụng phương thức PUT</td>
<td>Retry tối</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>tin</td>
<td>để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>đa 3 lần</td>
<td>RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Xóa
thông
tin</td>
<td>API
/network/qos/monitor
sử dụng phương thức
GET để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Export</td>
<td>API /ivr/callflow sử</td>
<td>Retry tối</td>
<td>Theo</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dữ
liệu</td>
<td>dụng phương thức PUT
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>đa 3 lần</td>
<td>chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Xóa thông tin,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>GET</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức GET
để Export dữ liệu, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PATCH</td>
<td>Xóa
thông
tin</td>
<td>API
/security/firewall/config
sử dụng phương thức
PATCH để Xóa thông
tin, có xác thực OAuth2</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>và log giao dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /customer/update
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /customer/update
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Xóa thông tin, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>GET</td>
<td>Export</td>
<td>API</td>
<td>Retry tối</td>
<td>Tích hợp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dữ
liệu</td>
<td>/network/qos/monitor
sử dụng phương thức
GET để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>đa 3 lần</td>
<td>với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /ivr/callflow sử
dụng phương thức GET
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API /invoice/export sử
dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /crm/lead/import
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức PUT
để Thêm bản ghi, có
xác thực OAuth2 và log
giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>PATCH</td>
<td>Thêm
bản</td>
<td>API /invoice/export sử
dụng phương thức
PATCH để Thêm bản</td>
<td>Thành
công</td>
<td>Có
versioning</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>ghi</td>
<td>ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td><1s</td>
<td>v1/v2</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /rpa/task/execute
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /customer/update
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>PATCH</td>
<td>Thêm
bản
ghi</td>
<td>API /rpa/task/execute
sử dụng phương thức
PATCH để Thêm bản
ghi, có xác thực
OAuth2 và log giao</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>dịch chi tiết.</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/network/qos/monitor
sử dụng phương thức
PUT để Kiểm tra trạng
thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PUT</td>
<td>Thêm
bản
ghi</td>
<td>API /customer/update
sử dụng phương thức
PUT để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/rpa/task/execute</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API /rpa/task/execute
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>PUT</td>
<td>Export
dữ
liệu</td>
<td>API /crm/lead/import
sử dụng phương thức
PUT để Export dữ liệu,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Export
dữ
liệu</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API
/security/firewall/config
sử dụng phương thức
POST để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức PUT
để Cập nhật cấu hình,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /crm/lead/import
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/crm/lead/import</td>
<td>GET</td>
<td>Thêm
bản
ghi</td>
<td>API /crm/lead/import
sử dụng phương thức
GET để Thêm bản ghi,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>PATCH</td>
<td>Export
dữ
liệu</td>
<td>API
/security/firewall/config
sử dụng phương thức
PATCH để Export dữ
liệu, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>PUT</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /ivr/callflow sử
dụng phương thức PUT
để Kiểm tra trạng thái,
có xác thực OAuth2 và
log giao dịch chi tiết.</td>
<td>Rollback
khi lỗi</td>
<td>Hỗ trợ
JSON và
XML</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>DELETE</td>
<td>Kiểm
tra</td>
<td>API
/network/qos/monitor</td>
<td>Rollback</td>
<td>Hỗ trợ
JSON và</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>trạng
thái</td>
<td>sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>khi lỗi</td>
<td>XML</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/network/qos/monitor</td>
<td>POST</td>
<td>Thêm
bản
ghi</td>
<td>API
/network/qos/monitor
sử dụng phương thức
POST để Thêm bản
ghi, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Giới hạn
rate-limit
1000
req/min</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Xóa
thông
tin</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>Thông
báo sự
kiện qua
Kafka</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/invoice/export</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /invoice/export sử
dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Thành
công
<1s</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Xóa
thông</td>
<td>API /customer/update
sử dụng phương thức</td>
<td>Rollback</td>
<td>Tích hợp
với API</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>tin</td>
<td>PATCH để Xóa thông
tin, có xác thực OAuth2
và log giao dịch chi tiết.</td>
<td>khi lỗi</td>
<td>Gateway</td>
</tr>
<tr>
<td>/ivr/callflow</td>
<td>POST</td>
<td>Cập
nhật
cấu
hình</td>
<td>API /ivr/callflow sử
dụng phương thức
POST để Cập nhật cấu
hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>DELETE</td>
<td>Cập
nhật
cấu
hình</td>
<td>API
/security/firewall/config
sử dụng phương thức
DELETE để Cập nhật
cấu hình, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Tích hợp
với API
Gateway</td>
</tr>
<tr>
<td>/customer/update</td>
<td>DELETE</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
DELETE để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Retry tối
đa 3 lần</td>
<td>Có
versioning
v1/v2</td>
</tr>
<tr>
<td>/customer/update</td>
<td>PATCH</td>
<td>Kiểm
tra
trạng
thái</td>
<td>API /customer/update
sử dụng phương thức
PATCH để Kiểm tra
trạng thái, có xác thực
OAuth2 và log giao
dịch chi tiết.</td>
<td>Log đầy
đủ</td>
<td>Theo
chuẩn
RESTful</td>
</tr>
<tr>
<td>/security/firewall/config</td>
<td>POST</td>
<td>Export
dữ</td>
<td>API
/security/firewall/config
sử dụng phương thức</td>
<td>Log đầy
đủ</td>
<td>Tích hợp
với API</td>
</tr>
</tbody>
</table>
