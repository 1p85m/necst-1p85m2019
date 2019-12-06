#!/usr/bin/env python3

name = 'adios_att_set'

att1 = 10
att2 = 11
att3 = 12
att4 = 13

import sys
import rospy

sys.path.append("../../necst-core/scripts")
sys.path.append("../../necst-1p85m2019/scripts")

import core_controller
import controller_1p85m2019

rospy.init_node(name)

adios = controller_1p85m2019.adios_att()

adios.set_att_ch1(att1)
adios.set_att_ch2(att2)
adios.set_att_ch3(att3)
adios.set_att_ch4(att4)
