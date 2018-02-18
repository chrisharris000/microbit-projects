from microbit import *
from random import randint

def create_obstacle():
    obstacle = Image('00003:00003:00003:00003:00003')
    i = randint(1,2) #1 = duck, 2 = jump
    if i == 1:
        obstacle.set_pixel(4,4,0)
    if i == 2:
        obstacle.set_pixel(4,3,0)
        obstacle.set_pixel(4,2,0)
        obstacle.set_pixel(4,1,0)
        obstacle.set_pixel(4,0,0)
    return obstacle

player_y = 100
speed_y = 0
frame = 0
obstacle = create_obstacle()
score = 0
obstacle_delay = 10
new_obstacle_delay = 100
crouched = False

display.scroll('3...2...1')
while True:
    frame += 1
    display.show(obstacle)
    
    if speed_y < 5:
        speed_y += 1
    player_y += speed_y
    if player_y < 0:
        player_y = 0
        
    if player_y > 99:
        player_y = 99
    
    led_player_y = int(player_y/20)
  
    if button_a.was_pressed() and led_player_y == 4 and speed_y > 2:
        crouched = False
        speed_y = -10
    
    if button_b.was_pressed():
        crouched = not crouched
    
    if frame % obstacle_delay == 0:
        obstacle = obstacle.shift_left(1)
        
    if frame % new_obstacle_delay == 0:
        obstacle = create_obstacle()
        score += 1
        obstacle_delay -= 1
        if obstacle_delay < 5:
            obstacle_delay = 5
    
    if obstacle.get_pixel(0,led_player_y) != 0 or (not crouched and obstacle.get_pixel(0,led_player_y-1) != 0):
        display.show(Image.SAD)
        sleep(500)
        display.clear()
        display.scroll('SCORE: '+str(score))
        break
    
    display.set_pixel(0,led_player_y,9)
    if not crouched:
        display.set_pixel(0,led_player_y-1,9)
    sleep(20)
    display.set_pixel(0,led_player_y,0)
    display.set_pixel(0,led_player_y-1,0)