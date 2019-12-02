#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray

node_name = 'xffts_total_power'

class xffts_total_power(object):

    def __init__(self):
        self.board_num = rospy.get_param("~board_num")
        [rospy.Subscriber("/dev/xffts/board%d"%(i), Float64MultiArray, self.sum, callback_args = i) for i in range(int(self.board_num))]
        self.pub = [rospy.Publisher("/dev/xffts/board%d/tp"%(i), Float64, queue_size=1) for i in range(int(self.board_num))]


    def sum(self, q, arg):
        data = sum(q.data)
        self.pub[arg].publish(data)
        return

if __name__ == '__main__':
    rospy.init_node(node_name)
    xffts_total_power()
    rospy.spin()
