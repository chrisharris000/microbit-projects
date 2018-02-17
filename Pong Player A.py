from microbit import *
import radio
from random import choice

#program for player a

a_bat = 2
b_bat = 2
a_points = 0
b_points = 0
point_limit = 5
ball_x = 2
ball_y = 2
ball_brightness = 9
directions = [1, -1]
x_direction = choice(directions)
y_direction = choice(directions)
delay = 1000
playing = False
bat_map = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}

def move_ball():
    global ball_x, ball_y, x_direction, y_direction, counter, a_bat, b_bat, a_points, b_points
    display.set_pixel(ball_x,ball_y,0)
    ball_x += x_direction
    ball_y += y_direction
    
    if ball_x < 0: #edge case
        ball_x = 0
        x_direction = 1
        #ball_y += y_direction
        
    if ball_x > 4: #edge case
        ball_x = 4
        x_direction = -1
        #ball_y += y_direction
        
    if ball_y == 0: 
        if ball_x == b_bat: #ball comes into contact with player b's bat
            y_direction = 1
            ball_y = 0
        else:
            a_points += 1
            ball_y = 0
            y_direction = 1

    if ball_y == 4: 
        if ball_x == a_bat: #ball comes into contact with player a's bat
            y_direction = -1
            ball_y = 4
        else:
            b_points += 1
            ball_y = 4
            y_direction = -1
            
    radio.send('x:'+str(ball_x)+',y:'+str(ball_y)) #e.g. x:3,y:1
    
display.show(Image.ARROW_W,wait=False)    
while not playing:
    if button_a.is_pressed():
        playing = True
        display.clear()
        off_time = running_time() + delay

radio.on()
        
while playing:
    display.set_pixel(a_bat,4,9) #player a
    display.set_pixel(b_bat,0,9) #player b
    display.set_pixel(ball_x,ball_y,ball_brightness) #ball
    
    if button_a.was_pressed():
        display.set_pixel(a_bat,4,0)
        a_bat -= 1
        if a_bat < 0:
            a_bat = 0
        radio.send('ax:'+str(a_bat)) #e.g. ax:2
            
    if button_b.was_pressed():
        display.set_pixel(a_bat,4,0)
        a_bat += 1
        if a_bat > 4:
            a_bat = 4
        radio.send('ax:'+str(a_bat))
        
    msg = radio.receive()
    if msg:
        display.set_pixel(b_bat,0,0) #player b's bat off
        #b_bat = abs(4-int(msg[-1]))
        b_bat = bat_map[int(msg[-1])]       #b_bat = 4-int(msg[-1])
        
    if running_time() > off_time:
        off_time = running_time() + delay
        move_ball()
        
    if a_points == point_limit or b_points == point_limit:
        display.scroll('GAME OVER')
        playing = False
        radio.send('GAME OVER')
display.scroll('A:'+str(a_points)+',B:'+str(b_points))