#!/bin/bash

for i in {1..30}
do
if [ $(($i%4)) = 0 ]; then
        echo skydip start
        ipython skydip.py
        echo skydip end
        sleep 30
fi
echo sun_scan start
ipython sun_scan_loop.py
echo sun_scan end
sleep 300

done
