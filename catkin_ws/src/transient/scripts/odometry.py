#!/usr/bin/env python

import math
import rospy
from nav_msgs.msg import Odometry
from time import sleep
from go_to_specific_point_on_map import location_main

def odometryPrint(msg):
	print(msg)

if __name__ == "__main__":
	rospy.init_node('odometry', anonymous="True")
	message = rospy.wait_for_message('/odometry/filtered', Odometry)
	print(message.pose.pose.position.x, message.pose.pose.position.y)
	#rospy.spin()