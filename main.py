import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
from fortresses import fortressesBot, offer_finder
import storm_islands
import gui
import digit_recognizer
import fortresses
from actions import berimond_auto_attack, buy_glory_bonus_samurai
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision


# global map updated initial and final coordinates
desert_initial_x = 243 #+ 150
desert_initial_y = 224 #+ 150

desert_final_x = 1043 #- 150
desert_final_y = 1062 #- 100

peak_initial_x = 321 + 100
peak_initial_y = 302 + 150

peak_final_x = 984 - 200
peak_final_y = 1004 - 250

islands_initial_x = 538
islands_initial_y = 538

islands_final_x = 758
islands_final_y = 758


# delays
very_small_delay = 0.1
small_delay = 0.25
medium_delay = 0.5
big_delay= 0.75
very_big_delay = 1


# initialize the WindowCapture class
wincap = WindowCapture()


def main():
    #buy_glory_bonus_samurai(142)
    #exit()
    waves, attacks, type, is_desert, is_peaks, is_islands, is_beri, is_peak_and_desert, desert_distance, peak_distance, islands_distance, wholemap = gui.menu()
    """
    print("waves: ", waves + '\nattacks:', attacks)
    print("type: ", type)
    print("bot type is: ")
    print("desert? ", is_desert)
    print("desert? ", is_peaks)
    print("desert? ", is_islands)
    print("desert? ", is_beri)
    print("desert distance: ", desert_distance + '\npeaks distance:', peak_distance)
    exit()
    """

    if(is_islands):
        if(wholemap):
            storm_islands.storm_islands_bot(x_coord = islands_initial_x, y_coord = islands_initial_y, final_x = islands_final_x, final_y = islands_final_y, waves = int(waves), attacks = int(attacks), type = type)
        else:
            island_x = 523
            island_y = 622
            distance = int(islands_distance)
            storm_islands.storm_islands_bot(x_coord = island_x - distance, y_coord = island_y - distance, final_x = island_x + distance, final_y = island_y + distance, waves = int(waves), attacks = int(attacks), type = type)
        #storm_islands.storm_islands_bot(x_coord=633, y_coord=571, waves = int(waves), attacks = int(attacks), type = type)


    jzargo_delay = 165
    kid_trunks_delay = 197
    if(is_beri):
        i = 0
        while i < 999:
            screenshot = wincap.get_screenshot()
            offer_finder(screenshot)

            berimond_auto_attack()
            sleep(random.uniform(medium_delay, big_delay))
            #berimond_auto_attack()
            i = i+1

            sleep(jzargo_delay)
            #sleep(kid_trunks_delay)

            # move mouse to target
            sleep(random.uniform(very_small_delay, very_big_delay))
            pyautogui.moveTo(961 + random.uniform(0, 9.8), 713 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))
            pyautogui.click()
            sleep(random.uniform(very_small_delay, small_delay))



    if(is_peaks):
        if(wholemap):
            fortressesBot(init_fortress_x = peak_initial_x, init_fortress_y = peak_initial_y, final_fortress_x = peak_final_x, final_fortress_y = peak_final_y, reign = 'peak')
        else:
            peak_x = 523
            peak_y = 622
            distance = int(peak_distance)
            fortressesBot(init_fortress_x = peak_x - distance, init_fortress_y = peak_y - distance, final_fortress_x = peak_x + distance, final_fortress_y = peak_y + distance, reign = 'peak')
        


    if(is_desert):
        if(wholemap):
            fortressesBot(init_fortress_x = desert_initial_x, init_fortress_y = desert_initial_y, final_fortress_x = desert_final_x, final_fortress_y = desert_final_y, reign = 'desert')
        else:
            # default
            desert_x = 562
            desert_y = 497
            distance = int(desert_distance)
            fortressesBot(init_fortress_x = desert_x - distance, init_fortress_y = desert_y - distance, final_fortress_x = desert_x + distance, final_fortress_y = desert_y + distance, reign = 'desert')
    
            # custom init
            init_x = 280
            init_y = 555
            #fortressesBot(init_fortress_x = init_x, init_fortress_y = init_y, final_fortress_x = desert_x + distance, final_fortress_y = desert_y + distance, reign = 'desert')


    if(is_peak_and_desert):
        if(wholemap):
            fortressesBot(init_fortress_x = peak_initial_x, init_fortress_y = peak_initial_y, final_fortress_x = peak_final_x, final_fortress_y = peak_final_y, reign = 'peak')
        else:
            peak_x = 523
            peak_y = 622
            distance = int(peak_distance)
            fortressesBot(init_fortress_x = peak_x - distance, init_fortress_y = peak_y - distance, final_fortress_x = peak_x + distance, final_fortress_y = peak_y + distance, reign = 'peak')

        # open desert
        sleep(random.uniform(very_small_delay, very_big_delay))
        pyautogui.moveTo(1841 + random.uniform(0, 3.8), 971 + random.uniform(0, 2.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, big_delay))
        pyautogui.moveTo(1841 + random.uniform(0, 3.8), 824 + random.uniform(0, 2.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, very_big_delay))

        if(wholemap):
            fortressesBot(init_fortress_x = desert_initial_x, init_fortress_y = desert_initial_y, final_fortress_x = desert_final_x, final_fortress_y = desert_final_y, reign = 'desert')
        else:
            desert_x = 562
            desert_y = 497
            distance = int(desert_distance)
            fortressesBot(init_fortress_x = desert_x - distance, init_fortress_y = desert_y - distance, final_fortress_x = desert_x + distance, final_fortress_y = desert_y + distance, reign = 'desert')


    #cv.imshow('frame', screenshot)
    #cv.waitKey()
    #print('Done')

if __name__ == "__main__":
    main()