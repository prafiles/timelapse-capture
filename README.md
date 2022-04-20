# timelapse-capture
Pi HQ Cam Timelapse photography

Move day old files to nas.
```bash
0 0 * * * find /home/pi/sources/timelapse-capture/normal/* -mtime +1 -exec mv "{}" /home/pi/media/Nemesis/normal \;
```
