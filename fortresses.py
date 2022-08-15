import wave
import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
import digit_recognizer
from time import time, sleep
from spreadsheet import updateSpreadsheet
from windowcapture import WindowCapture
from vision import Vision
from actions import attack, set_coord, zoomOut
from datetime import date, time, datetime, timedelta

# delays
very_small_delay = 0.1
small_delay = 0.25
medium_delay = 0.5
big_delay_= 0.75
very_big_delay = 1

# static positions
fortress_center_x = 970
fortress_center_y = 574

# initialize the WindowCapture class
wincap = WindowCapture()

# initialize the Vision classes
vision_blocked_attack = Vision('needle_images/blocked_attack.png')

vision_blocked_desert_fortress = Vision('needle_images/blocked_desert_fortress.png')

# test - fortresses position adjustments
# search for blocked fortress on screen (if somewhy is not centered)
# results
"""
centro 			    962 	575

1 a menos em x		1014	575	+52
2 a menos em x 		1065	575	+51
3 a menos em x		1116	575	+51
10 a menos em x		1474	575	+512

1 a mais em x		911	575	-51
2 a mais em x		860	575	-51
3 a mais em x		809	575	-51
10 a mais em x		450	575	-512


1 a menos em y		962	626	+51
2 a menos em y		962	678	+52
3 a menos em y		962	729	+51
8 a menos em y		962	985	+410 (+51,25)

1 a mais em y		962	524	-51
2 a mais em y		962	473	-51
3 a mais em y		962	422	-51
8 a mais em y		962	166	-409 (-51,125)
"""
#sleep(3)
#screenshot = wincap.get_screenshot()
#blocked_desert_fortress = vision_blocked_desert_fortress.find(screenshot, 0.95, 'points')
#if len(blocked_desert_fortress):
#    print(blocked_desert_fortress[0][0])
#    print("\n")
#    print(blocked_desert_fortress[0][1])
#    exit()

#def fortressesBot(init_fortress_x = 243, init_fortress_y = 243, final_fortress_x = 1043, final_fortress_y = 1062):
def fortressesBot(init_fortress_x = 263, init_fortress_y = 341, final_fortress_x = 1043, final_fortress_y = 1062):
    # initial bot delay
    sleep(3)
    set_coord(init_fortress_x, init_fortress_y)
    x_coord = init_fortress_x
    y_coord = init_fortress_y

    #even_line = True
    even_line = False


    zoomOut()

    while((x_coord <= final_fortress_x) or (y_coord <= final_fortress_y)):
        sleep(random.uniform(small_delay, medium_delay))
        # pauses if p is pressed, and unpauses if p is pressed again
        if keyboard.is_pressed("p"):
            output = pyautogui.confirm('Program paused, press OK to continue or Cancel to exit.')
            # if cancel is pressed than exits program, if OK is pressed continues
            if(output == 'Cancel'):
                exit()


        # search for blocked fortress on screen
        screenshot = wincap.get_screenshot()
        blocked_desert_fortress = vision_blocked_desert_fortress.find(screenshot, 0.9, 'points')
        if len(blocked_desert_fortress):
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.moveTo(blocked_desert_fortress[0][0] - 5 + random.uniform(0, 9.8), blocked_desert_fortress[0][1] - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

            # adjusts x and y coordinates by comparing fortress coordinates with (962,575) that is the centered value on 1080p
            if(blocked_desert_fortress[0][0] != 962):
                x_coord = x_coord + int((blocked_desert_fortress[0][0] - 962) / 51 ) # delta / 51 where 1 coord = 51 pixels on screen (1080p)
            if(blocked_desert_fortress[0][1] != 575):
                y_coord = y_coord + int((blocked_desert_fortress[0][1] - 575) / 51 )
        else:
            while((not (len(blocked_desert_fortress))) and (x_coord <= final_fortress_x)):
                x_coord = x_coord + 19
                set_coord(x_coord, y_coord)
                sleep(random.uniform(small_delay, medium_delay))
                screenshot = wincap.get_screenshot()
                blocked_desert_fortress = vision_blocked_desert_fortress.find(screenshot, 0.9, 'points')
                if len(blocked_desert_fortress):
                    sleep(random.uniform(very_small_delay, small_delay))
                    pyautogui.moveTo(blocked_desert_fortress[0][0] - 5 + random.uniform(0, 9.8), blocked_desert_fortress[0][1] - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
                    sleep(random.uniform(very_small_delay, small_delay))
                    pyautogui.click()
                    sleep(random.uniform(very_small_delay, small_delay))

                    # adjusts x and y coordinates by comparing fortress coordinates with (962,575) that is the centered value on 1080p
                    if(blocked_desert_fortress[0][0] != 962):
                        x_coord = x_coord + int((blocked_desert_fortress[0][0] - 962) / 51 ) # delta / 51 where 1 coord = 51 pixels on screen (1080p)
                    if(blocked_desert_fortress[0][1] != 575):
                        y_coord = y_coord + int((blocked_desert_fortress[0][1] - 575) / 51 )



        hours = 0
        minutes = 0
        seconds = 0

        # search for blocked attack button
        screenshot = wincap.get_screenshot()
        blocked_attack_button = vision_blocked_attack.find(screenshot, 0.95, 'points')
        if len(blocked_attack_button):
            pyautogui.moveTo(blocked_attack_button[0][0] - 5 + random.uniform(0, 9.8), blocked_attack_button[0][1] - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))

            screenshot = wincap.get_screenshot()
            digits = digit_recognizer.digit_recognizer(screenshot, 0.93)
            print(digits)
            order_by_x = sorted(digits, key=lambda i: i[-1])
            print(order_by_x)
            time = []
            for i in order_by_x:
                time.append(i[0])
            print(time)

            if(((len(time)) % 2) == 0):
                if(len(time) >= 2):
                    seconds = str(time[0]) + str(time[1])
                    seconds = int(seconds)
                    print(seconds, "seconds")

                if(len(time) >= 4):
                    minutes = str(time[0]) + str(time[1])
                    minutes = int(minutes)
                    print(minutes, "minutes")

                    seconds = str(time[2]) + str(time[3])
                    seconds = int(seconds)
                    print(seconds, "seconds")

                if(len(time) >= 6):
                    hours = str(time[0]) + str(time[1])
                    hours = int(hours)
                    print(hours, "hours")

                    minutes = str(time[2]) + str(time[3])
                    minutes = int(minutes)
                    print(minutes, "minutes")

                    seconds = str(time[4]) + str(time[5])
                    seconds = int(seconds)
                    print(seconds, "seconds")

                #print("Livre em: ", (datetime.today() + timedelta(hours = hours, minutes = minutes, seconds = seconds)).strftime('%H:%M:%S'))
                updateSpreadsheet(coord_x = x_coord, coord_y = y_coord, hours = hours, minutes = minutes, seconds = seconds)
            

        # move thru entire map   
        if(x_coord < final_fortress_x):
            x_coord = x_coord + 39
        else:
            x_coord = init_fortress_x
            y_coord = y_coord + 19
            if(even_line):
                even_line = not even_line
                x_coord = x_coord - 19

        set_coord(x_coord, y_coord)