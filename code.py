#!/bin/python3
from picamera import PiCamera
from fractions import Fraction
import datetime, time, sched

while True:
    # Capture long exposure shot
    cur_time = datetime.datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M")

    # You can change these as needed. Six seconds (6000000)
    # is the max for shutter speed and 800 is the max for ISO.
    speed = 6 # 6 seconds max exposure
    camera = PiCamera(
        resolution=(4056,3040),
        framerate = Fraction(1,speed),
    )
    camera.shutter_speed = speed * 1000000
    camera.iso = 60
    camera.exposure_mode = 'off'
    camera.vflip = False
    camera.hflip = False

    outfile = "low/%s_%x.jpg" % (stub,speed)
    camera.start_preview()
    time.sleep(2)
    camera.capture(outfile, format='jpeg', quality=90)
    camera.close()

    # Capture normal shot
    for exposure in range(-6,12,6):
        time.sleep(1)
        camera = PiCamera(
            resolution=(4056,3040)
        )
        camera.iso = 60
        camera.exposure_mode = 'night'
        camera.exposure_compensation = exposure
        camera.vflip = False
        camera.hflip = False
        #camera.meter_mode = 'matrix'

        outfile = "normal/%s_%x.jpg" % (stub,exposure)
        camera.start_preview()
        time.sleep(2)
        camera.capture(outfile, format='jpeg', quality=90)
        camera.close()
    
    # Now let's sleep to complete the minute
    time.sleep(45)
