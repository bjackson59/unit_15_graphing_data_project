# Brianna Jackson
# 4/27/2025
# Creating a sine wave graph that displays air pressure over time

import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 3.0, 0.01)
air_pressure = 0.5 + np.sin(3.0 * time)
# y = sin(x)

plt.plot(time, air_pressure)

plt.show()