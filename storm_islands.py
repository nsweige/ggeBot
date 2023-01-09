import wave
import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
from time import time, sleep
from spreadsheet import updateSpreadsheet
from windowcapture import WindowCapture
from vision import Vision
from actions import attack, set_coord, zoomOut



# get mouse positions
#sleep(3)
#print(pyautogui.position())
#exit()

# delays
very_small_delay = 0.01
small_delay = 0.025
medium_delay = 0.15
big_delay_= 0.275
very_big_delay = 0.51


# map limits
init_x = 538
init_y = 538

map_final_x = 758
map_final_y = 758


# invariable positions at 1920x1080 with min zoom
spy_close_x = 1188
spy_close_y = 349

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
vision_spy = Vision('needle_images/spy.png')

vision_fort_60 = Vision('needle_images/fort_lvl_60.png')
vision_fort_70 = Vision('needle_images/fort_lvl_70.png')
vision_fort_80 = Vision('needle_images/fort_lvl_80.png')

vision_60_guards = Vision('needle_images/60_guards.png')
vision_65_guards = Vision('needle_images/65_guards.png')
vision_75_guards = Vision('needle_images/75_guards.png')

vision_attack = Vision('needle_images/attack.png')

vision_cmd = Vision('needle_images/cmd.png')


def get_fort_lvl(haystack_img, threshold=0.95):
    # recognize a forts lvl
    fort_lvl60 = vision_fort_60.find(haystack_img, threshold, 'points')
    if len(fort_lvl60):
        return 60

    fort_lvl70 = vision_fort_70.find(haystack_img, threshold, 'points')
    if len(fort_lvl70):
        return 70

    fort_lvl80 = vision_fort_80.find(haystack_img, threshold, 'points')
    if len(fort_lvl80):
        return 80

    return 1


def get_guards_amount(haystack_img, threshold=0.99):
    # get amount of guards on an island
    guards_60 = vision_60_guards.find(haystack_img, threshold, 'points')
    if len(guards_60):
        return 60

    guards_65 = vision_65_guards.find(haystack_img, threshold, 'points')
    if len(guards_65):
        return 65

    guards_75 = vision_75_guards.find(haystack_img, threshold, 'points')
    if len(guards_75):
        return 75

    return 1


def storm_islands_bot(x_coord = init_x, y_coord = init_y, final_x = map_final_x, final_y = map_final_y, waves = 0, attacks = 0, type = 'attack'):
    attacks_done = 0
    loop_time = time()
    # initial bot delay
    sleep(3)
    set_coord(x_coord, y_coord, First=True)
    exit = False
    updateY = False

    zoomOut()

    while((attacks_done < attacks or type == 'mark') and exit == False):
        # initial bot delay
        sleep(random.uniform(very_small_delay, medium_delay))

        # get an updated image of the game
        screenshot = wincap.get_screenshot()


        # display the processed image
        points = vision_fort.find(screenshot, 0.95, 'points')
        # print(points)


        # for every storm fort found
        for (cx, cy) in points:
            # pauses if p is pressed, and unpauses if p is pressed again
            if keyboard.is_pressed("p"):
                output = pyautogui.confirm('Program paused, press OK to continue or Cancel to exit.')
                # if cancel is pressed than exits program, if OK is pressed continues
                if(output == 'Cancel'):
                    exit()

            # move the mouse to the center of a storm fort
            pyautogui.moveTo(cx - 10 + random.uniform(0, 19.8), cy - 7 + random.uniform(0, 15.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))

            # get storm fort lvl
            screenshot = wincap.get_screenshot()
            fort_lvl = get_fort_lvl(screenshot, 0.95)

            # we are only intersted in storm forts lvl 60, 70 or 80
            if(fort_lvl > 1):
                pyautogui.click()
                # locates where is the espionage button
                screenshot = wincap.get_screenshot()
                spy_loc = vision_spy.find(screenshot, 0.95, 'points')
                print(spy_loc)

                # only moves forward if espionage button appears on screen
                if len(spy_loc):
                    # open espionage menu
                    sleep(random.uniform(very_small_delay, small_delay))
                    pyautogui.moveTo(spy_loc[0][0] - 5 + random.uniform(0, 9.8), spy_loc[0][1] - 5 + random.uniform(0, 9.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
                    sleep(random.uniform(very_small_delay, 0.3))
                    pyautogui.click()
                    sleep(random.uniform(0.1, 0.3))

                    # get guards amount
                    screenshot = wincap.get_screenshot()
                    guards = get_guards_amount(screenshot, 0.99)
                    
                    # close espionage menu
                    pyautogui.moveTo(spy_close_x - 5 + random.uniform(0, 9.8), spy_close_y - 5 + random.uniform(0, 9.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
                    sleep(random.uniform(very_small_delay, 0.3))
                    pyautogui.click()

                    # good storm forts for attacking can de decided based on how many guards it has
                    # all 3 good combinations are: storm fort lvl 60 with 60 guards, storm fort lvl 70 with 65 guards and storm fort lvl 80 with 75 guards
                    if((fort_lvl == 60 and guards == 60) or
                    (fort_lvl == 70 and guards == 65) or
                    (fort_lvl == 80 and guards == 75)):
                        if(type == 'attack'):
                            attack(cx, cy, waves, 'feather')
                            attacks_done = attacks_done + 1
                            if(attacks_done < attacks):
                                exit()
                        else:
                            updateSpreadsheet(coord_x = x_coord + int((cx - 962) / 51 ), coord_y = y_coord + int((cy - 575) / 51 ), reign = 'islands', lvl = fort_lvl)

                sleep(random.uniform(small_delay, very_big_delay))
        
        # move thru entire map
        if(x_coord < final_x):
            x_coord = x_coord + 39
        else:
            if(y_coord > final_y):
                exit = True
            x_coord = init_x
            y_coord = y_coord + 16
            updateY = True

        if(updateY):
            set_coord(x_coord, y_coord)
            updateY = False
        else:
            set_coord(x_coord, y_coord, True)

        # debug the loop rate
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
