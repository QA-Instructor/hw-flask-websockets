from flask_socketio import SocketIO
from flask import Flask, Response
from flask_cors import CORS
from flask_socketio import send, emit
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/testservice')
def testservice():
    print("Hello world")
    return Response("DONE", status=200)

@socketio.on('message')
def handle_message(message):
    send(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('my-event')
def handle_my_custom_event():
    #emit('my response', json)
    emit('aaa_response', {'data': 'Server'})
    send("hello world")


if __name__ == '__main__':
    print(f"started at {time.strftime('%X')}")
    socketio.run(app, host="0.0.0.0", port=8080)