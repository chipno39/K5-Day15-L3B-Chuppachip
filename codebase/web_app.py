"""Chạy giao diện demo tại http://127.0.0.1:8000 bằng thư viện chuẩn."""

import argparse
import json
import re
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from agent import answer
from ai import MODEL_PROVIDER
from tools import get_passage


WEB_ROOT = Path(__file__).with_name("web")
STATIC_FILES = {
    "/": ("index.html", "text/html"),
    "/app.css": ("app.css", "text/css"),
    "/app.js": ("app.js", "text/javascript"),
}
CITATION = re.compile(r"\[(B[0-9]{2}-P[0-9]{2})\]", re.IGNORECASE)
MAX_BODY_BYTES = 32768
MAX_QUESTION_CHARS = 4000


class DemoHandler(BaseHTTPRequestHandler):
    def send_body(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, data):
        self.send_body(status, "application/json", json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        passage_match = re.fullmatch(r"/api/passages/(B[0-9]{2}-P[0-9]{2})", self.path, re.IGNORECASE)
        if passage_match:
            passage = get_passage(passage_match[1])
            if "error" in passage:
                self.send_json(HTTPStatus.NOT_FOUND, {"error": "Không tìm thấy đoạn bài học."})
            else:
                self.send_json(HTTPStatus.OK, passage)
            return

        asset = STATIC_FILES.get(self.path)
        if asset is None:
            self.send_json(HTTPStatus.NOT_FOUND, {"error": "Không tìm thấy trang."})
            return
        filename, content_type = asset
        self.send_body(HTTPStatus.OK, content_type, (WEB_ROOT / filename).read_bytes())

    def do_POST(self):
        if self.path != "/api/ask":
            self.send_json(HTTPStatus.NOT_FOUND, {"error": "Không tìm thấy đường dẫn."})
            return
        if self.headers.get_content_type() != "application/json":
            self.send_json(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, {"error": "Dữ liệu gửi lên phải là JSON."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= MAX_BODY_BYTES:
                raise ValueError("invalid body length")
            payload = json.loads(self.rfile.read(length))
            question = payload.get("question") if isinstance(payload, dict) else None
            if not isinstance(question, str) or not 0 < len(question.strip()) <= MAX_QUESTION_CHARS:
                raise ValueError("invalid question")
        except (ValueError, UnicodeError):
            self.send_json(HTTPStatus.BAD_REQUEST, {"error": "Nhập câu hỏi từ 1 đến 4.000 ký tự."})
            return

        try:
            output = answer(question.strip())["output"]
            codes = dict.fromkeys(code.upper() for code in CITATION.findall(output))
            sources = []
            for code in codes:
                passage = get_passage(code)
                if "error" not in passage:
                    sources.append(passage)
        except Exception:
            self.send_json(HTTPStatus.BAD_GATEWAY, {"error": "Tutor chưa trả lời được. Kiểm tra cấu hình model rồi thử lại."})
            return

        self.send_json(HTTPStatus.OK, {"answer": output, "sources": sources, "is_mock": MODEL_PROVIDER == "fake"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    with ThreadingHTTPServer(("127.0.0.1", args.port), DemoHandler) as server:
        print(f"UI demo: http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
