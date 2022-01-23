#!/bin/python3
from fractions import Fraction
import datetime, time, sched, os

while True:
    cur_time = datetime.datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M")
    print("Capturing: " + stub)
    command = '/usr/bin/libcamera-still -o normal/%s.jpg --denoise cdn_off -q 100 --post-process-file hdr.json --tuning-file imx477_noir.json' % stub
    stream = os.popen(command)
    output = stream.read()
    # Now let's sleep to complete the minute
    time.sleep(50)
