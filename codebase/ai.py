"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá:
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng

Hỗ trợ sẵn:
    - MODEL_PROVIDER=fake   (mặc định khi chưa điền .env — chế độ giả cho CP2)
    - MODEL_PROVIDER=gemini (Google Gemini API qua urllib chuẩn, không cần pip install)
    - MODEL_PROVIDER=openai (OpenAI / nhà cung cấp tương thích Chat Completions)
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOW_RAW = False  # đổi thành True nếu cần in nguyên JSON phản hồi khi debug


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()

GEMINI_API_KEY = (os.environ.get("GEMINI_API_KEY") or (API_KEY if MODEL_PROVIDER == "gemini" else "")).strip()
GEMINI_MODEL_NAME = (os.environ.get("GEMINI_MODEL_NAME") or (MODEL_NAME if MODEL_PROVIDER == "gemini" else "gemini-2.5-flash-lite")).strip()

OPENAI_API_KEY = (os.environ.get("OPENAI_API_KEY") or (API_KEY if MODEL_PROVIDER == "openai" else "")).strip()
OPENAI_MODEL_NAME = (os.environ.get("OPENAI_MODEL_NAME") or (MODEL_NAME if MODEL_PROVIDER == "openai" else "gpt-4o-mini")).strip()


def post_json(url: str, headers: dict, body: dict, timeout: int = 60) -> dict:
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers),
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def call_gemini(system: str, user: str) -> dict:
    """Gọi Google Gemini REST API (generateContent), lấy token thật từ usageMetadata."""
    key = GEMINI_API_KEY or API_KEY
    if not key:
        raise RuntimeError("Thiếu API_KEY hoặc GEMINI_API_KEY trong file .env.")
    model = GEMINI_MODEL_NAME or MODEL_NAME or "gemini-2.5-flash-lite"
    url = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % model
    body = {
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 1024},
    }
    if system:
        body["system_instruction"] = {"parts": [{"text": system}]}

    data = post_json(url, {"x-goog-api-key": key}, body)
    candidates = data.get("candidates") or []
    parts = (candidates[0].get("content", {}).get("parts") or []) if candidates else []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought")).strip()
    if not text and parts:
        text = "".join(p.get("text", "") for p in parts).strip()

    usage = data.get("usageMetadata") or {}
    tokens_in = int(usage.get("promptTokenCount") or 0)
    tokens_out = int(usage.get("candidatesTokenCount") or 0) + int(usage.get("thoughtsTokenCount") or 0)
    return {"text": text, "model": model, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_openai(system: str, user: str) -> dict:
    """Gọi OpenAI Chat Completions (hoặc API tương thích OpenAI qua OPENAI_BASE_URL)."""
    key = OPENAI_API_KEY or API_KEY
    if not key:
        raise RuntimeError("Thiếu API_KEY hoặc OPENAI_API_KEY trong file .env.")
    model = OPENAI_MODEL_NAME or MODEL_NAME or "gpt-4o-mini"
    url = (os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1/chat/completions").strip()
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(url, {"Authorization": "Bearer " + key}, {"model": model, "messages": messages})
    u = data.get("usage") or {}
    return {
        "text": data["choices"][0]["message"]["content"],
        "model": model,
        "tokens_in": int(u.get("prompt_tokens") or 0),
        "tokens_out": int(u.get("completion_tokens") or 0),
    }


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    if MODEL_PROVIDER == "gemini":
        try:
            return call_gemini(system, user)
        except Exception as e:
            if OPENAI_API_KEY:
                print(f"[ai.py] Gemini gặp lỗi ({e}), tự động chuyển sang OpenAI ({OPENAI_MODEL_NAME})...")
                return call_openai(system, user)
            raise

    if MODEL_PROVIDER == "openai":
        try:
            return call_openai(system, user)
        except Exception as e:
            if GEMINI_API_KEY:
                print(f"[ai.py] OpenAI gặp lỗi ({e}), tự động chuyển sang Gemini ({GEMINI_MODEL_NAME})...")
                return call_gemini(system, user)
            raise

    raise NotImplementedError(
        "Chưa hỗ trợ MODEL_PROVIDER=%s trong codebase/ai.py — hỗ trợ: fake, gemini, openai."
        % MODEL_PROVIDER
    )
