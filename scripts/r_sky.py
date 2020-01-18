#!/usr/bin/env python3

import sys
import time
sys.path.append("/home/exito/ros/src/necst-telescope/scripts")
import telescope_controller
sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller
sys.path.append("/home/exito/ros/src/necst-1p85m2019/scripts")
import controller_1p85m2019
import rospy
import std_msgs
import datetime

name = "position_switch"

rospy.init_node(name)

logger = core_controller.logger()
load = controller_1p85m2019.load()

status = rospy.Publisher('/'+name+'/status', std_msgs.msg.String, queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

integ = 10

logger.start(file_name)

#observe hot
load.move_hot()
time.sleep(5)
status.publish("{0:9}".format('hot start'))
time.sleep(integ)
status.publish("{0:9}".format('hot end'))
load.move_sky()
time.sleep(5)

# observe off
status.publish("{0:9}".format('off start'))
time.sleep(integ)
status.publish("{0:9}".format('off end'))
time.sleep(1)

logger.stop()
