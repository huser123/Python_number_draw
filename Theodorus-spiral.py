import matplotlib.pyplot as plt
import matplotlib.animation as animation

def next_vertex(x, y):
    h = (x**2 + y**2)**0.5
    return (x - y/h, y + x/h)

fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.axis('off')

xdata, ydata = [0, 1], [0, 0]

def init():
    ax.plot([0, 1], [0, 0])
    return []

def update(frame):
    global xdata, ydata
    x_old, y_old = xdata[-1], ydata[-1]
    x_new, y_new = next_vertex(x_old, y_old)
    # draw short side
    ax.plot([x_old, x_new], [y_old, y_new], 'bo-')
    # draw hypotenuse
    ax.plot([0, x_new], [0, y_new], 'bo-')
    xdata.append(x_new)
    ydata.append(y_new)
    return []

ani = animation.FuncAnimation(fig, update, frames=range(1, 400), init_func=init, blit=False, repeat=False)
plt.show()
