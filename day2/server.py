import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
messages = [
    {'username': 'jack', 'text': 'Hello', 'time': time.time()},
    {'username': 'mary', 'text': 'Hi, jack!', 'time': time.time()}
]
users = {
    # username: password
    'jack': 'black',
    'mary': '12345'
}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/history")
def history():
    """
    request: ?after=1234567890.4567
    response: {
        "messages": [
            {"username": "str", "text": "str", "time": float},
            ...
        ]
    }
    """
    after = float(request.args['after'])

    # filtered_messages = []
    # for message in messages:
    #     if after < message['time']:
    #         filtered_messages.append(message)

    filtered_messages = [m for m in messages if after < m['time']]

    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send():
    """
    request: {"username": "str", "password": "str", "text": "str"}
    response: {"ok": true}
    """
    data = request.json  # JSON -> dict
    username = data['username']
    password = data['password']
    text = data['text']

    # если такой пользователь существует -> проверим пароль
    # иначе мы зарегистрируем его
    if username in users:
        real_password = users[username]
        if real_password != password:
            return {"ok": False}
    else:
        users[username] = password

    new_message = {'username': username, 'text': text, 'time': time.time()}
    messages.append(new_message)

    return {"ok": True}


app.run()
