from flask import Flask

app_service = Flask(__name__)

greetings = {
    "hello": "Hey bud, how are you doing?",
    "привет": "Здорово, чувак, как делища?" #с русским не работает, надо разибраться с ascii и как его отключить
}

@app_service.route('/api/v1/greetings/daria/', methods=['GET'])
def hello():
    return greetings['hello']
