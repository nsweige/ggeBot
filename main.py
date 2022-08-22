import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
from fortresses import fortressesBot
import storm_islands
import gui
import digit_recognizer
import fortresses
from actions import berimond_auto_attack
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision

# 243ppp
very_small_delay = 0.1
small_delay = 0.25
medium_delay = 0.5
big_delay_= 0.75
very_big_delay = 1

# initialize the WindowCapture class
wincap = WindowCapture()

def main():
    #waves, attacks = gui.menu()
    #print("waves: ", waves + '\nattacks:', attacks)
    #storm_islands.storm_islands_bot(int(waves), int(attacks))
    sleep(1)
    i = 0

    while i < 0:
        berimond_auto_attack()
        i = i+1
        sleep(200)
        # move mouse to target
        sleep(random.uniform(very_small_delay, very_big_delay))
        pyautogui.moveTo(961 + random.uniform(0, 9.8), 713 + random.uniform(0, 5.6), random.uniform(small_delay, medium_delay), pyautogui.easeOutQuad)
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))
        pyautogui.click()
        sleep(random.uniform(very_small_delay, small_delay))
    fortressesBot()

    #cv.imshow('frame', screenshot)
    #cv.waitKey()
    #print('Done')

if __name__ == "__main__":
    main()