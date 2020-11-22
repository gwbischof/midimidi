import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mido
import numpy
import time

# List available ports.
print(mido.get_input_names())

# TODO: Update this to get user input.
portname = 'Digital Piano'

fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y)
plt.xlim(0,20)
plt.ylim(0,120)
plt.show()

def update_plot(msg):
    if msg.type == 'note_on':
        if msg.velocity == 0:
            return
        x.append(time.time() - start)
        y.append(msg.note)
        sc.set_offsets(np.c_[x,y])
        fig.canvas.draw_idle()

port = mido.open_input(portname, callback=update_plot)
