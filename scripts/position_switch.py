#!/usr/bin/env python3

import sys
import time
sys.path.append("/home/exito/ros/src/necst-telescope/scripts")
import telescope_controller
sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller
sys.path.append("/home/exito/ros/src/necst-1p85m2019/scripts")
import controller_1p85m2019
import rospy
import std_msgs
import datetime

name = "position_switch"

rospy.init_node(name)

logger = core_controller.logger()
antenna = telescope_controller.antenna()
load = controller_1p85m2019.load()

obsmode = rospy.Publisher('/'+name+'/obsmode', std_msgs.msg.String, queue_size=1)
target = rospy.Publisher('/'+name+'/target', std_msgs.msg.String, queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

#off point coordinate
#orikl
off_ra_cmd = 82.55910596 #deg
off_dec_cmd = -5.66845794 #deg
# cyg x
#off_ra_cmd = 312.4486 #deg
#off_dec_cmd = 36.5084 #deg

# target radec
target_name = 'Orion KL'
obs_ra_cmd = 15*(5+35/60+14.16/3600) #deg
obs_dec_cmd = -5+22/60+21.5/3600 #deg

#target_name = 'Cyg X'
#obs_ra_cmd = 15*(20+28/60+40.8/3600) #deg
#obs_dec_cmd = 41+10/60+1/3600 #deg

integ = 10

# move OFF point
logger.start(file_name)

print("Moving OFF : ra,dec "+str(off_ra_cmd)+", "+str(off_dec_cmd))
antenna.move_wcs(off_ra_cmd,off_dec_cmd)
antenna.tracking_check()
print("track ")
#observe hot
load.move_hot()
time.sleep(5)
obsmode.publish("{0:9}".format('hot start'))
time.sleep(integ)
obsmode.publish("{0:9}".format('hot end'))
load.move_sky()
time.sleep(5)

# observe off
obsmode.publish("{0:9}".format('off start'))
time.sleep(integ)
obsmode.publish("{0:9}".format('off end'))
time.sleep(1)

# move&observe ON point
target.publish(target_name)
print("Moving ra,dec "+str(obs_ra_cmd)+", "+str(obs_dec_cmd))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd)
antenna.tracking_check()
print("track ")

obsmode.publish("{0:9}".format('on start'))
time.sleep(integ)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)

antenna.finalize()

logger.stop()
