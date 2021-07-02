# encoding: UTF-8
import cv2 #sudo apt-get install python-opencv
import numpy as py
import os
import sys
import time
try:
    import picamera
    from picamera.array import PiRGBArray
except:
    sys.exit(0)

from Focuser import Focuser
from AutoFocus import AutoFocus
import curses

image_count = 0
global status
status = 1

def main():
    camera = picamera.PiCamera()
    #open camera preview
    global image_count
    camera.resolution = (2500,1900)
    while status == 1:
        camera.capture("image{}.jpg".format(image_count))
        image_count += 1
        time.sleep(10)

if __name__ == "__main__":
    main()