#!/usr/bin/env python3

name = 'sis_set'

import sys
import rospy


sys.path.append("../../necst-core/scripts")
sys.path.append("../../necst-1p85m2019/scripts")

import core_controller
import controller_1p85m2019

rospy.init_node(name)

sis = controller_1p85m2019.sis()

v1 = input("How much voltage CH1 ? [mV]")
v2 = input("How much voltage CH2 ? [mV]")
v3 = input("How much voltage CH3 ? [mV]")
v4 = input("How much voltage CH4 ? [mV]")

sis.set_v(float(v1),"lhcp","lsb")
sis.set_v(float(v2),"lhcp","usb")
sis.set_v(float(v3),"rhcp","lsb")
sis.set_v(float(v4),"rhcp","usb")


