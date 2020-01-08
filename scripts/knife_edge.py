#! /usr/bin/env python3

name = "knife_edge"

import sys
import time
import numpy
import math
import os
import datetime
sys.path.append("../../necst-core/scripts")
import core_controller
import rospy

import std_msgs.msg

rospy.init_node(name)

logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

pub = {}
base = '/pyinterface/pci7415/rsw0'

use_axis = 'u'

for ax in use_axis:
    b = '{base}/{ax}/'.format(**locals())
    pub[ax] = {}
    pub[ax]['step'] = rospy.Publisher(b+'step_cmd', std_msgs.msg.Int64, queue_size=1)
    #pub[ax]['speed'] = rospy.Publisher(b+'speed_cmd', std_msgs.msg.Float64, queue_size=1)
    time.sleep(0.1)
pub_outputdo =rospy.Publisher(base+'/output_do', std_msgs.msg.Int64MultiArray, queue_size=1)


#conf = std_msgs.msg.Int64MultiArray()
#conf.data = [0,0,0,0]
#pub_outputdo.publish(conf)


pub[use_axis]['step'].publish(4750)
time.sleep(5)

logger.start(file_name)
time.sleep(2)

pub[use_axis]['step'].publish(19700)
time.sleep(7)

logger.stop()
