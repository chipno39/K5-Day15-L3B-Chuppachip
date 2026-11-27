# Canvas — Chuppachip · Track A

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | Track A (EdTech — A1: Tutor cho trang pre-class) · Trợ giảng trả lời câu hỏi dưới video có trích dẫn mã đoạn bài học và biết nói "không có trong bài". |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Học viên L3 tự học bài pre-class vào buổi tối (20:00–02:00) trước buổi học chính, lúc không có TA trực giải đáp. |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Học viên L3 tự học video pre-class buổi tối khi thắc mắc kiến thức hoặc gõ câu hỏi ngắn/ngoài bài thường nhận phản hồi dài, chung chung, không chỉ rõ đoạn bài nào (hoặc không báo nội dung đó ngoài bài), khiến họ mất thời gian tua lại video để kiểm chứng hoặc hiểu lệch và làm sai câu kiểm tra cuối bài. |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | **Đã đào `data/preclass/` (`evidence/count.py`, 1.260 lượt chat / 145 HV):** 34,0% (429/1.260) hỏi 20h–02h; 17,1% (216/1.260) câu ≤20 ký tự (reply trung vị 231c); 21,3% (261/1.223) `rubric_bam_bai=0` (reply trung vị 329c); **47,5% (598/1.260) hỏi nối tiếp ≤3 phút**; 20,3% (399/1.968) sai câu kiểm tra lần 1. **Đã hoàn thành 4 phỏng vấn thật (`P1–P4`), khảo sát tạm `n=8` (`evidence/survey/results.csv`, mở đến 09:00 28/11) và tổng hợp `evidence/summary.md`.** **Ví dụ:** `chat=C00485` (23h VN, hỏi 15c, `bam_bai=0` nhận reply 420c) & P4 (*"xem lúc 8h tối, có hỏi AI... mất tầm 2p tua lại video"*). |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Một học viên L3 tự học pre-class buổi tối · gửi câu hỏi thắc mắc dưới video bài giảng · AI quyết định hỏi lại 1 câu nếu quá mơ hồ, trả lời kèm mã đoạn trích từ bài nếu có căn cứ, hoặc nói rõ "không có trong bài" nếu ngoài tài liệu · học viên tự mở đúng đoạn bài kiểm chứng trong 30 giây mà không nhận thông tin bịa. |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | **AI tự làm khi chắc (trích đúng mã đoạn), hỏi lại khi mơ hồ, từ chối/chuyển TA khi ngoài bài** — vì kiến thức sai khiến học viên hiểu nhầm bài (sai đắt), nhưng việc gắn mã đoạn giúp học viên tự kiểm chứng rất rẻ. |
| 7 | Phân công có tên | Cặp 1 (Nguyễn Xuân Đạt, Trần Xuân Lộc): Kiến trúc, `codebase/`, `eval/` · Cặp 2 (Đinh Hoàng Phong, Phạm Văn Chiêu): Đào `data/preclass/`, phỏng vấn/khảo sát `evidence/`, `cost/`, slide. Cả nhóm cùng phỏng vấn và chốt lát cắt. |
| — | *(CP2)* Đã đổi gì so với CP1 | Giữ nguyên Track A1 và lát cắt 1 câu; bổ sung đào data tái lập (`evidence/count.py`), 4 phỏng vấn thật (`P1–P4`), khảo sát tạm `n=8` (`evidence/summary.md`), mở rộng bộ câu thử lên 18 câu (`eval/benchmark.csv`) với mã đoạn `[Bxx-Pxx]`, chốt kiến trúc workflow cố định 4 bước (`spec.md` §4), và chốt cứng chuẩn "đạt" bằng số (`spec.md` §7: ≥80% tổng, ≥85% `thuong`, 100% `tu_choi`/tấn công, ≥70% `kho`). |
