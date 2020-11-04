#! /usr/bin/env python3

name = "knife_edge"

import time
import rospy

import std_msgs.msg

rospy.init_node(name)

#logger = core_controller.logger()

#date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
#file_name = name + '/' + date + '.necstdb'
#print(file_name)

base = '/pyinterface/pci7415/rsw0'

pub_do3 = rospy.Publisher(base+'output_do3', std_msgs.msg.Int64, queue_size=1)
pub_do4 = rospy.Publisher(base+'output_do4', std_msgs.msg.Int64, queue_size=1)

#reset alart
pub_do3.publish(1)
time.sleep(5)

#initialize
pub_do4.publish(1)
time.sleep(5)
