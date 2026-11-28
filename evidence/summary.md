# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).
>
> **Bản CP3 — chốt** (28/11 00:30, người tổng hợp: Đinh Hoàng Phong). Số khảo sát chốt lúc 00:19 28/11 với 15 phiếu; thêm phỏng vấn P5 lúc 00:25.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ — 8 chỉ số + 6 ví dụ; TV2 chạy lại `count.py` trên data BTC ngày 27/11, khớp 8/8 số | `evidence/data-mining.md`, `evidence/count.py` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ — 5 buổi, **4 người đúng vai** (P2, P3, P4, P5); P1 không xem video pre-class. Không tính P2 (AI diễn đạt lại) vẫn còn 3 người đúng vai | `evidence/interviews/P1.md` … `P5.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ — 15 phiếu, trong đó **10 học viên L3** (8 có xem video); 5 phiếu vai "Khác" không tính | `evidence/survey/questions.md`, `results.csv` |

## 2. Số chính

- **Đào data** (`data/preclass/`, 05–25/11/2026):
  - **47,5%** (598/1.260) lượt chat là hỏi nối tiếp trong ≤3 phút trên cùng video.
  - **21,3%** (261/1.223) lượt bị chấm không bám bài nhưng câu trả lời vẫn dài, trung vị 329 ký tự.
  - **17,1%** (216/1.260) câu hỏi ≤20 ký tự.
  - **34,0%** (429/1.260) hỏi lúc 20h–02h.
  - **20,3%** (399/1.968) sai câu kiểm tra ở lần làm đầu tiên.
  - Chỉ **145/436** học viên hoạt động từng dùng chat.
- **Phỏng vấn** (n = 5, không ghi %):
  - **4/5** có tự xem video (đúng vai).
  - **3/5** gặp pain rõ (P2, P3, P5): đọc câu trả lời xong vẫn phải tua lại, tự tìm lại đoạn video để đối chiếu, hoặc hỏi thêm ví dụ.
  - **1/5** vướng nhẹ (P4); **1/5** không xem video (P1).
  - Số lần/tháng: P2 ~7–8, P3 ~5–6, P5 ~5–6, P4 không nêu, P1 "hầu như bài lab nào cũng vướng".
  - Mỗi lần mất (người đúng vai): P4 2', P5 2–3' chỉ để tìm lại đúng đoạn video, P2 ~10', P3 10–15'. P1 10–15' nếu nhờ AI tóm tắt, 30–60' nếu tự đọc lại.
- **Khảo sát** (n = 10 học viên L3, dưới ngưỡng 20 nên không ghi %):
  - **2/10** chưa từng tự xem video pre-class.
  - Trong 8 người có xem:
    - **8/8** từng sai câu kiểm tra cuối bài vì hiểu lệch nội dung video trong 1 tháng qua (3 người ≥2 lần).
    - **0/8** hiểu hẳn ở lần vướng gần nhất (6 hiểu một phần, 2 bỏ qua).
    - Lần vướng gần nhất đã làm gì: **4/8** hỏi ChatGPT hoặc AI bên ngoài, **3/8** hỏi khung chat dưới video, **3/8** tua lại video.
    - Sau khi đọc câu trả lời: **5/8** tua lại video để đối chiếu hoặc hỏi thêm trong khung chat.
    - Thời gian mỗi lần: **3/8** mất 2–5', **3/8** 5–15', **1/8** 15–30', **1/8** trên 30'. Giá trị giữa nằm trong khoảng **5–15'**.
    - Số lần vướng trong 1 tuần: 0, 0, 0, 3, 3, 5, 5, 10 (trung vị 3, tức khoảng 13 lần/tháng). Cùng độ lớn với 12,4 lượt chat/tháng/người trong data (khác đơn vị: lần vướng so với lượt chat).
- **Dùng cho `spec.md` §2:** thừa số thời gian lấy **5 phút/lần**, là cận dưới khoảng giữa của khảo sát. Phỏng vấn 4 người đúng vai cho 2', 2–3', ~10', 10–15', trung vị khoảng 6'.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Học viên L3, **không xem video pre-class** (ngoài vai chính) | Không ở video; vướng ở bài lab | "Hầu như bài lab nào cũng vướng" | 10–15' (nhờ AI tóm tắt) · 30–60' (tự đọc lại) | Đọc lại slide, AI bên ngoài tóm tắt |
| P2 | Học viên L3 tự học pre-class buổi tối (21:30–22:15) *(AI diễn đạt lại)* | **Có** | ~7–8 | ~10' | Tua video → hỏi khung chat (ví dụ chung chung) → tua lại để đối chiếu |
| P3 | Học viên L3 tự học pre-class buổi tối (~21:30) | **Có** | ~5–6 | 10–15' | Tua video → hỏi khung chat → hỏi thêm ví dụ có số liệu |
| P4 | Học viên L3 xem pre-class ~20:00 | Rất nhẹ | Không nêu số | ~2' | Hỏi AI, tua lại video |
| P5 | Học viên L3 tự xem lại video bài giảng | **Có** | ~5–6 | 2–3' để tìm lại đúng đoạn | Đọc câu trả lời → tự kéo thanh trượt tìm lại đoạn video → đối chiếu slide/code → tự ghi chú |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. "Ban đầu mình tua lại video, sau đó mình sử dụng khung chat để hỏi thêm. Tuy nhiên, câu trả lời khá nhiều chữ và mình vẫn phải tự hình dung." — P3
2. "Mình phải đọc lại câu trả lời và hỏi thêm một ví dụ có số liệu cụ thể thì mới hiểu được cơ bản." — P3
3. "từ nội dung vướng từ ngữ, thuật ngữ bằng tiếng anh tôi lại phải tìm hiểu lại từ đầu" — phiếu khảo sát 27/11 17:59
4. "Hầu như là làm bài lab nào là mình sẽ vướng, bởi vì kiến thức chương trình chạy hơi nhanh." — P1
5. "xem lúc 8h tối, có hỏi AI, trả lời hợp lí đủ hiểu, mất tầm 2p tua lại video, không làm sai trắc nghiệm" — P4 *(ví dụ ngược)*
6. "Mình phải tự kéo thanh trượt trên video lùi lại hoặc nhảy từng đoạn ngắn, nhìn lướt qua slide/hình ảnh trên khung hình xem có giống lúc mình vướng không, rồi bấm nghe lại từ đầu đoạn đó. Thường mất khoảng 2–3 phút, có hôm nhớ mang máng thì mò lâu hơn chút." — P5
7. "Khi nghe lại đúng đoạn đó rồi thì mình mới yên tâm hoặc nhận ra câu trả lời bị thiếu một ý nhỏ, rồi tự ghi chú lại cho mình chứ ít khi gõ hỏi lại thêm." — P5
8. Dòng data `chat=C00485` (23h VN): câu hỏi 15 ký tự, chấm `rubric_bam_bai=0`, nhưng trợ giảng vẫn trả lời 420 ký tự — `evidence/data-mining.md`

## 4. Các nguồn có khớp nhau không

**Data nói:** gần một nửa lượt chat là hỏi nối tiếp ngay trên cùng video, khoảng 1/5 câu trả lời không bám bài nhưng vẫn dài, và 1/5 lượt làm câu kiểm tra sai ở lần đầu.

**Người dùng nói:** người tự học buổi tối gặp khái niệm khó (P2, P3, P5) đọc câu trả lời xong vẫn phải tua lại, tự tìm lại đoạn video, hoặc hỏi thêm. Trong khảo sát, 8/8 người có xem video từng sai câu kiểm tra vì hiểu lệch, và không ai hiểu hẳn ở lần vướng gần nhất.

- **Khớp:**
  - Hành vi tua lại để đối chiếu hoặc hỏi thêm sau khi đọc câu trả lời (P2, P3, P5, 5/8 phiếu) khớp với 47,5% lượt hỏi nối tiếp trong data. P5 cho thấy con số 47,5% còn **đếm thiếu**: P5 tự tìm lại trong video chứ "ít khi gõ hỏi lại", nên những lần kiểm chứng như vậy không xuất hiện trong log chat.
  - Sai câu kiểm tra vì hiểu lệch (8/8 phiếu, P2, P3) khớp với 20,3% sai ở lần làm đầu tiên. Tỉ lệ trong khảo sát cao hơn vì câu 8 hỏi "trong 1 tháng có lần nào", còn data đếm theo từng lượt làm.
- **Lệch:**
  - P4 thấy trợ giảng hiện tại "hợp lí đủ hiểu" với câu hỏi đơn giản lúc 20h. Pain không xảy ra với mọi câu hỏi, mà tập trung vào khái niệm khó hoặc thuật ngữ mới.
  - Nhiều người dùng AI bên ngoài (4/8 phiếu, P1). P1 và 2/10 phiếu còn **không xem video pre-class**. Điều này khớp với data: chỉ 145/436 học viên từng dùng chat.
  - Thời gian mỗi lần cao hơn số nhóm tự ước tính (3 phút): khảo sát cho giá trị giữa 5–15', phỏng vấn trung vị khoảng 6'. Nhóm đã sửa `spec.md` §2 sang 5 phút.
- **Mới, nhóm chưa nghĩ tới:** vướng vì **thuật ngữ tiếng Anh** (phiếu 17:59; P3: "bài có thuật ngữ, công thức"); vướng chuyển sang bài lab hoặc thực hành (P1, P2).

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần.**

- **Ngưỡng đã đặt:**
  - (1) Data có ≥15% câu ngắn hoặc không bám bài → **đạt** (17,1% và 21,3%).
  - (2) ≥2/3 người phỏng vấn đúng vai phải tự kiểm chứng lại sau khi đọc câu trả lời → **đạt**: 3/4 (P2 tua lại đối chiếu, P3 đọc lại và hỏi thêm, P5 tự tìm lại đoạn video). Không tính P2 (AI diễn đạt lại) thì vẫn 2/3.
- **Phần đúng:** với học viên tự học buổi tối gặp khái niệm khó, câu trả lời dài hoặc chung chung khiến họ phải tua lại, tự tìm lại đoạn bài, đọc lại và hỏi thêm (P2, P3, P5, 5/8 phiếu, data 47,5%). Hiểu lệch dẫn tới sai câu kiểm tra (8/8 phiếu, data 20,3%).
- **Phần phải đổi:**
  - Pain không phổ biến với câu hỏi đơn giản (P4), nên trợ giảng cần ưu tiên đúng các khái niệm khó và thuật ngữ.
  - Một phần học viên bỏ qua video hoặc khung chat và dùng AI bên ngoài. Sản phẩm phải tốt hơn ChatGPT ở chỗ **trỏ về đúng đoạn bài** thì mới kéo được nhóm này.

**Điều vẫn chưa biết:**
- Mã đoạn có thật sự rút ngắn việc kiểm chứng hay không. Đã biết một phần: P5 kể phải tự kéo thanh trượt mất 2–3 phút mỗi lần để tìm lại đúng đoạn bài đối chiếu, đúng phần việc mà mã đoạn nhắm tới. Nhưng chưa ai dùng thử bản có mã đoạn, nên cần kiểm ở `validation/log.md`.
- Thời gian mỗi lần trên mẫu khảo sát đủ lớn (≥20 người).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| P1 · học viên L3 ngoài nhóm (TV2 Phong) | 27/11 ~18:15 | ✅ `interviews/P1.md` — không xem video pre-class nên không đúng vai |
| P2 · học viên L3 tự học pre-class buổi tối (TV2 Phong) | 27/11 tối | ✅ `interviews/P2.md` — AI diễn đạt lại, không có trích nguyên văn |
| P3 · học viên L3 tự học pre-class buổi tối (TV3 Lộc) | 27/11 | ✅ `interviews/P3.md` |
| P4 · học viên L3 xem pre-class ~20:00 (TV4 Chiêu) | 27/11 17:30 | ✅ `interviews/P4.md` |
| P5 · học viên L3 tự xem lại video bài giảng (TV2 Phong) | 28/11 ~00:25 | ✅ `interviews/P5.md` — chat 1-1, nguyên văn |
| Khảo sát Google Form (≥20 người) | mở 27/11 17:43 → chốt số liệu 28/11 00:19 | ✅ 15 phiếu, 10 học viên L3 (chưa đạt ngưỡng 20) |
