from microbit import *

player_x = 50
player_y = 50
speed_y = 0
frame = 0

while True:
    frame += 1
    if speed_y < 5:
        speed_y += 1
    player_y += speed_y
    if player_y < 0:
        player_y = 0
        
    if player_y > 99:
        player_y = 99
        
    if accelerometer.is_gesture('left'):
        player_x -= 5
        player_x %= 100
        
    if accelerometer.is_gesture('right'):
        player_x += 5
        player_x %= 100
    
    led_player_x = int(player_x/20)
    led_player_y = int(player_y/20)
  
    if led_player_y == 4 and speed_y > 2:
        speed_y = -12
        
    display.set_pixel(led_player_x,led_player_y,9)
    sleep(20)
    display.set_pixel(led_player_x,led_player_y,0)