from microbit import *
import neopixel, time

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

def colour_wheel(speed):
    # 6 colours cycle around the outside 6 LEDs on 1 board
    global colour_list
    n_LEDs = 6
    np = neopixel.NeoPixel(pin0, n_LEDs)
    np = list_to_np(colour_list, np)
    np.show()
    sleep(speed)
    colour_list = rotate(colour_list, 1)

def flash(colour, speed):
    # colour starts out at given brightness and is halved for each number of LEDs
    # using 50 or 100 as speed gives a good effect
    n_LEDs = 7
    np = neopixel.NeoPixel(pin0, n_LEDs)
    for i in range(n_LEDs):
        fill(n_LEDs, colour, np)
        np.show()
        sleep(speed)
        r, g, b = colour
        colour = (r//2, g//2, b//2)

def spiral(colour, speed, dim=False):
    # chosen colour spirals on outside LEDs
    # LEDs can be dimmed as the spiral
    n_LEDs = 6
    np = neopixel.NeoPixel(pin0, n_LEDs)
    spiral_list = [COLOURS["off"] for x in range(n_LEDs)]
    spiral_list[0] = colour
    for i in range(n_LEDs):
        np = list_to_np(spiral_list, np)
        np.show()
        spiral_list = rotate(spiral_list, 1)

        if dim:
            for i in range(n_LEDs):
                r, g, b = spiral_list[i]
                spiral_list[i] = (r//2, g//2, b//2)

        sleep(speed)

def line_rotate(colour, speed):
    # pin wheel style effect
    np = neopixel.NeoPixel(pin0, 7)
    effect = [COLOURS["off"] for x in range(7)]

    for i in range(3):
        effect[i], effect[i+3], effect[6] = colour, colour, colour
        effect[(i+1)%6], effect[(i+2)%6], effect[(i+4)%6], effect[(i+5)%6] = COLOURS["off"], COLOURS["off"], COLOURS["off"], COLOURS["off"]
        np = list_to_np(effect, np)
        np.show()
        sleep(speed)

def figure_eight(colour, speed):
    np = neopixel.NeoPixel(pin0, 7)
    effect = [COLOURS["off"] for x in range(7)]
    for i in range(8): # 7 steps in figure eight pattern
        index = eight_formula(i)
        for x in range(7):
            if x != index:
                effect[x] = COLOURS["off"]
            else:
                effect[index] = colour
        np = list_to_np(effect, np)
        np.show()
        sleep(speed)

def eight_formula(x):
    if x <= 2:
        return x
    if x == 3 or x == 7:
        return 6
    if x == 4:
        return 5
    if x == 5:
        return 4
    if x == 6:
        return 3

def rotate(l, n):
    return l[n:] + l[:n]

def list_to_np(l, np):
    for i in range(len(l)):
        np[i] = l[i]
    return np

def fill(n_LEDs, colour, np):
    for i in range(n_LEDs):
        np[i] = colour
    return np

colour = colour_list[0]
while True:
    colour_wheel(100)
    if button_a.was_pressed():
        index = (colour_list.index(colour) - 1) % len(colour_list)
        colour = colour_list[index]

    if button_b.was_pressed():
        index = (colour_list.index(colour) + 1) % len(colour_list)
        colour = colour_list[index]