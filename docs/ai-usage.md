# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Coding agent (Antigravity / Codex) | Dựng khung `codebase/agent.py`, `tools.py`, `ai.py` (nối Gemini REST API qua `urllib`, OpenAI fallback) và giao diện web demo local `codebase/web_app.py` | Đạt & Lộc rà toàn bộ luồng 4 bước, chạy test 4 nhánh (thường/mơ hồ/ngoài bài/tấn công), tự sửa lỗi khớp từ khoá chung ở vòng 2 (`_GENERIC_KW`) và chạy thật trên `gemini-3.5-flash-lite` | Nguyễn Xuân Đạt, Trần Xuân Lộc |
| Prompt / thiết kế lời gọi mô hình | Coding agent (Antigravity) | Gợi ý cấu trúc `SYSTEM` prompt ép trích dẫn `[Bxx-Pxx]` và từ chối ngoài tài liệu | Đạt rà từng quy tắc trong `SYSTEM` (khớp §4, HAX G10/G11) và kiểm chứng đầu ra thật trên 25 câu thử (`run-1.csv`, `run-2.csv`) | Nguyễn Xuân Đạt |
| Đào data (viết script đếm, gợi ý nhãn) | Coding agent (Claude Code) | Viết `evidence/count.py` đếm 8 chỉ số và lọc 6 ví dụ | Chạy lại script trên data BTC ngày 27/11: khớp 8/8 số và 6/6 ví dụ trong `data-mining.md`; kiểm lại giả định giờ UTC+7 và mẫu số 436 theo README của data | Đinh Hoàng Phong |
| Rà câu hỏi phỏng vấn / khảo sát | Claude Code | Soạn bộ câu hỏi Mom Test, tin nhắn hẹn, script Apps Script tạo Google Form; đánh dấu câu dẫn dắt cần tránh | Phong duyệt từng câu trước khi hỏi; người được phỏng vấn là người thật. **Riêng câu trả lời P2 đã được công cụ AI diễn đạt lại** trước khi ghi, nên `P2.md` chỉ giữ ý chính, bỏ chi tiết AI có thể đã thêm, không lấy làm trích nguyên văn | Đinh Hoàng Phong |
| Chuyển ghi âm phỏng vấn thành chữ | Whisper (`faster-whisper`, chạy trên máy, không gửi ra ngoài) | Chuyển ghi âm P1 thành chữ; Claude Code sắp vào mẫu `P1.md` | Phong nghe lại ghi âm, xác nhận và sửa 3 chỗ máy nhận sai ("lên trường mới", "tóm tắt hộ", "bài lab"); file ghi âm không commit | Đinh Hoàng Phong |
| Tổng hợp khảo sát | Claude Code (đọc Sheet kết quả qua Google Drive) | Đếm x/n từng câu, gắn cờ phiếu nghi là bản thử | Phong xác nhận phiếu thử, đối chiếu lại số với Google Forms | Đinh Hoàng Phong |

| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Claude Code | Trích chữ từ `demo-slides.pdf`, dò từng số / trích dẫn trang 1–8 với file nguồn → `slides/soat-so-lieu.md`; soạn khung ý cho `reflection/dinh-hoang-phong.md` | Phong duyệt từng dòng soát (vd câu trích P3 trên slide không có trong `P3.md`), gửi Chiêu sửa slide; tự viết lại reflection bằng lời của mình | Đinh Hoàng Phong |

| Viết câu thử (benchmark) | Coding agent (Antigravity / Codex) | Hỗ trợ chuẩn hoá format 6 cột và gợi ý câu thử mở rộng cho 4 lớp chỗ khó | Lộc & Đạt rà toàn bộ 25 câu `eval/benchmark.csv`; 11/25 câu (44%) lấy từ câu hỏi học viên thật (S01–S06, P3), 14 câu `tu_viet` ghi rõ nguồn; `python run.py check` 0 lỗi | Trần Xuân Lộc, Nguyễn Xuân Đạt |
| Sinh data `synthetic` (nếu có) | Coding agent + viết tay có cấu trúc | Tóm tắt 15 đoạn kiến thức phổ quát (`B01-P01`–`B08-P01`) vào `data/lessons.json` | Viết tay có cấu trúc (không sinh ngẫu nhiên), kiểm tay đủ 15/15 đoạn bởi Đạt & Lộc; không dùng nguyên tài liệu khoá và không tính là bằng chứng pain | Nguyễn Xuân Đạt, Trần Xuân Lộc |
| Chấm cột `pass` bằng LLM (nếu có) | Không dùng LLM chấm tự động | Codex chỉ đề xuất nháp B01–B05 để đối chiếu; toàn bộ điểm `pass` trong `run-1.csv` & `run-2.csv` được chấm thủ công theo `metric_spec.yaml` | Đạt & Lộc kiểm tra thủ công 25/25 câu và chấm chéo độc lập B01–B05 khớp **5/5** (`eval/README.md` mục 3) | Trần Xuân Lộc, Nguyễn Xuân Đạt |
Phong làm nốt validation/log.md (2–3 bạn ngoài nhóm dùng thử) để ăn +5đ Bonus.
**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
