# Phân công chi tiết — Nhóm Chuppachip (L3B · Track A1)

> **Kế hoạch chặng cuối CP4, Demo & Khoá bài (28/11 · 09:30 → 23:59):** xem chi tiết từng giờ tại [docs/cp4-final-plan.md](cp4-final-plan.md).
> **Kế hoạch tăng tốc CP3 (đã hoàn thành):** [docs/cp3-sprint-tonight.md](cp3-sprint-tonight.md).
> **Nguyên tắc bắt buộc:** Ai mang tên phần nào phải tự kiểm, tự thực hiện phần người thật và **giải thích được khi giám khảo hỏi** (không giải thích được → 0 điểm phần đó). Cả nhóm họp chốt 15 phút trước mỗi checkpoint để thống nhất mạch **Pain → Impact → Giải pháp → Đánh giá → Chi phí**.

---

## 1. Nguyễn Xuân Đạt *(Đội trưởng — `2A202603958`)*
**Phụ trách:** Điều phối chung, Kiến trúc giải pháp AI (`spec.md` §4) & Codebase (`codebase/agent.py`, `codebase/ai.py`)

- **Chặng CP2 (trước 19:30 Thứ Sáu 27/11):**
  - Rà soát sơ đồ workflow 4 bước ở `spec.md` §4 và luồng xử lý trong `codebase/agent.py`.
  - Quản lý Git (kéo phần làm của cả nhóm), chạy `python run.py` + `python run.py check`, nộp Form CP2.
- **Chặng CP3 (tối 27/11 → 10:00 Thứ Bảy 28/11):**
  - Tạo file `.env` trên máy (tuyệt đối không commit), nối model API thật trong `codebase/ai.py`.
  - Chạy `python run.py eval --try` (xác nhận token > 0) rồi chạy lượt 1 `python run.py eval` → `eval/run-1.csv`.
- **Chặng CP4 & Hạn chót (14:30 & 23:59 Thứ Bảy 28/11):**
  - Cùng Lộc phân tích lỗi lượt 1, thực hiện **1 lần cải tiến** cho lượt 2 (`eval/run-2.csv`), ghi changelog vào `spec.md` §10.
  - Chuẩn bị phần demo trực tiếp (1 câu thường + 1 câu khó + sẵn sàng chạy câu lạ giám khảo đưa).
  - Viết `reflection/nguyen-xuan-dat.md`.

---

## 2. Đinh Hoàng Phong *(Thành viên — `2A202604090`)*
**Phụ trách:** Bằng chứng Pain (`evidence/`) & Impact (`spec.md` §1–§2)

- **Chặng CP2 (trước 19:30 Thứ Sáu 27/11):**
  - Tự chạy lại `evidence/count.py` và đọc kỹ `evidence/data-mining.md` để nắm chắc từng con số, mẫu số và 6 ví dụ ẩn danh.
  - **Phỏng vấn trực tiếp 2 bạn học viên ngoài nhóm** (Mom Test, 10 phút/người, hỏi chuyện thật trong 1 tháng qua khi học pre-class buổi tối) → ghi vào `evidence/interviews/P1.md` và `evidence/interviews/P2.md` (bỏ tên, giữ trích dẫn nguyên văn).
- **Chặng CP3 (tối 27/11 → 10:00 Thứ Bảy 28/11):**
  - Tổng hợp kết quả đào data + phỏng vấn (≥3 người, **≥5 trích dẫn nguyên văn**) vào `evidence/summary.md` (xong trước CP3).
  - Cập nhật số phút trung vị thật từ phỏng vấn vào bảng Impact (`spec.md` §2).
- **Chặng CP4 & Hạn chót:**
  - Soát phần Pain & Impact trên slide (trang 1–3) đảm bảo mọi số liệu đều truy được về file.
  - Viết `reflection/dinh-hoang-phong.md`.

---

## 3. Trần Xuân Lộc *(Thành viên — `2A202603951`)*
**Phụ trách:** Công cụ tra cứu (`codebase/tools.py`) & Bộ đánh giá (`eval/`)

