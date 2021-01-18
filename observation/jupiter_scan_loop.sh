#!/bin/bash

for i in {1..5}
do
if [ $(($i%4)) = 0 ]; then
        echo skydip start
        ipython skydip.py
        echo skydip end
        sleep 30
fi
echo jupiter_scan_loop start
ipython jupiter_scan_loop.py
echo jupiter_scan_loop end
sleep 90
done
