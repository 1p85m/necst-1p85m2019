#!/bin/bash

sleep 10800
for i in {1..9}
do
if [ $(($i%4)) = 0 ]; then
        echo skydip start
        ipython skydip.py
        sleep 30
echo start position_switch
ipython position_swich.py
sleep 180
fi
done
