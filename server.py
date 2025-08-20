# server.py
# Flask app for emotion detection
from flask import Flask, request, jsonify
from emotion_app import emotion_predictor

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
