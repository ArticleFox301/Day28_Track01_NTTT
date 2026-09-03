# Memo quyết định — Trợ lý AI tra cứu tài liệu nội bộ

**Ngày đánh giá:** 3/9/2026 
**Người quyết định:** Trưởng phòng Vận hành (Business Owner)
**Phạm vi:** Nhân viên vận hành; tìm chính sách, tóm tắt hướng dẫn và kiểm chứng trước khi phản hồi khách hàng.

## 1. Vấn đề và nguyên nhân gốc

Triệu chứng là nhân viên ít quay lại công cụ và vẫn tìm file/hỏi đồng nghiệp. Hai nguyên nhân gốc là: (1) câu trả lời thiếu chuỗi tin cậy gồm nguồn hợp lệ, ngày cập nhật, QA và chuyển người; (2) AI chưa được đặt vào workflow chính thức với ranh giới trách nhiệm rõ ràng. Vì vậy, tăng số login hay mở thêm lớp đào tạo riêng lẻ sẽ không xử lý đúng gốc.

## 2. Framework và bằng chứng

- **Gartner-Lite:** Direction đạt vì bài toán giảm thời gian tra cứu đã rõ; Readiness thiếu data owner/lịch cập nhật; Absorption thiếu owner chất lượng và vòng phản hồi.
- **ADKAR:** nghẽn chính ở Desire (không tin khi thiếu nguồn), sau đó là Ability và Reinforcement trong công việc thật; Knowledge không phải nguyên nhân duy nhất.
- **Mollick:** AI tìm và tóm tắt; nhân viên kiểm chứng, quyết định sử dụng và chịu trách nhiệm; tự động hoá chỉ dành cho logging/routing rủi ro thấp.
- **Bằng chứng:** đề bài ghi nhận dấu hiệu “không chỉ rõ nguồn và ngày cập nhật”, “người dùng vẫn tìm file/hỏi đồng nghiệp”. Đây là bằng chứng case mẫu, chưa phải bằng chứng doanh nghiệp. Trước gate 30 ngày, Process Owner phải lấy baseline từ ≥10 tác vụ và phỏng vấn 3–5 người dùng.

## 3. Thay đổi sau phản biện

Góp ý mô phỏng 1: “Tỷ lệ có nguồn chưa chứng minh nguồn đúng hoặc còn hiệu lực.” V2 bổ sung tiêu chí nguồn hợp lệ (đúng tài liệu, đúng quyền, còn hiệu lực) và tỷ lệ câu trả lời đạt QA không làm lại.

Góp ý mô phỏng 2: “Mức sử dụng có thể tăng mà giá trị không tăng.” V2 đổi sang tỷ lệ tác vụ hoàn tất theo TO-BE có kiểm chứng, thêm thời gian tra cứu từ timestamp và guardrail lỗi nghiêm trọng. Hai góp ý này phải được thay/xác nhận bằng phản biện thật của nhóm bạn trước khi nộp.

## 4. Quyết định

**SỬA rồi tiếp tục pilot hẹp; chưa rollout rộng.** Pilot chỉ qua gate 60 ngày nếu đạt đồng thời chất lượng nguồn, tỷ lệ không làm lại và không có lỗi nghiêm trọng. Nếu không đạt sau một chu kỳ sửa có owner, dừng mở rộng và đánh giá lại dữ liệu/giải pháp.

## 5. Lý do, bước tiếp theo và owner

Hướng đi có tiềm năng tạo giá trị, nhưng dữ liệu hiện tại chưa đủ chứng minh chất lượng và giá trị nghiệp vụ. Trong 0–30 ngày, **Process Owner** lấy baseline và khoá TO-BE, **Data Owner** lập danh mục nguồn/quyền/lịch cập nhật. Trong 31–60 ngày, **AI Product Owner** bật trích nguồn và routing, **QA Lead** kiểm mẫu hàng tuần. Trong 61–90 ngày, **Business Owner** áp dụng quy tắc: mở rộng khi toàn bộ gate đạt; sửa khi metric giá trị đạt nhưng quality/behavior chưa đạt; dừng khi có lỗi nghiêm trọng hoặc giá trị không cải thiện sau chu kỳ sửa.

