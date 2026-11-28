# Kế hoạch phân công chi tiết chặng cuối — CP4, Demo & Khoá bài (28/11 · 09:30 → 23:59)

> **Mục tiêu:** Gom trọn **39 điểm còn lại** (CP4 `4đ` · R4 chấm chéo `2đ` · R5 `8đ` · R6 `12đ` · R7 `10đ` · Bonus `+5đ`) để đạt **95–100/100 điểm** và qua đủ **4 điều kiện cứng xét giải** trước **14:30 hôm nay**.
>
> **3 LUẬT SẮT PHẢI GIỮ ĐẾN 23:59:**
> 1. **KHÔNG sửa** chuẩn "đạt" (`spec.md` §7), `eval/metric_spec.yaml`, `eval/benchmark.csv` (đã chạy lượt 1), hoặc output trong `eval/run-*.csv`.
> 2. **KHÔNG commit `.env`**, API key, hay tên thật người dùng thử (`validation/log.md` chỉ ghi vai).
> 3. **Mọi thay đổi sau CP2/CP4** phải có 1 dòng trong bảng Changelog (`spec.md` §10), và **mỗi người bắt buộc nộp 1 file `reflection/<ten-khong-dau>.md`** trước 23:59.

---

## 1. Bảng tiến độ mốc giờ (09:30 → 23:59)

| Khung giờ | Việc phải xong | Đầu ra trên Git | Ai phụ trách |
|---|---|---|---|
| **09:30 – 10:30** | Chấm chéo 5 câu lượt 1 · Sửa lỗi `B08` · **Chạy Eval lượt 2 (`eval/run-2.csv`)** | `eval/run-2.csv`, `traces/run-2.jsonl`, `eval/README.md` | **Đạt** + **Lộc** |
| **10:30 – 11:30** | **Chạy `simulate` ≥50 phiên** · Viết `eval/report.md` · **Mời 2–3 bạn dùng thử** · Dựng khung Slide 8 trang | `cost/simulate-1.csv`, `eval/report.md`, `validation/log.md` | **Đạt** (simulate) · **Lộc** (`report.md`) · **Phong** (dùng thử) · **Chiêu** (Slide) |
| **11:30 – 13:00** | Viết `cost/cost-estimate.md` + `spec.md` §8 · Đổ số vào **Slide 8 trang** · Quay **Video demo dự phòng** · Dọn `README.md` | `cost/cost-estimate.md`, `demo-slides.pdf`, `README.md` | **Chiêu** (`cost` + Slide + Video) · **Phong** (`README.md` + soát số Slide) |
| **13:00 – 14:00** | Chốt kết luận **Go / Iterate / Stop** · Chạy thử repo trên máy sạch · **Tập Demo 2 phút (4 người đều nói)** | `slides/outline.md` (đủ phân công nói) | **Cả 4 bạn** |
| **14:00 – 14:25** | Vào phòng · Merge toàn bộ PR vào `main` · Chạy `python run.py check` · Kiểm Slide & Video bằng Tab Ẩn Danh → **Nộp Form CP4** | Commit sạch trên `main` trước 14:30 | **Đạt** + **Cả nhóm** |
| **14:30 – 18:00** | **Demo Zone (14:30–16:00)** & **Demo Phòng (16:00–18:00)** | Demo trực tiếp + hỏi đáp | **Cả 4 bạn** |
| **18:00 – 23:59** | Sửa góp ý (nếu có) + ghi changelog `spec.md` §10 · **Nộp 4 file `reflection/`** | `reflection/*.md` | **Cả 4 bạn** |

---

## 2. Nhiệm vụ chi tiết từng thành viên (chia nhánh riêng — tránh conflict)

### 1. Nguyễn Xuân Đạt *(Đội trưởng — `2A202603958` · nhánh `dat/cp4-run2-sim`)*
**Trọng tâm:** Cải tiến sửa lỗi lượt 1 → chạy Eval lượt 2 → chạy Simulate ≥50 phiên → duyệt merge & nộp CP4.

- [ ] **09:30 – 10:30 · Vòng cải tiến & Eval lượt 2:**
  1. Thống nhất với Lộc phương án sửa lỗi `B08` (`"giải thích lại đi"` bị khớp nhầm từ khoá chung `"giai thich"` trong `tools.py`/`lessons.json` thay vì kích hoạt HAX G10 hỏi lại 1 câu; có thể tinh chỉnh nhẹ prompt tránh thừa mã phụ ở `B05` — **tuyệt đối không hardcode câu thử**).
  2. Sửa code (`codebase/tools.py` / `agent.py`), chạy lại trọn bộ 25 câu:
     ```powershell
     python run.py eval --wait 4
     ```
     → sinh `eval/run-2.csv` và `traces/run-2.jsonl` (kiểm `lỗi: 0`).
  3. Chấm cột `pass` (`1`/`0`) + `ghi_chu` theo đúng `eval/metric_spec.yaml`, chạy:
     ```powershell
     python run.py score eval/run-2.csv
     ```
  4. Cập nhật kết quả lượt 2 (`x/25`, `%`, `Run ID`) vào `spec.md` §7 và ghi 1 dòng changelog vào `spec.md` §10.
