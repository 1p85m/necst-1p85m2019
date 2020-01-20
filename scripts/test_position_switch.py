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

name = "test_position_switch"

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
#off_ra_cmd = 82.55910596 #deg
#off_dec_cmd = -5.66845794 #deg
# cyg x
off_ra_cmd = 312.4486 #deg
off_dec_cmd = 36.5084 #deg

integ1 = 1
integ2 = 120
# move OFF point
logger.start(file_name)

print("Moving OFF : ra,dec "+str(off_ra_cmd)+", "+str(off_dec_cmd))
antenna.move_wcs(off_ra_cmd,off_dec_cmd)
antenna.tracking_check()
print("track ")
#observe hot
load.move_hot()
time.sleep(5)
obsmode.publish("{0:10}".format('hot start'))
time.sleep(integ1)
obsmode.publish("{0:10}".format('hot end'))
load.move_sky()
time.sleep(5)

# observe off
obsmode.publish("{0:10}".format('off start'))
time.sleep(integ1)
obsmode.publish("{0:10}".format('off end'))
time.sleep(1)

# move&observe ON point
#target.publish(target_name)

obsmode.publish("{0:10}".format('off2 start'))
time.sleep(integ2)
obsmode.publish("{0:10}".format('off2 end'))
time.sleep(1)

antenna.finalize()

logger.stop()
