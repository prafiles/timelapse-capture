#!/bin/python3
from fractions import Fraction
import datetime, time, sched, os

while True:
    cur_time = datetime.datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M")

    if cur_time.hour < 8 or cur_time.hour > 17:
        print("Capturing Night " + stub)
        command = '/usr/bin/libcamera-still -o low/%s.jpg --shutter 3000000 --denoise cdn_off -q 100 --post-process-file hdr.json' % stub
        stream = os.popen(command)
        output = stream.read()
        time.sleep(5)
    
    if cur_time.hour > 5 and cur_time.hour < 20:
        print("Capturing HDR " + stub)
        # Capture HDR shot
        command = '/usr/bin/libcamera-still -o normal/%s.jpg --denoise cdn_off -q 100 --post-process-file hdr.json' % stub
        stream = os.popen(command)
        output = stream.read()
        time.sleep(5)
            
    # Now let's sleep to complete the minute
    time.sleep(50)
