from microbit import *
import radio

def move(location,direction):
    x,y = location[0],location[1]
    display.set_pixel(x,y,0)
    if location[0] == 0 and direction == 'SW':
        direction = 'SE'
        location = (x+1,y+1)
        return location,direction
        
    elif location[0] == 0 and direction == 'NW':
        direction = 'NE'
        location = (x+1,y-1)
        return location,direction
        
    elif location[0] == 4 and direction == 'SE':
        direction = 'SW'
        location = (x-1,y+1)
        return location,direction
        
    elif location[0] == 4 and direction == 'NE':
        direction = 'NW'
        location = (x-1,y-1)
        return location,direction
    
    elif direction == 'SW':
        location = (x-1,y+1)
        return location,direction
        
    elif direction == 'SE':
        location = (x+1,y+1)
        return location,direction
        
    elif direction == 'NW':
        location = (x-1,y-1)
        return location,direction
        
    elif direction == 'NE':
        location = (x+1,y-1)
        return location,direction
    
playing = False
player_1 = True
player_1_side = True
ball = (2,0)
paddle = 3
direction = 'SE'
ball_delay = 1000

radio.on()
display.show(Image.ARROW_W,wait=False)

while not playing:
    if button_a.is_pressed() and not playing:
        playing = True
        display.clear()
        display.scroll('3...2...1')
        display.set_pixel(paddle,4,9)
        ball_off = running_time() + ball_delay
        if player_1:
            display.set_pixel(ball[0],ball[1],9)
            
    while playing:
            
        if button_a.was_pressed() and paddle > 0:
            display.set_pixel(paddle,4,0)
            paddle = paddle-1
            display.set_pixel(paddle,4,9)
            
        if button_b.was_pressed() and paddle < 4:
            display.set_pixel(paddle,4,0)
            paddle = paddle+1
            display.set_pixel(paddle,4,9)
            
        if running_time() > ball_off and player_1_side:
            ball_off = running_time() + ball_delay
            ball, direction = move(ball,direction)
            
            try:
                display.set_pixel(ball[0],ball[1],9)
                
            except ValueError:
                player_1_side = False

            
        if ball[0] == paddle and ball[1] == 3:
            if direction == 'SE':
                direction = 'NE'
                
            if direction == 'SW':
                direction = 'NW'