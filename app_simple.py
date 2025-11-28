"""
Simple Flask AI Chat App - Minimal dependencies
"""
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

# Knowledge base
RESPONSES = {
    "hello": ["Hello! 👋 How can I help?", "Hi there! What's up?"],
    "hi": ["Hey! What do you need?", "Hi! Nice to see you!"],
    "how are you": ["I'm doing great! How about you?", "All systems go! Ready to help!"],
    "python": ["Python is awesome! 🐍 What would you like to know?", "Python is my favorite! Ask away!"],
    "code": ["I love coding! What do you want to build?", "Let's code something cool! 🚀"],
    "bye": ["Goodbye! See you later!", "Take care! 👋"],
    "thanks": ["You're welcome! 😊", "Happy to help!"],
    "help": ["I'm here to help! Ask me anything about programming or code.", "What do you need help with?"],
}

DEFAULT = [
    "That's interesting! 🤔 Tell me more!",
    "I got it. What else?",
    "Nice! Anything else you'd like to know?",
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        msg = data.get("msg", "").lower().strip()
        
        if not msg:
            return jsonify({"response": "Please type something! 😊"}), 400
        
        # Find matching response
        response = None
        for keyword, responses in RESPONSES.items():
            if keyword in msg:
                response = random.choice(responses)
                break
        
        if not response:
            response = random.choice(DEFAULT) + f"\n\nYou said: {data.get('msg', '')[:40]}"
        
        return jsonify({"response": response}), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": f"⚠️ Error: {str(e)}"}), 500

if __name__ == "__main__":
    print("🚀 Starting Flask app on http://0.0.0.0:8080")
    try:
        app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False, threaded=True)
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        import traceback
        traceback.print_exc()
