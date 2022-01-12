import zmq
import time

from zmq.sugar import context
context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

i = 1

while True:

    i += 1

    for topic in range(1,4):
        data = topic * i
        socket.send_string("{0} {1}".format(topic, data))
        print("Topic {0} -< {1} sent".format(topic, data))

        time.sleep(1)