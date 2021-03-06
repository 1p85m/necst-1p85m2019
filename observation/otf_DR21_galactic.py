import sys
import time
import numpy
import math
import os
import datetime
sys.path.append("/home/exito/ros/src/necst-telescope/scripts")
import telescope_controller
sys.path.append("/home/exito/ros/src/necst-core/scripts")
import core_controller
sys.path.append("/home/exito/ros/src/necst-1p85m2019/scripts")
import controller_1p85m2019
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String


###############parameter###################


name = "otf_DR21_gal"
param = {}

#Cygnus DR21
param["on_x"] = 81.68073214 #deg
param["on_y"] = 0.537422372

param["on_frame"] = "galactic"


param["on_offset_x"] = 0 #deg
param["on_offset_y"] = 0 #deg

param["num_x"] = 30
param["num_y"] = 30
param["delta_x"] = 40/3600
param["delta_y"] = 40/3600
param["delta_t"] = 0.5

param["ramp"] = 2

#DR 21
param["off_x"] = 86.4
param["off_y"] = -3.1

param["off_frame"] = "galactic"
param["off_integ"] = 5 #sec

param["hot_time"] = 5 #sec
param["hot_interval"] = 5 #min

param["direction"] = "H"


param["target"] = "DR 21"

param["dcos"] = 1


###################START OBSERVATION##########################

