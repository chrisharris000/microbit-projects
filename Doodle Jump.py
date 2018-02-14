#idea and code structure sourced from blog.codewith.uk
from microbit import *
from random import randint

player_x = 50
player_y = 50
score = 0
speed_y = 0
frame = 0

platform_gap = 2
level_score_limit = 10

platforms = Image("03330:00000:00033:00000:33333")
levels = [30, 25, 20, 18, 15, 12, 10]
current_level = 0

display.scroll('3...2...1')
while True:
    frame += 1
    if speed_y < 5:
        speed_y += 1
    player_y += speed_y
    if player_y < 0:
        player_y = 0
        
    if player_y > 99:
        player_y = 99
        
    if button_a.is_pressed():
        player_x -= 5
        if player_x < 0:
            player_x = 0
        
    if button_b.is_pressed():
        player_x += 5
        if player_x > 99: #change if wanted like normal doodle jump
            player_x = 99
            
    display.show(platforms)
    
    led_player_x = int(player_x/20)
    led_player_y = int(player_y/20)
    
    if frame % levels[current_level] == 0:
        score += 1
        platforms = platforms.shift_down(1)
        
        if score % level_score_limit == 0:
            current_level += 1
            if current_level > len(levels):
                current_level = len(levels)
                
        if score % platform_gap == 0:
            platform_start = randint(0,3)
            platform_end = randint(platform_start + 1, 4)
            for x in range(platform_start, platform_end):
                platforms.set_pixel(x, 0, 3)
                
    if platforms.get_pixel(led_player_x,led_player_y) == 3 and speed_y > 2:
        speed_y = -11
        
    elif led_player_y == 4:
        display.show(Image.SAD)
        sleep(500)
        display.clear()
        display.scroll('SCORE: '+str(score))
        break
        
    display.set_pixel(led_player_x,led_player_y,9)
    sleep(20)