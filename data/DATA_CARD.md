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
| Dùng để làm gì | Nguồn tri thức cho `search_lesson` và `get_passage`, đồng thời dùng để đối chiếu mã đoạn trong benchmark |
| Từ đâu | 12 đoạn mẫu do nhóm viết lại từ các khái niệm của khoá và 3 đoạn văn bản mẫu Bài 07 do Phạm Văn Chiêu cung cấp |
| Xử lý những bước gì | Chuẩn hoá JSON gồm `code`, `lesson`, `title`, `keywords`, `text`. Giữ nguyên nội dung ba đoạn Bài 07 và thêm từ khóa tra cứu. Đã kiểm tra bằng các câu B16–B18 |
| Số dòng / số đoạn | **15 đoạn** dùng dạng `Bxx-Pxx`. `B01` dành cho Bài 07, `B02`–`B08` dành cho 7 bài mẫu còn lại. Số trong mã là số thứ tự trong kho, độc lập với ngày học |
| Phiên bản / ngày lấy | v1.1 · bổ sung Bài 07 ngày 27/11/2026 · soạn thủ công, không dùng seed |
| Nhãn | **`synthetic`** (chỉ dùng chạy thử và đánh giá kỹ thuật, **không phải** bằng chứng pain) |
| Giới hạn | Kho chỉ bao phủ nội dung trong 15 đoạn. Ba đoạn Bài 07 chưa có mốc thời gian video để đối chiếu |
