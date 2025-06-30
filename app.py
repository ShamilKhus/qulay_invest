# app.py
from flask import Flask, request, jsonify, send_from_directory
from AI_agent import qulay_invest_chat

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_home():
    return send_from_directory('.', 'index.html')

@app.route('/health', methods=['GET'])
def health():
    # A simple check that the AI function is importable and responding
    test_reply = qulay_invest_chat("Hello")
    # We expect either a proper AI reply or our beta-notice; anything non-error is fine
    status = "ok" if "beta test" in test_reply or "savollarga yordam bera" in test_reply else "error"
    return jsonify({'status': status, 'test_reply': test_reply})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    response = qulay_invest_chat(question)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
