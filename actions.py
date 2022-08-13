import wave
import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision


# get mouse positions
#sleep(5)
#print(pyautogui.position())
#exit()

# delays
very_small_delay = 0.1
small_delay = 0.25
medium_delay = 0.5
big_delay_= 0.75
very_big_delay = 1


# invariable positions at 1920x1080 with min zoom
confirm_attack1_x = 1054
confirm_attack1_y = 697

apply_preset_to_wave_x = 719
apply_preset_to_wave_y = 931

next_wave_x = 777
next_wave_y = 878

confirm_attack2_x = 1410
confirm_attack2_y = 990

gold_travel_x = 750
gold_travel_y = 589

feather_travel_x = 1165
feather_travel_y = 587

confirm_attack3_x = 1086
confirm_attack3_y = 788

coord_box1_x = 850
coord_box1_y = 112

coord_box2_x = 893
coord_box2_y = 112

jump_to_coord_x = 939
jump_to_coord_y = 117

select_cmd_x = 626
select_cmd_y = 880


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture()

# initialize the Vision classes
vision_fort = Vision('needle_images/fort.png')

vision_attack = Vision('needle_images/attack.png')

vision_cmd = Vision('needle_images/cmd.png')


def berimond_auto_attack(type='gold'):
    # move mouse to target
    sleep(random.uniform(very_small_delay, very_big_delay))
    pyautogui.moveTo(960 + random.uniform(0, 9.8), 567 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.click()
    sleep(random.uniform(very_small_delay, small_delay))

    # search for attack button
    screenshot = wincap.get_screenshot()
    attack_button = vision_attack.find(screenshot, 0.95, 'points')
    if len(attack_button):
        pyautogui.moveTo(attack_button[0][0] - 5 + random.uniform(0, 9.8), attack_button[0][1] - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # first confirmation
        pyautogui.moveTo(confirm_attack1_x - 5 + random.uniform(0, 9.8), confirm_attack1_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # apply preset to wave
        pyautogui.moveTo(apply_preset_to_wave_x - 2 + random.uniform(0, 3.8), apply_preset_to_wave_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # complete other waves
        pyautogui.moveTo(1284 - 2 + random.uniform(0, 3.8), 988 - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # second confirmation
        pyautogui.moveTo(confirm_attack2_x - 10 + random.uniform(0, 19.8), confirm_attack2_y - 8 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        if(type == 'feather'):
            # moves to feather travel option
            pyautogui.moveTo(feather_travel_x - 5 + random.uniform(0, 9.8), feather_travel_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        if(type == 'gold'):
            # moves to gold travel option
            pyautogui.moveTo(gold_travel_x - 5 + random.uniform(0, 9.8), gold_travel_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        # third confirmation
        pyautogui.moveTo(confirm_attack3_x - 8 + random.uniform(0, 15.8), confirm_attack3_y - 8 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))


def attack(cx, cy, waves = 3, type='feather'):
    # move mouse to target
    sleep(random.uniform(very_small_delay, very_big_delay))
    pyautogui.moveTo(cx - 10 + random.uniform(0, 19.8), cy - 7 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.click()
    sleep(random.uniform(very_small_delay, small_delay))

    # search for attack button
    screenshot = wincap.get_screenshot()
    attack_button = vision_attack.find(screenshot, 0.95, 'points')
    if len(attack_button):
        pyautogui.moveTo(attack_button[0][0] - 5 + random.uniform(0, 9.8), attack_button[0][1] - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # first confirmation
        pyautogui.moveTo(confirm_attack1_x - 5 + random.uniform(0, 9.8), confirm_attack1_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # select commander
        pyautogui.moveTo(select_cmd_x - 5 + random.uniform(0, 9.8), select_cmd_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # search for cmd
        screenshot = wincap.get_screenshot()
        found_cmd = vision_cmd.find(screenshot, 0.95, 'points')
        if len(found_cmd):
            pyautogui.moveTo(found_cmd[0][0] - 5 + random.uniform(0, 9.8), found_cmd[0][1] - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        for times in range(waves):
            # apply preset to wave
            pyautogui.moveTo(apply_preset_to_wave_x - 2 + random.uniform(0, 3.8), apply_preset_to_wave_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

            # moves to next to wave
            pyautogui.moveTo(next_wave_x - 2 + random.uniform(0, 3.8), next_wave_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        # second confirmation
        pyautogui.moveTo(confirm_attack2_x - 10 + random.uniform(0, 19.8), confirm_attack2_y - 8 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        if(type == 'feather'):
            # moves to feather travel option
            pyautogui.moveTo(feather_travel_x - 5 + random.uniform(0, 9.8), feather_travel_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        if(type == 'gold'):
            # moves to gold travel option
            pyautogui.moveTo(gold_travel_x - 5 + random.uniform(0, 9.8), gold_travel_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        # third confirmation
        pyautogui.moveTo(confirm_attack3_x - 8 + random.uniform(0, 15.8), confirm_attack3_y - 8 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))


def set_coord(x, y):
    # moves to first coordinates box(x)
    pyautogui.moveTo(coord_box1_x - 5 + random.uniform(0, 9.8), coord_box1_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.doubleClick()
    sleep(random.uniform(very_small_delay, small_delay))
    # types new x coordinates
    pyautogui.typewrite(str(x), interval=random.uniform(very_small_delay, small_delay))
    sleep(random.uniform(very_small_delay, small_delay))

    # moves to second coordinates box(y)
    pyautogui.moveTo(coord_box2_x - 5 + random.uniform(0, 9.8), coord_box2_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.doubleClick()
    sleep(random.uniform(very_small_delay, small_delay))
    # types new y coordinates
    pyautogui.typewrite(str(y), interval=random.uniform(very_small_delay, small_delay))
    sleep(random.uniform(very_small_delay, small_delay))

    # jump to new coordinates
    pyautogui.moveTo(jump_to_coord_x - 5 + random.uniform(0, 9.8), jump_to_coord_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.click()
    sleep(random.uniform(very_small_delay, small_delay))

def zoomOut():
     # moves to screens center and zooms out fully
    pyautogui.moveTo(900 + random.uniform(0, 19.8), 500 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    range_scroll = int(random.uniform(12, 15))
    for i in range(range_scroll):
        pyautogui.scroll(-1)