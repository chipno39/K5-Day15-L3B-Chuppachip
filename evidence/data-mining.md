# Đào data — cách đếm và kết quả

> Script tái lập: `evidence/count.py` (chạy trên thư mục `data/preclass/` do BTC cấp, không commit nguyên file data vào repo).

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** `data/preclass/chat.csv` (1.260 dòng) và `data/preclass/answers.csv` (3.776 dòng), nhật ký hành vi thật đã ẩn danh trên trang pre-class từ **05/11/2026 đến 25/11/2026** (Day01 → Day13).
- **Đếm gì · trên tập nào · lọc gì:**
  1. Tỉ lệ lượt chat hỏi dưới video (`channel == "video_question"`) và do trợ giảng AI trả lời (`agent_id == "teaching_assistant"`).
  2. Tỉ lệ lượt chat vào khung giờ tối muộn (**20:00–02:00 giờ VN = UTC + 7**), khi không có TA trực.
  3. Tỉ lệ câu hỏi rất ngắn/mơ hồ (`do_dai_cau_hoi <= 20` ký tự) và độ dài phản hồi trung vị của trợ giảng.
  4. Tỉ lệ lượt chat đã chấm (`nguon == "chat"` & `trang_thai_cham == "da_cham"`) có `rubric_bam_bai == 0` (không bám bài) hoặc `rubric_dung_ngu_canh == 0`, kèm độ dài phản hồi trung vị.
  5. Tỉ lệ lượt hỏi nối tiếp trong ≤3 phút trên cùng một video của cùng một học viên (`hv` trùng, `transcript` trùng, `Δt ≤ 180s`).
  6. Tỉ lệ làm sai ngay lần đầu (`lan_thu == 1`, `was_correct == False`) ở câu hỏi kiểm tra hiểu bài (`nguon == "pre_post_post"`).
- **Mẫu số là gì:**
  - Chỉ số 1, 2, 3, 5: tổng lượt chat `N = 1.260` (từ 145 học viên có nhắn chat trong 436 học viên có hoạt động).
  - Chỉ số 4: tổng lượt chat đã được chấm rubric `N = 1.223` (loại 24 dòng `bo_qua` và 13 dòng `chua_cham`).
  - Chỉ số 6: tổng lượt trả lời `pre_post_post` lần đầu có nhãn đúng/sai `N = 1.968`.
- **Script tái lập:** `evidence/count.py` — chạy `python evidence/count.py "<đường-dẫn-tới-data/preclass>"`.

## 2. Đọc trước, đếm sau

Đã đọc 30 dòng đầu của `chat.csv`, `answers.csv` và toàn bộ `data/preclass/README.md`. Các *kiểu* hành vi thấy được trước khi đếm:
- Phần lớn lượt nhắn tập trung ở kênh `video_question` hỏi `teaching_assistant`, nhiều lượt diễn ra vào khung 20h–02h giờ VN.
- Nhiều câu hỏi rất ngắn (9–19 ký tự) hoặc bị chấm `rubric_bam_bai = 0`, nhưng trợ giảng AI vẫn trả lời đoạn rất dài (300–600 ký tự).
- Nhiều học viên nhắn liên tiếp nhiều lượt trong vòng 1–3 phút trên cùng một video.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| Lượt chat là hỏi dưới video (`video_question`) | 1.108 / 1.260 | 87,9% | 145/436 học viên hoạt động đã dùng chat |
| Lượt chat do `teaching_assistant` xử lý | 1.153 / 1.260 | 91,5% | Kênh chính học viên dựa vào khi tự học |
| Lượt chat diễn ra lúc tối muộn (20:00–02:00 VN) | 429 / 1.260 | 34,0% | Khung giờ không có TA trực giải đáp |
| Câu hỏi ngắn/mơ hồ (`≤ 20` ký tự) | 216 / 1.260 | 17,1% | Trung vị câu trả lời vẫn dài **231 ký tự** |
| Lượt chat bị chấm không bám bài (`rubric_bam_bai = 0`) | 261 / 1.223 | 21,3% | Trung vị câu trả lời vẫn dài **329 ký tự** |
| Lượt chat bị chấm lệch ngữ cảnh (`rubric_dung_ngu_canh = 0`) | 264 / 1.223 | 21,6% | Khớp sát tỉ lệ không bám bài |
| Lượt hỏi nối tiếp trong ≤3 phút trên cùng video | 598 / 1.260 | 47,5% | Tín hiệu học viên phải hỏi đi hỏi lại ngay tại chỗ |
| Câu hỏi kiểm tra (`pre_post_post`) sai ngay lần đầu | 399 / 1.968 | 20,3% | 1/5 lượt kiểm tra hiểu bài bị sai lần 1 |

