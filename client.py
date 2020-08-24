#from flask_socketio import SocketIO
from flask import Flask, Response
from flask_cors import CORS
from flask_socketio import send, emit
import time
import socketio
import asyncio

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# sockio = SocketIO(app)

sio = socketio.AsyncClient()
eventLoop = asyncio.get_event_loop()

async def test_send():
    print("Sending data...")
    await sio.connect('http://localhost:8080')
    sio.send("Hello from client", namespace="/testio")

if __name__ == '__main__':
    print(f"started at {time.strftime('%X')}")
    asyncio.run(test_send())
    print(f"completed at {time.strftime('%X')}")


