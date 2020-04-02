#!/usr/bin/env python3

import sys
import time
sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller
sys.path.append("/home/exito/ros/src/necst-1p85m2019/scripts")
import controller_1p85m2019
import rospy
import std_msgs
import datetime

name = "motor_speed_test"

rospy.init_node(name)

logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

pub = {}
base = '/pyinterface/pci7415/rsw0'

use_axis = 'x'

for ax in use_axis:
    b = '{base}/{ax}/'.format(**locals())
    pub[ax] = {}
    pub[ax]['step'] = rospy.Publisher(b+'step_cmd', std_msgs.msg.Int64, queue_size=1)
    pub[ax]['speed'] = rospy.Publisher(b+'speed_cmd', std_msgs.msg.Float64, queue_size=1)
    time.sleep(0.1)
#pub_outputdo =rospy.Publisher(base+'/output_do', std_msgs.msg.Int64MultiArray, queue_size=1)

time.sleep(0.1)
logger.start(file_name)
#conf = std_msgs.msg.Int64MultiArray()
#conf.data = [1,1,1,1]
#pub_outputdo.publish(conf)

#=====================================================
_speed = 5000

pub[use_axis]['speed'].publish(_speed)
time.sleep(10)

pub[use_axis]['speed'].publish(0)

logger.stop()
