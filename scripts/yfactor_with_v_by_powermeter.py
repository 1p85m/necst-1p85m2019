#!/usr/bin/env python3

name = 'yfactor_with_v_by_powermeter'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
import argparse
import datetime


sys.path.append("../../necst-core/scripts")


import core_controller
import controller_1p85m2019

rospy.init_node(name)

sis = controller_1p85m2019.sis()
logger = core_controller.logger()


initial_voltage = 0.  # mV
final_voltage   = 10. # mV
step            = 0.03 # mV
roop = int((final_voltage - initial_voltage) / step)


date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name_hot = name  + '/'+date +'/hot/' + date + '.necstdb'
file_name_cold = name + '/'+date +'/cold/' + date + '.necstdb'
print(file_name_hot)
print(file_name_cold)


time.sleep(1)
input('READY HOT MEASUREMENT? PRESS ENTER!!')
sis.set_v(float(initial_voltage),"lhcp","lsb")
sis.set_v(float(initial_voltage),"lhcp","usb")
sis.set_v(float(initial_voltage),"rhcp","lsb")
sis.set_v(float(initial_voltage),"rhcp","usb")
time.sleep(1)
logger.start(file_name_hot)
#####measure y-factor#####

for i in range(roop+1):
    v=initial_voltage+ step*i
    sis.set_v(float(v),"lhcp","lsb")
    sis.set_v(float(v),"lhcp","usb")
    sis.set_v(float(v),"rhcp","lsb")
    sis.set_v(float(v),"rhcp","usb")
    time.sleep(0.3)
    continue
logger.stop()


input('READY COLD MEASUREMENT? PRESS ENTER!!')

sis.set_v(float(initial_voltage),"lhcp","lsb")
sis.set_v(float(initial_voltage),"lhcp","usb")
sis.set_v(float(initial_voltage),"rhcp","lsb")
sis.set_v(float(initial_voltage),"rhcp","usb")
time.sleep(1)
logger.start(file_name_cold)
for i in range(roop+1):
    v=initial_voltage+ step*i
    sis.set_v(float(v),"lhcp","lsb")
    sis.set_v(float(v),"lhcp","usb")
    sis.set_v(float(v),"rhcp","lsb")
    sis.set_v(float(v),"rhcp","usb")
    time.sleep(0.3)
    continue
logger.stop()

sis.set_v(0,"lhcp","lsb")
sis.set_v(0,"lhcp","usb")
sis.set_v(0,"rhcp","lsb")
sis.set_v(0,"rhcp","usb")
