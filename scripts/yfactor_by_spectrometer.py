#!/usr/bin/env python3

name = 'yfactor_by_spectrometer'

import sys
import rospy
import time
import std_msgs.msg
import argparse
import datetime


sys.path.append("../../necst-core/scripts")
sys.path.append("../../necst-1p85m2019/scripts")

import controller
import core_controller
import controller_1p85m2019

rospy.init_node(name)

sis = controller_1p85m2019.sis()
logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name_hot = name  + '/hot/' + date + '.necstdb'
file_name_cold = name + '/cold/' + date + '.necstdb'
print(file_name_cold)
print(file_name_hot)

v1 = input("How much voltage CH1 ? [mV]")
v2 = input("How much voltage CH2 ? [mV]")
v3 = input("How much voltage CH3 ? [mV]")
v4 = input("How much voltage CH4 ? [mV]")
t  = input("How much integration time [s]")

sis.set_v(float(v1),"lhcp","lsb")
sis.set_v(float(v2),"lhcp","usb")
sis.set_v(float(v3),"rhcp","lsb")
sis.set_v(float(v4),"rhcp","usb")
time.sleep(1)
input('READY HOT MEASUREMENT? PRESS ENTER!!')
logger.start(file_name_hot)
time.sleep(int(t))
logger.stop()

input('READY COLD MEASUREMENT? PRESS ENTER!!')
logger.start(file_name_cold)
time.sleep(int(t))
logger.stop()
