from microbit import *
import neopixel

n_LEDs = 6
np = neopixel.NeoPixel(pin0, n_LEDs)

COLOURS = {"red":(128, 0, 0),
            "orange":(128, 64, 0),
            "yellow":(128, 128, 0),
            "greenyellow":(64, 128, 0),
            "green":(0, 128, 0),
            "greencyan":(0, 128, 64),
            "cyan":(0, 128, 128),
            "bluecyan":(0, 64, 128),
            "blue":(0,0,128),
            "bluemagenta":(128, 0, 128),
            "redmagenta":(128, 0, 64),
            "off": (0, 0, 0),
            "white":(128, 128, 128)}

colour_list = [COLOURS["red"], COLOURS["yellow"], COLOURS["green"],
                COLOURS["cyan"], COLOURS["blue"], COLOURS["bluemagenta"]]
def colour_wheel():
    global colour_list
    for i in range(n_LEDs):
        np[i] = colour_list[i]
    np.show()
    sleep(100)
    colour_list = rotate(colour_list, 1)

def rotate(l, n):
    return l[n:] + l[:n]

while True:
    colour_wheel()