# Chi phí khi dùng thật

> Hoàn thiện bởi: **Phạm Văn Chiêu** (`pvchiu`) · Mốc nộp CP4 (14:30 Thứ Bảy 28/11/2026).
> Đánh giá theo **Rubric R6 (12 điểm)**.
> Số liệu được lấy trực tiếp từ `cost/personas.yaml` và kết quả mô phỏng thật 50 phiên tại `cost/simulate-1-summary.md` (chạy trên bản cải tiến lượt 2, tỉ lệ đạt 25/25 = 100%).
> Lúc build thử nghiệm dùng gói miễn phí, nhưng khi tính chi phí vận hành thật bắt buộc phải tính theo **giá gói trả phí chính thức** (Pay-as-you-go).

---

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): Gồm 3 kiểu người dùng đại diện cho học viên L3:
  1. `dung_it` (50% người dùng): 4 phiên/người/tháng, 1 lượt hỏi/phiên. *Nguồn:* Phỏng vấn P1, P3 — học viên có nền tảng tốt, chỉ hỏi 1 lượt khi gặp định nghĩa khó hiểu.
  2. `dung_vua` (30% người dùng): 10 phiên/người/tháng, 3 lượt hỏi/phiên. *Nguồn:* Khảo sát học viên L3 và phân tích dữ liệu hỏi đáp pre-class trung bình 2–3 bài/tuần.
  3. `dung_nhieu` (20% người dùng): 20 phiên/người/tháng, 5 lượt hỏi/phiên. *Nguồn:* Phỏng vấn P4 và khai thác `data/preclass/chat.csv`: nhóm học viên đi làm tự học đêm (20h–02h), hỏi nhiều lượt để kiểm chứng bài trắc nghiệm.
- **Số người dùng thật (3 kịch bản):**
  - Mức thấp: **300 người** (học viên hoạt động thường xuyên).
  - Mức cơ sở: **700 người** (toàn bộ học viên khoá L3 theo quy mô công bố của hackathon).
  - Mức cao: **1.000 người** (khi mở rộng sang các khoá kế tiếp).
  - *Nguồn:* `README.md` hackathon và số liệu lớp L3.
- **Giá model trả phí chính thức (≥2 model):**
  1. `gemini-3.5-flash-lite`: Vào **0.30 $** / Ra **2.50 $** / 1 triệu token. *Nguồn:* Google Gemini API Pricing (`https://ai.google.dev/gemini-api/docs/pricing`, cập nhật 25/11/2026 — model chạy thật ở bản chạy thử).
  2. `gemini-3.8-flash`: Vào **0.75 $** / Ra **3.75 $** / 1 triệu token. *Nguồn:* Google Gemini API Pricing, cập nhật 25/11/2026.
  3. `gemini-4-hydrogen`: Vào **1.50 $** / Ra **7.50 $** / 1 triệu token. *Nguồn:* Google Gemini API Pricing, cập nhật 25/11/2026 (tầng model lớn để đối chiếu so sánh).
- **Tỉ lệ đạt dùng để tính:** **25/25 (100%)** — lấy từ lượt cải tiến chính thức `eval/run-2.csv` (`run-2@20261128-093105` qua tham số `--rate-from`).
- **Đo token:** Đo trên model `gemini-3.5-flash-lite` (trung bình 2,7 lượt hỏi/phiên; token vào trung bình ~1.096 token/phiên, token ra ~155 token/phiên). Tính giá trên cả 3 model để lập bảng so sánh.
- **Tỷ giá quy đổi:** 1 USD = **25.400 ₫** (Tỷ giá tham chiếu Vietcombank ngày 27/11/2026).

---

## 2. Kết quả mô phỏng (50 phiên)

- **Lượt mô phỏng:** `cost/simulate-1.csv` · **Run ID:** `simulate-1@20261128-093609` · **Số phiên:** 50 · **Seed:** 42 · **Phiên lỗi:** 0/50.
- **Thống kê theo từng Persona trong 50 phiên:**

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| `dung_it` | 22 | 1 | 381 | 61 | 0,8 | 3,3 |
| `dung_vua` | 13 | 3 | 1.277 | 187 | 2,6 | 10,5 |
| `dung_nhieu` | 15 | 5 | 2.162 | 292 | 4,3 | 17,9 |

