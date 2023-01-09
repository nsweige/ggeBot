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
#sleep(3)
#print(pyautogui.position())
#exit()

# delays

# default
load_screen_delay = 1.5
# lag
#load_screen_delay = 2
#load_screen_delay = 3

min_typing_delay = 0.01
max_typing_delay = 0.05
very_small_delay = 0.1
small_delay = 0.25
medium_delay = 0.5
big_delay= 0.75
very_big_delay = 1


# invariable positions at 1920x1080 with min zoom
confirm_attack1_x = 1054
confirm_attack1_y = 697

# old gui
apply_preset_to_wave_x = 719
apply_preset_to_wave_y = 931

next_wave_x = 777
next_wave_y = 878

confirm_attack2_x = 1410
confirm_attack2_y = 990

# new gui
all_waves_x = 663
all_waves_y = 560

first_wave_x = 662
first_wave_y = 608

apply_preset_to_waves_x = 1438
apply_preset_to_waves_y = 762

new_confirm_attack_x = 1116
new_confirm_attack_y = 940

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

def buy_glory_bonus_samurai(amount):
    sleep(3)
    for i in range(amount):
        # move mouse to target
        sleep(random.uniform(very_small_delay, medium_delay))
        pyautogui.moveTo(916 + random.uniform(0, 9.8), 689 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        sleep(random.uniform(very_small_delay, medium_delay))
        pyautogui.moveTo(899 + random.uniform(0, 2.8), 573 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))

        for i in range(24):
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))

        # confirm
        sleep(random.uniform(very_small_delay, medium_delay))
        pyautogui.moveTo(1067 + random.uniform(0, 2.8), 663 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

    


def berimond_auto_attack(type='gold'):
    # move mouse to target
    sleep(random.uniform(very_small_delay, very_big_delay))
    pyautogui.moveTo(950 + random.uniform(0, 9.8), 562 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
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
        sleep(random.uniform(2, 2.5))

        # old gui
        '''
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
        

        # clean waves
        pyautogui.moveTo(all_waves_x - 2 + random.uniform(0, 3.8), all_waves_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # select only first wave
        pyautogui.moveTo(first_wave_x - 2 + random.uniform(0, 3.8), first_wave_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))
        
        # apply preset to it
        pyautogui.moveTo(apply_preset_to_waves_x - 2 + random.uniform(0, 3.8), apply_preset_to_waves_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # confirm attack
        pyautogui.moveTo(new_confirm_attack_x - 2 + random.uniform(0, 3.8), new_confirm_attack_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))
        '''
        # apply preset to first wave
        pyautogui.moveTo(1309 - 2 + random.uniform(0, 3.8), 801 - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # fullfill wave
        pyautogui.moveTo(1361 - 2 + random.uniform(0, 3.8), 701 - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))

        # confirm attack
        pyautogui.moveTo(858 - 2 + random.uniform(0, 3.8), new_confirm_attack_y - 2 + random.uniform(0, 3.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
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
            sleep(random.uniform(0.1, 0.5))
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

# first is false for navegation using tab key, or true to set it using mouse mov(first time is necessary)
def set_coord(x=0, y=0, only_x=False, only_y=False, First=False):
    if(not only_y):
        if(First):
            # moves to first coordinates box(x)
            pyautogui.moveTo(coord_box1_x - 5 + random.uniform(0, 9.8), coord_box1_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.doubleClick()
            sleep(random.uniform(very_small_delay, small_delay))
        
        else:
            pyautogui.keyDown('tab')
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.keyUp('tab')
            sleep(random.uniform(very_small_delay, small_delay))

        # types new x coordinates
        pyautogui.typewrite(str(x), interval=random.uniform(min_typing_delay, max_typing_delay))
        sleep(random.uniform(very_small_delay, small_delay))

    if(not only_x):
        if(First):
            # moves to second coordinates box(y)
            pyautogui.moveTo(coord_box2_x - 5 + random.uniform(0, 9.8), coord_box2_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.doubleClick()
            sleep(random.uniform(very_small_delay, small_delay))

        else:
            pyautogui.keyDown('tab')
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.keyUp('tab')
            sleep(random.uniform(very_small_delay, small_delay))

        # types new y coordinates
        pyautogui.typewrite(str(y), interval=random.uniform(min_typing_delay, max_typing_delay))
        sleep(random.uniform(very_small_delay, small_delay))

    '''
    # jump to new coordinates
    pyautogui.moveTo(jump_to_coord_x - 5 + random.uniform(0, 9.8), jump_to_coord_y - 3 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.click()
    '''
    pyautogui.keyDown('enter')
    sleep(random.uniform(very_small_delay, small_delay))
    pyautogui.keyUp('enter')
    sleep(random.uniform(medium_delay, load_screen_delay))
    



def zoomOut():
     # moves to screens center and zooms out fully
    pyautogui.moveTo(800 + random.uniform(0, 190.8), 400 + random.uniform(0, 150.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
    sleep(random.uniform(very_small_delay, small_delay))
    range_scroll = int(random.uniform(12, 15))
    for i in range(range_scroll):
        pyautogui.scroll(-1)