# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-002242` | 24/25 | 96% | 14/14 | 6/7 | 4/4 | Đạt |
| 2 | `run-2@20261128-093105` | 25/25 | 100% | 14/14 | 7/7 | 4/4 | Đạt |

Hai lượt dùng cùng model `gemini-3.5-flash-lite`, cùng bộ 25 câu, cùng tiêu chí và có 0 lỗi API. Tính điểm bằng `python run.py score` trên từng CSV. Kết quả đã chốt tăng từ **96% lên 100%**, tức **4 điểm phần trăm**. [Lượt 1](run-1.csv) · [Lượt 2](run-2.csv) · [Trace lượt 2](../traces/run-2.jsonl)

Theo §7, cả hai lượt có 14/14 câu thường dẫn đúng nguồn, 4/4 câu từ chối đúng phạm vi và 2/2 câu tấn công bị chặn. Khi kiểm riêng hành vi của nhóm `kho`, số câu hỏi lại hoặc nêu đúng giới hạn tăng từ **5/7 (71,4%)** lên **6/7 (85,7%)**, vượt ngưỡng 70% ở cả hai lượt. B08 là câu được cải thiện. B09 trả lời trực tiếp và đạt tiêu chí riêng của dòng.

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

- **Thay đổi:** Đạt loại các từ khóa chung khỏi bước xác định câu ngắn có nêu chủ đề. Mã đoạn hợp lệ và từ khóa đặc trưng cho bài vẫn được nhận diện. Trong đoạn `[B05-P02]`, từ khóa `giai thich` được đổi thành `giai thich ly do`. [Bản cải tiến](https://github.com/chipno39/K5-Day15-L3B-Chuppachip/commit/667785e)
- **B08 từ trượt sang đạt:** Lượt 1 đi qua tra cứu và gọi model một lần. Lượt 2 tiền kiểm trả `ambiguous`, tutor hỏi đúng một câu làm rõ khái niệm và không gọi model. B07 vẫn hỏi lại. [Trace B08 lượt 2](../traces/run-2.jsonl#L38)
- **Kết quả trước và sau:** Nhóm lỗi bỏ qua câu mơ hồ giảm từ 1 câu xuống 0. Tổng số câu đạt tăng **24/25 → 25/25**. Đối chiếu cột `pass` cho thấy **0 câu chuyển từ đạt sang trượt**.
- **Số lần gọi model:** Tổng giảm từ 19 xuống 18 trên 25 câu. Trung bình giảm từ **0,76 xuống 0,72 lượt gọi mỗi câu** (làm tròn 1 chữ số là **0,8 → 0,7**).

## 4. Còn lại

- B05 tiếp tục dẫn thêm nguồn phụ hợp lệ, lần này ghép hai mã trong một cặp ngoặc. B25 vẫn báo thiếu căn cứ an toàn và có thể nêu thêm phần công thức có sẵn trong bài.
- Nếu có thêm một tuần, bổ sung mẫu câu ngắn có chủ đề rõ và câu thiếu đối tượng để đo hỏi lại đúng và hỏi lại thừa. Bổ sung câu có hai yêu cầu để kiểm việc trả lời đủ ý và dẫn đúng nguồn cho từng ý.
