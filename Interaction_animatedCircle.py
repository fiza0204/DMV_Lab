import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial position
x = 5
y = 5

fig, ax = plt.subplots()
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Animation function
def update(frame):
    circle.center = (x, y)
    return circle,

# Key press event
def on_key(event):
    global x, y
    
    if event.key == 'up':
        y += 0.5
    elif event.key == 'down':
        y -= 0.5
    elif event.key == 'left':
        x -= 0.5
    elif event.key == 'right':
        x += 0.5

fig.canvas.mpl_connect('key_press_event', on_key)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.title("Animated Circle with Keyboard Interaction")
plt.show()