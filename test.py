#!/bin/python

import picamera
import time

camera = picamera.PiCamera()

# Set camera config
camera.resolution = (1920, 1080)
camera.framerate = 100

camera.start_preview()
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    camera.stop_preview()
