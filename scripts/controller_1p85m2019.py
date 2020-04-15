#!/usr/bin/env python3

name = '1p85m_controller'

import rospy

import time
import std_msgs.msg


class controller(object):
    def __init__(self):
        self.sis = sis()
        self.sglo = sglo()
        self.camera = camera()
        self.adios_att = adios_att()
        self.load = load()


class make_pub(object):

    def __init__(self):
        self.pub = {}
        pass

    def publish(self, topic_name, data_class, msg):
        if topic_name not in self.pub:
            self.set_publisher(topic_name = topic_name, data_class = data_class)
            pass

        self.pub[topic_name].publish(msg)
        return

    def set_publisher(self, topic_name, data_class):
        self.pub[topic_name] = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
        time.sleep(0.1)
        return

class sis(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_vp(self, cmd, pol, side_band):
        topic_dict = {
            'lhcp': {
                'lsb': '/1p85m/sis_l1/vp_cmd',
                'usb': '/1p85m/sis_l2/vp_cmd',
            },
            'rhcp': {
                'lsb': '/1p85m/sis_r1/vp_cmd',
                'usb': '/1p85m/sis_r2/vp_cmd',
            },
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[pol][side_band], data_class, msg=cmd)
        return

    def set_vgap(self, cmd, pol, side_band):
        topic_dict = {
            'lhcp': {
                'lsb': '/1p85m/sis_l1/vgap_cmd',
                'usb': '/1p85m/sis_l2/vgap_cmd',
            },
            'rhcp': {
                'lsb': '/1p85m/sis_r1/vgap_cmd',
                'usb': '/1p85m/sis_r2/vgap_cmd',
            },
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[pol][side_band], data_class, msg=cmd)
        return

    def set_v(self, cmd, pol, side_band):
        topic_dict = {
            'lhcp': {
                'lsb': '/1p85m/sis_l1/v_cmd',
                'usb': '/1p85m/sis_l2/v_cmd',
            },
            'rhcp': {
                'lsb': '/1p85m/sis_r1/v_cmd',
                'usb': '/1p85m/sis_r2/v_cmd',
            },
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[pol][side_band], data_class, msg=cmd)
        return


class sglo(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_1st_lo(self, cmd, pol):
        topic_dict = {
            'lhcp': '/1p85m/1st_lo_lhcp/f_cmd',
            'rhcp': '/1p85m/1st_lo_rhcp/f_cmd',
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[pol], data_class, msg=cmd)
        return

    def set_2nd_lo(self, cmd, side_band):
        topic_dict = {
            'lsb': '/1p85m/2nd_lo_lsb/f_cmd',
            'usb': '/1p85m/2nd_lo_usb/f_cmd',
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[side_band], data_class, msg=cmd)
        return

    def set_1st_sg(self, cmd, pol):
        topic_dict = {
            'lhcp': '/1p85m/1st_sg_lhcp/f_cmd',
            'rhcp': '/1p85m/1st_sg_rhcp/f_cmd',
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[pol], data_class, msg=cmd)
        return

    def set_2nd_sg(self, cmd, side_band):
        topic_dict = {
            'lsb': '/1p85m/2nd_sg_lsb/f_cmd',
            'usb': '/1p85m/2nd_sg_usb/f_cmd',
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[side_band], data_class, msg=cmd)
        return

    def set_1st_sg_onoff(self, cmd, pol):
        topic_dict = {
            'lhcp': '/1p85m/1st_sg_lhcp/onoff_cmd',
            'rhcp': '/1p85m/1st_sg_rhcp/onoff_cmd',
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[pol], data_class, msg=cmd)
        return

    def set_2nd_sg_onoff(self, cmd, side_band):
        topic_dict = {
            'lsb': '/1p85m/2nd_sg_lsb/onoff_cmd',
            'usb': '/1p85m/2nd_sg_usb/onoff_cmd',
        }
        data_class = std_msgs.msg.Float64
        self.make_pub.publish(topic_dict[side_band], data_class, msg=cmd)
        return

    def set_1st_lo_onoff(self, cmd, pol):
        topic_dict = {
            'lhcp': '/1p85m/1st_lo_lhcp/onoff_cmd',
            'rhcp': '/1p85m/1st_lo_rhcp/onoff_cmd',
        }
        data_class = std_msgs.msg.String
        self.make_pub.publish(topic_dict[pol], data_class, msg=cmd)
        return

    def set_2nd_lo_onoff(self, cmd, side_band):
        topic_dict = {
            'lsb': '/1p85m/2nd_lo_lsb/onoff_cmd',
            'usb': '/1p85m/2nd_lo_usb/onoff_cmd',
        }
        data_class = std_msgs.msg.String
        self.make_pub.publish(topic_dict[side_band], data_class, msg=cmd)
        return

class adios_att(object):
    def __init__(self):
        self.make_pub = make_pub()

    def set_att_ch1(self, cmd):
        data_class = std_msgs.msg.Int32
        topic_name = "/1p85m/adios/ch1/att_cmd"
        self.make_pub.publish(topic_name, data_class, msg=cmd)
        return

    def set_att_ch2(self, cmd):
        data_class = std_msgs.msg.Int32
        topic_name = "/1p85m/adios/ch2/att_cmd"
        self.make_pub.publish(topic_name, data_class, msg=cmd)
        return

    def set_att_ch3(self, cmd):
        data_class = std_msgs.msg.Int32
        topic_name = "/1p85m/adios/ch3/att_cmd"
        self.make_pub.publish(topic_name, data_class, msg=cmd)
        return

    def set_att_ch4(self, cmd):
        data_class = std_msgs.msg.Int32
        topic_name = "/1p85m/adios/ch4/att_cmd"
        self.make_pub.publish(topic_name, data_class, msg=cmd)
        return


class camera(object):
    def __init__(self):
        self.make_pub = make_pub()

    def capture(self,savepath):
        """
        msg
        - type : String

        """
        topic_name = '/dev/m100/capture/savepath'
        data_class = std_msgs.msg.String
        cmd = savepath
        self.make_pub.publish(topic_name, data_class, msg = cmd)
        pass


class load(object):
    def __init__(self):
        self.make_pub = make_pub()
        self.load_posi = topic_utils.receiver('/1p85m/load/position' ,std_msgs.msg.String)
        pass

    def move_sky(self):
        cmd = "sky"
        data_class = std_msgs.msg.String
        topic_name = "/1p85m/load/position_cmd"
        self.make_pub.publish(topic_name, data_class, msg=cmd)
        pass

    def move_hot(self):
        cmd = "hot"
        data_class = std_msgs.msg.String
        topic_name = "/1p85m/load/position_cmd"
        self.make_pub.publish(topic_name, data_class, msg=cmd)
        pass

    def check_hot(self):
        while not self.load_posi.recv() == "hot":
            time.sleep(0.01)
            continue
        return True

    def check_sky(self):
        while not self.load_posi.recv() == "sky":
            time.sleep(0.01)
            continue
        return True

    def check_load(self):
        return self.load_posi.recv()
