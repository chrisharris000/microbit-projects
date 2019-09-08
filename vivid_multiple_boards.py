from microbit import *
import neopixel, math, random

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

    for rotation in range(len(colour_order)):
        for index in range(n_LEDs):
            board_num = index // 7  # determines which board current pixel is on
            pixel_num = index % 7   # determines which pixel on the board the current pixel is
            if board_num in (0, 2):
                if pixel_num in (2,3):
                    np[index] = colour_order[0]
                elif pixel_num in (1,4,6):
                    np[index] = colour_order[1]
                elif pixel_num in (0,5):
                    np[index] = colour_order[2]

            else:
                if pixel_num in (2,3):
                    np[index] = colour_order[3]
                elif pixel_num in (1,4,6):
                    np[index] = colour_order[4]
                elif pixel_num in (0,5):
                    np[index] = colour_order[5]
        np.show()
        colour_order = rotate(colour_order,1)
        sleep(100)

def random_colours():
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)
    unassigned = list(range(n_LEDs))

    while unassigned:
        pixel = random.choice(unassigned)
        colour = random.choice(list(COLOURS.values()))
        np[pixel] = colour
        np.show()
        unassigned.remove(pixel)
        sleep(500)

def colour_wheel(speed):
    colour_list = [COLOURS["red"], COLOURS["yellow"], COLOURS["green"],
                COLOURS["cyan"], COLOURS["blue"], COLOURS["bluemagenta"]]
    n_boards = 4
    n_LEDs = n_boards * 7
    np = neopixel.NeoPixel(pin0, n_LEDs)

    for rotation in range(len(colour_list)):
        for i, colour in enumerate(colour_list):
            np[i] = colour
            np[i + 7] = colour
            np[i + 14] = colour
            np[i + 21] = colour
        np.show()
        sleep(speed)
        colour_list = rotate(colour_list,1)

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

colour_list = [COLOURS["red"], COLOURS["yellow"], COLOURS["green"],
                COLOURS["cyan"], COLOURS["blue"], COLOURS["bluemagenta"]]
colour = colour_list[0]
while True:
    if button_a.was_pressed():
        index = (colour_list.index(colour) - 1) % len(colour_list)
        colour = colour_list[index]

    if button_b.was_pressed():
        index = (colour_list.index(colour) + 1) % len(colour_list)
        colour = colour_list[index]