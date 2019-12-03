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

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)


initial_voltage = 0.  # mV
final_voltage   = 12. # mV
step            = 0.1 # mV
roop = int((final_voltage - initial_voltage) / step)


date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name_hot = name  + '/'+date +'/hot/' + date + '.necstdb'
file_name_cold = name + '/'+date +'/cold/' + date + '.necstdb'
print(file_name_hot)
print(file_name_cold)


time.sleep(1)
input('READY HOT MEASUREMENT? PRESS ENTER!!')
sis.set_vgap(0)
logger.start(file_name_hot)
#####measure y-factor#####

for v in range(roop+1):
    v=initial_voltage+ step*i
    sis.set_v(float(v),"lhcp","lsb")
    sis.set_v(float(v),"lhcp","usb")
    sis.set_v(float(v),"rhcp","lsb")
    sis.set_v(float(v),"rhcp","usb")
    time.sleep(0.3)
    continue
logger.stop()


input('READY COLD MEASUREMENT? PRESS ENTER!!')
sis.set_vgap(0)
logger.start(file_name_cold)
ffor v in range(roop+1):
    v=initial_voltage+ step*i
    sis.set_v(float(v),"lhcp","lsb")
    sis.set_v(float(v),"lhcp","usb")
    sis.set_v(float(v),"rhcp","lsb")
    sis.set_v(float(v),"rhcp","usb")
    time.sleep(0.3)
    continue
logger.stop()

sis.set_v(0)