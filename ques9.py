import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3 * np.pi, 100)
sin_y = np.sin(x)
cos_y = np.cos(x)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))

ax[0].plot(x, sin_y, color='red', label='Sine')
ax[0].set_xlabel('Angle (in radians)')
ax[0].set_ylabel('Value')
ax[0].set_title('Sine Function')
ax[0].legend()

ax[1].plot(x, cos_y, color='blue', label='Cosine')
ax[1].set_xlabel('Angle (in radians)')
ax[1].set_ylabel('Value')
ax[1].set_title('Cosine Function')
ax[1].legend()

plt.show()
