const form = document.querySelector("#question-form");
const question = document.querySelector("#question");
const submit = document.querySelector("#submit");
const examples = document.querySelectorAll(".example");
const chat = document.querySelector("#chat-log");
const welcome = document.querySelector("#welcome");
const status = document.querySelector("#status");
const sourceContent = document.querySelector("#source-content");
const chapters = Array.from(document.querySelectorAll(".chapter"));
const cover = document.querySelector("#lesson-cover");
const video = document.querySelector("#lesson-video");
const videoFile = document.querySelector("#video-file");
const pickVideo = document.querySelector("#pick-video");
const mediaStatus = document.querySelector("#media-status");
const isCompact = window.matchMedia("(max-width: 760px)");
let activeCitation;
let activeInlineSource;
let passageRequest = 0;
let videoUrl;

function element(tag, className, text) {
  const node = document.createElement(tag);
  node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function passageView(passage) {
  const view = element("div", "passage");
  view.append(
    element("span", "passage-code", passage.code),
    element("p", "passage-lesson", passage.lesson),
    element("h3", "passage-title", passage.title),
    element("p", "passage-text", passage.text),
  );
  return view;
}

function openPassage(passage, { citation, inlineSource, focus = true } = {}) {
  passageRequest += 1;
  activeCitation?.setAttribute("aria-pressed", "false");
  activeInlineSource?.replaceChildren();
  activeCitation = citation;
  activeInlineSource = inlineSource;
  citation?.setAttribute("aria-pressed", "true");
  chapters.forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.code === passage.code));
  });
  sourceContent.replaceChildren(passageView(passage));
  inlineSource?.replaceChildren(passageView(passage));

  if (!focus) return;
  const visibleSource = isCompact.matches && inlineSource ? inlineSource : sourceContent;
  visibleSource.focus({ preventScroll: true });
  visibleSource.scrollIntoView({ block: "nearest" });
}

async function loadChapter(button, focus = true) {
  const request = ++passageRequest;
  try {
    const response = await fetch(`/api/passages/${button.dataset.code}`);
    if (!response.ok) throw new Error("Đoạn bài học chưa đọc được.");
    const passage = await response.json();
    if (request === passageRequest) openPassage(passage, { focus });
  } catch {
    if (request === passageRequest) {
      sourceContent.replaceChildren(element("p", "source-empty", "Chưa mở được đoạn bài. Thử chọn lại."));
    }
  }
}

chapters.forEach((button) => button.addEventListener("click", () => loadChapter(button)));
loadChapter(chapters[0], false);

pickVideo.addEventListener("click", () => {
  videoFile.value = "";
  videoFile.click();
});
videoFile.addEventListener("change", () => {
  const selected = videoFile.files[0];
  if (!selected) return;
  if (videoUrl) URL.revokeObjectURL(videoUrl);
  videoUrl = URL.createObjectURL(selected);
  video.src = videoUrl;
  video.hidden = false;
  cover.hidden = true;
  pickVideo.textContent = "Đổi video";
  mediaStatus.textContent = "Đang mở video…";
});
video.addEventListener("loadedmetadata", () => { mediaStatus.textContent = "Đang xem video local"; });
video.addEventListener("error", () => {
  if (!videoUrl) return;
  console.warn("Không thể mở video local:", video.error?.message);
  URL.revokeObjectURL(videoUrl);
  videoUrl = undefined;
  video.removeAttribute("src");
  video.hidden = true;
  cover.hidden = false;
  pickVideo.textContent = "Mở video local";
  mediaStatus.textContent = "Video này chưa phát được. Thử tệp MP4 hoặc WebM khác.";
});

function renderAnswer(text, sources, inlineSource) {
  const content = element("p", "message-text");
  const passages = new Map(sources.map((passage) => [passage.code, passage]));
  let cursor = 0;
  for (const match of text.matchAll(/\[(B[0-9]{2}-P[0-9]{2})\]/gi)) {
    const passage = passages.get(match[1].toUpperCase());
    if (!passage) continue;

    content.append(text.slice(cursor, match.index));
    const citation = element("button", "citation", match[0]);
    citation.type = "button";
    citation.setAttribute("aria-label", `Mở đoạn ${passage.code}`);
    citation.setAttribute("aria-pressed", "false");
    citation.addEventListener("click", () => openPassage(passage, { citation, inlineSource }));
    content.append(citation);
    cursor = match.index + match[0].length;
  }
  content.append(text.slice(cursor));
  return content;
}

function appendMessage(role, text, sources = [], isMock = false) {
  const message = element("article", `message ${role}`);
  const isTutor = role === "tutor";
  const label = element("div", "message-label", isTutor ? "Trợ giảng" : "Bạn");
  if (isTutor && isMock) label.append(element("span", "mock-label", "Chế độ giả"));
  message.append(label);
  if (isTutor) {
    const inlineSource = element("div", "inline-source");
    inlineSource.tabIndex = -1;
    message.append(renderAnswer(text, sources, inlineSource), inlineSource);
  } else {
    message.append(element("p", "message-text", text));
  }
  chat.append(message);
  chat.scrollTop = chat.scrollHeight;
  return message;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const text = question.value.trim();
  if (submit.disabled) return;
  if (!text) {
    status.textContent = "Nhập câu hỏi trước khi gửi.";
    question.focus();
    return;
  }

  welcome.hidden = true;
  const sent = appendMessage("learner", text);
  question.value = "";
  question.readOnly = true;
  submit.disabled = true;
  examples.forEach((button) => { button.disabled = true; });
  status.classList.remove("is-error");
  status.textContent = "Trợ giảng đang trả lời…";

  try {
    const response = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: text }),
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error);
    const mockPassage = result.is_mock ? result.sources[0] : undefined;
    const answerText = mockPassage
      ? `Tìm thấy đoạn phù hợp: ${mockPassage.title} [${mockPassage.code}].`
      : result.answer;
    appendMessage("tutor", answerText, result.sources, Boolean(mockPassage));
    status.textContent = "";
  } catch (error) {
    sent.remove();
    welcome.hidden = Boolean(chat.querySelector(".message"));
    question.value = text;
    status.classList.add("is-error");
    status.textContent = error instanceof TypeError ? "Không kết nối được với tutor. Thử gửi lại." : error.message;
  } finally {
    question.readOnly = false;
    submit.disabled = false;
    examples.forEach((button) => { button.disabled = false; });
    question.focus({ preventScroll: true });
  }
});

question.addEventListener("keydown", (event) => {
  if (event.key !== "Enter" || event.shiftKey || event.isComposing) return;
  event.preventDefault();
  if (!submit.disabled) form.requestSubmit();
});

examples.forEach((button) => {
  button.addEventListener("click", () => {
    question.value = button.dataset.question;
    form.requestSubmit();
  });
});
