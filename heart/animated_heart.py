import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('black')
line, = ax.plot([], [], color='cyan', linewidth=2, glow=True)

t = np.linspace(0, 2 * np.pi, 100)
x, y = heart_shape(t)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_alpha(min(1, frame / 20))  # Gradually increase opacity like a firework
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=50)
plt.show()
