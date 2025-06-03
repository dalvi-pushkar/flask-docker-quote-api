from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "It's not who I am underneath, but what I do that defines me.",
    "Why do we fall? So we can learn to pick ourselves up.",
    "With great power comes great responsibility.",
    "Don’t watch the clock; do what it does. Keep going.",
    "The struggle you're in today is developing the strength you need for tomorrow."
    "Difficult roads often lead to beautiful destinations."
    "Push yourself, because no one else is going to do it for you."
]

@app.route('/quote', methods=['GET'])
def random_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
