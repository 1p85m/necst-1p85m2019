#!/bin/bash
echo otf start
for i in {1..16}
do
if [ $(($i%5)) = 0 ]; then
        echo skydip start
        ipython ../../necst-1p85m2019/scripts/skydip.py
        echo skydip end
        sleep 30
fi
ipython cross_scan_IRC_radec_2021_V.py
sleep 30
ipython cross_scan_IRC_radec_2021_H.py
sleep 30
done
echo otf end
