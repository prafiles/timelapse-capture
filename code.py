#!/bin/python3
from picamera import PiCamera
from fractions import Fraction
import datetime, time, sched, os

while True:
    cur_time = datetime.datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M")

    if cur_time.hour < 8 or cur_time.hour > 17:
        # Capture long exposure shot
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
        time.sleep(5)
    
    if cur_time.hour > 5 or cur_time.hour < 20:

        # Capture HDR shot
        command = '/usr/local/bin/libcamera-still -o %s.jpg --denoise cdn_off -q 100 --post-process-file hdr.json' % stub
        stream = os.popen(command)
        output = stream.read()
            
    # Now let's sleep to complete the minute
    time.sleep(60)
