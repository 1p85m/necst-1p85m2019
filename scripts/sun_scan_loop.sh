#!/bin/bash

for i in {1..24}
do
if [ $(($i%4)) = 0 ]; then
        echo skydip start
        ipython skydip.py
        sleep 30
echo start sun_scan
ipython ../../necst-telescope/scripts/sun_scan_loop.py
sleep 300
fi
done
