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

x = [0,0]

def print_diff(msg, time):
        x.append(time)
        print(x[-1] - x[-2])


with mido.open_input(portname) as inport:
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity !=0:
            print_diff(msg, time.time() - start)
