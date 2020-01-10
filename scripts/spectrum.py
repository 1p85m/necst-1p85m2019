#!/usr/bin/env python3

import sys
import time
import rospy
from std_msgs.msg import Float64MultiArray

import numpy

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot

sys.path.append("../../necst-core/scripts")
import topic_utils

rospy.init_node('spec')
spec ={i: topic_utils.recv("/xffts_board0%d"%(i), Float64MultiArray) for i in range(1,5)}


fig = matplotlib.pyplot.figure(figsize=[16,8])
ax = [fig.add_subplot(2,2,i) for i in range(1,5)]
x = numpy.linspace(0,2,2**15)

[ax[i].plot(x, spec[i+1]) for i in range(4)]
[ax[i].set_title("xffts_board0%d"%(i+1)) for i in range(4)]
matplotlib.pyplot.show()
#time.sleep(10)
