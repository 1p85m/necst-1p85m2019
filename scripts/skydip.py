#!/usr/bin/env python3

import sys
import time
impport controller_1p85m2019
sys.path.append("/home/exito/necst-telescope/scripts")
import telescope_controller
sys.path.append("/home/exito/necst-core/scripts")
import core_controller
import rospy
import datetime

name = "skydip"

rospy.init_node(name)

logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

antenna = telescope_controller.antenna()
load = controller_1p85m2019.load()

az = 90
el = 20
el_cmds = [20, 24, 30, 40, 70]


print("Moving az: "+str(az)+ ", el: "+str(el))
antenna.move_azel(float(az),float(el))
time.sleep(10)

logger.start(file_name)

load.move_hot()
time.sleep(2)
load.move_sky()
time.sleep(2)

for el_cmds in el_cmds:
    print("Moving az: "+str(az)+ ", el: "+str(el_cmd))
    antenna.move_azel(float(az),float(el_cmd))
    time.sleep(5)
    continue

antenna.finalize()

load.move_hot()
time.sleep(2)
load.move_sky()
time.sleep(2)

logger.stop()
