import sys
import zmq

topic = "1"

context = zmq.Context()

socket = context.socket(zmq.SUB)
#socket.connect("tcp://localhost:5556")
socket.connect("tcp://10.40.1.43:5556")

socket.setsockopt_string(zmq.SUBSCRIBE, topic)

while True:
    string = socket.recv_string()
    Topic, data = string.split()

    print("Topic {0} -> {1} received".format(Topic, data))