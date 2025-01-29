import zmq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This test script demonstrates how to connect to a ZMQ.
# Author: Bryan Samuels
# Date 28 Jan 2025

IP = "192.168.4.70"
PORT = "6080"

# set up ZMQ subscriber  
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{IP}:{PORT}")
socket.setsockopt(zmq.SUBSCRIBE, b"")


# remove break to continue printing the values
while True:
    try:
        # Receive raw bytes
        raw_data = socket.recv()

        # Convert bytes to numpy array (change format based on data type in GNU Radio)
        data = np.frombuffer(raw_data, dtype=np.float32)  # Change dtype as needed
        
        # print the received data
        print(data.tolist()[:31])
        break

    except KeyboardInterrupt:
        print("\nStopped.")
        break