- **Chặng CP2 (trước 19:30 Thứ Sáu 27/11):**
  - Đọc soát `codebase/tools.py`, `eval/benchmark.csv` (15 câu) và `eval/metric_spec.yaml` (4 metric) — cùng cả nhóm chốt ngưỡng chuẩn "đạt" ở `spec.md` §7 trước 19:30.
  - Phỏng vấn 1 bạn học viên ngoài nhóm → ghi vào `evidence/interviews/P3.md` (đủ chuẩn ≥3 người).
- **Chặng CP3 (tối 27/11 → 10:00 Thứ Bảy 28/11):**
  - Mở rộng `eval/benchmark.csv` từ 15 → **25 câu** (bổ sung câu lấy từ lời phỏng vấn thật `nguoi_dung: P1..P3`, đảm bảo ≥5 `kho`, ≥2 `tu_choi` gồm 2 tấn công, ≥1/3 từ người dùng/data thật).
  - Chạy `python run.py check` sạch lỗi trước khi chạy lượt 1.
- **Chặng CP4 & Hạn chót:**
  - Chấm cột `pass` (1/0) cho `eval/run-1.csv` và `eval/run-2.csv`, chạy `python run.py score`.
  - **Chấm chéo 5 output** với Đạt (khớp ≥4/5), ghi kết quả vào `eval/README.md`.
  - Viết `eval/report.md` (≥3 lỗi cụ thể gom thành nhóm có tên, báo % lượt 1 → lượt 2).
  - Viết `reflection/tran-xuan-loc.md`.

---

## 4. Phạm Văn Chiêu *(Thành viên — `2A202604033`)*
**Phụ trách:** Dữ liệu mẫu (`data/`), Mô phỏng chi phí (`cost/`), Slide, Video & Người dùng thử (`validation/`)

- **Chặng CP2 (trước 19:30 Thứ Sáu 27/11):**
  - Kiểm tra và bổ sung nếu cần các đoạn bài học mẫu trong `data/lessons.json` và `data/DATA_CARD.md`.
  - Phỏng vấn thêm 1 bạn học viên ngoài nhóm (`evidence/interviews/P4.md`, dư chuẩn càng chắc) hoặc phụ Phong lọc trích dẫn.
- **Chặng CP3 (tối 27/11 → 10:00 Thứ Bảy 28/11):**
  - Quay **video 30 giây** bản chạy thử gọi AI thật (đăng YouTube "Không công khai" hoặc Google Drive "Bất kỳ ai có đường liên kết", kiểm mở được bằng tab ẩn danh).
  - Điền bản đầu `cost/personas.yaml` (3 persona + giá ≥2 model trả phí từ `further-reading/model-prices.md`), chạy thử `python run.py simulate --try`.
- **Chặng CP4 & Hạn chót:**
  - Chạy `python run.py simulate --rate-from eval/run-2.csv` (≥50 phiên) → viết `cost/cost-estimate.md` (3 kịch bản thấp/cơ sở/cao + so sánh với impact/người/tháng).
  - Làm **Slide 8 trang** (`slides/outline.md` → `demo-slides.pdf`) + quay **video demo dự phòng**.
  - Tổ chức **2–3 bạn ngoài nhóm dùng thử** theo 5 nhịp, ghi vào `validation/log.md` (**+5 điểm Bonus**).
  - Viết `reflection/pham-van-chieu.md`.

---

## Mốc đồng bộ cả nhóm (bắt buộc)
- **19:00–19:15 Thứ Sáu 27/11:** Cả nhóm đọc lại `canvas.md`, `spec.md` §4 & §7 (chốt cứng chuẩn "đạt") → nộp CP2 trước 19:30.
- **09:00–09:30 Thứ Bảy 28/11:** Chạy lượt 1 cùng nhau, kiểm đủ video 30s & `evidence/summary.md` → nộp CP3 trước 10:00.
- **13:30–14:15 Thứ Bảy 28/11:** Chốt Go/Iterate/Stop, tập demo mỗi người nói 1 phần → nộp CP4 trước 14:30.
- **Trước 23:59 Thứ Bảy 28/11:** Đủ 4 file `reflection/`, cập nhật `docs/ai-usage.md` và `spec.md` §10.
