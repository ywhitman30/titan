# app.py
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Function to send a message to TinyLlama and get a clean reply
def ask_ai(message):
    import requests

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": message,
                "stream": False
            },
            timeout=120
        )

        data = response.json()
        return data.get("response", "Titan: (No response)")

    except Exception as e:
        return f"Titan: (Error: {e})"
# Routes
@app.route("/")
def home():
    return render_template("chat.html")  # simple chat page

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    reply = ask_ai(user_message)
    return reply

# Run the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
