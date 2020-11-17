#!/bin/bash

sleep 10800
for i in {1..9}
do
if [ $(($i%4)) = 0 ]; then
        echo skydip start
        ipython skydip.py
        echo skydip end
        sleep 30
fi
echo position_switch start
ipython position_swich.py
echo position_switch start
sleep 180
done
