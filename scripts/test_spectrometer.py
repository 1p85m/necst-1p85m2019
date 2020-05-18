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

name = "test_spectrometer"

rospy.init_node(name)

logger = core_controller.logger()
antenna = telescope_controller.antenna()
load = controller_1p85m2019.load()


date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)


az = 180
el = 20
obstime = 30

print("Moving az: "+str(az)+ ", el: "+str(el))
antenna.move_azel(float(az),float(el))
antenna.tracking_check()

load.move_hot()
time.sleep(5)

logger.start(file_name)

time.sleep(obstime)

logger.stop()

antenna.finalize()

load.move_sky()
time.sleep(5)