class otf_observation(object):

    last_timestamp = 0.
    interval = 10
    regist_time = 0

    def __init__(self):
        self.logger = core_controller.logger()
        self.antenna = telescope_controller.antenna()
        self.load = controller_1p85m2019.load()

        self.obsstatus = rospy.Publisher('/otf/status', String, queue_size=1)
        self.target = rospy.Publisher('/otf/target', String, queue_size=1)
        self.otfparam_on = rospy.Publisher('/otf/param/on', Float64MultiArray, queue_size=1)
        self.otfparam_scan = rospy.Publisher('/otf/param/scan', Float64MultiArray, queue_size=1)
        self.otfparam_off = rospy.Publisher('/otf/param/off', Float64MultiArray, queue_size=1)
        self.otfparam_hot = rospy.Publisher('/otf/param/hot', Float64MultiArray, queue_size=1)
        self.otfparam_direc = rospy.Publisher('/otf/param/direction', String, queue_size=1)

    def hot_obs(self,hot_time):
        self.load.move_hot()
        self.load.check_hot()
        self.obsstatus.publish("{0:9}".format('hot start'))
        time.sleep(hot_time)
        self.obsstatus.publish("{0:9}".format('hot end'))
        self.load.move_sky()
        self.load.check_hot()
        time.sleep(0.01)
        pass

    def off_obs(self,off_x,off_y,off_frame,off_integ):
        self.antenna.move_wcs(off_x,off_y,frame=off_frame)
        self.antenna.tracking_check()
        self.obsstatus.publish("{0:9}".format('off start'))
        time.sleep(off_integ)
        self.obsstatus.publish("{0:9}".format('off end'))
        time.sleep(0.01)
        pass

    def timer_regist(self,t):
        self.interval = t*60 #min->sec
        self.regist_time = time.time()
        pass

    def timer_check(self):
        now = time.time()
        if self.interval <= (now - self.regist_time):
            self.last_timestamp = now
            return True
        return False


    def pub_scan_param(self,param):

        on = Float64MultiArray()
        off = Float64MultiArray()
        scan = Float64MultiArray()
        hot = Float64MultiArray()
        target = String()
        direc = String()

        on.data = [param["on_x"],param["on_y"],param["on_offset_x"],param["on_offset_y"] ]
        scan.data = [param["num_x"],param["num_y"],param["delta_x"],param["delta_y"],param["delta_t"],param["ramp"]]
        off.data = [param["off_x"],param["off_y"],param["off_integ"]]
        hot.data = [param["hot_time"],param["hot_interval"]]
        target.data = param["target"]
        direc.data = param["direction"]

        time.sleep(0.01)
        self.otfparam_on.publish(on)
        time.sleep(0.01)
        self.otfparam_scan.publish(scan)
        time.sleep(0.01)
        self.otfparam_off.publish(off)
        time.sleep(0.01)
        self.otfparam_hot.publish(hot)
        time.sleep(0.01)
        self.target.publish(target)
        time.sleep(0.01)
        self.otfparam_direc.publish(direc)
        time.sleep(0.01)

    def start(self,param):
        name = "otf_test"
        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        file_name = name + '/' + date + '.necstdb'
        print(file_name)

        hot_time = param["hot_time"]
        hot_interval = param["hot_interval"]

        if param["direction"] == "H":
            total_scan = param["num_y"]
            x = param["on_x"]
            y = param["on_y"]
            dx = param["delta_x"]
            dy = param["delta_y"]
            frame = param["on_frame"]
            ramp = param["ramp"]
            num_x = param["num_x"]
            num_y = param["num_y"]
            dt = param["delta_t"]
            off_x = param["off_x"]
            off_y = param["off_y"]
            off_frame = param["off_frame"]
            off_integ = param["off_integ"]
            on_offset_x = param["on_offset_x"]
            on_offset_y = param["on_offset_y"]

        elif param["direction"] == "V":
            total_scan = param["num_x"]
            x = param["on_x"]
            y = param["on_y"]
            dx = param["delta_x"]
            dy = param["delta_y"]
            frame = param["on_frame"]
            ramp = param["ramp"]
            num_x = param["num_x"]
            num_y = param["num_y"]
            dt = param["delta_t"]
            off_x = param["off_x"]
            off_y = param["off_y"]
            off_frame = param["off_frame"]
            off_integ = param["off_integ"]
            on_offset_x = param["on_offset_x"]
            on_offset_y = param["on_offset_y"]

        self.logger.start(file_name)

        self.pub_scan_param(param)

        for scan_num in range(total_scan):
            self.obsstatus.publish("{0:9}".format('otf line '+str(scan_num)))
            time.sleep(0.1)
            #################HOT##############
            if self.timer_check():
                print("hot")
                self.antenna.move_wcs(off_x,off_y,frame=off_frame)
                self.load.move_hot()
                self.antenna.tracking_check()
                self.hot_obs(hot_time)
                self.timer_regist(hot_interval)
            else:
                pass

            #################OFF##############
            print("off")
            self.off_obs(off_x,off_y,off_frame,off_integ)

            #################ON##############
            if param["direction"] == "H":
                _lx = dx * (num_x+1)
                _ly = dy * (num_y)
                lx = _lx + dx/dt*ramp
                ly = 0
                ctr_x = x + on_offset_x
                ctr_y = y + on_offset_y
                sx = ctr_x - _lx/2 - dx/dt*ramp
                sy = ctr_y - _ly/2 + dy*scan_num
                scan_t = dt*(num_x+1) + ramp

            elif param["direction"] == "V":
                _lx = dx * (num_x)
                _ly = dy * (num_y+1)
                lx = 0
                ly = _ly + dy/dt*ramp
                ctr_x = x + on_offset_x
                ctr_y = y + on_offset_y
                sx = ctr_x - _lx/2 - dx*scan_num
                sy = ctr_y - _ly/2 + dy/dt*ramp
                scan_t = dt*(num_y+1) + ramp
                pass

            self.obsstatus.publish("{0:9}".format('on start'))
            print("scan "+str(scan_num))
            self.antenna.move_raster_wcs(sx,sy,lx,ly,scan_t,l_unit="deg",frame=frame)
            self.obsstatus.publish("{0:9}".format('on finish'))
            time.sleep(0.1)

        self.antenna.finalize()
        self.logger.stop()

        return

if __name__ == "__main__":
    rospy.init_node(name)
    otf = otf_observation()
    otf.start(param)
