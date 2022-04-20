#!/bin/python3
# from fractions import Fraction
# from threading import Thread
from time import sleep
from datetime import datetime
from os import popen

def get_time():
    cur_time = datetime.now()
    stub = cur_time.strftime("%Y%m%d%H%M")
    return stub

def capture():
    stub = get_time()
    print("Capturing: " + stub)
    command = '/usr/bin/libcamera-still -o normal/%s.jpg --denoise cdn_off -q 100 --post-process-file hdr.json --tuning-file imx477_noir.json' % stub
    print("Command: " + command)
    stream = popen(command)
    output = stream.read()
    print("Output: " + str(output))

def timer():
    while True:
        print("Capture started: " + get_time())
        capture() # called every minute
        # Now let's sleep to complete the minute
        sleep(55)

print("Starting Timer")
timer()