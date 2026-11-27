# Kế hoạch tăng tốc hoàn thiện CP3 trong tối nay (27/11 · 19:15 → 22:30)

> **Mục tiêu:** Chốt trọn 100% yêu cầu **CP3 (hạn 10:00 sáng Thứ Bảy 28/11 · 4 điểm)** ngay trong tối nay để sáng mai chỉ cần rà lại, cập nhật thêm khảo sát (nếu tăng thêm người) và tập trung dốc toàn lực cho **CP4 (14:30) & Demo**.
>
> **2 LUẬT SẮT SAU 19:30 (KHÔNG ĐƯỢC VI PHẠM):**
> 1. **KHÔNG sửa** chuẩn "đạt" ở `spec.md` §7 và `eval/metric_spec.yaml`.
> 2. **KHÔNG commit `.env` hoặc API key** (trừ 10 điểm!). Mọi thay đổi code/prompt/dữ liệu sau 19:30 phải ghi 1 dòng vào bảng Changelog `spec.md` §10.

---

## Tiến độ mốc giờ tối nay (3 tiếng gọn gàng)

| Khung giờ | Mốc cần đạt | Ai phụ trách |
|---|---|---|
| **19:15 – 20:00** | Nối Gemini API chạy thật (`eval --try` token > 0) + mở rộng `benchmark.csv` lên 25 câu + chốt bằng chứng `evidence/` | Cả 4 bạn chạy song song (mỗi người 1 nhánh) |
| **20:00 – 20:30** | Merge các nhánh vào `main` → **Chạy Eval lượt 1** (`eval/run-1.csv`) | Đạt + Lộc |
| **20:30 – 21:15** | Chấm `pass` lượt 1 (`run.py score`) + chạy thử `simulate --try` + **Quay Video 30s AI thật** | Lộc (chấm) · Chiêu (simulate + video) · Đạt (chấm chéo 5 câu) |
| **21:15 – 22:00** | Cập nhật `spec.md` §4 & §7 + `spec.md` §10 changelog + kiểm tra chéo đủ 6 mục CP3 | Cả nhóm soát 15 phút |
| **22:00 – 22:30** | Push sạch lên `main` · Kiểm video bằng Tab Ẩn Danh → **Sẵn sàng nộp CP3** (nộp luôn tối nay hoặc 09:30 sáng mai sau khi chốt khảo sát) | Đạt |

---

## Nhiệm vụ chi tiết từng thành viên tối nay

### 1. Nguyễn Xuân Đạt *(Đội trưởng — nhánh `dat/cp3-gemini`)*
**Mục tiêu:** Nối Gemini API thật, chạy thông `eval --try` → `eval` lượt 1, tổng hợp merge & nộp CP3.

- [ ] **19:15–19:45 — Lấy Gemini API key & nối máy local:**
  1. Lấy API key miễn phí tại Google AI Studio (`aistudio.google.com/apikey`).
  2. Chạy lệnh tạo `.env` ở thư mục gốc repo (tuyệt đối **không** `git add .env`):
     ```powershell
     copy .env.example .env
     ```
  3. Điền đúng 3 dòng vào `.env` (không dấu ngoặc kép):
     ```env
     MODEL_PROVIDER=gemini
     MODEL_NAME=gemini-2.5-flash
     API_KEY=<dán-key-của-bạn-vào-đây>
     ```
     *(Code gọi Gemini đã viết sẵn trong `codebase/ai.py` dùng thư viện chuẩn `urllib`, không cần `pip install`.)*
  4. Chạy thử 1 câu và 3 câu đầu:
     ```powershell
     python run.py
     python run.py eval --try --wait 4
     ```
     → Thấy `"Nối model được"` và `tokens_in > 0`, `tokens_out > 0` là xong!
- [ ] **20:00–20:30 — Chạy Eval lượt 1 (sau khi Lộc merge 25 câu):**
  ```powershell
  git pull origin main
  python run.py check
  python run.py eval --wait 4
  ```
  → Sinh `eval/run-1.csv` + `traces/run-1.jsonl`. Push ngay cho Lộc chấm `pass`.
- [ ] **20:45–21:30 — Chấm chéo 5 câu + cập nhật `spec.md`:**
  - Chấm độc lập 5 câu đầu của `eval/run-1.csv` so với Lộc (mục tiêu khớp ≥4/5, ghi vào `eval/README.md`).
  - Cập nhật kết quả lượt 1 (`x/25`, `%`, `run ID`) vào `spec.md` §7, xoá dòng "model giả" ở `spec.md` §4, ghi changelog vào `spec.md` §10.

---

### 2. Trần Xuân Lộc *(nhánh `loc/cp3-eval-25`)*
**Mục tiêu:** Mở rộng bộ câu thử 18 → **25 câu** đạt sạch 100% `python run.py check`, chấm `eval/run-1.csv`.

- [ ] **19:15–20:00 — Thêm 7 câu thử vào `eval/benchmark.csv` (18 → 25 câu):**
  - Ưu tiên lấy câu hỏi thật từ `evidence/interviews/P1..P4.md` và câu 10 trong `evidence/survey/results.csv` để gắn `source = "nguoi_dung: P1..."` (giúp đạt mạnh chuẩn ≥1/3 câu từ người dùng/data thật).
  - Đảm bảo đủ tỉ lệ: tổng **25 câu**, ≥5 `kho`, ≥2 `tu_choi` (đã có 4), không đổi mã `[Bxx-Pxx]` đang dùng, không sửa `eval/metric_spec.yaml`.
  - Chạy `python run.py check` → **0 cảnh báo** → tạo PR merge vào `main` trước 20:00.
