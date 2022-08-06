import wave
import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
import digit_recognizer
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision
from actions import attack, set_coord, zoomOut

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

def updateSpreadsheet(init_fortress_x = 243, init_fortress_y = 224, final_fortress_x = 1043, final_fortress_y = 1062):
    # initial bot delay
    sleep(3)
    set_coord(init_fortress_x, init_fortress_y)
    x_coord = init_fortress_x
    y_coord = init_fortress_y

    even_line = True

    zoomOut()

    while((x_coord <= final_fortress_x) and (y_coord <= final_fortress_y)):
        # pauses if p is pressed, and unpauses if p is pressed again
        if keyboard.is_pressed("p"):
            output = pyautogui.confirm('Program paused, press OK to continue or Cancel to exit.')
            # if cancel is pressed than exits program, if OK is pressed continues
            if(output == 'Cancel'):
                exit()

        # moves to fortress center and clicks on it
        pyautogui.moveTo(fortress_center_x - 5 + random.uniform(0, 9.8), fortress_center_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

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
                if(len(time) >= 6):
                    hours = str(time[0]) + str(time[1])
                    hours = int(hours)
                    print(hours, "hours")

                if(len(time) >= 4):
                    minutes = str(time[2]) + str(time[3])
                    minutes = int(minutes)
                    print(minutes, "minutes")

                if(len(time) >= 2):
                    seconds = str(time[4]) + str(time[5])
                    seconds = int(seconds)
                    print(seconds, "seconds")

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