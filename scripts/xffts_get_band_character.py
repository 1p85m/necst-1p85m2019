#! /usr/bin/env python3

# Configurations
# ==============

name = 'xffts_get_band_character'


# import
# ======

import sys
import time
import argparse
import numpy
import rospy
import std_msgs.msg

sys.path.append("../../necst-core/scripts")
import core_controller

rospy.init_node(name)

logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

# argparse
# ========

# configurations
# --------------


integ = 1.0

"""
desc = 'Measure XFFTS band character.'
p = argparse.ArgumentParser(description=desc)
p.add_argument('--integ', type=float,
               help='integration time in sec. default is  %f'%(integ))
args = p.parse_args()

# load args
# ---------
if args.integ is not None: integ = args.integ
"""
# main
# ====
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Mesure XFFTS band character')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# start logging
# -------------
db_path = name + '/' + date

pub_integ = rospy.Publisher('/'+name+'/integ', std_msgs.msg.Float32, queue_size=1)
time.sleep(0.5)

logger.start(file_name)
time.sleep(0.5)

pub_integ.publish(integ)
# get band character
# --------------
time.sleep(integ)

logger.stop()


print('')
print('FINISH!!')
print('')
