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

name = "ps_W51"

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

# W51
off_frame = "fk4"
off_ra_cmd = 290.359 #deg
off_dec_cmd = 13.9953 #deg

# target radec

target_name = "W51"
on_frame = "fk4"
obs_ra_cmd = 290.359 #deg
obs_dec_cmd = 14.4119 #deg
offset_x = 0.0
offset_y = 0.0

integ = 60

# move OFF point
logger.start(file_name)

print("Moving OFF : ra,dec "+str(off_ra_cmd)+", "+str(off_dec_cmd))
antenna.move_wcs(off_ra_cmd,off_dec_cmd,frame=off_frame)
antenna.tracking_check()
print("track ")
#observe hot
load.move_hot()
time.sleep(5)
obsmode.publish("{0:9}".format('hot start'))
time.sleep(integ)
obsmode.publish("{0:9}".format('hot end'))
print('observe_hot')
input()
load.move_sky()
time.sleep(5)

# observe off
obsmode.publish("{0:9}".format('off start'))
time.sleep(integ)
obsmode.publish("{0:9}".format('off end'))
print('observe_off')
input()
time.sleep(1)

# move&observe ON point
target.publish(target_name)
print("Moving ra,dec "+str(obs_ra_cmd+offset_x)+", "+str(obs_dec_cmd+offset_y))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x,offset_y,frame=on_frame)
antenna.tracking_check()
print("track ")

obsmode.publish("{0:9}".format('on start'))
time.sleep(integ)
obsmode.publish("{0:9}".format('on end'))
print('move&observe_ON_point_input')
input()
time.sleep(1)

antenna.finalize()

logger.stop()
