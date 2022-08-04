import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
import storm_islands
import gui
import digit_recognizer
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision

# initialize the WindowCapture class
wincap = WindowCapture()

def main():
    #waves, attacks = gui.menu()
    #print("waves: ", waves + '\nattacks:', attacks)
    #storm_islands.storm_islands_bot(int(waves), int(attacks))
    sleep(5)
    screenshot = wincap.get_screenshot()
    digits = digit_recognizer.digit_recognizer(screenshot, 0.95)
    print(digits)
    cv.imshow('frame', screenshot)
    cv.waitKey()
    print('Done')

if __name__ == "__main__":
    main()