## 4. ≥5 ví dụ cụ thể (mã đã ẩn danh, không đoán ai là ai)

1. `chat=C00485` (`ans=A02662`, `hv=L0638`, `Day01/d01-r1-v01.txt`, **23h VN**): câu hỏi chỉ **15 ký tự**, chấm `rubric_bam_bai=0`, `rubric_dung_ngu_canh=0`, nhưng trợ giảng trả lời dài **420 ký tự**.
2. `chat=C00542` (`ans=A01213`, `hv=L0342`, `Day01/d01-r1-v05.txt`, **09h VN**): câu hỏi chỉ **19 ký tự**, chấm `rubric_bam_bai=0`, `rubric_dung_ngu_canh=0`, trợ giảng trả lời **318 ký tự**.
3. `chat=C00434` (`ans=A01007`, `hv=L0418`, `Day04/d04-r3-v06.txt`, **23h VN**): câu hỏi chỉ **9 ký tự**, chấm `rubric_bam_bai=0`, trợ giảng vẫn trả lời **440 ký tự**.
4. `chat=C00438` (`ans=A00628`, `hv=L0031`, `Day01/d01-r1-v02.txt`, **23h VN**): câu hỏi dài 91 ký tự lúc đêm muộn, chấm `rubric_bam_bai=0`, `rubric_dung_ngu_canh=0`, trợ giảng trả lời **523 ký tự**.
5. `chat=C00731` (`ans=A01395`, `hv=L0303`, `Day01/d01-r1-v02.txt`, **23h VN**): câu hỏi 110 ký tự lúc 23h, chấm `rubric_bam_bai=0`, `rubric_dung_ngu_canh=0`, trợ giảng trả lời **627 ký tự**.
6. `chat=C00878` (`ans=A01070`, `hv=L0430`, `Day03/d03-r2-v02.txt`, **23h VN**): câu hỏi 93 ký tự lúc 23h, chấm `rubric_bam_bai=0`, `rubric_dung_ngu_canh=0`, trợ giảng trả lời **599 ký tự**.

## 5. Giới hạn của data

- `data/preclass/` đã ẩn danh toàn bộ nội dung chữ học viên gõ (chỉ còn độ dài và điểm rubric), nên **cho biết học viên làm gì nhưng không cho biết vì sao** (họ hỏi ngắn vì mơ hồ hay vì gõ vội; họ hỏi nối tiếp 47,5% vì câu trả lời chưa có mã đoạn căn cứ hay vì muốn đào sâu).
- Dữ liệu chỉ phản ánh 145/436 học viên có dùng khung chat trong giai đoạn 05/11–25/11/2026.
- **→ Kiểm lại bằng:** Phỏng vấn trực tiếp **≥3 học viên L3 ngoài nhóm** (hỏi chuyện thật trong 1 tháng qua khi dùng trợ giảng pre-class) vào `evidence/interviews/P1.md`, `P2.md`, `P3.md` để xác nhận nguyên nhân và lấy ≥5 trích dẫn nguyên văn trước CP3.
