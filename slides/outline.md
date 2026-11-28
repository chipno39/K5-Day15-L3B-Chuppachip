# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Định dạng nào cũng được (PDF, PPTX, HTML…); hoặc nộp link slide (Drive, Canva, Google Slides…) ở form CP4, để ai có link cũng xem được.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ☑ |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☑ |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☑ |
| 4 | Demo live | 1 trường hợp thường + 1 trường hợp khó (lấy từ bộ câu thử); mạng hỏng → video dự phòng | `eval/benchmark.csv` | ☑ |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ☑ |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☑ |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ☑ |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☑ |

- **File slide chính thức trong repo:** [demo-slides.pdf](file:///e:/Vinuni/K5-Day15-L3B-Chuppachip/demo-slides.pdf) (nằm ở thư mục gốc repo).
- **Thư mục Video Demo & Slide dự phòng (Google Drive):** [Google Drive Folder](https://drive.google.com/drive/folders/15K2J5MsfUC9AZHLjgaSxlLuV7l08G172?usp=sharing)
  - Video demo CP3: `Video-democp3.mp4`
  - Video demo dự phòng CP4 (1,5–2 phút): `Vid-duphong.mp4` (mở được bằng Tab Ẩn Danh)

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần):

| Trang | Người nói |
|---|---|
| Trang 1–2 (Người dùng, Pain & Impact) | **Đinh Hoàng Phong** |
| Trang 3–4 (Giải pháp kiến trúc & Demo live) | **Nguyễn Xuân Đạt** |
| Trang 5 (Đánh giá & Vòng cải tiến lượt 1 → 2) | **Trần Xuân Lộc** |
| Trang 6–8 (Chi phí mô phỏng, Kết luận Go & Hướng 1 tuần tới) | **Phạm Văn Chiêu** |
