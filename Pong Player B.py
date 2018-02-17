from microbit import *
import radio

a_bat = 2
b_bat = 2
ball_x = 2
ball_y = 2
ball_brightness = 9
playing = False
bat_map = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
display.show(Image.ARROW_E,wait=False)
while not playing:
    if button_b.is_pressed():
        playing = True
        display.clear()

radio.on()

while playing:
    display.set_pixel(a_bat,0,9)
    display.set_pixel(b_bat,4,9)
    display.set_pixel(ball_x,ball_y,ball_brightness)
    
    if button_a.was_pressed():
        display.set_pixel(b_bat,4,0)
        b_bat -= 1
        if b_bat < 0:
            b_bat = 0
        radio.send('bx:'+str(b_bat)) #e.g. bx:2
            
    if button_b.was_pressed():
        display.set_pixel(b_bat,4,0)
        b_bat += 1
        if b_bat > 4:
            b_bat = 4
        radio.send('bx:'+str(b_bat))
        
    msg = radio.receive()
    if msg:
        if msg.startswith('ax:'):
            display.set_pixel(a_bat,0,0)
            a_bat = bat_map[int(msg[-1])]       #a_bat = 4-int(msg[-1])
            
        if msg.startswith('x:'):
            display.set_pixel(ball_x,ball_y,0)
            ball_x,ball_y = bat_map[int(msg[2])],bat_map[int(msg[-1])]      #ball_x,ball_y = 4-int(msg[2]),4-int(msg[-1])
            
        if msg == 'GAME OVER':
            display.clear()
            playing = False
            break