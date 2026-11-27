# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Coding agent (Claude Code) | Viết `evidence/count.py` đếm 8 chỉ số và lọc 6 ví dụ | Chạy lại script trên data BTC ngày 27/11: khớp 8/8 số và 6/6 ví dụ trong `data-mining.md`; kiểm lại giả định giờ UTC+7 và mẫu số 436 theo README của data | Đinh Hoàng Phong |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn bộ câu hỏi Mom Test, tin nhắn hẹn, script Apps Script tạo Google Form; đánh dấu câu dẫn dắt cần tránh | Phong duyệt từng câu trước khi hỏi; người được phỏng vấn là người thật. **Riêng câu trả lời P2 đã được công cụ AI diễn đạt lại** trước khi ghi, nên `P2.md` chỉ giữ ý chính, bỏ chi tiết AI có thể đã thêm, không lấy làm trích nguyên văn | Đinh Hoàng Phong |
| Chuyển ghi âm phỏng vấn thành chữ | Whisper (`faster-whisper`, chạy trên máy, không gửi ra ngoài) | Chuyển ghi âm P1 thành chữ; Claude Code sắp vào mẫu `P1.md` | Phong nghe lại ghi âm, sửa các chỗ máy nhận sai (đánh dấu `[...]`); file ghi âm không commit | Đinh Hoàng Phong |
| Tổng hợp khảo sát | Claude Code (đọc Sheet kết quả qua Google Drive) | Đếm x/n từng câu, gắn cờ phiếu nghi là bản thử | Phong xác nhận phiếu thử, đối chiếu lại số với Google Forms | Đinh Hoàng Phong |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
