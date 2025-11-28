#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple test to debug the issue"""
import sys
import io

# Fix Windows encoding issues
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 50)
print("Testing imports...")
print("=" * 50)

try:
    from flask import Flask
    print("✓ Flask imported")
except Exception as e:
    print(f"✗ Flask import failed: {e}")
    exit(1)

try:
    from model import generate_response
    print("✓ Model imported")
except Exception as e:
    print(f"✗ Model import failed: {e}")
    exit(1)

print("\n" + "=" * 50)
print("Creating Flask app...")
print("=" * 50)

app = Flask(__name__)

@app.route("/test")
def test():
    return {"status": "OK"}

@app.route("/ask", methods=["POST"])
def ask():
    from flask import request
    try:
        data = request.get_json()
        msg = data.get("msg", "")
        print(f"[*] Received message: '{msg}'")
        response = generate_response(f"User asked: {msg}")
        print(f"[*] Generated response: '{response}'")
        return {"response": response}
    except Exception as e:
        print(f"[ERROR] Exception in /ask: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return {"response": f"Server error: {str(e)}"}, 500

print("✓ Routes created")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Starting server on http://localhost:5000")
    print("=" * 50)
    try:
        app.run(host="127.0.0.1", port=5000, debug=False)
    except Exception as e:
        print(f"✗ Server failed: {e}")
        import traceback
        traceback.print_exc()
