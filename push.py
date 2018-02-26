import zmq
import time
context = zmq.Context()

socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5555")

for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"Hello from pusher")
    time.sleep(1)


