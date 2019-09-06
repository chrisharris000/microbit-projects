from microbit import *
import neopixel, math

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

def colour_flow(speed):
    colour_list = [COLOURS["red"],  COLOURS["yellow"],
                COLOURS["greencyan"], COLOURS["bluemagenta"]]
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)
    for i in range(n_boards):
        for i in range(n_boards):
            set_board(colour_list[i], i, np)
        sleep(speed)
        colour_list = rotate(colour_list, 1)

def flash(colour, speed):
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)
    for i in range(7):
        fill(n_LEDs, colour, np)
        np.show()
        sleep(speed)
        r, g, b = colour
        colour = (r//2, g//2, b//2)

def progressive_fill(colour, speed, undo_fill = False, clear_all = False, increasing = False):
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)

    for i in range(n_LEDs):
        np[i] = colour
        if not increasing:
            sleep(speed)
        else:
            k = -math.log(1/3)/(7*n_boards)
            t = i
            wait_time = speed * math.exp(-k*t)
            sleep(wait_time)
        np.show()

    if undo_fill:
        for i in range(n_LEDs):
            np[n_LEDs - i - 1] = COLOURS["off"]
            np.show()
            sleep(speed)

    elif clear_all:
        for i in range(n_LEDs):
            np[i] = COLOURS["off"]
        np.show()

    else:
        for i in range(n_LEDs):
            np.show()
            np[i] = COLOURS["off"]

def smooth_rainbow():
    colour_order = [COLOURS["red"],COLOURS["yellow"],COLOURS["green"],
                    COLOURS["cyan"],COLOURS["blue"],COLOURS["redmagenta"]]

    pixel_order = [[2,3],[1,4,6],[0,5]] # 0 indexed
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)

def set_board(colour, board_num, np):
    for i in range(7):
        np[board_num*7 + i] = colour
    np.show()

def rotate(l, n):
    return l[n:] + l[:n]

def fill(n_LEDs, colour, np):
    for i in range(n_LEDs):
        np[i] = colour
    return np

while True:
    smooth_rainbow()