import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,  3* np.pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y, label='Sine')
plt.plot(x, cos_y, label='Cosine')
plt.xlabel('Angle (in radians)')
plt.ylabel('Value')
plt.title('Sine and Cosine functions')
plt.legend()
plt.show()

data = np.random.rand(100, 3)

flattened_data = data.flatten()

plt.hist(flattened_data, bins=30)

plt.xlabel('Data values')

plt.ylabel('Frequency')

plt.title('Histogram of data from random matrix')

plt.show()