- [ ] **10:30 – 11:30 · Chạy mô phỏng chi phí ≥50 phiên (hỗ trợ Chiêu):**
  1. Chạy lệnh mô phỏng thật qua bản chạy thử đã cải tiến (lấy đúng tỉ lệ đạt từ lượt 2):
     ```powershell
     python run.py simulate --rate-from eval/run-2.csv --wait 4
     ```
     → sinh `cost/simulate-1.csv`, `cost/simulate-1-summary.md`, `traces/simulate-1.jsonl`.
  2. Push nhánh `dat/cp4-run2-sim` và merge vào `main` ngay để Lộc viết `eval/report.md` và Chiêu viết `cost/cost-estimate.md`.
- [ ] **13:00 – 14:25 · Chuẩn bị máy Demo & Nộp CP4:**
  - Test chạy `python codebase/web_app.py` (tại `http://127.0.0.1:8000`) và `python run.py` với `.env` thật trong vòng **1 giờ trước khi lên demo** (kiểm không bị lỗi 429/503).
  - Duyệt & merge sạch mọi PR của Lộc, Phong, Chiêu vào `main` → kiểm `git status` không có `.env` → nộp **Form CP4 trước 14:30**.
- [ ] **Trước 23:59:** Tạo `reflection/nguyen-xuan-dat.md` (3 câu, mỗi câu 3–6 dòng).

---

### 2. Trần Xuân Lộc *(Thành viên — `2A202603951` · nhánh `loc/cp4-eval-report`)*
**Trọng tâm:** Chấm chéo 5 câu (`+2đ` R4) + hoàn thiện `eval/report.md` (`8đ` R5) & `eval/README.md`.

- [ ] **09:30 – 10:00 · Chấm chéo 5 câu đầu lượt 1 *(bắt buộc Rubric R4)*:**
  1. Mở `eval/run-1.csv`, tự chấm độc lập 5 câu đầu (`B01`–`B05`) theo `eval/metric_spec.yaml` (không nhìn cột `pass` trước khi tự đánh giá).
  2. So khớp với kết quả chấm của Đạt (cần khớp **≥4/5**).
  3. Cập nhật kết quả chấm chéo (ghi rõ khớp `x/5`, tên 2 người chấm, ngày chấm) vào **`eval/README.md` mục 3**.
- [ ] **10:30 – 11:45 · Viết báo cáo `eval/report.md` *(Rubric R5 — 8 điểm)*:**
  1. Kéo `main` sau khi Đạt push `eval/run-2.csv`.
  2. Điền đầy đủ 4 mục trong **`eval/report.md`**:
     - *Mục 1:* Bảng so sánh lượt 1 → lượt 2 (Run ID, Đạt/tổng, %, `thuong`, `kho`, `tu_choi`, So với chuẩn "đạt").
     - *Mục 2:* Gom nhóm lỗi có tên + bảng **≥3 lỗi / điểm yếu cụ thể** (`Câu · Input · Output · Vì sao sai` — ví dụ: `B08` lỗi bỏ qua HAX G10 do từ khoá chung · `B05` dẫn thừa mã đoạn phụ `[B01-P02]` · `B25` từ chối an toàn nhưng chưa gợi công thức `[B08-P01]`).
     - *Mục 3:* Mô tả 1 lần cải tiến (nhắm nhóm lỗi đau nhất, đã sửa gì, kết quả trước → sau, ghi thật câu nào tệ đi nếu có).
     - *Mục 4:* Lỗi còn lại + rủi ro + nếu có thêm 1 tuần sẽ làm gì (dùng trực tiếp cho Slide trang 8).
  3. Cập nhật bảng lượt 2 và mục 6 vào **`eval/README.md`**.
  4. Tạo PR `loc/cp4-eval-report` trước **12:00** để Chiêu lấy số đổ vào Slide trang 5.
- [ ] **Trước 23:59:** Tạo `reflection/tran-xuan-loc.md`.

---

