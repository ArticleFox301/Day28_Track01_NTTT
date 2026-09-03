from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]

V1 = {
    "Tổng quan": [
        ["DASHBOARD HÀNH ĐỘNG V1", "Trợ lý AI tra cứu tài liệu nội bộ"],
        ["Trạng thái", "Bản trước phản biện — số liệu mẫu cần thay bằng dữ liệu thật"],
        ["Sản phẩm", "Trợ lý AI tra cứu tài liệu nội bộ"],
        ["Người dùng", "Nhân viên vận hành xử lý yêu cầu khách hàng"],
        ["Workflow", "Tìm chính sách; tóm tắt hướng dẫn; kiểm chứng trước phản hồi"],
        ["Triệu chứng", "Người dùng vẫn tìm file hoặc hỏi đồng nghiệp"],
        ["Quyết định sơ bộ", "Tiếp tục pilot"],
    ],
    "Chẩn đoán": [
        ["Framework/Trục", "Nhận định", "Mức", "Bằng chứng/kiểm chứng"],
        ["Gartner-Lite — Direction", "Mục tiêu giảm thời gian tra cứu rõ", "ĐẠT", "Phạm vi case"],
        ["Gartner-Lite — Readiness", "Thiếu owner và lịch cập nhật nguồn", "THIẾU", "Dấu hiệu trong đề; cần audit nguồn"],
        ["Gartner-Lite — Absorption", "Thiếu owner chất lượng và vòng phản hồi", "THIẾU", "Dấu hiệu workflow; cần phỏng vấn"],
        ["ADKAR — Desire", "Ngại tin câu trả lời vì thiếu nguồn", "NGHẼN", "Dấu hiệu trong đề; cần phỏng vấn 3–5 người"],
        ["Mollick", "AI tìm/tóm tắt; người kiểm chứng và quyết định", "CHƯA RÕ", "AS-IS chưa có RACI"],
        ["Nguyên nhân gốc 1", "Thiếu kiến trúc tin cậy", "GỐC", "Thiếu nguồn, QA và chuyển người"],
        ["Nguyên nhân gốc 2", "AI nằm ngoài workflow chính thức", "GỐC", "Không có owner/handoff"],
    ],
    "Workflow": [
        ["Workflow", "AS-IS", "TO-BE v1", "AI", "Người chịu trách nhiệm", "Khi AI không chắc"],
        ["Tìm chính sách", "Tìm nhiều thư mục/hỏi đồng nghiệp", "Hỏi AI → xem trích nguồn", "Tìm và xếp hạng", "Nhân viên vận hành", "Tìm thủ công"],
        ["Tóm tắt hướng dẫn", "Đọc và tự ghi chú", "AI tóm tắt → người đọc lại", "Tạo bản tóm tắt", "Nhân viên vận hành", "Hỏi SME"],
        ["Kiểm chứng", "Không có bước chuẩn", "Mở tài liệu nguồn → đối chiếu", "Gợi ý đoạn nguồn", "Nhân viên vận hành", "Không sử dụng kết quả"],
    ],
    "Roadmap": [
        ["Giai đoạn", "Mục tiêu/Gate", "Hành động", "Owner", "Dấu hiệu hoàn thành"],
        ["0–30 ngày", "Chứng minh vấn đề", "Khoá phạm vi; audit nguồn; đo ≥10 tác vụ", "Process Owner + Data Owner", "Có baseline, data owner và TO-BE được duyệt"],
        ["31–60 ngày", "Chứng minh chất lượng", "Bật trích nguồn; QA mẫu; hỗ trợ người dùng", "AI Product Owner + QA Lead", "Có báo cáo chất lượng và vòng phản hồi"],
        ["61–90 ngày", "Quyết định mở rộng", "So mục tiêu; rà governance; chốt vận hành", "Business Owner", "Quyết định mở rộng/sửa/dừng bằng dữ liệu"],
    ],
    "Metrics": [
        ["Cấp", "Tầng", "Chỉ số", "Baseline", "Mục tiêu", "Nguồn dữ liệu", "Owner", "Khi chỉ số xấu"],
        ["Product", "Sử dụng", "Tỷ lệ người dùng hoạt động tuần", "35% (GIẢ ĐỊNH)", "≥70%", "Log đăng nhập", "AI Product Owner", "Đào tạo lại"],
        ["Product", "Tin cậy", "Tỷ lệ câu trả lời có trích nguồn", "55% (GIẢ ĐỊNH)", "≥90%", "Log câu trả lời", "AI Product Owner", "Sửa prompt/RAG"],
        ["Workflow", "Năng suất", "Trung vị thời gian tra cứu", "12 phút (GIẢ ĐỊNH)", "≤8 phút", "Tự khai người dùng", "Process Owner", "Xem lại workflow"],
        ["Workflow", "Chất lượng", "Tỷ lệ không phải QA làm lại", "70% (GIẢ ĐỊNH)", "≥85%", "QA mẫu", "QA Lead", "Tăng cỡ mẫu QA"],
    ],
}

