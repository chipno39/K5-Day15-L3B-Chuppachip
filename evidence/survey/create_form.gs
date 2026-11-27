/**
 * Tạo Google Form khảo sát Track A1 (Chuppachip) + Sheet nhận kết quả.
 * Cách chạy: script.google.com → New project → dán file này → chọn hàm createSurvey → Run
 * → cấp quyền → xem link ở View → Logs (Ctrl+Enter).
 * Bộ câu hỏi giữ khớp với evidence/survey/questions.md.
 */
function createSurvey() {
  var form = FormApp.create('Khảo sát nhanh (2–3 phút): Lần gần nhất bạn tự học video pre-class');
  form.setDescription(
    'Chào bạn, nhóm Chuppachip (L3B) đang tìm hiểu chuyện thật xảy ra khi học viên tự học video pre-class. ' +
    'Khảo sát ẩn danh, khoảng 2–3 phút, chỉ hỏi về những lần đã xảy ra. ' +
    'Không thu tên, email, mã học viên. Thành viên nhóm Chuppachip không tham gia. ' +
    'Nếu câu 2 chọn "Chưa bao giờ tự xem" thì form kết thúc luôn.'
  );
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setConfirmationMessage('Cảm ơn bạn đã dành thời gian giúp nhóm Chuppachip!');

  // --- Mục 1: lọc người ---
  form.addMultipleChoiceItem()
    .setTitle('1. Bạn là:')
    .setChoiceValues(['Học viên L3A', 'Học viên L3B', 'Lab coach / TA', 'Giảng viên', 'Khác'])
    .setRequired(true);

  var q2 = form.addMultipleChoiceItem()
    .setTitle('2. Lần gần nhất bạn tự xem một video pre-class là khi nào?')
    .setRequired(true);

  // --- Mục 2: lần gần nhất ---
  form.addPageBreakItem().setTitle('Lần gần nhất bạn tự học pre-class');

  form.addTextItem()
    .setTitle('3. Trong 1 tuần qua, có bao nhiêu lần bạn xem pre-class mà gặp chỗ chưa hiểu?')
    .setHelpText('Ghi một số. Không nhớ chính xác thì ước chừng. Không lần nào thì ghi 0.')
    .setValidation(FormApp.createTextValidation()
      .setHelpText('Nhập một số từ 0 đến 50')
      .requireNumberBetween(0, 50)
      .build())
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('4. Lần gần nhất bạn gặp chỗ chưa hiểu trong video pre-class, bạn đã làm gì?')
    .setHelpText('Chọn tất cả những gì bạn đã làm lần đó.')
    .setChoiceValues([
      'Tua lại video',
      'Hỏi ở khung chat dưới video',
      'Hỏi trên Discord / hỏi TA',
      'Hỏi bạn cùng lớp',
      'Hỏi ChatGPT / công cụ AI khác bên ngoài',
      'Đọc lại tài liệu / slide',
      'Bỏ qua, học tiếp',
      'Không nhớ / chưa gặp lần nào'
    ])
    .showOtherOption(true)
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('5. Nếu lần đó bạn có hỏi ở khung chat dưới video: đọc câu trả lời xong bạn làm gì tiếp?')
    .setChoiceValues([
      'Hiểu luôn, học tiếp',
      'Hỏi thêm câu nữa trong khung chat',
      'Tua lại video để đối chiếu',
      'Hỏi ở chỗ khác (Discord, bạn bè, công cụ khác)',
      'Bỏ qua',
      'Lần đó không hỏi khung chat'
    ])
    .showOtherOption(true)
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle('6. Lần đó, từ lúc vướng đến lúc hiểu (hoặc bỏ qua) mất khoảng bao lâu?')
    .setChoiceValues(['Dưới 2 phút', '2–5 phút', '5–15 phút', '15–30 phút', 'Trên 30 phút', 'Không nhớ'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('7. Lần đó cuối cùng bạn có hiểu được chỗ đó không?')
    .setChoiceValues(['Hiểu hẳn', 'Hiểu một phần', 'Không, bỏ qua'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('8. Trong 1 tháng qua, có lần nào bạn trả lời sai câu kiểm tra cuối bài pre-class rồi mới nhận ra mình hiểu lệch nội dung video không?')
    .setChoiceValues(['Có, từ 2 lần trở lên', 'Có, 1 lần', 'Không', 'Không nhớ'])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('9. Điều gì khiến bạn khó chịu nhất ở lần vướng gần nhất đó?')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('10. Nếu còn nhớ: lúc vướng bạn đã gõ câu hỏi gì? Viết lại đại khái.')
    .setHelpText('Đừng ghi tên hay thông tin cá nhân. Nhóm có thể dùng câu này (đã ẩn danh) làm câu thử.')
    .setRequired(false);

  // --- Mục 3: liên hệ (tuỳ chọn) ---
  form.addPageBreakItem().setTitle('Gần xong rồi');

  form.addTextItem()
    .setTitle('11. (Tuỳ chọn) Bạn có sẵn lòng cho nhóm hỏi thêm 10 phút, hoặc dùng thử bản thử vào chiều mai không? Nếu có, để lại tên Discord.')
    .setHelpText('Không bắt buộc. Chỉ dùng để liên hệ, không công bố.')
    .setRequired(false);

  // Câu 2 rẽ nhánh: chưa từng tự xem thì nộp luôn.
  var go = FormApp.PageNavigationType.CONTINUE;
  q2.setChoices([
    q2.createChoice('Hôm nay', go),
    q2.createChoice('Trong tuần này', go),
    q2.createChoice('Tuần trước', go),
    q2.createChoice('Lâu hơn', go),
    q2.createChoice('Chưa bao giờ tự xem', FormApp.PageNavigationType.SUBMIT)
  ]);

  var ss = SpreadsheetApp.create('Kết quả khảo sát pre-class (Chuppachip)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  // Form tạo bằng script có thể ở trạng thái chưa xuất bản.
  if (typeof form.setPublished === 'function') form.setPublished(true);

  Logger.log('Link gửi mọi người: ' + form.getPublishedUrl());
  Logger.log('Link sửa form:      ' + form.getEditUrl());
  Logger.log('Sheet kết quả:      ' + ss.getUrl());
}