### 3. Đinh Hoàng Phong *(Thành viên — `2A202604090` · nhánh `phong/cp4-validation-readme`)*
**Trọng tâm:** Người dùng thử (`+5đ Bonus`) + hoàn thiện `README.md` gốc + kiểm soát tính nhất quán số liệu toàn Slide.

- [ ] **10:00 – 11:30 · Tổ chức 2–3 người dùng thử ngoài nhóm *(Rubric Bonus — +5 điểm)*:**
  1. Mời **2–3 bạn học viên L3 ngoài nhóm** ngồi dùng thử trực tiếp bản chạy thử (`python codebase/web_app.py` hoặc `python run.py` chạy AI thật — mỗi người ~10 phút).
  2. Thực hiện đúng **5 nhịp** ở guide 4.3: *làm quen → bối cảnh → giao việc theo kết quả (không chỉ bấm nút) → quan sát chỗ do dự/hiểu sai → hỏi sau ("Nếu mai không được dùng nữa: rất tiếc / hơi tiếc / không sao?")*.
  3. Ghi đủ 5 cột (*Người thử (vai, KHÔNG ghi tên) · Việc giao · Quan sát · Trích nguyên văn · Mức nghiêm trọng cao/vừa/thấp*) vào **`validation/log.md`**.
  4. Rút ra **≥1 thay đổi cụ thể** (hoặc lý do giữ nguyên) ở mục *Tổng hợp* của `validation/log.md` và thêm 1 dòng vào `spec.md` §10.
- [ ] **11:30 – 13:00 · Dọn `README.md` gốc & soát chéo Slide:**
  1. Sửa **`README.md`** ở thư mục gốc repo:
     - **Xoá Mục 0** (*"Tạo repo nhóm từ khung này"*).
     - Điền tiêu đề `# Chuppachip — Trợ giảng Pre-class có căn cứ mã đoạn`.
     - Điền bảng **"Phần nào thật, phần nào giả"** (Model thật `gemini-3.5-flash-lite`, `data/lessons.json` là 15 đoạn `synthetic`).
     - Điền 2–3 dòng **"Dùng AI vào việc gì"** (khớp `docs/ai-usage.md`).
     - Điền link **Video demo dự phòng** (sau khi Chiêu gửi link).
  2. Soát từng trang Slide (1→8) cùng Chiêu: kiểm tra **mọi con số trên Slide đều truy được về file trong repo** (luật: số không truy được về file → trừ điểm!).
  3. Tạo PR `phong/cp4-validation-readme` trước **13:15**.
- [ ] **Trước 23:59:** Tạo `reflection/dinh-hoang-phong.md`.

---

### 4. Phạm Văn Chiêu *(Thành viên — `2A202604033` · nhánh `chieu/cp4-cost-slides`)*
**Trọng tâm:** Báo cáo chi phí `cost/cost-estimate.md` (`12đ` R6) + Slide 8 trang (`10đ` R7) + Video demo dự phòng.

- [ ] **09:30 – 11:15 · Dựng khung Slide 8 trang theo đúng `slides/outline.md`:**
  - Thiết kế trên Canva / Google Slides / PowerPoint (mỗi trang bắt buộc có **≥1 con số / trích dẫn có nguồn / kết quả đo**):
    - *Trang 1:* Người dùng & Pain (`evidence/summary.md`: 47,5% hỏi nối tiếp, 21,3% `bam_bai=0`, 3/4 PV đúng vai, trích dẫn P3/P5).
    - *Trang 2:* Vì sao chọn A1 — Bảng Impact (~150 giờ/tháng) & lý do loại A2, A5 (`spec.md` §2).
    - *Trang 3:* Giải pháp AI — Lát cắt 1 câu, sơ đồ Workflow 4 bước, 3 lớp chặn, HAX G10/G11 (`spec.md` §4).
    - *Trang 4:* Demo live — 1 câu thường + 1 câu khó/tấn công + link video dự phòng.
    - *Trang 5:* **Đánh giá thế nào** — 25 câu (11/25 người dùng thật), 4 metric, lượt 1 → lượt 2 (kèm Run ID), lỗi chính (`eval/README.md`, `eval/report.md`).
    - *Trang 6:* **Chi phí khi dùng thật** — 50 phiên mô phỏng, chi phí/task thành công, 3 kịch bản thấp/cơ sở/cao, ≥2 model trả phí, so sánh với impact (`cost/cost-estimate.md`).
    - *Trang 7:* Kết luận **Go / Iterate / Stop** — dẫn thẳng số từ trang 1, 5, 6.
    - *Trang 8:* Nếu có thêm 1 tuần — 2–3 việc cụ thể trỏ về `eval/report.md` mục 4 & `validation/log.md`.
