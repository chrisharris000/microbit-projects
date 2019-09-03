from microbit import *
import neopixel

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

colour_list = [COLOURS["red"],  COLOURS["green"],
                COLOURS["cyan"], COLOURS["bluemagenta"]]

def colour_flow():
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)
    for i in range(n_boards):
        for i in range(n_boards):
            set_board(colour_list[i], i*7, np)
        sleep(500)
        rotate(colour_list, 1)

def set_board(colour, index, np):
    for i in range(7):
        np[index + i] = colour
    np.show()

def rotate(l, n):
    return l[n:] + l[:n]

while True:
    colour_flow()