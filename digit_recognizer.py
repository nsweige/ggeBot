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
from actions import attack, set_coord

# initialize the WindowCapture class
wincap = WindowCapture()

# initialize the Vision classes
vision_digit_0 = Vision('needle_images/digit_0.png')
vision_digit_1 = Vision('needle_images/digit_1.png')
vision_digit_2 = Vision('needle_images/digit_2.png')
vision_digit_3 = Vision('needle_images/digit_3.png')
vision_digit_4 = Vision('needle_images/digit_4.png')
vision_digit_5 = Vision('needle_images/digit_5.png')
vision_digit_6 = Vision('needle_images/digit_6.png')
vision_digit_7 = Vision('needle_images/digit_7.png')
vision_digit_8 = Vision('needle_images/digit_8.png')
vision_digit_9 = Vision('needle_images/digit_9.png')


def digit_recognizer(haystack_img, threshold=0.93):
    # recognize a sequence of digits

    # list of tuples(digit, x on screen where it appeard)
    digits_found = []

    digits_0 = vision_digit_0.find(haystack_img, threshold, 'points')
    if len(digits_0):
        for (x,y) in digits_0:
            digits_found.append((0, x)) # stores the tuple (digit, x on screen where it appeard)

    digits_1 = vision_digit_1.find(haystack_img, threshold, 'points')
    if len(digits_1):
        for (x,y) in digits_1:
            digits_found.append((1, x))

    digits_2 = vision_digit_2.find(haystack_img, threshold, 'points')
    if len(digits_2):
        for (x,y) in digits_2:
            digits_found.append((2, x))

    digits_3 = vision_digit_3.find(haystack_img, threshold, 'points')
    if len(digits_3):
        for (x,y) in digits_3:
            digits_found.append((3, x))

    digits_4 = vision_digit_4.find(haystack_img, threshold, 'points')
    if len(digits_4):
        for (x,y) in digits_4:
            digits_found.append((4, x))

    digits_5 = vision_digit_5.find(haystack_img, threshold, 'points')
    if len(digits_5):
        for (x,y) in digits_5:
            digits_found.append((5, x))

    digits_6 = vision_digit_6.find(haystack_img, threshold, 'points')
    if len(digits_6):
        for (x,y) in digits_6:
            digits_found.append((6, x))

    digits_7 = vision_digit_7.find(haystack_img, threshold, 'points')
    if len(digits_7):
        for (x,y) in digits_7:
            digits_found.append((7, x))

    digits_8 = vision_digit_8.find(haystack_img, threshold, 'points')
    if len(digits_8):
        for (x,y) in digits_8:
            digits_found.append((8, x))

    digits_9 = vision_digit_9.find(haystack_img, threshold, 'points')
    if len(digits_9):
        for (x,y) in digits_9:
            digits_found.append((9, x))    

    return digits_found