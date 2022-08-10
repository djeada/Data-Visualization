import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

graph, = ax.plot([], [])
marker, = ax.plot([], [], color='lightblue')

def update_sine(i):
    graph.set_data(x[:i],y[:i])
    marker.set_data(x[i],y[i])

anim = animation.FuncAnimation(fig, update_sine, frames=len(x), interval=50)
plt.show()