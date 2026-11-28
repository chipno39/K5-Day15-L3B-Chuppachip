# Soát số liệu slide → file nguồn

> Người soát: Đinh Hoàng Phong (TV2) · 28/11/2026 ~12:20 · đối chiếu `demo-slides.pdf` (bản commit `e7a7705`) với file trong repo. Coding agent (Claude Code) trích chữ từ PDF và dò số trong repo; TV2 duyệt.
> Luật: số / trích dẫn không truy được về file → sửa slide, không sửa file nguồn cho khớp slide.

## Phải sửa trước khi nộp CP4

| Trang | Trên slide | Vấn đề | Sửa thành | Nguồn |
|---|---|---|---|---|
| 1 | "Đọc xong câu trả lời vẫn không biết nó lấy từ đoạn nào... tua lại video mất 10–15 phút." (P3) | **Không phải lời P3.** P3 không nói câu này; `P3.md` còn ghi rõ "chưa xác nhận câu trả lời có thiếu mã đoạn". "10–15 phút" là số ghi chép, không phải trích | "Ban đầu mình tua lại video, sau đó mình sử dụng khung chat để hỏi thêm. Tuy nhiên, câu trả lời khá nhiều chữ và mình vẫn phải tự hình dung." (P3) | `evidence/interviews/P3.md` mục Trích nguyên văn |
| 1 | "Mình không tin ngay... tự kéo thanh trượt trên video tìm lại đúng đoạn mất 2–3 phút." (P5) | Ghép 2 câu khác nhau và đổi chữ | "Mình phải tự kéo thanh trượt trên video lùi lại hoặc nhảy từng đoạn ngắn… Thường mất khoảng 2–3 phút." (P5) | `evidence/interviews/P5.md` |
| 1 | 47,5% "598 lượt phải hỏi nối tiếp trong 3 phút **vì câu trả lời chung chung**" | Data không cho biết *vì sao* (`data-mining.md` dòng 52 tự nói vậy) | "598/1.260 lượt hỏi nối tiếp trong ≤3 phút trên cùng video" | `evidence/data-mining.md` |
| 1 | 21,3% "**câu ngoài bài** mà AI cũ vẫn trả lời dài" | Chỉ số là lượt bị chấm *không bám bài* (`rubric_bam_bai = 0`), không phải "câu ngoài bài" | "261/1.223 lượt trả lời bị chấm không bám bài, trung vị vẫn dài 329 ký tự" | `evidence/data-mining.md` |
| 1 | "Khảo sát: 8/8 bạn từng sai câu kiểm tra, 5/8 bạn phải tua lại video để đối chiếu" | Thiếu mẫu số gốc và chữ "hoặc hỏi thêm"; khảo sát **chưa đạt ngưỡng 20** | "Khảo sát (8 học viên L3 có xem video, chưa đủ ngưỡng 20): 8/8 từng sai câu kiểm tra vì hiểu lệch · 5/8 tua lại video hoặc hỏi thêm" | `evidence/summary.md`, `spec.md` §1 |
| 2 | "145 học viên **hay chat thường xuyên**" | 145 là số HV *có dùng chat* trong 21 ngày (trên 436 HV hoạt động) | "145 học viên có dùng chat (21 ngày)" | `evidence/data-mining.md`, `spec.md` §2 |
| 2 | 5 phút/lượt "**mức thấp nhất đã kiểm chứng, chưa tính lúc phải tua video**" | Sai cả hai ý: 5' là cận dưới khoảng giữa của khảo sát (5–15'), có phỏng vấn thấp hơn (P4 2', P5 2–3'); và thời gian đó **đã gồm** tua video | "cận dưới khoảng giữa trong khảo sát (5–15'), phỏng vấn trung vị ~6'" | `evidence/summary.md`, `spec.md` §2 |
| 2 | Bỏ A5 "Dữ liệu **do tụi mình giả lập**" | `data/training-ops/` là data giả lập BTC cấp, không phải nhóm làm | "Data training-ops là giả lập, không tính là bằng chứng; khó hẹn ≥3 key coach trong 2 ngày" | `spec.md` §2 |
| 7 | "Cả bài thử 25 câu lẫn **mô phỏng 50 phiên đều đạt 100%**" | Mô phỏng không đo chất lượng: tỉ lệ đạt 100% là **đầu vào** lấy từ `run-2.csv` (`--rate-from`). Mô phỏng chỉ cho 0/50 phiên lỗi | "25/25 câu thử đạt ở lượt 2; mô phỏng 50 phiên chạy 0 lỗi" | `cost/cost-estimate.md`, `cost/simulate-1-summary.md` |
| 8 | "rút ra từ kết quả đánh giá **và phản hồi của học viên dùng thử**" | `validation/log.md` đang **trống** | Bỏ vế "phản hồi của học viên dùng thử", hoặc giữ nếu kịp điền `validation/log.md` bằng phiên dùng thử thật | `validation/log.md` |

## Nên sửa (không sai số, nhưng dễ bị hỏi vặn)

| Trang | Trên slide | Góp ý |
|---|---|---|
| 7 | "~150 giờ học viên **được tiết kiệm**" | 150 giờ là thời gian học viên *đang mất* để kiểm chứng; công cụ chỉ giảm một phần. Nói "đang mất ~150 giờ/tháng" an toàn hơn |
| 4, 7 | "mở đúng đoạn bài trong chưa đầy 30 giây" | Đây là mục tiêu của lát cắt (`spec.md` §4), chưa có số đo. Trang 4 ghi "Điều cần thấy" là ổn; trang 7 nên ghi là mục tiêu |
| 5 | "11 câu lấy từ người dùng thật" | Khớp `spec.md` §7, nhưng nguồn `S01–S06` trong `eval/benchmark.csv` chưa có file minh chứng trong repo — nên chuẩn bị câu trả lời nếu bị hỏi |

## Đã khớp

| Trang | Số trên slide | File |
|---|---|---|
| 1 | 34,0% (429/1.260) · 20,3% (399/1.968) · 1.260 lượt | `evidence/data-mining.md` |
| 2 | 145 × 12,4 × 5 ≈ 150 giờ/tháng · 200 HV ≈ 200 giờ · A2 ~107 giờ · A5 ~27 giờ | `spec.md` §2 |
| 3 | 4 bước, `gemini-3.5-flash-lite`, kiểm mã `[Bxx-Pxx]`, 3 nhánh hỏi lại / trả lời / không có trong bài | `spec.md` §4 |
| 5 | 24/25 → 25/25 · chấm chéo 5/5 · 0,8 → 0,7 lượt gọi/câu · 14/7/4 câu · ngưỡng 85/70/100/80% | `eval/README.md`, `eval/report.md`, `spec.md` §7 |
| 6 | $0,00075 (~19 ₫) · $6,02 (~152.819 ₫) · ~218 ₫/người · $2,58 · $8,59 · persona 50/30/20% | `cost/cost-estimate.md`, `cost/simulate-1-summary.md` |

## Ghi chú khảo sát

Sheet lúc 12:20 có 18 phiếu (12 học viên L3), vẫn dưới ngưỡng 20. Slide và `evidence/summary.md` dùng số chốt lúc 00:19 28/11 (15 phiếu, 10 L3, 8 có xem video) — giữ nguyên để slide khớp file.
