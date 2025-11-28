# Public_444

<table>
<tbody>
<tr>
<td>Tên ứng dụng</td>
<td>Chức năng</td>
<td>API/Action</td>
<td>Mô tả</td>
<td>Kết
quả
mong
muốn</td>
<td>Ghi chú</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>BCCS2-Core</td>
<td>Validate
IVRPrompt</td>
<td>/ivrprompt/validate</td>
<td>Validate dữ liệu
IVRPrompt trong
BCCS2-Core.</td>
<td>Thông
báo
qua
SMS</td>
<td>Có cơ
chế
rollback</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Infra-Server</td>
<td>Config QoS</td>
<td>/qos/config</td>
<td>Config dữ liệu QoS
trong Infra-Server.</td>
<td>Hiển
thị báo
cáo</td>
<td>Có cơ
chế
rollback</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>RPA-Engine</td>
<td>Delete
CustomerProfile</td>
<td>/customerprofile/delete</td>
<td>Delete dữ liệu
CustomerProfile
trong RPA-Engine.</td>
<td>Cảnh
báo</td>
<td>Kết nối
với hệ
thống
Billing</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QA-
Automation</td>
<td>Generate
AgentStatus</td>
<td>/agentstatus/generate</td>
<td>Generate dữ liệu
AgentStatus trong
QA-Automation.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Security-
Firewall</td>
<td>Config
ClusterNode</td>
<td>/clusternode/config</td>
<td>Config dữ liệu
ClusterNode trong
Security-Firewall.</td>
<td>Không
lỗi</td>
<td>Tích
hợp với
CRM</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Security-
Firewall</td>
<td>Update Queue</td>
<td>/queue/update</td>
<td>Update dữ liệu
Queue trong
Security-Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
quy
định
Viettel</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>IPCC-
ContactCenter</td>
<td>Insert
AccountLock</td>
<td>/accountlock/insert</td>
<td>Insert dữ liệu
AccountLock trong</td>
<td>Không
lỗi</td>
<td>Chỉ
dùng</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter.</td>
<td>cho
admin</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Monitor
ClusterNode</td>
<td>/clusternode/monitor</td>
<td>Monitor dữ liệu
ClusterNode trong
IVR-System.</td>
<td>Thông
báo
qua
email</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Import Contact</td>
<td>/contact/import</td>
<td>Import dữ liệu
Contact trong Infra-
Server.</td>
<td>Hiển
thị báo
cáo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Insert Blacklist</td>
<td>/blacklist/insert</td>
<td>Insert dữ liệu
Blacklist trong
IPCC-
ContactCenter.</td>
<td>Thông
báo
qua
SMS</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Import Blacklist</td>
<td>/blacklist/import</td>
<td>Import dữ liệu
Blacklist trong
Security-Firewall.</td>
<td>Tự
động
retry</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Schedule
PackagePlan</td>
<td>/packageplan/schedule</td>
<td>Schedule dữ liệu
PackagePlan trong
QA-Automation.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Analyze
Blacklist</td>
<td>/blacklist/analyze</td>
<td>Analyze dữ liệu
Blacklist trong RPA-
Engine.</td>
<td>Ghi log
đầy đủ</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Analyze VPN</td>
<td>/vpn/analyze</td>
<td>Analyze dữ liệu
VPN trong Infra-
Server.</td>
<td>Không
lỗi</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Analyze
FirewallPolicy</td>
<td>/firewallpolicy/analyze</td>
<td>Analyze dữ liệu
FirewallPolicy trong
Infra-Network.</td>
<td>Thông
báo</td>
<td>Chạy
theo</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>qua
SMS</td>
<td>lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import
Opportunity</td>
<td>/opportunity/import</td>
<td>Import dữ liệu
Opportunity trong
BCCS2-Core.</td>
<td>Tự
động
retry</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Analyze
AgentStatus</td>
<td>/agentstatus/analyze</td>
<td>Analyze dữ liệu
AgentStatus trong
IPCC-
ContactCenter.</td>
<td>Cảnh
báo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Insert
IVRPrompt</td>
<td>/ivrprompt/insert</td>
<td>Insert dữ liệu
IVRPrompt trong
CRM-Platform.</td>
<td>Hiển
thị báo
cáo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import
CDRReport</td>
<td>/cdrreport/import</td>
<td>Import dữ liệu
CDRReport trong
BCCS2-Core.</td>
<td>Cảnh
báo</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Analyze QoS</td>
<td>/qos/analyze</td>
<td>Analyze dữ liệu QoS
trong CRM-
Platform.</td>
<td>Cảnh
báo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Update
Campaign</td>
<td>/campaign/update</td>
<td>Update dữ liệu
Campaign trong
BCCS2-Core.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Export
AccountLock</td>
<td>/accountlock/export</td>
<td>Export dữ liệu
AccountLock trong
Infra-Network.</td>
<td>Hiển
thị báo
cáo</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Analyze
TransactionLog</td>
<td>/transactionlog/analyze</td>
<td>Analyze dữ liệu
TransactionLog
trong CRM-
Platform.</td>
<td>Không
lỗi</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Config
KPIReport</td>
<td>/kpireport/config</td>
<td>Config dữ liệu
KPIReport trong
CRM-Platform.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Optimize
Campaign</td>
<td>/campaign/optimize</td>
<td>Optimize dữ liệu
Campaign trong
RPA-Engine.</td>
<td>Thông
báo
qua
email</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Delete Queue</td>
<td>/queue/delete</td>
<td>Delete dữ liệu Queue
trong IVR-System.</td>
<td>Tự
động
retry</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Delete
AgentStatus</td>
<td>/agentstatus/delete</td>
<td>Delete dữ liệu
AgentStatus trong
RPA-Engine.</td>
<td>Thông
báo
qua
SMS</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Schedule
AgentStatus</td>
<td>/agentstatus/schedule</td>
<td>Schedule dữ liệu
AgentStatus trong
BCCS2-Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Validate
CustomerProfile</td>
<td>/customerprofile/validate</td>
<td>Validate dữ liệu
CustomerProfile
trong CRM-
Platform.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Update VPN</td>
<td>/vpn/update</td>
<td>Update dữ liệu VPN
trong Security-
Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Schedule
Invoice</td>
<td>/invoice/schedule</td>
<td>Schedule dữ liệu
Invoice trong IVR-
System.</td>
<td>Không
lỗi</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Search
Whitelist</td>
<td>/whitelist/search</td>
<td>Search dữ liệu
Whitelist trong
BCCS2-Core.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize
PackagePlan</td>
<td>/packageplan/optimize</td>
<td>Optimize dữ liệu
PackagePlan trong
BCCS2-Core.</td>
<td>Hiển
thị báo
cáo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Optimize VPN</td>
<td>/vpn/optimize</td>
<td>Optimize dữ liệu
VPN trong Infra-
Server.</td>
<td>Thông
báo
qua
email</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Schedule QoS</td>
<td>/qos/schedule</td>
<td>Schedule dữ liệu
QoS trong IVR-
System.</td>
<td>Hiển
thị báo
cáo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Optimize
IVRPrompt</td>
<td>/ivrprompt/optimize</td>
<td>Optimize dữ liệu
IVRPrompt trong
CRM-Platform.</td>
<td>Thông
báo
qua
email</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Optimize
KPIReport</td>
<td>/kpireport/optimize</td>
<td>Optimize dữ liệu
KPIReport trong
IPCC-
ContactCenter.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Schedule
FirewallPolicy</td>
<td>/firewallpolicy/schedule</td>
<td>Schedule dữ liệu
FirewallPolicy trong
Infra-Server.</td>
<td>Tự
động
retry</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Schedule QoS</td>
<td>/qos/schedule</td>
<td>Schedule dữ liệu
QoS trong Security-
Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Optimize
KPIReport</td>
<td>/kpireport/optimize</td>
<td>Optimize dữ liệu
KPIReport trong
RPA-Engine.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Update
KPIReport</td>
<td>/kpireport/update</td>
<td>Update dữ liệu
KPIReport trong
IPCC-
ContactCenter.</td>
<td>Tự
động
retry</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Config
FirewallPolicy</td>
<td>/firewallpolicy/config</td>
<td>Config dữ liệu
FirewallPolicy trong
RPA-Engine.</td>
<td>Thành
công</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Optimize
ClusterNode</td>
<td>/clusternode/optimize</td>
<td>Optimize dữ liệu
ClusterNode trong
Security-Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Schedule
SwitchConfig</td>
<td>/switchconfig/schedule</td>
<td>Schedule dữ liệu
SwitchConfig trong
Infra-Network.</td>
<td>Thông
báo
qua
email</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Analyze
KPIReport</td>
<td>/kpireport/analyze</td>
<td>Analyze dữ liệu
KPIReport trong
RPA-Engine.</td>
<td>Không
lỗi</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Config
IVRPrompt</td>
<td>/ivrprompt/config</td>
<td>Config dữ liệu
IVRPrompt trong
QA-Automation.</td>
<td>Không
lỗi</td>
<td>Kết nối
với hệ</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>thống
Billing</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Monitor Invoice</td>
<td>/invoice/monitor</td>
<td>Monitor dữ liệu
Invoice trong QA-
Automation.</td>
<td>Cảnh
báo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Insert
CustomerProfile</td>
<td>/customerprofile/insert</td>
<td>Insert dữ liệu
CustomerProfile
trong IVR-System.</td>
<td>Hiển
thị báo
cáo</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Optimize QoS</td>
<td>/qos/optimize</td>
<td>Optimize dữ liệu
QoS trong IVR-
System.</td>
<td>Hiển
thị báo
cáo</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Schedule
Invoice</td>
<td>/invoice/schedule</td>
<td>Schedule dữ liệu
Invoice trong
BCCS2-Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Search
DebtControl</td>
<td>/debtcontrol/search</td>
<td>Search dữ liệu
DebtControl trong
BCCS2-Billing.</td>
<td>Cảnh
báo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Optimize Lead</td>
<td>/lead/optimize</td>
<td>Optimize dữ liệu
Lead trong IVR-
System.</td>
<td>Không
lỗi</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Config Lead</td>
<td>/lead/config</td>
<td>Config dữ liệu Lead
trong RPA-Engine.</td>
<td>Cảnh
báo</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Monitor
ClusterNode</td>
<td>/clusternode/monitor</td>
<td>Monitor dữ liệu
ClusterNode trong
Security-Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Update QoS</td>
<td>/qos/update</td>
<td>Update dữ liệu QoS
trong Security-
Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Import Blacklist</td>
<td>/blacklist/import</td>
<td>Import dữ liệu
Blacklist trong RPA-
Engine.</td>
<td>Ghi log
đầy đủ</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Delete
StorageVolume</td>
<td>/storagevolume/delete</td>
<td>Delete dữ liệu
StorageVolume
trong RPA-Engine.</td>
<td>Tự
động
retry</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Generate
Invoice</td>
<td>/invoice/generate</td>
<td>Generate dữ liệu
Invoice trong RPA-
Engine.</td>
<td>Không
lỗi</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Search
CDRReport</td>
<td>/cdrreport/search</td>
<td>Search dữ liệu
CDRReport trong
Infra-Network.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize
DebtControl</td>
<td>/debtcontrol/optimize</td>
<td>Optimize dữ liệu
DebtControl trong
BCCS2-Core.</td>
<td>Thông
báo
qua
email</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Delete
Campaign</td>
<td>/campaign/delete</td>
<td>Delete dữ liệu
Campaign trong
Infra-Network.</td>
<td>Thành
công</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Delete
CustomerProfile</td>
<td>/customerprofile/delete</td>
<td>Delete dữ liệu
CustomerProfile
trong Infra-Network.</td>
<td>Không
lỗi</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Monitor
TransactionLog</td>
<td>/transactionlog/monitor</td>
<td>Monitor dữ liệu
TransactionLog
trong BCCS2-Core.</td>
<td>Hiển
thị báo
cáo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Export Contact</td>
<td>/contact/export</td>
<td>Export dữ liệu
Contact trong QA-
Automation.</td>
<td>Hiển
thị báo
cáo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Delete Contact</td>
<td>/contact/delete</td>
<td>Delete dữ liệu
Contact trong
Security-Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Search
Whitelist</td>
<td>/whitelist/search</td>
<td>Search dữ liệu
Whitelist trong
Security-Firewall.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Import Contact</td>
<td>/contact/import</td>
<td>Import dữ liệu
Contact trong
BCCS2-Billing.</td>
<td>Cảnh
báo</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Insert
APIGateway</td>
<td>/apigateway/insert</td>
<td>Insert dữ liệu
APIGateway trong
Infra-Server.</td>
<td>Không
lỗi</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Optimize
TransactionLog</td>
<td>/transactionlog/optimize</td>
<td>Optimize dữ liệu
TransactionLog
trong QA-
Automation.</td>
<td>Thành
công</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Optimize
Opportunity</td>
<td>/opportunity/optimize</td>
<td>Optimize dữ liệu
Opportunity trong
Infra-Network.</td>
<td>Không
lỗi</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Update
PackagePlan</td>
<td>/packageplan/update</td>
<td>Update dữ liệu
PackagePlan trong
RPA-Engine.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Generate
Invoice</td>
<td>/invoice/generate</td>
<td>Generate dữ liệu
Invoice trong
BCCS2-Core.</td>
<td>Thông
báo
qua
email</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import
SwitchConfig</td>
<td>/switchconfig/import</td>
<td>Import dữ liệu
SwitchConfig trong
BCCS2-Core.</td>
<td>Không
lỗi</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Schedule
Campaign</td>
<td>/campaign/schedule</td>
<td>Schedule dữ liệu
Campaign trong
Security-Firewall.</td>
<td>Tự
động
retry</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Update
Whitelist</td>
<td>/whitelist/update</td>
<td>Update dữ liệu
Whitelist trong
BCCS2-Billing.</td>
<td>Tự
động
retry</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Insert DataLake</td>
<td>/datalake/insert</td>
<td>Insert dữ liệu
DataLake trong QA-
Automation.</td>
<td>Ghi log
đầy đủ</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Import
CDRReport</td>
<td>/cdrreport/import</td>
<td>Import dữ liệu
CDRReport trong
CRM-Platform.</td>
<td>Tự
động
retry</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Config
AgentStatus</td>
<td>/agentstatus/config</td>
<td>Config dữ liệu
AgentStatus trong
QA-Automation.</td>
<td>Hiển
thị báo
cáo</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Search
CDRReport</td>
<td>/cdrreport/search</td>
<td>Search dữ liệu
CDRReport trong
IVR-System.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Validate
SwitchConfig</td>
<td>/switchconfig/validate</td>
<td>Validate dữ liệu
SwitchConfig trong
Infra-Network.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Monitor
ClusterNode</td>
<td>/clusternode/monitor</td>
<td>Monitor dữ liệu
ClusterNode trong
BCCS2-Billing.</td>
<td>Thông
báo
qua
SMS</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Validate
Opportunity</td>
<td>/opportunity/validate</td>
<td>Validate dữ liệu
Opportunity trong
Security-Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Schedule
Whitelist</td>
<td>/whitelist/schedule</td>
<td>Schedule dữ liệu
Whitelist trong
Security-Firewall.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Delete
APIGateway</td>
<td>/apigateway/delete</td>
<td>Delete dữ liệu
APIGateway trong
BCCS2-Billing.</td>
<td>Thành
công</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Search
ClusterNode</td>
<td>/clusternode/search</td>
<td>Search dữ liệu
ClusterNode trong
Infra-Network.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Config Contact</td>
<td>/contact/config</td>
<td>Config dữ liệu
Contact trong
BCCS2-Core.</td>
<td>Thông
báo
qua
email</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Config Contact</td>
<td>/contact/config</td>
<td>Config dữ liệu
Contact trong IPCC-
ContactCenter.</td>
<td>Thành
công</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Config
CDRReport</td>
<td>/cdrreport/config</td>
<td>Config dữ liệu
CDRReport trong
QA-Automation.</td>
<td>Không
lỗi</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Schedule
KPIReport</td>
<td>/kpireport/schedule</td>
<td>Schedule dữ liệu
KPIReport trong
BCCS2-Core.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Delete
IVRPrompt</td>
<td>/ivrprompt/delete</td>
<td>Delete dữ liệu
IVRPrompt trong
Infra-Network.</td>
<td>Tự
động
retry</td>
<td>Dữ liệu
backup</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>mỗi
ngày</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Validate
DebtControl</td>
<td>/debtcontrol/validate</td>
<td>Validate dữ liệu
DebtControl trong
Security-Firewall.</td>
<td>Thành
công</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize Lead</td>
<td>/lead/optimize</td>
<td>Optimize dữ liệu
Lead trong BCCS2-
Core.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Validate
Opportunity</td>
<td>/opportunity/validate</td>
<td>Validate dữ liệu
Opportunity trong
RPA-Engine.</td>
<td>Cảnh
báo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Update
DataLake</td>
<td>/datalake/update</td>
<td>Update dữ liệu
DataLake trong
IVR-System.</td>
<td>Không
lỗi</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Config
CustomerProfile</td>
<td>/customerprofile/config</td>
<td>Config dữ liệu
CustomerProfile
trong Infra-Server.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Validate
StorageVolume</td>
<td>/storagevolume/validate</td>
<td>Validate dữ liệu
StorageVolume
trong BCCS2-
Billing.</td>
<td>Thông
báo
qua
email</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Analyze
APIGateway</td>
<td>/apigateway/analyze</td>
<td>Analyze dữ liệu
APIGateway trong
CRM-Platform.</td>
<td>Tự
động
retry</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Search Contact</td>
<td>/contact/search</td>
<td>Search dữ liệu
Contact trong Infra-
Network.</td>
<td>Hiển
thị báo
cáo</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Monitor QoS</td>
<td>/qos/monitor</td>
<td>Monitor dữ liệu QoS
trong Infra-Network.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Update
KPIReport</td>
<td>/kpireport/update</td>
<td>Update dữ liệu
KPIReport trong
Security-Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Export
StorageVolume</td>
<td>/storagevolume/export</td>
<td>Export dữ liệu
StorageVolume
trong RPA-Engine.</td>
<td>Tự
động
retry</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Config
PackagePlan</td>
<td>/packageplan/config</td>
<td>Config dữ liệu
PackagePlan trong
IVR-System.</td>
<td>Cảnh
báo</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Update
FirewallPolicy</td>
<td>/firewallpolicy/update</td>
<td>Update dữ liệu
FirewallPolicy trong
CRM-Platform.</td>
<td>Thành
công</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Analyze
Blacklist</td>
<td>/blacklist/analyze</td>
<td>Analyze dữ liệu
Blacklist trong QA-
Automation.</td>
<td>Không
lỗi</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Insert
AgentStatus</td>
<td>/agentstatus/insert</td>
<td>Insert dữ liệu
AgentStatus trong
CRM-Platform.</td>
<td>Tự
động
retry</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Config
DataLake</td>
<td>/datalake/config</td>
<td>Config dữ liệu
DataLake trong
BCCS2-Core.</td>
<td>Ghi log
đầy đủ</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Generate
Invoice</td>
<td>/invoice/generate</td>
<td>Generate dữ liệu
Invoice trong IPCC-
ContactCenter.</td>
<td>Thành
công</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Update
DebtControl</td>
<td>/debtcontrol/update</td>
<td>Update dữ liệu
DebtControl trong
BCCS2-Core.</td>
<td>Tự
động
retry</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Optimize
IVRPrompt</td>
<td>/ivrprompt/optimize</td>
<td>Optimize dữ liệu
IVRPrompt trong
BCCS2-Billing.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Update
IVRPrompt</td>
<td>/ivrprompt/update</td>
<td>Update dữ liệu
IVRPrompt trong
BCCS2-Core.</td>
<td>Thành
công</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Validate
CDRReport</td>
<td>/cdrreport/validate</td>
<td>Validate dữ liệu
CDRReport trong
IVR-System.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Insert Blacklist</td>
<td>/blacklist/insert</td>
<td>Insert dữ liệu
Blacklist trong
IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import
PackagePlan</td>
<td>/packageplan/import</td>
<td>Import dữ liệu
PackagePlan trong
BCCS2-Core.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Delete
IVRPrompt</td>
<td>/ivrprompt/delete</td>
<td>Delete dữ liệu
IVRPrompt trong
QA-Automation.</td>
<td>Cảnh
báo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Import
Opportunity</td>
<td>/opportunity/import</td>
<td>Import dữ liệu
Opportunity trong
QA-Automation.</td>
<td>Ghi log
đầy đủ</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Delete
Promotion</td>
<td>/promotion/delete</td>
<td>Delete dữ liệu
Promotion trong
RPA-Engine.</td>
<td>Cảnh
báo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Update
Campaign</td>
<td>/campaign/update</td>
<td>Update dữ liệu
Campaign trong
IVR-System.</td>
<td>Không
lỗi</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Optimize
CDRReport</td>
<td>/cdrreport/optimize</td>
<td>Optimize dữ liệu
CDRReport trong
IPCC-
ContactCenter.</td>
<td>Thông
báo
qua
email</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Monitor VPN</td>
<td>/vpn/monitor</td>
<td>Monitor dữ liệu
VPN trong Infra-
Network.</td>
<td>Thành
công</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Import
IVRPrompt</td>
<td>/ivrprompt/import</td>
<td>Import dữ liệu
IVRPrompt trong
RPA-Engine.</td>
<td>Không
lỗi</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Validate
StorageVolume</td>
<td>/storagevolume/validate</td>
<td>Validate dữ liệu
StorageVolume
trong BCCS2-
Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Delete Invoice</td>
<td>/invoice/delete</td>
<td>Delete dữ liệu
Invoice trong QA-
Automation.</td>
<td>Ghi log
đầy đủ</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Update
PackagePlan</td>
<td>/packageplan/update</td>
<td>Update dữ liệu
PackagePlan trong
BCCS2-Core.</td>
<td>Tự
động
retry</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Search
Campaign</td>
<td>/campaign/search</td>
<td>Search dữ liệu
Campaign trong
CRM-Platform.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Insert VPN</td>
<td>/vpn/insert</td>
<td>Insert dữ liệu VPN
trong BCCS2-
Billing.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Schedule
ClusterNode</td>
<td>/clusternode/schedule</td>
<td>Schedule dữ liệu
ClusterNode trong
IVR-System.</td>
<td>Thông
báo
qua
email</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Optimize
KPIReport</td>
<td>/kpireport/optimize</td>
<td>Optimize dữ liệu
KPIReport trong
Security-Firewall.</td>
<td>Cảnh
báo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Analyze
Promotion</td>
<td>/promotion/analyze</td>
<td>Analyze dữ liệu
Promotion trong
Infra-Server.</td>
<td>Tự
động
retry</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Export
IVRPrompt</td>
<td>/ivrprompt/export</td>
<td>Export dữ liệu
IVRPrompt trong
BCCS2-Billing.</td>
<td>Thành
công</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Insert
DebtControl</td>
<td>/debtcontrol/insert</td>
<td>Insert dữ liệu
DebtControl trong
Security-Firewall.</td>
<td>Không
lỗi</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Schedule
KPIReport</td>
<td>/kpireport/schedule</td>
<td>Schedule dữ liệu
KPIReport trong
QA-Automation.</td>
<td>Tự
động
retry</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Monitor
Whitelist</td>
<td>/whitelist/monitor</td>
<td>Monitor dữ liệu
Whitelist trong
Infra-Server.</td>
<td>Thông
báo
qua
email</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Config
FirewallPolicy</td>
<td>/firewallpolicy/config</td>
<td>Config dữ liệu
FirewallPolicy trong
Infra-Server.</td>
<td>Thông
báo
qua
SMS</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Monitor Lead</td>
<td>/lead/monitor</td>
<td>Monitor dữ liệu
Lead trong Infra-
Network.</td>
<td>Không
lỗi</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Delete
PackagePlan</td>
<td>/packageplan/delete</td>
<td>Delete dữ liệu
PackagePlan trong
IPCC-
ContactCenter.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Generate
AccountLock</td>
<td>/accountlock/generate</td>
<td>Generate dữ liệu
AccountLock trong
BCCS2-Core.</td>
<td>Thông
báo
qua
email</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Config
IVRPrompt</td>
<td>/ivrprompt/config</td>
<td>Config dữ liệu
IVRPrompt trong
IVR-System.</td>
<td>Ghi log
đầy đủ</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Optimize
Opportunity</td>
<td>/opportunity/optimize</td>
<td>Optimize dữ liệu
Opportunity trong
Infra-Network.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Monitor
Contact</td>
<td>/contact/monitor</td>
<td>Monitor dữ liệu
Contact trong Infra-
Network.</td>
<td>Không
lỗi</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Import
Campaign</td>
<td>/campaign/import</td>
<td>Import dữ liệu
Campaign trong
Security-Firewall.</td>
<td>Thành
công</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Schedule
AgentStatus</td>
<td>/agentstatus/schedule</td>
<td>Schedule dữ liệu
AgentStatus trong
Infra-Network.</td>
<td>Hiển
thị báo
cáo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Import
CustomerProfile</td>
<td>/customerprofile/import</td>
<td>Import dữ liệu
CustomerProfile
trong Security-
Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Delete QoS</td>
<td>/qos/delete</td>
<td>Delete dữ liệu QoS
trong IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Validate Lead</td>
<td>/lead/validate</td>
<td>Validate dữ liệu
Lead trong Infra-
Server.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Delete
CustomerProfile</td>
<td>/customerprofile/delete</td>
<td>Delete dữ liệu
CustomerProfile
trong BCCS2-
Billing.</td>
<td>Hiển
thị báo
cáo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Generate
AccountLock</td>
<td>/accountlock/generate</td>
<td>Generate dữ liệu
AccountLock trong
BCCS2-Billing.</td>
<td>Thành
công</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Delete
PackagePlan</td>
<td>/packageplan/delete</td>
<td>Delete dữ liệu
PackagePlan trong
CRM-Platform.</td>
<td>Ghi log
đầy đủ</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Validate
Opportunity</td>
<td>/opportunity/validate</td>
<td>Validate dữ liệu
Opportunity trong
CRM-Platform.</td>
<td>Ghi log
đầy đủ</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Optimize
Promotion</td>
<td>/promotion/optimize</td>
<td>Optimize dữ liệu
Promotion trong
Infra-Network.</td>
<td>Không
lỗi</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Search
DebtControl</td>
<td>/debtcontrol/search</td>
<td>Search dữ liệu
DebtControl trong
IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Generate
AgentStatus</td>
<td>/agentstatus/generate</td>
<td>Generate dữ liệu
AgentStatus trong
RPA-Engine.</td>
<td>Không
lỗi</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Config VPN</td>
<td>/vpn/config</td>
<td>Config dữ liệu VPN
trong Infra-Server.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Update
ClusterNode</td>
<td>/clusternode/update</td>
<td>Update dữ liệu
ClusterNode trong
Security-Firewall.</td>
<td>Không
lỗi</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Config
IVRPrompt</td>
<td>/ivrprompt/config</td>
<td>Config dữ liệu
IVRPrompt trong
RPA-Engine.</td>
<td>Thông
báo
qua
SMS</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Search
DataLake</td>
<td>/datalake/search</td>
<td>Search dữ liệu
DataLake trong
CRM-Platform.</td>
<td>Ghi log
đầy đủ</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Optimize
TransactionLog</td>
<td>/transactionlog/optimize</td>
<td>Optimize dữ liệu
TransactionLog
trong Security-
Firewall.</td>
<td>Thông
báo
qua
email</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Schedule
Invoice</td>
<td>/invoice/schedule</td>
<td>Schedule dữ liệu
Invoice trong IPCC-
ContactCenter.</td>
<td>Thành
công</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Update
TransactionLog</td>
<td>/transactionlog/update</td>
<td>Update dữ liệu
TransactionLog
trong BCCS2-Core.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Delete
TransactionLog</td>
<td>/transactionlog/delete</td>
<td>Delete dữ liệu
TransactionLog
trong BCCS2-Core.</td>
<td>Ghi log
đầy đủ</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Config VPN</td>
<td>/vpn/config</td>
<td>Config dữ liệu VPN
trong IVR-System.</td>
<td>Không
lỗi</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Generate
ClusterNode</td>
<td>/clusternode/generate</td>
<td>Generate dữ liệu
ClusterNode trong
CRM-Platform.</td>
<td>Không
lỗi</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize Lead</td>
<td>/lead/optimize</td>
<td>Optimize dữ liệu
Lead trong BCCS2-
Core.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Update
CustomerProfile</td>
<td>/customerprofile/update</td>
<td>Update dữ liệu
CustomerProfile
trong IVR-System.</td>
<td>Thông
báo
qua
email</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Schedule
AccountLock</td>
<td>/accountlock/schedule</td>
<td>Schedule dữ liệu
AccountLock trong
Infra-Network.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Search
ClusterNode</td>
<td>/clusternode/search</td>
<td>Search dữ liệu
ClusterNode trong
BCCS2-Core.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Monitor
Opportunity</td>
<td>/opportunity/monitor</td>
<td>Monitor dữ liệu
Opportunity trong
BCCS2-Billing.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Import
Campaign</td>
<td>/campaign/import</td>
<td>Import dữ liệu
Campaign trong
RPA-Engine.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Search
SwitchConfig</td>
<td>/switchconfig/search</td>
<td>Search dữ liệu
SwitchConfig trong
QA-Automation.</td>
<td>Tự
động
retry</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Export QoS</td>
<td>/qos/export</td>
<td>Export dữ liệu QoS
trong BCCS2-
Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Update Invoice</td>
<td>/invoice/update</td>
<td>Update dữ liệu
Invoice trong Infra-
Server.</td>
<td>Ghi log
đầy đủ</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Monitor VPN</td>
<td>/vpn/monitor</td>
<td>Monitor dữ liệu
VPN trong BCCS2-
Billing.</td>
<td>Thông
báo
qua
SMS</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Search
SwitchConfig</td>
<td>/switchconfig/search</td>
<td>Search dữ liệu
SwitchConfig trong
QA-Automation.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Optimize
PackagePlan</td>
<td>/packageplan/optimize</td>
<td>Optimize dữ liệu
PackagePlan trong
Security-Firewall.</td>
<td>Thành
công</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Delete Contact</td>
<td>/contact/delete</td>
<td>Delete dữ liệu
Contact trong QA-
Automation.</td>
<td>Tự
động
retry</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Schedule
SwitchConfig</td>
<td>/switchconfig/schedule</td>
<td>Schedule dữ liệu
SwitchConfig trong
BCCS2-Core.</td>
<td>Thông
báo
qua
SMS</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Analyze
Promotion</td>
<td>/promotion/analyze</td>
<td>Analyze dữ liệu
Promotion trong
IVR-System.</td>
<td>Không
lỗi</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Import Invoice</td>
<td>/invoice/import</td>
<td>Import dữ liệu
Invoice trong QA-
Automation.</td>
<td>Thành
công</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Import VPN</td>
<td>/vpn/import</td>
<td>Import dữ liệu VPN
trong QA-
Automation.</td>
<td>Thông
báo
qua
email</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Update
SwitchConfig</td>
<td>/switchconfig/update</td>
<td>Update dữ liệu
SwitchConfig trong
IVR-System.</td>
<td>Thành
công</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Insert
CDRReport</td>
<td>/cdrreport/insert</td>
<td>Insert dữ liệu
CDRReport trong
BCCS2-Billing.</td>
<td>Thành
công</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Export
Whitelist</td>
<td>/whitelist/export</td>
<td>Export dữ liệu
Whitelist trong
Security-Firewall.</td>
<td>Cảnh
báo</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Search
DataLake</td>
<td>/datalake/search</td>
<td>Search dữ liệu
DataLake trong
CRM-Platform.</td>
<td>Cảnh
báo</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Schedule
IVRPrompt</td>
<td>/ivrprompt/schedule</td>
<td>Schedule dữ liệu
IVRPrompt trong
Infra-Server.</td>
<td>Thông
báo
qua
email</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Analyze
Campaign</td>
<td>/campaign/analyze</td>
<td>Analyze dữ liệu
Campaign trong
Infra-Network.</td>
<td>Thông
báo
qua
SMS</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Delete
Opportunity</td>
<td>/opportunity/delete</td>
<td>Delete dữ liệu
Opportunity trong
BCCS2-Billing.</td>
<td>Hiển
thị báo
cáo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Monitor
AccountLock</td>
<td>/accountlock/monitor</td>
<td>Monitor dữ liệu
AccountLock trong
QA-Automation.</td>
<td>Ghi log
đầy đủ</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Monitor
Campaign</td>
<td>/campaign/monitor</td>
<td>Monitor dữ liệu
Campaign trong
BCCS2-Core.</td>
<td>Không
lỗi</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Export QoS</td>
<td>/qos/export</td>
<td>Export dữ liệu QoS
trong IVR-System.</td>
<td>Ghi log
đầy đủ</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Config
KPIReport</td>
<td>/kpireport/config</td>
<td>Config dữ liệu
KPIReport trong
Security-Firewall.</td>
<td>Hiển
thị báo
cáo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Monitor
Blacklist</td>
<td>/blacklist/monitor</td>
<td>Monitor dữ liệu
Blacklist trong Infra-
Server.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize
FirewallPolicy</td>
<td>/firewallpolicy/optimize</td>
<td>Optimize dữ liệu
FirewallPolicy trong
BCCS2-Core.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Search
PackagePlan</td>
<td>/packageplan/search</td>
<td>Search dữ liệu
PackagePlan trong
IPCC-
ContactCenter.</td>
<td>Tự
động
retry</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Delete
Promotion</td>
<td>/promotion/delete</td>
<td>Delete dữ liệu
Promotion trong
IPCC-
ContactCenter.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Monitor
SwitchConfig</td>
<td>/switchconfig/monitor</td>
<td>Monitor dữ liệu
SwitchConfig trong
BCCS2-Core.</td>
<td>Tự
động
retry</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Schedule
DataLake</td>
<td>/datalake/schedule</td>
<td>Schedule dữ liệu
DataLake trong
IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Insert Queue</td>
<td>/queue/insert</td>
<td>Insert dữ liệu Queue
trong IPCC-
ContactCenter.</td>
<td>Thông
báo
qua
email</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Validate
APIGateway</td>
<td>/apigateway/validate</td>
<td>Validate dữ liệu
APIGateway trong
RPA-Engine.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Schedule
AgentStatus</td>
<td>/agentstatus/schedule</td>
<td>Schedule dữ liệu
AgentStatus trong
Infra-Server.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Optimize Lead</td>
<td>/lead/optimize</td>
<td>Optimize dữ liệu
Lead trong IVR-
System.</td>
<td>Không
lỗi</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize
Promotion</td>
<td>/promotion/optimize</td>
<td>Optimize dữ liệu
Promotion trong
BCCS2-Core.</td>
<td>Thông
báo
qua
SMS</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Generate Queue</td>
<td>/queue/generate</td>
<td>Generate dữ liệu
Queue trong
BCCS2-Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Monitor
PackagePlan</td>
<td>/packageplan/monitor</td>
<td>Monitor dữ liệu
PackagePlan trong
BCCS2-Core.</td>
<td>Hiển
thị báo
cáo</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Analyze
StorageVolume</td>
<td>/storagevolume/analyze</td>
<td>Analyze dữ liệu
StorageVolume
trong Security-
Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Export Contact</td>
<td>/contact/export</td>
<td>Export dữ liệu
Contact trong IPCC-
ContactCenter.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Validate QoS</td>
<td>/qos/validate</td>
<td>Validate dữ liệu QoS
trong Infra-Network.</td>
<td>Thành
công</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Search Invoice</td>
<td>/invoice/search</td>
<td>Search dữ liệu
Invoice trong RPA-
Engine.</td>
<td>Thông
báo
qua
SMS</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Update
FirewallPolicy</td>
<td>/firewallpolicy/update</td>
<td>Update dữ liệu
FirewallPolicy trong
IPCC-
ContactCenter.</td>
<td>Tự
động
retry</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Config
ClusterNode</td>
<td>/clusternode/config</td>
<td>Config dữ liệu
ClusterNode trong
QA-Automation.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Delete
FirewallPolicy</td>
<td>/firewallpolicy/delete</td>
<td>Delete dữ liệu
FirewallPolicy trong
BCCS2-Billing.</td>
<td>Cảnh
báo</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Schedule
APIGateway</td>
<td>/apigateway/schedule</td>
<td>Schedule dữ liệu
APIGateway trong
IVR-System.</td>
<td>Hiển
thị báo
cáo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Config
DataLake</td>
<td>/datalake/config</td>
<td>Config dữ liệu
DataLake trong
BCCS2-Core.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Optimize
Whitelist</td>
<td>/whitelist/optimize</td>
<td>Optimize dữ liệu
Whitelist trong
BCCS2-Billing.</td>
<td>Không
lỗi</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Search
ClusterNode</td>
<td>/clusternode/search</td>
<td>Search dữ liệu
ClusterNode trong
Infra-Network.</td>
<td>Hiển
thị báo
cáo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Search Blacklist</td>
<td>/blacklist/search</td>
<td>Search dữ liệu
Blacklist trong
IPCC-
ContactCenter.</td>
<td>Hiển
thị báo
cáo</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Optimize Queue</td>
<td>/queue/optimize</td>
<td>Optimize dữ liệu
Queue trong IPCC-
ContactCenter.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Schedule
IVRPrompt</td>
<td>/ivrprompt/schedule</td>
<td>Schedule dữ liệu
IVRPrompt trong
Infra-Network.</td>
<td>Tự
động
retry</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Schedule
CustomerProfile</td>
<td>/customerprofile/schedule</td>
<td>Schedule dữ liệu
CustomerProfile
trong RPA-Engine.</td>
<td>Thông
báo
qua
email</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Analyze Queue</td>
<td>/queue/analyze</td>
<td>Analyze dữ liệu
Queue trong Infra-
Network.</td>
<td>Không
lỗi</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Update
DataLake</td>
<td>/datalake/update</td>
<td>Update dữ liệu
DataLake trong
CRM-Platform.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Export
AgentStatus</td>
<td>/agentstatus/export</td>
<td>Export dữ liệu
AgentStatus trong
QA-Automation.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Schedule
SwitchConfig</td>
<td>/switchconfig/schedule</td>
<td>Schedule dữ liệu
SwitchConfig trong
BCCS2-Billing.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Update Contact</td>
<td>/contact/update</td>
<td>Update dữ liệu
Contact trong IVR-
System.</td>
<td>Hiển
thị báo
cáo</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Insert
ClusterNode</td>
<td>/clusternode/insert</td>
<td>Insert dữ liệu
ClusterNode trong
IVR-System.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Validate
Campaign</td>
<td>/campaign/validate</td>
<td>Validate dữ liệu
Campaign trong
Security-Firewall.</td>
<td>Hiển
thị báo
cáo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Search Queue</td>
<td>/queue/search</td>
<td>Search dữ liệu
Queue trong IPCC-
ContactCenter.</td>
<td>Tự
động
retry</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Search
Whitelist</td>
<td>/whitelist/search</td>
<td>Search dữ liệu
Whitelist trong
IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Config
FirewallPolicy</td>
<td>/firewallpolicy/config</td>
<td>Config dữ liệu
FirewallPolicy trong
IVR-System.</td>
<td>Hiển
thị báo
cáo</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Validate
AccountLock</td>
<td>/accountlock/validate</td>
<td>Validate dữ liệu
AccountLock trong
QA-Automation.</td>
<td>Tự
động
retry</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Insert
AccountLock</td>
<td>/accountlock/insert</td>
<td>Insert dữ liệu
AccountLock trong
RPA-Engine.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Insert Invoice</td>
<td>/invoice/insert</td>
<td>Insert dữ liệu
Invoice trong Infra-
Network.</td>
<td>Thông
báo
qua
SMS</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Generate
Whitelist</td>
<td>/whitelist/generate</td>
<td>Generate dữ liệu
Whitelist trong
RPA-Engine.</td>
<td>Tự
động
retry</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Analyze Invoice</td>
<td>/invoice/analyze</td>
<td>Analyze dữ liệu
Invoice trong
BCCS2-Core.</td>
<td>Thông
báo
qua
email</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Generate
FirewallPolicy</td>
<td>/firewallpolicy/generate</td>
<td>Generate dữ liệu
FirewallPolicy trong
QA-Automation.</td>
<td>Tự
động
retry</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Analyze
AgentStatus</td>
<td>/agentstatus/analyze</td>
<td>Analyze dữ liệu
AgentStatus trong
Infra-Server.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Export
DataLake</td>
<td>/datalake/export</td>
<td>Export dữ liệu
DataLake trong
Infra-Server.</td>
<td>Thành
công</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Insert
PackagePlan</td>
<td>/packageplan/insert</td>
<td>Insert dữ liệu
PackagePlan trong
BCCS2-Core.</td>
<td>Ghi log
đầy đủ</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Delete
DataLake</td>
<td>/datalake/delete</td>
<td>Delete dữ liệu
DataLake trong
BCCS2-Core.</td>
<td>Ghi log
đầy đủ</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Validate
DataLake</td>
<td>/datalake/validate</td>
<td>Validate dữ liệu
DataLake trong
Infra-Server.</td>
<td>Không
lỗi</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Schedule QoS</td>
<td>/qos/schedule</td>
<td>Schedule dữ liệu
QoS trong Infra-
Server.</td>
<td>Tự
động
retry</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Search
CustomerProfile</td>
<td>/customerprofile/search</td>
<td>Search dữ liệu
CustomerProfile
trong RPA-Engine.</td>
<td>Hiển
thị báo
cáo</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Update Lead</td>
<td>/lead/update</td>
<td>Update dữ liệu Lead
trong Infra-Server.</td>
<td>Không
lỗi</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Generate
CDRReport</td>
<td>/cdrreport/generate</td>
<td>Generate dữ liệu
CDRReport trong
Security-Firewall.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Monitor
PackagePlan</td>
<td>/packageplan/monitor</td>
<td>Monitor dữ liệu
PackagePlan trong
Security-Firewall.</td>
<td>Cảnh
báo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Export
FirewallPolicy</td>
<td>/firewallpolicy/export</td>
<td>Export dữ liệu
FirewallPolicy trong</td>
<td>Thông
báo</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter.</td>
<td>qua
SMS</td>
<td>ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Import
Promotion</td>
<td>/promotion/import</td>
<td>Import dữ liệu
Promotion trong
Security-Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Delete
KPIReport</td>
<td>/kpireport/delete</td>
<td>Delete dữ liệu
KPIReport trong
BCCS2-Billing.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Import VPN</td>
<td>/vpn/import</td>
<td>Import dữ liệu VPN
trong IPCC-
ContactCenter.</td>
<td>Cảnh
báo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Monitor
Whitelist</td>
<td>/whitelist/monitor</td>
<td>Monitor dữ liệu
Whitelist trong
IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Optimize
DebtControl</td>
<td>/debtcontrol/optimize</td>
<td>Optimize dữ liệu
DebtControl trong
QA-Automation.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Insert
SwitchConfig</td>
<td>/switchconfig/insert</td>
<td>Insert dữ liệu
SwitchConfig trong
IPCC-
ContactCenter.</td>
<td>Tự
động
retry</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Config
CDRReport</td>
<td>/cdrreport/config</td>
<td>Config dữ liệu
CDRReport trong
IPCC-
ContactCenter.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Config
PackagePlan</td>
<td>/packageplan/config</td>
<td>Config dữ liệu
PackagePlan trong
IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Config
AgentStatus</td>
<td>/agentstatus/config</td>
<td>Config dữ liệu
AgentStatus trong
IPCC-
ContactCenter.</td>
<td>Cảnh
báo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Monitor
IVRPrompt</td>
<td>/ivrprompt/monitor</td>
<td>Monitor dữ liệu
IVRPrompt trong
Security-Firewall.</td>
<td>Ghi log
đầy đủ</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Update
FirewallPolicy</td>
<td>/firewallpolicy/update</td>
<td>Update dữ liệu
FirewallPolicy trong
RPA-Engine.</td>
<td>Hiển
thị báo
cáo</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Delete Contact</td>
<td>/contact/delete</td>
<td>Delete dữ liệu
Contact trong Infra-
Server.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Insert Invoice</td>
<td>/invoice/insert</td>
<td>Insert dữ liệu
Invoice trong Infra-
Network.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Schedule
Campaign</td>
<td>/campaign/schedule</td>
<td>Schedule dữ liệu
Campaign trong QA-
Automation.</td>
<td>Ghi log
đầy đủ</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Analyze
Whitelist</td>
<td>/whitelist/analyze</td>
<td>Analyze dữ liệu
Whitelist trong
BCCS2-Billing.</td>
<td>Thông
báo
qua
SMS</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Generate
CDRReport</td>
<td>/cdrreport/generate</td>
<td>Generate dữ liệu
CDRReport trong
Security-Firewall.</td>
<td>Thành
công</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Analyze
Whitelist</td>
<td>/whitelist/analyze</td>
<td>Analyze dữ liệu
Whitelist trong
IPCC-
ContactCenter.</td>
<td>Không
lỗi</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Export Invoice</td>
<td>/invoice/export</td>
<td>Export dữ liệu
Invoice trong QA-
Automation.</td>
<td>Hiển
thị báo
cáo</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Export QoS</td>
<td>/qos/export</td>
<td>Export dữ liệu QoS
trong IPCC-
ContactCenter.</td>
<td>Cảnh
báo</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Insert
CDRReport</td>
<td>/cdrreport/insert</td>
<td>Insert dữ liệu
CDRReport trong
BCCS2-Core.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Update
APIGateway</td>
<td>/apigateway/update</td>
<td>Update dữ liệu
APIGateway trong
BCCS2-Core.</td>
<td>Tự
động
retry</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Export
TransactionLog</td>
<td>/transactionlog/export</td>
<td>Export dữ liệu
TransactionLog
trong Infra-Server.</td>
<td>Cảnh
báo</td>
<td>Theo
chuẩn</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>ISO
27001</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Update Contact</td>
<td>/contact/update</td>
<td>Update dữ liệu
Contact trong Infra-
Server.</td>
<td>Cảnh
báo</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Insert
CDRReport</td>
<td>/cdrreport/insert</td>
<td>Insert dữ liệu
CDRReport trong
CRM-Platform.</td>
<td>Thành
công</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Export
KPIReport</td>
<td>/kpireport/export</td>
<td>Export dữ liệu
KPIReport trong
BCCS2-Core.</td>
<td>Hiển
thị báo
cáo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Monitor
APIGateway</td>
<td>/apigateway/monitor</td>
<td>Monitor dữ liệu
APIGateway trong
IVR-System.</td>
<td>Ghi log
đầy đủ</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Import Queue</td>
<td>/queue/import</td>
<td>Import dữ liệu
Queue trong
Security-Firewall.</td>
<td>Cảnh
báo</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import Queue</td>
<td>/queue/import</td>
<td>Import dữ liệu
Queue trong
BCCS2-Core.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Analyze
Campaign</td>
<td>/campaign/analyze</td>
<td>Analyze dữ liệu
Campaign trong
IVR-System.</td>
<td>Ghi log
đầy đủ</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Generate
APIGateway</td>
<td>/apigateway/generate</td>
<td>Generate dữ liệu
APIGateway trong
Security-Firewall.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Kết nối
với hệ</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>thống
Billing</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Monitor
Promotion</td>
<td>/promotion/monitor</td>
<td>Monitor dữ liệu
Promotion trong
CRM-Platform.</td>
<td>Cảnh
báo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Monitor
Whitelist</td>
<td>/whitelist/monitor</td>
<td>Monitor dữ liệu
Whitelist trong
Security-Firewall.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Delete
PackagePlan</td>
<td>/packageplan/delete</td>
<td>Delete dữ liệu
PackagePlan trong
IPCC-
ContactCenter.</td>
<td>Thành
công</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Insert
DebtControl</td>
<td>/debtcontrol/insert</td>
<td>Insert dữ liệu
DebtControl trong
IVR-System.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Optimize
Whitelist</td>
<td>/whitelist/optimize</td>
<td>Optimize dữ liệu
Whitelist trong
Infra-Server.</td>
<td>Tự
động
retry</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Monitor
Promotion</td>
<td>/promotion/monitor</td>
<td>Monitor dữ liệu
Promotion trong
Infra-Network.</td>
<td>Hiển
thị báo
cáo</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import
IVRPrompt</td>
<td>/ivrprompt/import</td>
<td>Import dữ liệu
IVRPrompt trong
BCCS2-Core.</td>
<td>Không
lỗi</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Validate
TransactionLog</td>
<td>/transactionlog/validate</td>
<td>Validate dữ liệu
TransactionLog
trong IVR-System.</td>
<td>Ghi log
đầy đủ</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Import
CustomerProfile</td>
<td>/customerprofile/import</td>
<td>Import dữ liệu
CustomerProfile
trong BCCS2-Core.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Optimize QoS</td>
<td>/qos/optimize</td>
<td>Optimize dữ liệu
QoS trong BCCS2-
Billing.</td>
<td>Cảnh
báo</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Schedule Queue</td>
<td>/queue/schedule</td>
<td>Schedule dữ liệu
Queue trong
BCCS2-Core.</td>
<td>Cảnh
báo</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Optimize
ClusterNode</td>
<td>/clusternode/optimize</td>
<td>Optimize dữ liệu
ClusterNode trong
CRM-Platform.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Delete
FirewallPolicy</td>
<td>/firewallpolicy/delete</td>
<td>Delete dữ liệu
FirewallPolicy trong
CRM-Platform.</td>
<td>Tự
động
retry</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Export
Whitelist</td>
<td>/whitelist/export</td>
<td>Export dữ liệu
Whitelist trong
Infra-Server.</td>
<td>Thành
công</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Import
CDRReport</td>
<td>/cdrreport/import</td>
<td>Import dữ liệu
CDRReport trong
Infra-Server.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Update
KPIReport</td>
<td>/kpireport/update</td>
<td>Update dữ liệu
KPIReport trong
Infra-Server.</td>
<td>Tự
động
retry</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Config Lead</td>
<td>/lead/config</td>
<td>Config dữ liệu Lead
trong BCCS2-
Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Analyze
Blacklist</td>
<td>/blacklist/analyze</td>
<td>Analyze dữ liệu
Blacklist trong
CRM-Platform.</td>
<td>Cảnh
báo</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Update
Whitelist</td>
<td>/whitelist/update</td>
<td>Update dữ liệu
Whitelist trong QA-
Automation.</td>
<td>Thông
báo
qua
SMS</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Monitor Invoice</td>
<td>/invoice/monitor</td>
<td>Monitor dữ liệu
Invoice trong IPCC-
ContactCenter.</td>
<td>Ghi log
đầy đủ</td>
<td>Bảo
mật 2
lớp</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>CRM-
Platform</td>
<td>Export Invoice</td>
<td>/invoice/export</td>
<td>Export dữ liệu
Invoice trong CRM-
Platform.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Import
KPIReport</td>
<td>/kpireport/import</td>
<td>Import dữ liệu
KPIReport trong
Infra-Server.</td>
<td>Tự
động
retry</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Validate Lead</td>
<td>/lead/validate</td>
<td>Validate dữ liệu
Lead trong QA-
Automation.</td>
<td>Thành
công</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Update VPN</td>
<td>/vpn/update</td>
<td>Update dữ liệu VPN
trong Infra-Server.</td>
<td>Thông
báo
qua
email</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Search VPN</td>
<td>/vpn/search</td>
<td>Search dữ liệu VPN
trong Infra-Network.</td>
<td>Thông
báo
qua
email</td>
<td>Chạy
theo
lịch
cron</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Export
APIGateway</td>
<td>/apigateway/export</td>
<td>Export dữ liệu
APIGateway trong
BCCS2-Billing.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Import
KPIReport</td>
<td>/kpireport/import</td>
<td>Import dữ liệu
KPIReport trong
Infra-Network.</td>
<td>Thông
báo
qua
email</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Security-
Firewall</td>
<td>Export
APIGateway</td>
<td>/apigateway/export</td>
<td>Export dữ liệu
APIGateway trong
Security-Firewall.</td>
<td>Tự
động
retry</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Schedule
Blacklist</td>
<td>/blacklist/schedule</td>
<td>Schedule dữ liệu
Blacklist trong Infra-
Server.</td>
<td>Hiển
thị báo
cáo</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Schedule
Blacklist</td>
<td>/blacklist/schedule</td>
<td>Schedule dữ liệu
Blacklist trong QA-
Automation.</td>
<td>Tự
động
retry</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Monitor
CustomerProfile</td>
<td>/customerprofile/monitor</td>
<td>Monitor dữ liệu
CustomerProfile
trong Infra-Server.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Generate
PackagePlan</td>
<td>/packageplan/generate</td>
<td>Generate dữ liệu
PackagePlan trong
IVR-System.</td>
<td>Thông
báo
qua
SMS</td>
<td>Có cơ
chế
rollback</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-Core</td>
<td>Optimize
IVRPrompt</td>
<td>/ivrprompt/optimize</td>
<td>Optimize dữ liệu
IVRPrompt trong
BCCS2-Core.</td>
<td>Đồng
bộ dữ
liệu</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Delete Whitelist</td>
<td>/whitelist/delete</td>
<td>Delete dữ liệu
Whitelist trong
Infra-Network.</td>
<td>Lỗi
nghiêm
trọng</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Server</td>
<td>Delete
PackagePlan</td>
<td>/packageplan/delete</td>
<td>Delete dữ liệu
PackagePlan trong
Infra-Server.</td>
<td>Không
lỗi</td>
<td>Theo
chuẩn
ISO
27001</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Update
IVRPrompt</td>
<td>/ivrprompt/update</td>
<td>Update dữ liệu
IVRPrompt trong
RPA-Engine.</td>
<td>Thông
báo
qua
SMS</td>
<td>Theo
quy
định
Viettel</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Generate
Blacklist</td>
<td>/blacklist/generate</td>
<td>Generate dữ liệu
Blacklist trong IVR-
System.</td>
<td>Thành
công</td>
<td>Kết nối
với hệ
thống
Billing</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Analyze
CDRReport</td>
<td>/cdrreport/analyze</td>
<td>Analyze dữ liệu
CDRReport trong
RPA-Engine.</td>
<td>Hiển
thị báo
cáo</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IPCC-
ContactCenter</td>
<td>Search Contact</td>
<td>/contact/search</td>
<td>Search dữ liệu
Contact trong IPCC-
ContactCenter.</td>
<td>Thành
công</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Analyze
FirewallPolicy</td>
<td>/firewallpolicy/analyze</td>
<td>Analyze dữ liệu
FirewallPolicy trong
IVR-System.</td>
<td>Không
lỗi</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Search
IVRPrompt</td>
<td>/ivrprompt/search</td>
<td>Search dữ liệu
IVRPrompt trong
Infra-Network.</td>
<td>Thông
báo
qua
email</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>Infra-Network</td>
<td>Schedule VPN</td>
<td>/vpn/schedule</td>
<td>Schedule dữ liệu
VPN trong Infra-
Network.</td>
<td>Hiển
thị báo
cáo</td>
<td>Chỉ
dùng
cho
admin</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>IVR-System</td>
<td>Monitor
TransactionLog</td>
<td>/transactionlog/monitor</td>
<td>Monitor dữ liệu
TransactionLog
trong IVR-System.</td>
<td>Tự
động
retry</td>
<td>Yêu
cầu xác
thực
người
dùng</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>QA-
Automation</td>
<td>Monitor
StorageVolume</td>
<td>/storagevolume/monitor</td>
<td>Monitor dữ liệu
StorageVolume
trong QA-
Automation.</td>
<td>Thông
báo
qua
email</td>
<td>Tích
hợp với
CRM</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>BCCS2-
Billing</td>
<td>Insert
FirewallPolicy</td>
<td>/firewallpolicy/insert</td>
<td>Insert dữ liệu
FirewallPolicy trong
BCCS2-Billing.</td>
<td>Thông
báo
qua
email</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>RPA-Engine</td>
<td>Optimize
Campaign</td>
<td>/campaign/optimize</td>
<td>Optimize dữ liệu
Campaign trong
RPA-Engine.</td>
<td>Tự
động
retry</td>
<td>Dữ liệu
backup
mỗi
ngày</td>
</tr>
</tbody>
</table>