- [ ] **11:30 – 12:30 · Hoàn thiện `cost/cost-estimate.md` & `spec.md` §8 *(Rubric R6 — 12 điểm)*:**
  1. Kéo `main` sau khi Đạt push `cost/simulate-1.csv` & `cost/simulate-1-summary.md`.
  2. Chép bảng kết quả từ `cost/simulate-1-summary.md` vào **`cost/cost-estimate.md`** (tuyệt đối không tự điền tay sai số).
  3. Viết rõ mục 3 (**So với impact:** `chi phí / người / tháng` ở kịch bản cơ sở so với `~1 giờ tiết kiệm / người / tháng` từ §2 → kết luận 1 dòng có đáng làm không).
  4. Điền tóm tắt số vào **`spec.md` §8** và đổ số vào **Slide trang 6**.
- [ ] **12:30 – 13:15 · Quay Video demo dự phòng & xuất Slide:**
  1. Quay video 1,5–2 phút chạy thật trên Web UI (`python codebase/web_app.py`) hoặc terminal `python run.py`: 1 câu thường (trích mã `[Bxx-Pxx]` + hiện thẻ nguồn) + 1 câu khó/tấn công (chặn/hỏi lại). **Không để lộ `.env`!**
  2. Đăng YouTube *"Không công khai"* hoặc Drive *"Bất kỳ ai có đường liên kết"* → kiểm mở bằng **Tab Ẩn Danh**.
  3. Xuất slide thành **`demo-slides.pdf`** đặt ở thư mục gốc repo (và giữ link online dự phòng cho Form CP4).
  4. Cập nhật `slides/outline.md` (tích đủ 8 trang + bảng ai nói trang nào) → tạo PR `chieu/cp4-cost-slides` trước **13:30**.
- [ ] **Trước 23:59:** Tạo `reflection/pham-van-chieu.md`.

---

## 3. Phân công thuyết trình Demo (mỗi người đều nói + đều trả lời được Q&A)

| Phần / Trang Slide | Người trình bày | Câu hỏi giám khảo dễ hỏi vặn (cả 4 bạn đều phải biết!) |
|---|---|---|
| Trang 1–2 (Pain & Impact) | **Đinh Hoàng Phong** | Mẫu số đào data lấy sao? Vì sao chọn cận dưới 5 phút? P4 ngược giả thuyết thì xử lý sao? |
| Trang 3–4 (Kiến trúc & Demo live) | **Nguyễn Xuân Đạt** | Vì sao chọn Workflow cố định mà không chọn Agent? 3 lớp chặn rủi ro nằm ở đâu? Câu lạ giám khảo đưa sẽ đi nhánh nào? |
| Trang 5 (Đánh giá lượt 1 → 2) | **Trần Xuân Lộc** | Chuẩn đạt §7 là gì? Chấm chéo 5 câu khớp mấy/5? Lỗi nguy hiểm nhất là gì, lượt 2 sửa gì? |
| Trang 6–8 (Chi phí, Kết luận & 1 tuần tới) | **Phạm Văn Chiêu** | Chi phí / task thành công tính công thức nào? Sao build free mà tính giá trả phí? So với impact đáng làm không? |

---

## 4. Checklist 14:15 trước khi bấm Nộp CP4 (14:30)

- [ ] **4 Điều kiện cứng xét giải:** (1) Gọi AI thật (`gemini-3.5-flash-lite`) · (2) Bằng chứng ≥1 nguồn đạt ngưỡng (`evidence/summary.md`) · (3) Bộ 25 câu + % đạt lượt 1 → lượt 2 (`eval/run-1.csv`, `eval/run-2.csv`, `eval/report.md`) · (4) Slide `demo-slides.pdf` (hoặc link xem được Tab Ẩn Danh).
- [ ] **Đủ 7 hạng mục bắt buộc + Bonus:** `evidence/` · `spec.md` §0–§10 · `codebase/` · `data/DATA_CARD.md` · `eval/` · `cost/simulate-1.csv` + `cost/cost-estimate.md` · `demo-slides.pdf` + Video dự phòng · `validation/log.md` (+5đ).
- [ ] `python run.py check` → **0 lỗi** · `git status` & trên GitHub **KHÔNG có `.env`**, không lộ tên thật người phỏng vấn/dùng thử.
- [ ] **14:30:** Nộp xong **Form CP4**!
- [ ] **Trước 23:59:** Đủ 4 file `reflection/nguyen-xuan-dat.md`, `reflection/dinh-hoang-phong.md`, `reflection/tran-xuan-loc.md`, `reflection/pham-van-chieu.md` + changelog mọi sửa đổi sau 14:30 trong `spec.md` §10.
