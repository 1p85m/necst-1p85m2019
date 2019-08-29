#!/usr/bin/env python3

name = '1p85m2019_controller'

import rospy

import time
import std_msgs.msg


class controller(object):

    def __init__(self):
        self.sis = sis()
        self.sglo1 = sglo1()
        self.sgirr = sgirr()
        #self.loatt_h = loatt_h()
        #self.loatt_v = loatt_v()


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

    def set_v1_vp(self, command):
        topic_name = '/tz2019/sis_v1/vp_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h1_vp(self, command):
        topic_name = '/tz2019/sis_h1/vp_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h2_vp(self, command):
        topic_name = '/tz2019/sis_h2/vp_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v2_vp(self, command):
        topic_name = '/tz2019/sis_v2/vp_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v1_vgap(self, command):
        topic_name = '/tz2019/sis_v1/vgap_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h1_vgap(self, command):
        topic_name = '/tz2019/sis_h1/vgap_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h2_vgap(self, command):
        topic_name = '/tz2019/sis_h2/vgap_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v2_vgap(self, command):
        topic_name = '/tz2019/sis_v2/vgap_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v1_v(self, command):
        topic_name = '/tz2019/sis_v1/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h1_v(self, command):
        topic_name = '/tz2019/sis_h1/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_h2_v(self, command):
        topic_name = '/tz2019/sis_h2/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_v2_v(self, command):
        topic_name = '/tz2019/sis_v2/v_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class sglo1(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_freq(self, command):
        topic_name = '/tz2019/sg_lo1/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_power(self, command):
        topic_name = '/tz2019/sg_lo1/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_onoff(self, command):
        topic_name = '/tz2019/sg_lo1/onoff_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class sgirr(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_freq(self, command):
        topic_name = '/tz2019/sg_irr/f_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_power(self, command):
        topic_name = '/tz2019/sg_irr/p_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return

    def set_onoff(self, command):
        topic_name = '/tz2019/sg_irr/onoff_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class loatt_h(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_cur(self, command):
        topic_name = '/tz2019/loatt_h/i_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return


class loatt_v(object):

    def __init__(self):
        self.make_pub = make_pub()

    def set_cur(self, command):
        topic_name = '/tz2019/loatt_v/i_cmd'
        data_class = std_msgs.msg.Float64

        self.make_pub.publish(topic_name, data_class, msg = command)
        return
