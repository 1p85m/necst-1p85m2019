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

name = "five_pointing_obs"

rospy.init_node(name)

logger = core_controller.logger()
antenna = telescope_controller.antenna()
load = controller_1p85m2019.load()

obsmode = rospy.Publisher('/'+name+'/obsmode', std_msgs.msg.String, queue_size=1)
target = rospy.Publisher('/'+name+'/target', std_msgs.msg.String, queue_size=1)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)


"""
parameter
"""
offset_x = 0 #deg
offset_y = 0 #deg
integ_hot = 20 #s
integ_off = 20 #s
integ_on = 20 #s

dx = 60/3600 #deg
dy = 60/3600 #deg
"""
off point coordinate
"""
#orikl
off_frame = "fk5"
off_ra_cmd = 82.55910596 #deg
off_dec_cmd = -5.66845794 #deg

#M17
#off_frame = "fk5"
#off_ra_cmd = 272.428 #deg
#off_dec_cmd = -14.0845 #deg

#IRC+10216
#off_frame = "fk4"
#off_ra_cmd = 146.562 #deg
#off_dec_cmd = 13.5125 #deg

# cyg x
#off_ra_cmd = 312.4486 #deg
#off_dec_cmd = 36.5084 #deg

# W51
#off_frame = "fk4"
#off_ra_cmd = 290.359 #deg
#off_dec_cmd = 13.9953 #deg

"""
target radec
"""
target_name = "Orion KL"
on_frame = "fk5"
obs_ra_cmd = 15*(5+35/60+14.16/3600) #deg
obs_dec_cmd = -(5+22/60+21.5/3600) #deg

#target_name = "IRC+10216"
#on_frame = "fk5"
#obs_ra_cmd = 146.989193 #deg
#obs_dec_cmd = 13.278768 #deg

#target_name = "M17"
#on_frame = "fk5"
#obs_ra_cmd = 275.096 #deg
#obs_dec_cmd = -16.1954 #deg

#target_name = 'Cyg X'
#obs_ra_cmd = 15*(20+28/60+40.8/3600) #deg
#obs_dec_cmd = 41+10/60+1/3600 #deg

#target_name = "W51"
#on_frame = "fk4"
#obs_ra_cmd = 290.359 #deg
#obs_dec_cmd = 14.4119 #deg

logger.start(file_name)
# move OFF point1
print("Moving OFF : ra,dec "+str(off_ra_cmd)+", "+str(off_dec_cmd))
antenna.move_wcs(off_ra_cmd,off_dec_cmd,frame=off_frame)
antenna.tracking_check()
print("track ")

#observe hot1
load.move_hot()
time.sleep(5)
obsmode.publish("{0:9}".format('hot start'))
time.sleep(integ_hot)
obsmode.publish("{0:9}".format('hot end'))
load.move_sky()
time.sleep(5)

# observe off1
obsmode.publish("{0:9}".format('off start'))
time.sleep(integ_off)
obsmode.publish("{0:9}".format('off end'))
time.sleep(1)

# move&observe ON point x_scan
# move&observe ON -dx point
target.publish(target_name)
print("Moving ra,dec "+str(obs_ra_cmd)+", "+str(obs_dec_cmd)+ ', dx:'+str(-dx))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x-dx,offset_y,frame=on_frame)
antenna.tracking_check()
print("track ")
obsmode.publish("{0:9}".format('on start'))
time.sleep(integ_on)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)
# move&observe ON point
print("Moving ra,dec "+str(obs_ra_cmd+offset_x)+", "+str(obs_dec_cmd+offset_y))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x,offset_y,frame=on_frame)
antenna.tracking_check()
print("track ")
obsmode.publish("{0:9}".format('on start'))
time.sleep(integ_on)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)

# move&observe ON +dx point
print("Moving ra,dec "+str(obs_ra_cmd+offset_x)+", "+str(obs_dec_cmd+offset_y)+ ', dx:'+str(+dx))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x+dx,offset_y,frame=on_frame)
antenna.tracking_check()
print("track ")
obsmode.publish("{0:9}".format('on start'))
time.sleep(integ_on)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)

# move OFF point2
print("Moving OFF : ra,dec "+str(off_ra_cmd)+", "+str(off_dec_cmd))
antenna.move_wcs(off_ra_cmd,off_dec_cmd,frame=off_frame)
antenna.tracking_check()
print("track ")

#observe hot2
load.move_hot()
time.sleep(5)
obsmode.publish("{0:9}".format('hot start'))
time.sleep(integ_hot)
obsmode.publish("{0:9}".format('hot end'))
load.move_sky()
time.sleep(5)

# observe off2
obsmode.publish("{0:9}".format('off start'))
time.sleep(integ_off)
obsmode.publish("{0:9}".format('off end'))
time.sleep(1)

# move&observe ON point y_scan
# move&observe ON -dy point
target.publish(target_name)
print("Moving ra,dec "+str(obs_ra_cmd+offset_x)+", "+str(obs_dec_cmd+offset_y)+ ', dy:'+str(-dy))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x,offset_y-dy,frame=on_frame)
antenna.tracking_check()
print("track ")
obsmode.publish("{0:9}".format('on start'))
time.sleep(integ_on)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)
# move&observe ON point
print("Moving ra,dec "+str(obs_ra_cmd+offset_x)+", "+str(obs_dec_cmd+offset_y))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x,offset_y,frame=on_frame)
antenna.tracking_check()
print("track ")
obsmode.publish("{0:9}".format('on start'))
time.sleep(integ_on)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)

# move&observe ON +dx point
print("Moving ra,dec "+str(obs_ra_cmd+offset_x)+", "+str(obs_dec_cmd+offset_y)+ ', dy:'+str(+dy))
antenna.move_wcs(obs_ra_cmd,obs_dec_cmd,offset_x,offset_y+dy,frame=on_frame)
antenna.tracking_check()
print("track ")
obsmode.publish("{0:9}".format('on start'))
time.sleep(integ_on)
obsmode.publish("{0:9}".format('on end'))
time.sleep(1)


antenna.finalize()

logger.stop()
