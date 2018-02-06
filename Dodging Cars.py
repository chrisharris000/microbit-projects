from microbit import *
from random import randrange

playing = False
player_x = 3
obstacle_brightness = 5

#CARS
car0_y = 3
car1_y = 2
car2_y = 0
car3_y = 2
car4_y = 3

#CAR DELAYS
car_delay_0 = 400
car_delay_1 = 400
car_delay_2 = 400
car_delay_3 = 400
car_delay_4 = 400

#TIMERS FOR CAR 0
off_time_0 = running_time() + car_delay_0
big_delay_0 = False
big_delay_time_0 = 0

#TIMERS FOR CAR 1
off_time_1 = running_time() + car_delay_1
big_delay_1 = False
big_delay_time_1 = 0

#TIMERS FOR CAR 2
off_time_2 = running_time() + car_delay_2
big_delay_2 = False
big_delay_time_2 = 0

#TIMERS FOR CAR 3
off_time_3 = running_time() + car_delay_3
big_delay_3 = False
big_delay_time_3 = 0

#TIMERS FOR CAR 4
off_time_4 = running_time() + car_delay_4
big_delay_4 = True
big_delay_time_4 = 0


display.show(Image.ARROW_W,wait=False)
while True:
    if button_a.is_pressed():
        playing = True
        display.scroll('3...2...1')
        display.set_pixel(player_x,4,9)
        display.set_pixel(0,car0_y,obstacle_brightness)
        display.set_pixel(1,car1_y,obstacle_brightness)
        display.set_pixel(2,car2_y,obstacle_brightness)
        display.set_pixel(3,car3_y,obstacle_brightness)
        display.set_pixel(4,car4_y,obstacle_brightness)
        player_start = running_time()
        off_time_common = running_time() + 1000 #EVENTUAL INCREASE OF SPEED OF DROPPPING OBJECTS 
        

    while playing:
        if button_a.was_pressed() and player_x > 0 and playing: #MOVE LEFT
            player_x -= 1
            display.set_pixel(player_x,4,9)
            display.set_pixel(player_x+1,4,0)
        
        if button_b.was_pressed() and player_x < 4 and playing: #MOVE RIGHT
            player_x += 1
            display.set_pixel(player_x,4,9)
            display.set_pixel(player_x-1,4,0)
        
        
        
        if running_time() > off_time_0 and not big_delay_0: #CAR 0 MOVING DOWN (START OF CODE)
            display.set_pixel(0,(car0_y)%5,0)
            display.set_pixel(0,(car0_y+1)%5,obstacle_brightness)
            car0_y += 1
            if car0_y > 4:
                big_delay_0 = True
                big_delay_time_0 = running_time() + randrange(500,1000)
                car0_y = 0
            off_time_0 = running_time() + car_delay_0
        
        if running_time() > big_delay_time_0:
            big_delay_0 = False #CAR 0 MOVING DOWN (END OF CODE)
        
    
    
        if running_time() > off_time_1 and not big_delay_1: #CAR 1 MOVING DOWN (START OF CODE)
            display.set_pixel(1,(car1_y)%5,0)
            display.set_pixel(1,(car1_y+1)%5,obstacle_brightness)
            car1_y += 1
            if car1_y > 4:
                big_delay_1 = True
                big_delay_time_1 = running_time() + randrange(0,100)
                car1_y = 0
            off_time_1 = running_time() + car_delay_1
        
        if running_time() > big_delay_time_1:
            big_delay_1 = False #CAR 1 MOVING DOWN (END OF CODE)
            
            
        if running_time() > off_time_2 and not big_delay_2: #CAR 2 MOVING DOWN (START OF CODE)
            display.set_pixel(2,(car2_y)%5,0)
            display.set_pixel(2,(car2_y+1)%5,obstacle_brightness)
            car2_y += 1
            if car2_y > 4:
                big_delay_2 = True
                big_delay_time_2 = running_time() + randrange(500,1000)
                car2_y = 0
            off_time_2 = running_time() + car_delay_2
        
        if running_time() > big_delay_time_2:
            big_delay_2 = False #CAR 2 MOVING DOWN (END OF CODE)
            
            
        if running_time() > off_time_3 and not big_delay_3: #CAR 3 MOVING DOWN (START OF CODE)
            display.set_pixel(3,(car3_y)%5,0)
            display.set_pixel(3,(car3_y+1)%5,obstacle_brightness)
            car3_y += 1
            if car3_y > 4:
                big_delay_3 = True
                big_delay_time_3 = running_time() + randrange(500,1000)
                car3_y = 0
            off_time_3 = running_time() + car_delay_3
        
        if running_time() > big_delay_time_3:
            big_delay_3 = False #CAR 3 MOVING DOWN (END OF CODE)
        
        
        if running_time() > off_time_4 and not big_delay_4: #CAR 4 MOVING DOWN (START OF CODE)
            display.set_pixel(4,(car4_y)%5,0)
            display.set_pixel(4,(car4_y+1)%5,obstacle_brightness)
            car4_y += 1
            if car4_y > 4:
                big_delay_4 = True
                big_delay_time_4 = running_time() + randrange(500,1000)
                car4_y = 0
            off_time_4 = running_time() + car_delay_4
        
        if running_time() > big_delay_time_4:
            big_delay_4 = False #CAR 4 MOVING DOWN (END OF CODE)
        
        if running_time() > off_time_common:
            car_delay_0 -= 20
            car_delay_1 -= 20
            car_delay_2 -= 20
            car_delay_3 -= 20
            car_delay_4 -= 20
            print(car_delay_0,car_delay_1,car_delay_2,car_delay_3,car_delay_4)
            off_time_common = running_time() + 5000
        
        if (player_x == 0 and car0_y == 4) or (player_x == 1 and car1_y == 4) or (player_x == 2 and car2_y == 4) or (player_x == 3 and car3_y == 4) or (player_x == 4 and car4_y == 4):
            playing = False
            display.clear()
            player_score = (running_time() - player_start)//1000
            display.show(Image.NO)
            sleep(2000)
            display.scroll('SCORE: '+str(player_score))
            display.off()