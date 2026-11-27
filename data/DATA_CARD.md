# Data card — dữ liệu bản chạy thử dùng

> Bản đầu cho CP2 (cập nhật bổ sung ở CP3 nếu mở rộng số đoạn bài học). Không commit nguyên file data BTC cấp hay nguyên tài liệu khoá vào repo.

## Dataset 1 · Nhật ký hành vi pre-class (`data/preclass/`)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain (`evidence/data-mining.md`), tính thừa số Impact (`spec.md` §2), xác định tần suất dùng cho persona (`cost/personas.yaml`) |
| Từ đâu | Data BTC cấp trong repo đề (`K5-L3-Day15-AI-Product-Hackathon/data/preclass/`), gồm `chat.csv` và `answers.csv` |
| Xử lý những bước gì | Không sửa dữ liệu gốc; lọc theo `channel`, `agent_id`, múi giờ VN (UTC+7), độ dài câu hỏi `<=20`, trạng thái chấm `da_cham` và `lan_thu == 1` bằng script tái lập `evidence/count.py` |
| Số dòng / số đoạn | `chat.csv`: 1.260 dòng (145 học viên) · `answers.csv`: 3.776 dòng (173 học viên) · 436 học viên hoạt động / 721 tài khoản |
| Phiên bản / ngày lấy | 05/11/2026 → 25/11/2026 (Day01 → Day13), lấy ngày 27/11/2026 |
| Nhãn | **thật** (đã ẩn danh hoàn toàn bởi BTC) |
| Giới hạn | Không chứa nội dung chữ học viên viết (chỉ có độ dài và điểm rubric) nên không biết *vì sao* học viên hỏi ngắn hoặc hỏi nối tiếp → kiểm chéo bằng phỏng vấn ≥3 học viên ngoài nhóm |

## Dataset 2 · Kho đoạn bài học mẫu có mã đoạn (`data/lessons.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn tri thức chỉ đọc cho công cụ `search_lesson` và `get_passage` trong `codebase/tools.py`; làm chuẩn đối chiếu mã đoạn `[Dxx-Pxx]` cho `eval/benchmark.csv` |
| Từ đâu | **Nhóm tự viết lại (`synthetic`)** bản tóm tắt ngắn các khái niệm cốt lõi phổ quát của khoá (Day01, Day02, Day03, Day05, Day09, Day11, Day13) — không chép nguyên văn slide/transcript khoá học |
| Xử lý những bước gì | Chuẩn hoá cấu trúc JSON gồm `code`, `lesson`, `title`, `keywords`, `text`; kiểm tay từng đoạn bởi Nguyễn Xuân Đạt & Trần Xuân Lộc |
| Số dòng / số đoạn | **12 đoạn** (`D01-P01` đến `D13-P01`), độ dài 2–3 câu/đoạn |
| Phiên bản / ngày lấy | v1.0 · tạo ngày 27/11/2026 (seed: viết tay có cấu trúc, không dùng sinh ngẫu nhiên) |
| Nhãn | **`synthetic`** (chỉ dùng chạy thử và đánh giá kỹ thuật, **không phải** bằng chứng pain) |
| Giới hạn | Mới phủ 12 khái niệm chính của 7 ngày học; các câu hỏi thuộc ngày khác hoặc ngoài 12 đoạn này phải được hệ thống trả về "không có trong bài" |
