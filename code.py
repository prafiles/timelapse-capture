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
    for speed in range(2,8,2):
        camera = PiCamera(
            resolution=(4056,3040),
            framerate = Fraction(1,speed),
        )
        camera.shutter_speed = speed * 1000000
        camera.iso = 100
        camera.exposure_mode = 'off'
        camera.vflip = True
        camera.hflip = True
        camera.format = 'rgb'

        outfile = "low/%s_%x.raw" % (stub,speed)
        camera.start_preview()
        time.sleep(4)
        camera.capture(outfile)
        camera.close()

    # Capture normal shot
    for exposure in range(-10,15,5):
        time.sleep(5)
        camera = PiCamera(
            resolution=(4056,3040)
        )
        camera.iso = 100
        camera.exposure_compensation = exposure,
        camera.vflip = True
        camera.hflip = True
        camera.meter_mode = 'matrix'
        camera.format = 'rgb'

        outfile = "normal/%s_%x.raw" % (stub,exposure)
        camera.start_preview()
        time.sleep(5)
        camera.capture(outfile)
        camera.close()
    
    # Now let's sleep to complete the minute
