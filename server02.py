from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/testservice')
def testservice():
    print("Hello world")
    return Response("DONE", status=200)

@socketio.on('aaa')
def test_connect():
    print("Welcome, aaa received")
    emit('aaa_response', {'data': 'Server'})

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=8080)