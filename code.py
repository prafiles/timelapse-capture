#!/bin/python3
from picamera import PiCamera
import time
from fractions import Fraction
import datetime

while True:
    # Capture long exposure shot
    cur_time = datetime.datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M_low")
    
    camera = PiCamera(framerate=Fraction(1,6))
    
    
    # You can change these as needed. Six seconds (6000000)
    # is the max for shutter speed and 800 is the max for ISO.
    camera.shutter_speed = 1750000
    camera.iso = 100
    camera.exposure_mode = 'off'
    camera.vflip=True
    camera.resolution=(4056,3040)
    outfile = "low/%s.jpg" % (stub)
    camera.start_preview()
    time.sleep(2)
    camera.capture(outfile)
    camera.close()

    # Capture normal shot
    stub = cur_time.strftime("%Y%m%d%H%M")
    camera = PiCamera()
    # camera.shutter_speed = 1750000
    camera.iso = 100
    camera.exposure_mode = 'off'
    camera.vflip=True
    camera.resolution=(4056,3040)
    outfile = "normal/%s.jpg" % (stub)
    camera.start_preview()
    time.sleep(2)
    camera.capture(outfile)
    camera.close()
    
    # Now let's sleep to complete the minute
    time.sleep(45)
