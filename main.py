import cv2 as cv
import numpy as np
import os
import pyautogui
import random
import keyboard
from fortresses import updateSpreadsheet
import storm_islands
import gui
import digit_recognizer
import fortresses
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision

# initialize the WindowCapture class
wincap = WindowCapture()

def main():
    #waves, attacks = gui.menu()
    #print("waves: ", waves + '\nattacks:', attacks)
    #storm_islands.storm_islands_bot(int(waves), int(attacks))
    sleep(2)
    updateSpreadsheet()

    #cv.imshow('frame', screenshot)
    #cv.waitKey()
    #print('Done')

if __name__ == "__main__":
    main()