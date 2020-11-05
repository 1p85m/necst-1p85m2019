#!/bin/bash

for i in {1..10}
do
echo start ps_obs
ipython position_swich.py
sleep 2
if [ $(($i%2)) = 0 ]; then
        echo skydip
        ipython skydip.py
        sleep 2
fi
done
