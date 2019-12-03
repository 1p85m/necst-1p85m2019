#!/usr/bin/env python3

name = 'lo_freq_set'

import sys
import rospy

sys.path.append("../../necst-1p85m2019/scripts")

import controller_1p85m2019

rospy.init_node(name)

sis = controller_1p85m2019.sglo()

f1 = 225
f2 = 235.6
f3 = 4.0
f4 = 6.5

sis.set_1st_lo(float(f1),"lhcp")
sis.set_1st_lo(float(f2),"rhcp")
sis.set_2nd_lo(float(f3),"usb")
sis.set_2nd_lo(float(f4),"lsb")

sis.set_1st_lo_onoff("on","lhcp")
sis.set_1st_lo_onoff("on","rhcp")
sis.set_2nd_lo_onoff("on","usb")
sis.set_2nd_lo_onoff("on","lsb")
