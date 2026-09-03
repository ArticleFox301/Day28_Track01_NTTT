# Day 28 Track 01 — Dashboard Hành Động Cho Áp Dụng AI

## 1. Thành viên và đóng góp

| Họ tên | MSSV | Phần phụ trách | Góp ý đã đưa cho nhóm bạn |
|---|---|---|---|
| Nguyễn Trung Đức | 2A202601750 | Khoá phạm vi, Gartner-Lite, ADKAR, chẩn đoán nguyên nhân gốc và tổng hợp README | Không có nhóm phản biện |
| Nguyễn Thị Thu Trang | 2A202601634 | Mollick, AS-IS/TO-BE, kiến trúc tin cậy, roadmap, dashboard và memo quyết định | Không có nhóm phản biện |


## 2. Phạm vi

- **Sản phẩm AI:** Trợ lý AI tra cứu tài liệu nội bộ.
- **Người dùng chính:** Nhân viên vận hành xử lý yêu cầu khách hàng.
- **Ba workflow:** (1) tìm chính sách/quy trình, (2) tóm tắt hướng dẫn xử lý, (3) kiểm chứng trước khi trả lời khách hàng.
- **Vấn đề quan sát:** Công cụ đã được cấp nhưng nhân viên vẫn quay lại tìm file hoặc hỏi đồng nghiệp; đây là triệu chứng, chưa phải nguyên nhân gốc.

## 3. Nguyên nhân gốc

1. **Thiếu kiến trúc tin cậy:** câu trả lời chưa bảo đảm nguồn, phiên bản/ngày cập nhật, QA mẫu và đường chuyển người. Gartner-Lite cho thấy Readiness/Absorption còn thiếu; ADKAR cho thấy nghẽn Desire vì người dùng không đủ căn cứ để tin.
2. **AI nằm ngoài workflow chính thức:** chưa quy định phần việc AI, bước kiểm chứng và người chịu trách nhiệm. Phân chia Mollick cho thấy AI chỉ nên tìm/tóm tắt; nhân viên giữ quyền dùng kết quả và xử lý ngoại lệ.

**Bằng chứng hiện có:** dấu hiệu workflow từ case xuyên suốt trong đề bài (không có nguồn/ngày cập nhật, người dùng quay về cách cũ). **Bằng chứng bắt buộc phải bổ sung:** tối thiểu 10 tác vụ baseline trong tuần 1 và 3–5 phỏng vấn ngắn của người dùng thực tế.

## 4. Cách làm mới

Workflow TO-BE bắt buộc câu trả lời có nguồn và ngày cập nhật; nhân viên vận hành kiểm chứng và chịu trách nhiệm cuối; khi thiếu nguồn, nguồn cũ hoặc độ tin cậy thấp thì không dùng câu trả lời, chuyển SME/data owner và ghi log phản hồi. QA kiểm tra mẫu hàng tuần để cập nhật kho tri thức.

## 5. Chỉ số

- **Product metric:** tỷ lệ câu trả lời có nguồn hợp lệ — baseline mẫu 55%, mục tiêu ≥95%; nguồn: log trợ lý + danh mục tài liệu; owner: AI Product Owner.
- **Workflow metric:** trung vị thời gian hoàn tất một lượt tra cứu đã kiểm chứng — baseline mẫu 12 phút, mục tiêu ≤7 phút; nguồn: timestamp hệ thống tác vụ; owner: Process Owner.
- **Guardrails:** tỷ lệ không phải QA làm lại ≥90%; lỗi nghiêm trọng do dùng câu trả lời sai = 0. Chi tiết và hành động khi xấu nằm trong dashboard v2.

## 6. Quyết định

**SỬA rồi tiếp tục pilot hẹp**, chưa rollout rộng: hướng đi có giá trị nhưng trust architecture và ownership chưa đạt gate. Sau khi nhóm tự rà soát v1, v2 (1) bổ sung tính hợp lệ/độ mới của nguồn và guardrail lỗi nghiêm trọng, (2) thay mục tiêu dùng AI đơn thuần bằng tỷ lệ hoàn tất có kiểm chứng, đồng thời thêm quy tắc sửa/dừng rõ ràng.



