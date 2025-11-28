from flask import Flask, render_template, request, jsonify
from model import generate_response
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        if not data or "msg" not in data:
            return jsonify({"response": "❌ No message provided"}), 400
        
        user_msg = data["msg"].strip()
        if not user_msg:
            return jsonify({"response": "❌ Empty message"}), 400
        
        prompt = f"User asked: {user_msg}\nExplain clearly:\n"
        reply = generate_response(prompt)
        
        return jsonify({"response": reply}), 200
    
    except Exception as e:
        error_msg = f"⚠️ Server error: {str(e)}"
        print(f"Error in /ask: {traceback.format_exc()}")
        return jsonify({"response": error_msg}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