V2 = {
    "Tổng quan": [
        ["DASHBOARD HÀNH ĐỘNG V2", "Trợ lý AI tra cứu tài liệu nội bộ"],
        ["Trạng thái", "Sau phản biện — số liệu GIẢ ĐỊNH phải thay bằng dữ liệu thật"],
        ["Sản phẩm", "Trợ lý AI tra cứu tài liệu nội bộ"],
        ["Người dùng", "Nhân viên vận hành xử lý yêu cầu khách hàng"],
        ["Ba workflow", "Tìm chính sách; tóm tắt hướng dẫn; kiểm chứng trước phản hồi"],
        ["Vấn đề đo được", "Tỷ lệ tác vụ hoàn tất theo TO-BE thấp; thời gian và làm lại chưa cải thiện"],
        ["Nguyên nhân gốc", "Thiếu trust architecture; thiếu owner/handoff trong workflow"],
        ["Quyết định", "SỬA rồi tiếp tục pilot hẹp; CHƯA rollout rộng"],
        ["Điều kiện dữ liệu", "Baseline từ ≥10 tác vụ + phỏng vấn 3–5 người trước gate 30 ngày"],
    ],
    "Chẩn đoán": V1["Chẩn đoán"] + [
        ["Kết luận", "Sửa tin cậy và workflow trước khi tăng usage", "HÀNH ĐỘNG", "Đo log + QA + phỏng vấn"],
    ],
    "Workflow": [
        ["Workflow", "AS-IS", "TO-BE v2", "Vai trò AI", "Quyền/Owner cuối", "Kiểm soát & ngoại lệ"],
        ["Tìm chính sách", "Tìm nhiều thư mục/hỏi đồng nghiệp", "Hỏi AI → xem nguồn, phiên bản, ngày hiệu lực", "Tìm/xếp hạng trong nguồn được duyệt", "Nhân viên vận hành", "Thiếu/cũ/sai quyền → chặn dùng, route Data Owner"],
        ["Tóm tắt hướng dẫn", "Đọc và tự ghi chú", "AI tóm tắt kèm đoạn dẫn → người đối chiếu", "Tạo nháp, không phê duyệt", "Nhân viên vận hành", "Mâu thuẫn nguồn → route SME, ghi log"],
        ["Kiểm chứng", "Không có bước chuẩn", "Checklist nguồn → đối chiếu → dùng/báo lỗi", "Gợi ý độ tin cậy và đoạn nguồn", "Nhân viên vận hành chịu trách nhiệm", "Độ tin cậy thấp → không dùng; QA lấy mẫu hàng tuần"],
        ["Vòng phản hồi", "Phản hồi rời rạc", "Gắn nhãn lỗi → triage → sửa nguồn/prompt → đóng lỗi", "Tự động logging/routing rủi ro thấp", "AI Product Owner", "Lỗi nghiêm trọng → tạm dừng workflow bị ảnh hưởng"],
    ],
    "Roadmap": [
        ["Giai đoạn", "Gate quyết định", "Hành động", "Owner", "Tiêu chí qua gate"],
        ["0–30 ngày", "Chứng minh vấn đề & đo được", "Khoá TO-BE; audit nguồn/quyền; ≥10 tác vụ; 3–5 phỏng vấn", "Process Owner + Data Owner", "Baseline đủ; 100% nguồn pilot có owner/lịch cập nhật; TO-BE duyệt"],
        ["31–60 ngày", "Chứng minh chất lượng & hành vi", "Trích nguồn/phiên bản; QA ≥30 câu/tuần; office hour; triage lỗi", "AI Product Owner + QA Lead", "Nguồn hợp lệ ≥95%; không làm lại ≥90%; lỗi nghiêm trọng = 0"],
        ["61–90 ngày", "Chứng minh giá trị & governance", "So nhóm/baseline; review quyền/chi phí; chốt SOP và owner", "Business Owner", "Thời gian ≤7 phút; hoàn tất TO-BE ≥75%; quality gate giữ 2 tuần"],
        ["Quy tắc", "Mở rộng/Sửa/Dừng", "Mở rộng nếu tất cả gate đạt; sửa nếu giá trị đạt nhưng quality/behavior hụt; dừng nếu lỗi nghiêm trọng hoặc không cải thiện sau 1 chu kỳ sửa", "Business Owner", "Biên bản quyết định có dữ liệu và owner"],
    ],
    "Metrics": [
        ["Cấp", "Tầng", "Chỉ số/định nghĩa", "Baseline", "Mục tiêu/Gate", "Nguồn dữ liệu", "Owner", "Khi chỉ số xấu"],
        ["Product", "Tin cậy", "% câu trả lời có nguồn hợp lệ: đúng tài liệu, đúng quyền, còn hiệu lực", "55% (GIẢ ĐỊNH; đo ≥30 mẫu)", "≥95% trong 2 tuần", "Log câu trả lời + registry tài liệu", "AI Product Owner", "Khoanh nguồn lỗi; Data Owner sửa/ẩn; chạy lại eval trước mở"],
        ["Product", "Rủi ro", "Số lỗi nghiêm trọng do dùng câu trả lời sai", "Chưa đo", "0", "Incident log + QA", "Risk/QA Lead", "Tạm dừng workflow liên quan; điều tra và phê duyệt lại"],
        ["Workflow", "Hành vi", "% tác vụ hoàn tất đủ Hỏi AI → Xem nguồn → Kiểm chứng", "25% (GIẢ ĐỊNH; log tuần 1)", "≥75%", "Event log theo task ID", "Team Lead", "Phỏng vấn 5 ca bỏ bước; sửa UX/SOP/hỗ trợ tại chỗ"],
        ["Workflow", "Năng suất", "Trung vị phút từ mở tác vụ đến kiểm chứng xong", "12 phút (GIẢ ĐỊNH; ≥10 tác vụ)", "≤7 phút và không giảm quality", "Timestamp hệ thống tác vụ", "Process Owner", "Phân tích từng bước; sửa retrieval/handoff; không nới quality gate"],
        ["Workflow", "Chất lượng", "% tác vụ đạt QA ngay, không phải làm lại", "70% (GIẢ ĐỊNH; ≥30 mẫu)", "≥90%", "QA form liên kết task ID", "QA Lead", "Tăng QA tạm thời; phân loại lỗi; sửa nguồn/prompt/SOP"],
        ["Workflow", "Giá trị", "% yêu cầu khách hàng đúng SLA ở nhóm pilot", "82% (GIẢ ĐỊNH)", "≥90% và cao hơn baseline ≥5 điểm %", "Ticketing/CRM", "Business Owner", "Nếu không tăng sau 1 chu kỳ sửa: dừng mở rộng, đánh giá lại"],
    ],
    "Phản biện v1-v2": [
        ["Góp ý", "Vấn đề ở v1", "Thay đổi trong v2", "Cách chứng minh"],
        ["1 (mô phỏng — cần xác nhận)", "Có trích nguồn chưa nói nguồn đúng/còn hiệu lực", "Định nghĩa nguồn hợp lệ; thêm registry, QA và incident guardrail", "QA ≥30 mẫu/tuần + incident log"],
        ["2 (mô phỏng — cần xác nhận)", "Usage có thể tăng mà không tạo giá trị", "Đo completion TO-BE, timestamp, làm lại và SLA", "Event log + task ID + ticketing/CRM"],
        ["Khác biệt quyết định", "V1: tiếp tục pilot chung chung", "V2: sửa/pilot hẹp với gate mở rộng-sửa-dừng", "Biên bản gate 30/60/90"],
    ],
}

