#!/usr/bin/env python3

import sys
import time
import controller_1p85m2019
sys.path.append("../../necst-telescope/scripts")
import telescope_controller
sys.path.append("../../necst-core/scripts")
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

az = 
el = 20
el_cmd = 80


print("Moving az: "+str(az)+ ", el: "+str(el))
antenna.move_azel(float(az),float(el))
antenna.tracking_check()

logger.start(file_name)

load.move_hot()
time.sleep(5)
load.move_sky()
time.sleep(5)

print("Moving az: "+str(az)+ ", el: "+str(el_cmd))
antenna.move_azel(float(az),float(el_cmd))
time.sleep(2)
antenna.tracking_check()
time.sleep(1)

antenna.finalize()

load.move_hot()
time.sleep(5)
load.move_sky()
time.sleep(5)

logger.stop()
