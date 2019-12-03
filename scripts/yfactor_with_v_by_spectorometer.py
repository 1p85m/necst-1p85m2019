#!/usr/bin/env python3
name = 'yfactor_with_v_by_spectrometer'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse
import datetime

sys.path.append("../../necst-core/scripts")

import controller_1p85m2019
import core_controller

rospy.init_node(name)

logger = core_controller.logger()
sis = controller_1p85m2019.sis()

status = rospy.Publisher('/'+name+'/status', std_msgs.msg.String, queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)


# set params.

initial_voltage = 0.  # mV
final_voltage   = 10. # mV
step            = 0.1 # mV
integ_time      = 1
roop = int((final_voltage - initial_voltage) / step)


logger.start(file_name)
sis.set_v(float(initial_voltage),"lhcp","usb")
sis.set_v(float(initial_voltage),"lhcp","lsb")
sis.set_v(float(initial_voltage),"rhcp","usb")
sis.set_v(float(initial_voltage),"rhcp","lsb")

time.sleep(1)

input('READY HOT MEASUREMENT? PRESS ENTER!!')
status.publish("{0:4}".format("hot"))

for i in range(roop+1):
    v = initial_voltage + i*step
    sis.set_v(float(v),"lhcp","usb")
    sis.set_v(float(v),"lhcp","lsb")
    sis.set_v(float(v),"rhcp","usb")
    sis.set_v(float(v),"rhcp","lsb")
    time.sleep(integ_time)

sis.set_v(float(initial_voltage),"lhcp","usb")
sis.set_v(float(initial_voltage),"lhcp","lsb")
sis.set_v(float(initial_voltage),"rhcp","usb")
sis.set_v(float(initial_voltage),"rhcp","lsb")

input('READY COLD MEASUREMENT? PRESS ENTER!!')
status.publish("{0:4}".format("cold"))

for i in range(roop+1):
    v = initial_voltage + i*step
    sis.set_v(float(v),"lhcp","usb")
    sis.set_v(float(v),"lhcp","lsb")
    sis.set_v(float(v),"rhcp","usb")
    sis.set_v(float(v),"rhcp","lsb")
    time.sleep(integ_time)
status.publish("{0:4}".format("hot"))
time.sleep(0.1)
logger.stop()

sis.set_v(0,"lhcp","usb")
sis.set_v(0,"lhcp","lsb")
sis.set_v(0,"rhcp","usb")
sis.set_v(0,"rhcp","lsb")

print('')
print('FINISH!!')
print('')