def col_name(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

def worksheet_xml(rows):
    widths = []
    max_cols = max(len(r) for r in rows)
    for c in range(max_cols):
        widths.append(min(55, max(12, max((len(str(r[c])) if c < len(r) else 0) for r in rows) + 2)))
    cols = "".join(f'<col min="{i}" max="{i}" width="{w}" customWidth="1"/>' for i, w in enumerate(widths, 1))
    xml_rows = []
    for ri, row in enumerate(rows, 1):
        cells = []
        for ci, value in enumerate(row, 1):
            ref = f"{col_name(ci)}{ri}"
            style = 1 if ri == 1 else (2 if ci == 1 else 3)
            cells.append(f'<c r="{ref}" t="inlineStr" s="{style}"><is><t xml:space="preserve">{escape(str(value))}</t></is></c>')
        xml_rows.append(f'<row r="{ri}" ht="30" customHeight="1">{"".join(cells)}</row>')
    auto = f'A1:{col_name(max_cols)}{len(rows)}'
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews><sheetFormatPr defaultRowHeight="18"/><cols>{cols}</cols><sheetData>{"".join(xml_rows)}</sheetData><autoFilter ref="{auto}"/><pageMargins left="0.25" right="0.25" top="0.5" bottom="0.5" header="0.2" footer="0.2"/></worksheet>'''

def build(path, sheets):
    path.parent.mkdir(parents=True, exist_ok=True)
    names = list(sheets)
    content_overrides = [
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>',
    ] + [f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(1, len(names)+1)]
    types = '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">' + ''.join(content_overrides) + '</Types>'
    root_rels = '''<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>'''
    wb_sheets = ''.join(f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>' for i, name in enumerate(names, 1))
    workbook = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>{wb_sheets}</sheets></workbook>'''
    wb_rels_items = [f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>' for i in range(1, len(names)+1)]
    wb_rels_items.append(f'<Relationship Id="rId{len(names)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>')
    wb_rels = '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + ''.join(wb_rels_items) + '</Relationships>'
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="3"><font><sz val="11"/><name val="Aptos"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Aptos"/></font><font><b/><color rgb="FF17365D"/><sz val="11"/><name val="Aptos"/></font></fonts><fills count="4"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF17365D"/><bgColor indexed="64"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFD9EAF7"/><bgColor indexed="64"/></patternFill></fill></fills><borders count="2"><border/><border><left style="thin"><color rgb="FFD0D7DE"/></left><right style="thin"><color rgb="FFD0D7DE"/></right><top style="thin"><color rgb="FFD0D7DE"/></top><bottom style="thin"><color rgb="FFD0D7DE"/></bottom></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="4"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="center"/></xf><xf numFmtId="0" fontId="2" fillId="3" borderId="1" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf><xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf></cellXfs></styleSheet>'''
    with ZipFile(path, "w", ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", root_rels)
        z.writestr("xl/workbook.xml", workbook)
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        z.writestr("xl/styles.xml", styles)
        for i, name in enumerate(names, 1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", worksheet_xml(sheets[name]))

build(ROOT / "v1" / "dashboard_hanh_dong_v1.xlsx", V1)
build(ROOT / "dashboard" / "dashboard_hanh_dong_v2.xlsx", V2)
print("Created both dashboard workbooks")
