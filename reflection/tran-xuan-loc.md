# Reflection — Trần Xuân Lộc

## 1. Vai trò và phần việc

- Mình phụ trách [tra cứu bài học](../codebase/tools.py) và [bộ câu thử](../eval/benchmark.csv), bổ sung tra theo mã đoạn `Bxx-Pxx` và mở rộng từ 18 lên 25 câu.
- Mình phỏng vấn một học viên ngoài nhóm và ghi [biên bản ẩn danh P3](../evidence/interviews/P3.md). Bộ câu thử cuối cùng có 11 câu từ học viên.
- Mình dựng [giao diện demo](../codebase/web/index.html) để học viên bấm mã trích dẫn và mở đúng đoạn nguồn.
- Mình đối chiếu điểm B01–B05 với Đạt, khớp 5/5, rồi viết [báo cáo so sánh hai lượt](../eval/report.md).

## 2. AI hỗ trợ thế nào

- Mình dùng Codex để hỗ trợ viết code tra cứu và giao diện, soạn nháp câu thử, rà mã đoạn và chuẩn bị báo cáo đánh giá.
- Khi rà nguồn câu hỏi, mình xác nhận lại 11 câu với các nguồn ẩn danh S01–S06 và P3. Log BTC chỉ lưu thông tin như độ dài câu hỏi và mã bài nên không xác nhận được câu chữ.
- Codex giúp soạn biên bản từ ghi chép mình cung cấp. Câu trả lời số 5 của P3 được rút gọn và ghi rõ là tóm tắt. Điểm chấm chéo trong báo cáo do mình và Đạt đối chiếu.

## 3. Một câu thử trượt và điều học được

- B08 là câu “giải thích lại đi”. Ở lượt 1, tutor tự trả lời về HAX G10 và G11 vì cụm “giải thích” khớp từ khóa của đoạn `[B05-P02]`.
- Đạt lọc các từ khóa quá chung ở bước nhận diện câu mơ hồ. Lượt 2, tutor hỏi đúng một câu để biết học viên muốn giải thích phần nào. B08 chuyển sang đạt và số câu đạt tăng từ 24/25 lên 25/25.
- Mình rút ra rằng từ chỉ hành động như “giải thích” chưa nói lên chủ đề. Khi kiểm thử cách nhận diện câu mơ hồ, cần có cả câu ngắn đủ ngữ cảnh lẫn câu ngắn thiếu đối tượng để kiểm xem tutor hỏi lại đúng lúc.
