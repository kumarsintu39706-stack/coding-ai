"""
Simple AI response generator without heavy dependencies
Uses pattern matching for quick responses
"""

import random
from datetime import datetime

# Knowledge base for responses
KNOWLEDGE_BASE = {
    "hello": [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! Nice to meet you. What can I do for you?"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking. How about you?",
        "I'm functioning perfectly! Ready to help you with anything.",
        "All systems operational! How can I assist?"
    ],
    "name": [
        "I'm an AI assistant created to help you. You can call me AI!",
        "I'm your friendly AI assistant here to help!",
        "Just call me AI - that's what I'm here for!"
    ],
    "time": [
        f"The current time is {datetime.now().strftime('%H:%M:%S')}",
        f"It's currently {datetime.now().strftime('%I:%M %p')}",
        f"The time is {datetime.now().strftime('%H:%M')}"
    ],
    "code": [
        "Here's a simple Python example:\n\n```python\ndef hello_world():\n    print('Hello, World!')\nhello_world()\n```\n\nWould you like me to explain or create something specific?",
        "Code examples are my specialty! What programming language or concept would you like help with?",
        "I can help with code! What would you like to code today?"
    ],
    "python": [
        "Python is a great language! It's known for being simple and readable.\n\n```python\n# Simple Python example\nfor i in range(5):\n    print(f'Count: {i}')\n```",
        "Python is awesome! Do you need help with:\n- Loops and functions?\n- Data structures?\n- Web development?\n- Data analysis?",
        "Python lovers unite! 🐍 What would you like to learn?"
    ],
    "javascript": [
        "JavaScript powers the web! Here's a simple example:\n\n```javascript\nconst greeting = () => console.log('Hello!');\ngreeting();\n```",
        "JS is everywhere - browsers, servers, apps! What do you want to build?",
        "JavaScript is fun and flexible. What project are you working on?"
    ],
    "help": [
        "I'm here to help! You can ask me about:\n- Programming languages\n- Code examples\n- General questions\n- And more!\n\nWhat do you need?",
        "I can assist with many topics! Try asking about code, programming, or any general question.",
        "How can I help you today? Ask me anything!"
    ],
    "thanks": [
        "You're welcome! Feel free to ask me anything else.",
        "Happy to help! Let me know if you need anything else.",
        "Anytime! What else can I do for you?"
    ]
}

def get_simple_response(user_input: str) -> str:
    """Generate a response based on user input"""
    user_lower = user_input.lower().strip()
    
    # Check for exact or partial matches
    for keyword, responses in KNOWLEDGE_BASE.items():
        if keyword in user_lower:
            return random.choice(responses)
    
    # Default response for unknown queries
    default_responses = [
        "That's interesting! I understand you're asking about: " + user_input[:50] + "\n\nI'm a simple AI, so I work best with specific questions about code, programming, or general knowledge.",
        f"Interesting question! 🤔 While I don't have a specific answer for '{user_input[:40]}...', I can help with programming topics or general questions.",
        "I'm still learning! 📚 Try asking me about programming, code examples, or other topics in my knowledge base.",
        f"You asked: '{user_input[:40]}...'\n\nWhile that's outside my main expertise, feel free to ask about code or programming!",
    ]
    return random.choice(default_responses)

def generate_response(prompt: str) -> str:
    """Main function called by Flask app"""
    try:
        # Extract user message from prompt
        if "User asked:" in prompt:
            user_msg = prompt.split("User asked:")[1].strip().split("\n")[0]
        else:
            user_msg = prompt
        
        response = get_simple_response(user_msg)
        return response if response else "I'm not sure about that. Can you ask me something specific about programming or code?"
    
    except Exception as e:
        return f"Got an error: {str(e)}\n\nTry asking a simpler question!"

