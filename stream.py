import mido
import time

# Need to update the port name.
# List available ports.
print(mido.get_input_names())
portname = 'Digital Piano'

with mido.open_input(portname) as inport:
    for msg in inport:
        if msg.type != 'clock':
            print(msg)
