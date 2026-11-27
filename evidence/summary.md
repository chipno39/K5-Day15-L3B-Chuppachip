# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).
>
> **Bản tạm tại CP2 (27/11 18:35, người tổng hợp: Đinh Hoàng Phong).** Phỏng vấn và khảo sát vẫn đang chạy, số sẽ cập nhật trước CP3.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ — 8 chỉ số + 6 ví dụ; TV2 chạy lại `count.py` trên data BTC ngày 27/11, khớp 8/8 số | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ — có 3 buổi (P1, P3, P4) nhưng mới **2 người đúng vai** (P3, P4); P1 không xem video pre-class. Còn thiếu P2 | `evidence/interviews/P1.md`, `P3.md`, `P4.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ — đang mở, mới **7** câu trả lời hợp lệ (5 người có xem video) | `evidence/survey/questions.md`, `results.csv` |

## 2. Số chính

- **Đào data** (`data/preclass/`, 05–25/11/2026): **47,5%** (598/1.260) lượt chat là hỏi nối tiếp trong ≤3 phút trên cùng video · **21,3%** (261/1.223) lượt bị chấm không bám bài nhưng câu trả lời vẫn dài, trung vị 329 ký tự · **17,1%** (216/1.260) câu hỏi ≤20 ký tự · **34,0%** (429/1.260) hỏi lúc 20h–02h · **20,3%** (399/1.968) sai câu kiểm tra ở lần làm đầu tiên · chỉ **145/436** học viên hoạt động từng dùng chat.
- **Phỏng vấn** (n nhỏ nên không ghi %): **1/2** người đúng vai gặp pain rõ (P3), P4 chỉ vướng nhẹ · số lần/tháng: P3 khoảng 5–6, P4 không nêu số · mỗi lần mất **2–15 phút** (P4: 2', P3: 10–15'). P1 (ngoài vai) vướng ở bài lab, tự đọc lại mất 30–60'.
- **Khảo sát** (n = 7 học viên L3 hợp lệ, dưới 10 người nên không ghi %):
  - **2/7** chưa từng tự xem video pre-class.
  - Trong 5 người có xem:
    - **5/5** từng sai câu kiểm tra cuối bài vì hiểu lệch nội dung video trong 1 tháng qua (1 người ≥2 lần).
    - **0/5** hiểu hẳn ở lần vướng gần nhất (4 hiểu một phần, 1 bỏ qua).
    - **3/5** hỏi ChatGPT hoặc công cụ AI bên ngoài.
    - **0/5** chọn "hỏi ở khung chat dưới video" ở câu 4.
    - Thời gian mỗi lần: **3/5** mất 2–5', **2/5** mất 5–15'.
    - Số lần vướng trong 1 tuần: 0, 0, 3, 3, 5.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Học viên L3, **không xem video pre-class** (ngoài vai chính) | Không ở video; vướng ở bài lab | "Hầu như bài lab nào cũng vướng" | 10–15' (nhờ AI tóm tắt) · 30–60' (tự đọc lại) | Đọc lại slide, AI bên ngoài tóm tắt |
| P2 | *(chưa phỏng vấn — TV2 làm trước CP3)* | | | | |
| P3 | Học viên L3 tự học pre-class buổi tối (~21:30) | **Có** | ~5–6 | 10–15' | Tua video → hỏi khung chat → hỏi thêm ví dụ có số liệu |
| P4 | Học viên L3 xem pre-class ~20:00 | Rất nhẹ | Không nêu số | ~2' | Hỏi AI, tua lại video |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Ban đầu mình tua lại video, sau đó mình sử dụng khung chat để hỏi thêm. Tuy nhiên, câu trả lời khá nhiều chữ và mình vẫn phải tự hình dung." — P3
2. "Mình phải đọc lại câu trả lời và hỏi thêm một ví dụ có số liệu cụ thể thì mới hiểu được cơ bản." — P3
3. "từ nội dung vướng từ ngữ, thuật ngữ bằng tiếng anh tôi lại phải tìm hiểu lại từ đầu" — phiếu khảo sát 27/11 17:59
4. "Hầu như là làm bài lab nào là mình sẽ vướng, bởi vì kiến thức chương trình chạy hơi nhanh." — P1
5. "xem lúc 8h tối, có hỏi AI, trả lời hợp lí đủ hiểu, mất tầm 2p tua lại video, không làm sai trắc nghiệm" — P4 *(ví dụ ngược)*
6. Dòng data `chat=C00485` (23h VN): câu hỏi 15 ký tự, chấm `rubric_bam_bai=0`, nhưng trợ giảng vẫn trả lời 420 ký tự — `evidence/data-mining.md`

## 4. Các nguồn có khớp nhau không

**Data nói:** gần một nửa lượt chat là hỏi nối tiếp ngay trên cùng video, khoảng 1/5 câu trả lời không bám bài nhưng vẫn dài, và 1/5 lượt làm câu kiểm tra sai ở lần đầu.

**Người dùng nói:** người tự học buổi tối với khái niệm mới (P3) phải đọc lại câu trả lời dài rồi hỏi thêm. Trong khảo sát, cả 5/5 người có xem video đều từng sai câu kiểm tra vì hiểu lệch, và không ai hiểu hẳn ở lần vướng gần nhất.

- **Khớp:**
  - Hành vi "hỏi thêm sau khi đọc câu trả lời" (P3, 1 phiếu khảo sát) khớp với 47,5% lượt hỏi nối tiếp trong data.
  - Việc sai câu kiểm tra vì hiểu lệch khớp với 20,3% sai ở lần làm đầu tiên.
  - Thời gian 2–5' mỗi lần (3/5 phiếu) khớp với con số "3 phút" nhóm tự ước tính ở `spec.md` §2. Tuy nhiên P3 cho thấy có lần mất tới 10–15'.
- **Lệch:**
  - P4 thấy trợ giảng hiện tại "hợp lí đủ hiểu" với câu hỏi đơn giản lúc 20h. Pain không xảy ra với mọi người, mà tập trung vào khái niệm khó hoặc thuật ngữ mới.
  - Nhiều người không dùng khung chat mà dùng ChatGPT bên ngoài (3/5 phiếu, P1). P1 và 2/7 phiếu còn **không xem video pre-class**. Điều này khớp với data: chỉ 145/436 học viên từng dùng chat.
- **Mới, nhóm chưa nghĩ tới:** vướng vì **thuật ngữ tiếng Anh** (phiếu 17:59, P3: "bài có thuật ngữ, công thức").

## 5. Kết luận *(tạm tại CP2)*

Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần.**

- **Phần đúng:** với học viên có xem video và gặp khái niệm khó, câu trả lời dài khiến họ phải đọc lại và hỏi thêm (P3, data 47,5%). Hiểu lệch dẫn tới sai câu kiểm tra (5/5 phiếu, data 20,3%).
- **Phần phải đổi:**
  - Pain không phổ biến với câu hỏi đơn giản (P4).
  - Một phần lớn học viên bỏ qua video pre-class hoặc khung chat và dùng AI bên ngoài.

**Điều vẫn chưa biết:**
- Việc thiếu mã đoạn trích dẫn có phải nguyên nhân khiến học viên phải hỏi lại hay không. Chưa ai nhắc trực tiếp; P3.md ghi rõ là chưa xác nhận.
- Trung vị số phút mỗi lần trên mẫu đủ lớn (cần P2 và khảo sát ≥20 người).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| P1 · học viên L3 ngoài nhóm (TV2 Phong) | 27/11 ~18:15 | ✅ `interviews/P1.md` — không xem video pre-class nên không đúng vai |
| P2 · học viên L3 tự học pre-class buổi tối (TV2 Phong) | 27/11 tối, __:__ | ☐ |
| P3 · học viên L3 tự học pre-class buổi tối (TV3 Lộc) | 27/11 | ✅ `interviews/P3.md` |
| P4 · học viên L3 xem pre-class ~20:00 (TV4 Chiêu) | 27/11 17:30 | ✅ `interviews/P4.md` |
| Khảo sát Google Form (≥20 người) | mở 27/11 17:43 → chốt 28/11 09:00 | ⏳ 7 hợp lệ |
