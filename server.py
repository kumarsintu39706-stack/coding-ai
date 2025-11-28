#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Ultra-simple working Flask server"""
import sys
import io
import os

# Fix Windows encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Disable Flask logging to avoid encoding issues
os.environ['WERKZEUG_LOG_FORMAT'] = '%(message)s'

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple knowledge base
responses = {
    "hello": "Hi! How can I help?",
    "hi": "Hello there!",
    "how": "I'm doing great!",
    "python": "Python is awesome!",
    "code": "I can help with code!",
    "time": "It's 3:30 PM",
}

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error loading home: {e}", 500

@app.route("/ask", methods=["GET", "POST"])
def ask():
    try:
        # Handle both GET and POST
        if request.method == "GET":
            msg = request.args.get("msg", "").lower().strip()
        else:
            data = request.get_json() or {}
            msg = str(data.get("msg", "")).lower().strip()
        
        if not msg:
            return jsonify({"response": "Please send a message"}), 400
        
        # Find matching response
        for key in responses:
            if key in msg:
                return jsonify({"response": responses[key]})
        
        return jsonify({"response": "I don't know about that. Try: hello, python, code"})
    
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return jsonify({"response": f"Error: {type(e).__name__}: {str(e)}"}), 500

if __name__ == "__main__":
    try:
        print("Starting server on http://localhost:5000")
        print("Visit: http://localhost:5000")
        print("Send requests to: http://localhost:5000/ask")
        app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False, threaded=False)
    except KeyboardInterrupt:
        print("\nServer stopped")
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
