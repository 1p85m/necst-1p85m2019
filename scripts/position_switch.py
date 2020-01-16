#!/usr/bin/env python3

import sys
import time
sys.path.append("/home/exito/ros/src/necst-telescope/scripts")
import telescope_controller
sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller
sys.path.append("/home/exito/ros/src/necst-1p85m2019/scripts")
import core_controller
import rospy
import datetime

name = "position_switch"

rospy.init_node(name)

logger = core_controller.logger()
antenna = telescope_controller.antenna()
load = controller_1p85m2019.load()

obsmode = rospy.Publisher('/'+name+'/obsmode', std_msgs.msg.String, queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

#off point coordinate
obs_ra_cmd = 15*(5+35/60+17.3/3600)
obs_dec_cmd = -5-23/60-28/3600
coord = 'fk4'

# target radec
obs_ra_cmd = 15*(5+35/60+17.3/3600)
obs_dec_cmd = -5-23/60-28/3600


# move OFF point
logger.start(file_name)

print("Moving OFF : ra,dec "+str(offf_ra_cmd)+", "+str(off_dec_cmd)+", frame="+ coord)
antenna.move_wcs(off_ra_cmd,off_dec_cmd,frame=coord)
antenna.tracking_check()
print("track ")
#observe hot
load.move_hot()
time.sleep(5)
obsmode.publish({0:9}.format('hot start'))
time.sleep(10)
obsmode.publish({0:9}.format('hot end'))
load.move_sky()
time.sleep(5)

# observe off
obsmode.publish({0:9}.format('off start'))
time.sleep(10)
obsmode.publish({0:9}.format('off end'))
time.sleep(1)

# move&observe ON point
print("Moving ra,dec "+str(ra_cmd)+", "+str(dec_cmd))
antenna.move_wcs(ra_cmd,dec_cmd)
antenna.tracking_check()
print("track ")

obsmode.publish({0:9}.format('on start'))
time.sleep(10)
obsmode.publish({0:9}.format('on end'))
time.sleep(1)

anntena.finalize()

logger.stop()