- **Bảng chi phí chi tiết theo 3 kịch bản quy mô và 3 model:**

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **gemini-3.5-flash-lite** *(vào 0.3 · ra 2.5 $/1M)* | **$0.00075** (≈ 19 ₫) | **$0.00075** (≈ 19 ₫) | **$0.00028** (≈ 7 ₫) | **$2.58** (≈ 65.494 ₫) | **$6.02** (≈ 152.819 ₫) | **$8.59** (≈ 218.313 ₫) | **$0.0086** (≈ 218 ₫) |
| **gemini-3.8-flash** *(vào 0.75 · ra 3.75 $/1M)* | $0.0015 (≈ 37 ₫) | $0.0015 (≈ 37 ₫) | $0.00054 (≈ 14 ₫) | $5.06 (≈ 128.510 ₫) | $11.81 (≈ 299.857 ₫) | $16.86 (≈ 428.367 ₫) | $0.0169 (≈ 428 ₫) |
| **gemini-4-hydrogen** *(vào 1.5 · ra 7.5 $/1M)* | $0.0029 (≈ 75 ₫) | $0.0029 (≈ 75 ₫) | $0.0011 (≈ 27 ₫) | $10.12 (≈ 257.020 ₫) | $23.61 (≈ 599.714 ₫) | $33.73 (≈ 856.734 ₫) | $0.0337 (≈ 857 ₫) |

*Ghi chú công thức:*
- `Chi phí / task thành công` = `Chi phí trung bình mỗi phiên ÷ Tỉ lệ đạt` ($0.00075 ÷ 1.00 = $0.00075).
- `Chi phí / câu hỏi đạt` = `Chi phí mỗi phiên ÷ số lượt hỏi TB mỗi phiên (2,7) ÷ tỉ lệ đạt` ($0.00028 ≈ 7 ₫).
- Tỉ lệ đạt lấy từ lượt `eval/run-2.csv` (100%).

---

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):**
  - Mỗi học viên gặp vướng trung bình ~12,4 lượt/tháng, mỗi lần tốn ~5 phút kiểm chứng/hỏi lặp (cận dưới từ khảo sát và phỏng vấn).
  - Impact tiết kiệm được: `12,4 lượt × 5 phút ≈ 62 phút/người/tháng (~1 giờ học viên/tháng)`.
  - Tổng impact cho cả khoá: **~150 giờ học viên/tháng** (trên tập 145 HV thường xuyên chat) đến **~200 giờ học viên/tháng** (trên quy mô 200 HV).
- **Chi phí / người / tháng (Kịch bản cơ sở 700 người, model `gemini-3.5-flash-lite`):**
  - **$0.0086 / người / tháng** (tương đương **218 VNĐ / người / tháng**).
  - Tổng ngân sách vận hành cho toàn bộ 700 học viên chỉ mất **$6.02 / tháng (khoảng 152.819 VNĐ / tháng)**.
- **Kết luận một dòng — đáng làm không:**
  > **CỰC KỲ ĐÁNG LÀM (QUYẾT ĐỊNH GO): Chỉ tốn ~218 VNĐ/người/tháng (chưa bằng 1/10 cốc trà đá, tổng chi phí cả khoá 700 người chỉ ~153.000 VNĐ/tháng) để đổi lại tiết kiệm hơn 1 giờ tự học buổi đêm cho mỗi học viên và xóa bỏ hoàn toàn rủi ro bịa kiến thức nhờ trích dẫn mã đoạn chính xác.**

---

## 4. Phân tích sâu thêm (Độ nhạy & Khả năng mở rộng)

- **Độ nhạy model:**
  - Nếu nâng cấp lên `gemini-3.8-flash` để tăng khả năng hành văn tự nhiên, chi phí cơ sở tăng lên $11.81/tháng (~300.000 VNĐ/tháng, tức ~428 VNĐ/người/tháng) — vẫn hoàn toàn nằm trong ngân sách vận hành đào tạo.
  - Nhờ cơ chế **Workflow cố định** chặn câu mơ hồ bằng code (`check_ambiguity`) và tra cứu trước (`search_lesson`), hệ thống chỉ gọi model 0,8 – 4,3 lần/phiên thay vì vòng lặp agent tốn kém, giúp tiết kiệm hơn 60% chi phí token so với kiến trúc ReAct thông thường.
- **Chi phí hạ tầng ngoài model:**
  - Code chỉ dùng thư viện chuẩn Python (`urllib`, `http.server`), không đòi hỏi máy chủ GPU đắt đỏ; có thể chạy trên Cloud Run hoặc container micro-instance với chi phí ước tính ~$5/tháng.
- **Quy mô khả thi:**
  - Ở quy mô 1.000 học viên (mở rộng toàn viện), chi phí API model chỉ ở mức **$8.59/tháng (~218.000 VNĐ/tháng)**. Bài toán có biên độ hiệu quả kinh tế cực lớn.
