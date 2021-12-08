from flask import Flask, jsonify
import json


app = Flask(__name__)

greetings = {
    "hello": "Hey bud, how are you doing?",
    "привет": "Здорово, чувак, как делища?" #с русским не работает, надо разибраться с ascii и как его отключить
}

@app.route('/api/v1/greetings/daria/', methods=['GET'])
def hello():
    return greetings['hello']


if __name__ == '__main__':
    app.run(debug=True)
