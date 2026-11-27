# Khảo sát — bộ câu hỏi, kênh gửi, giờ mở / chốt

> Người phụ trách: Đinh Hoàng Phong. Form tạo bằng script `evidence/survey/create_form.gs` (nội dung khớp bảng dưới).
> Ngưỡng: **≥20 người ngoài nhóm, đúng người dùng** (học viên L3). Người chọn "Chưa bao giờ tự xem" hoặc không phải học viên L3 thì không tính vào n.

- **Link form:** https://forms.gle/FYpo2q2QWy34xaWa9
- **Kênh đã gửi:** Discord kênh chung khoá (L3A, L3B)
- **Giờ mở:** 17:43 Thứ Sáu 27/11/2026 · **Giờ chốt:** 09:00 Thứ Bảy 28/11/2026 (kịp tổng hợp trước CP3)

## Bộ câu hỏi

| # | Câu hỏi | Kiểu trả lời | Bắt buộc | Dùng cho |
|---|---|---|---|---|
| 1 | Bạn là: | Chọn một: L3A · L3B · Lab coach/TA · Giảng viên · Khác | Có | Lọc đúng người dùng |
| 2 | Lần gần nhất bạn tự xem một video pre-class là khi nào? | Hôm nay · tuần này · tuần trước · lâu hơn · chưa bao giờ (→ nộp luôn) | Có | Lọc |
| 3 | Trong 1 tuần qua, có bao nhiêu lần bạn xem pre-class mà gặp chỗ chưa hiểu? | Số 0–50 | Có | `spec.md` §2 số lần (×4,3 ra tháng) |
| 4 | Lần gần nhất gặp chỗ chưa hiểu, bạn đã làm gì? | Chọn nhiều | Có | §1 "đang giải bằng gì" |
| 5 | Nếu có hỏi khung chat dưới video: đọc câu trả lời xong bạn làm gì tiếp? | Chọn nhiều | Không | Kiểm chéo 47,5% hỏi nối tiếp |
| 6 | Lần đó từ lúc vướng đến lúc hiểu (hoặc bỏ qua) mất bao lâu? | <2' · 2–5' · 5–15' · 15–30' · >30' · không nhớ | Có | §2 thay "3 phút" tự ước tính |
| 7 | Lần đó cuối cùng bạn có hiểu được không? | Hiểu hẳn · một phần · không, bỏ qua | Có | Mức độ pain |
| 8 | Trong 1 tháng qua, có lần nào sai câu kiểm tra cuối bài rồi mới nhận ra hiểu lệch nội dung video không? | ≥2 lần · 1 lần · không · không nhớ | Có | Kiểm chéo 20,3% sai lần 1 |
| 9 | Điều gì khó chịu nhất ở lần vướng đó? | Đoạn văn | Không | Trích nguyên văn → `summary.md` |
| 10 | Lúc vướng bạn đã gõ câu hỏi gì? (viết lại đại khái) | Đoạn văn | Không | Câu thử `source = nguoi_dung` |
| 11 | (Tuỳ chọn) Sẵn lòng cho hỏi thêm 10' / dùng thử? Để lại tên Discord | Ô ngắn | Không | Hẹn phỏng vấn, `validation/log.md` |

Form không thu email. Khi xuất `results.csv` để commit: **xoá cột câu 11** (tên Discord) và cột thời gian nếu cần.
