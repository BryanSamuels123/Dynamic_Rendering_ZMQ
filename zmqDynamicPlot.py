import zmq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import MultipleLocator, FuncFormatter

# This script demonstrates how to use ZMQ with matplotlib's animated graphs.
# Author: Bryan Samuels
# Date 28 Jan 2025

IP = "192.168.4.70"
PORT = "6080"

REFRESH_PERIOD = 30 
"""Value in ms"""

# set up ZMQ subscriber  
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{IP}:{PORT}")
socket.setsockopt(zmq.SUBSCRIBE, b"")

# set xValues for plotting
xVals = np.linspace(0, np.pi, 31)

# set figure for dynamic plot and customize
fig, ax = plt.subplots()
line, = ax.plot(xVals, np.zeros_like(xVals), "b-")


# format x-axis with π ticks
ax.xaxis.set_major_locator(MultipleLocator(np.pi / 6))
ax.xaxis.set_major_formatter(FuncFormatter(lambda val, pos: f"{int(round(val / np.pi * 6))}π/6" if val != 0 else "0"))


# add labels
ax.set_xlabel('θ (rads)')
ax.set_ylabel('Signal Strength (dBm)')
ax.set_title('Signal Strength vs. Angle')
ax.set_ylim(-1.25, 1.25)

# set index to handle rolling the received values (needed because current values are the same each time)
index = 0

def scramble(yVals):
    """Function to add Dynamism to the data"""
    shift_size = (index % 200) * 0.4 # roll the data based on this size
    shifted_data = np.roll(yVals, -shift_size)

    return shifted_data



def update(frame):
    """Callback Function for Dynamic Rendering and Reading from the ZMQ"""
    
    # define the index used here as the global one
    global index

    # try reading from the buffer
    try:
        raw_data = socket.recv()
        data = np.frombuffer(raw_data, dtype=np.float32)
        
        shifted_data = scramble(data)
        # print(shifted_data)

        line.set_data(xVals, shifted_data.tolist()[:31])
        index += 1 
        # uncomment to use pure data from socket.
        # line.set_data(xVals, data.tolist()[:31])


    # print the error for logging if error
    except Exception as e:
        print(f"Error: {e}")
    
    # comma makes return a tuple instead of just a val
    # FuncAnimation Requires this
    return line,

# Create and run animation
ani = FuncAnimation(fig, update, interval=REFRESH_PERIOD, blit=True, cache_frame_data=False)

# Show plot
plt.show()

