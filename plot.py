import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mido
import numpy
import time

# List available ports.
print(mido.get_input_names())

# TODO: Update this to get user input.
portname = 'Digital Piano'
start = time.time()

plt.ion()
fig, ax = plt.subplots()
x, y, z = [],[],[]
sc = ax.scatter(x,y)
plt.ylim(0,5)
plt.xlim(20,109)
plt.show(block=False)

def update_plot(msg, time):
    if msg.type == 'note_on':
        print(msg)
        x.append(time)
        y.append(msg.note)
        z.append(max(1, msg.velocity-40)*3)
        sc.set_offsets(numpy.c_[y,x])
        sc.set_sizes(z)
        fig.canvas.draw_idle()
        plt.ylim(time - 15, time+1)
        plt.pause(0.01)


with mido.open_input(portname) as inport:
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity !=0:
            update_plot(msg, time.time() - start)
