#!/bin/bash

for i in {1..25}
do
if [ $(($i%5)) = 0 ]; then
        echo skydip start
        ipython skydip.py
        echo skydip end
        sleep 30
fi
echo position_switch start
python ps_orionKL_202101.py
echo position_switch start
sleep 10
done
