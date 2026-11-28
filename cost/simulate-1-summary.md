# Tóm tắt mô phỏng simulate-1@20261128-093609

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 22 | 1 | 381 | 61 | 0.8 | 3.3 |
| dung_vua | 13 | 3 | 1277 | 187 | 2.6 | 10.5 |
| dung_nhieu | 15 | 5 | 2162 | 292 | 4.3 | 17.9 |

Tỉ lệ đạt dùng để tính: 25/25 (100%) — lượt run-2@20261128-093105

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00075 (≈ 19 ₫) | $0.00075 (≈ 19 ₫) | $0.00028 (≈ 7 ₫) | $2.58 (≈ 65.494 ₫) | $6.02 (≈ 152.819 ₫) | $8.59 (≈ 218.313 ₫) | $0.0086 (≈ 218 ₫) |
| gemini-3.8-flash (vào 0.75 · ra 3.75 $/1M) | $0.0015 (≈ 37 ₫) | $0.0015 (≈ 37 ₫) | $0.00054 (≈ 14 ₫) | $5.06 (≈ 128.510 ₫) | $11.81 (≈ 299.857 ₫) | $16.86 (≈ 428.367 ₫) | $0.0169 (≈ 428 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0029 (≈ 75 ₫) | $0.0029 (≈ 75 ₫) | $0.0011 (≈ 27 ₫) | $10.12 (≈ 257.020 ₫) | $23.61 (≈ 599.714 ₫) | $33.73 (≈ 856.734 ₫) | $0.0337 (≈ 857 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.7) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.5-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ (Tỷ giá tham chiếu Vietcombank ngày 27/11/2026.).
