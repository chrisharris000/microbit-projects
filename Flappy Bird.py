from microbit import *
from random import randint

def create_pipe():
    pipe = Image("00003:00003:00003:00003:00003")
    gap = randint(0,3)
    pipe.set_pixel(4,gap,0)
    pipe.set_pixel(4,gap+1,0)
    return pipe

bird_y = 50
led_bird_y = int(bird_y/20)
speed = 0
pipe = create_pipe()
frame = 0
delay = 20
pipe_shift_delay = 20
new_pipe_delay = 100

display.scroll('3...2...1')
display.set_pixel(1,led_bird_y,9)

while True:
    frame += 1
    display.show(pipe)
    
    if button_a.was_pressed():
        speed -= 8
    
    speed += 1
    if speed > 2:
        speed = 2
        
    bird_y += speed
    if bird_y > 99:
        bird_y = 99
    
    if bird_y < 0:
        bird_y = 0
        
    led_bird_y = int(bird_y/20)
    display.set_pixel(1,led_bird_y,9)
    
    if pipe.get_pixel(1,led_bird_y) != 0:
        display.show(Image.SAD)
        sleep(500)
        display.clear()
        break
    
    if frame % pipe_shift_delay == 0:
        pipe = pipe.shift_left(1)
        
    if frame % new_pipe_delay == 0:
        pipe = create_pipe()
        
    sleep(20)