- [ ] **20:30–21:15 — Chấm cột `pass` (`1`/`0`) cho `eval/run-1.csv`:**
  - Chấm trung thực 100% theo 4 metric trong `eval/metric_spec.yaml` (kết quả thấp mà trung thực vẫn đủ điểm, tuyệt đối không sửa output hay xoá câu trượt).
  - Chạy `python run.py score eval/run-1.csv` lấy % đạt tổng và theo từng `type`.
  - Ghi nhận ≥3 lỗi tiêu biểu (nháp cho `eval/report.md` CP4) → push lên `main`.

---

### 3. Đinh Hoàng Phong *(nhánh `phong/cp3-evidence`)*
**Mục tiêu:** Hoàn thiện bằng chứng pain đạt chuẩn 14/14 điểm R1 trong `evidence/summary.md` và cập nhật `spec.md` §2.

- [ ] **19:15–20:30 — Soát & hoàn thiện `evidence/summary.md`:**
  - Kiểm lại 4 file phỏng vấn `P1.md–P4.md` đảm bảo **không có tên thật / SĐT / email / mã HV**.
  - Kiểm `evidence/summary.md` có đủ:
    1. Số chính từ đào data (`evidence/count.py`, `1.260` lượt chat) + số từ 4 phỏng vấn (`x/4 người`, không ghi % cho n=4) + số khảo sát hiện tại (`n=...`).
    2. **≥5 trích dẫn / ví dụ nguyên văn** đã bỏ tên, có nguồn rõ (`P1`, `P2`, `P3`, `P4`, `C00485`...).
    3. Kết luận rõ ràng: giả thuyết ban đầu đúng chỗ nào, lệch chỗ nào (như trường hợp P4 học sớm 20h chỉ mất 2 phút).
  - Cập nhật lại thừa số *"số phút / lần"* trong bảng Impact `spec.md` §2 bằng con số thật từ phỏng vấn/khảo sát (ghi rõ nguồn).
  - *(Sáng mai 09:00 trước CP3: nếu khảo sát tăng thêm nhiều người thì xuất lại `results.csv` — nhớ **xoá cột câu 11 tên Discord** — và cập nhật số `n` mới vào `summary.md`.)*

---

### 4. Phạm Văn Chiêu *(nhánh `chieu/cp3-video-cost`)*
**Mục tiêu:** Quay **Video 30 giây AI thật** (điều kiện bắt buộc CP3) + chạy thử `simulate --try` (10 phiên).

- [ ] **19:15–20:30 — Rà `cost/personas.yaml` & chuẩn bị kịch bản quay video 30s:**
  - Kiểm `cost/personas.yaml` có đủ ≥3 persona (tần suất lấy từ `data/preclass/` & phỏng vấn), giá ≥2 model trả phí có **link + ngày xem** (khớp `further-reading/model-prices.md`, trong đó có đúng tên model Gemini đang chạy ở `.env`).
  - Chuẩn bị sẵn 2 câu mẫu để gõ khi quay: 1 câu `thuong` (ra mã đoạn `[Bxx-Pxx]` + token > 0) và 1 câu `kho`/`tu_choi` (hỏi lại hoặc từ chối).
- [ ] **20:30–21:15 — Quay Video 30s & chạy `simulate --try`:**
  - Chạy `python run.py` (trên máy đã có `.env` Gemini thật — quay cùng Đạt hoặc tự gắn key local): quay màn hình rõ **30 giây** thao tác gõ câu hỏi thật → AI trả lời thật kèm dòng `(model: gemini-... · token vào ... / ra ...)`. **Tuyệt đối không để lộ file `.env` hay API key trong khung hình!**
  - Đăng lên YouTube chế độ **"Không công khai" (Unlisted)** hoặc Google Drive **"Bất kỳ ai có đường liên kết"** → **mở thử bằng Tab Ẩn Danh** để chắc chắn xem được.
  - Chạy `python run.py simulate --try --wait 4` → kiểm ra `cost/simulate-try.csv` không lỗi → push lên `main`.

---

## Checklist tự soát trước khi bấm Nộp CP3 (trước 10:00 Thứ Bảy 28/11)

- [ ] `evidence/summary.md`: đạt ngưỡng ≥1 nguồn + ≥5 trích dẫn nguyên văn, bỏ tên.
- [ ] `eval/benchmark.csv`: **20–30 câu**, ≥5 `kho`, ≥2 `tu_choi` (gồm 2 tấn công), ≥1/3 từ người dùng/data thật → `python run.py check` **0 cảnh báo**.
- [ ] **Video 30 giây** bản chạy thử gọi AI thật — mở được bằng Tab Ẩn Danh.
- [ ] `eval/run-1.csv` đã chấm `pass`, `python run.py score eval/run-1.csv` ra `x/N` câu đạt + `run ID`.
- [ ] `spec.md` đủ §0–§7 (chuẩn "đạt" §7 giữ nguyên từ CP2), có changelog §10.
- [ ] Kiểm `git status` & trên GitHub: **KHÔNG có `.env`**, không có API key, không có tên thật người phỏng vấn/khảo sát.
