import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import json

# This script demonstrates the functionallity of the dynamic plot with test data
# Author: Bryan Samuels
# Date 28 Jan 2025

file = "testData.json"
fh = open(file, "r")
# possible xValues 
xVals = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180]
xTicks = [0, 30, 60, 90, 120, 150, 180]
data = json.load(fh)



# set up figure for dynamic plot and customize
fig, ax = plt.subplots()
line, = ax.plot(xVals, data[0], "b-")

ax.set_xticks(xTicks)
ax.set_xlabel('θ (degrees)')
ax.set_ylabel('Signal Strength (dBm)')
ax.set_title('Signal Strength vs. Angle (degrees)')


i = [0]

def update(frame):
    """ Callback Function For Dynamic Data Rendering """
    curr = i[0]
    line.set_data(xVals, data[curr])

    i[0] += 1
    if i[0] >= len(data):
        i[0] = 0  # Reset to loop the animation
    return line,


# Create and run animation
ani = FuncAnimation(fig, update, interval=30, blit=True, cache_frame_data=False)

# Show plot
plt.show()

fh.close()
