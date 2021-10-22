# timelapse-capture
Pi HQ Cam Timelapse photography

Move day old files to nas.
```bash
0 10 * * * find /home/pi/sources/timelapse-capture/low/* -mtime +1 -exec mv "{}" /home/pi/media/Nemesis/low \;
0 0 * * * find /home/pi/sources/timelapse-capture/normal/* -mtime +1 -exec mv "{}" /home/pi/media/Nemesis/normal \;
```

Move all files after the mode has finished
```bash
0 9 * * * mv /home/pi/sources/timelapse-capture/low/* /home/pi/media/Nemesis/low
0 21 * * * mv /home/pi/sources/timelapse-capture/normal/* /home/pi/media/Nemesis/normal
```