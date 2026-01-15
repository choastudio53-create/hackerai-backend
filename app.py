from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("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")

SYSTEM_PROMPT = """
You are a hacker-style AI assistant.
Speak Bangla and English.
Teach ethical hacking, cybersecurity, Linux, Termux.
No illegal hacking or fraud.
"""

@app.route("/")
def home():
    return "HackerAI Backend Running"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ]
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        json=payload,
        headers=headers,
        timeout=60
    )

    reply = r.json()["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
