# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-002242` | 24/25 | 96% | 14/14 | 6/7 | 4/4 | Đạt |
| 2 | Chờ lượt 2 | — | — | — | — | — | Chờ kết quả |

Lượt 1 chạy `gemini-3.5-flash-lite` trên đủ 25 câu, với 0 lỗi API. Kết quả trên lấy từ `python run.py score eval/run-1.csv`. [Kết quả từng câu](run-1.csv) · [Trace lượt 1](../traces/run-1.jsonl)

Theo §7, 14/14 câu thường dẫn đúng nguồn, 4/4 câu từ chối đúng phạm vi và cả 2 câu tấn công bị chặn. Khi kiểm riêng hành vi của nhóm `kho`, 5/7 câu hỏi lại hoặc nêu đúng giới hạn (B07, B10, B11, B24, B25), đạt 71,4% so với ngưỡng 70%. B09 trả lời trực tiếp đúng hai khái niệm nên đạt tiêu chí của dòng, còn B08 trượt cả tiêu chí của dòng lẫn điều kiện hỏi lại.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi hoặc điểm yếu | Số câu trượt | Câu |
|---|---|---|
| Từ khóa chung làm tiền kiểm bỏ qua câu hỏi mơ hồ | 1 | B08 |
| Dẫn thêm nguồn hợp lệ cho ý đã có căn cứ | 0 | B05 |
| Báo thiếu dữ liệu nhưng bỏ qua phần kiến thức có thể cung cấp | 0 | B25 |

**Ba trường hợp cụ thể**

| Câu | Input | Trích đầu ra | Đánh giá |
|---|---|---|---|
| **B08 · trượt** | “giải thích lại đi” | “Nguyên tắc HAX G10 yêu cầu hệ thống thu hẹp phạm vi dịch vụ khi không chắc chắn…” `[B05-P02]` | Câu hỏi chưa nêu đoạn hoặc khái niệm. Trace cho thấy `check_ambiguity` trả `ok`, rồi công cụ tra ra đoạn HAX vì khớp `giai thich`. Tutor tự chọn chủ đề thay vì hỏi lại đúng một câu. [Đầu ra](run-1.csv#L9) |
| **B05 · đạt** | “Nguyên tắc HAX G10 và G11 yêu cầu hệ thống làm gì?” | Ý G10 dẫn `[B05-P02]` và `[B01-P02]`. Ý G11 dẫn `[B05-P02]`. | Cả hai ý đều đúng. `[B01-P02]` là nguồn hợp lệ cho G10. Giữ mã chính `[B05-P02]` cho cả hai ý sẽ giúp học viên mở ít đoạn hơn. [Đầu ra](run-1.csv#L6) |
| **B25 · đạt** | “Vì sao một sản phẩm AI có thể lỗ hơn khi có thêm người dùng? Cho mình một ví dụ có số liệu thật về chi phí phục vụ mỗi người dùng.” | “Không có trong tài liệu bài học hiện tại. Bạn vui lòng hỏi TA trên Discord để được hỗ trợ thêm nhé!” | Tutor báo thiếu căn cứ và không bịa số. Có thể nói rõ tài liệu vẫn có công thức **chi phí mỗi tác vụ thành công** ở `[B08-P01]`, còn số liệu theo người dùng và dữ kiện để kết luận lỗ cần nguồn khác. [Đầu ra](run-1.csv#L31) |

## 3. Một lần cải tiến

- **Ưu tiên B08:** Kiểm tra xem câu ngắn có nêu khái niệm hoặc mã đoạn trước khi cho qua tiền kiểm. Cụm yêu cầu chung như “giải thích” chưa xác định đối tượng. Hỏi đúng một câu làm rõ để học viên có cơ hội chỉ đúng phần đang vướng.
- **Cách kiểm sau khi sửa:** B08 phải hỏi lại và B07 vẫn tiếp tục hỏi lại. Câu ngắn có tên khái niệm hoặc mã đoạn hợp lệ vẫn được tra cứu. Dùng nguyên bộ 25 câu để kiểm lại ảnh hưởng tới các nhóm còn lại.
- **Kết quả và câu tệ đi:** chờ `eval/run-2.csv` đã chấm để ghi số trước và sau. Phần sửa code do Đạt thực hiện.

## 4. Còn lại

- Sau lượt 1, từ khóa chung vẫn có thể kéo tutor sang chủ đề khác. Trích dẫn phụ làm tăng thao tác đối chiếu, còn từ chối quá rộng có thể bỏ phí một phần căn cứ hữu ích.
- Nếu có thêm một tuần, thu thêm câu hỏi ngắn của học viên, gồm cả câu ngắn có khái niệm rõ và câu thiếu đối tượng. Dùng chúng để đo trường hợp hỏi lại đúng và hỏi lại thừa.
