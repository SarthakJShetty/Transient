#!/usr/bin/env python

import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from go_to_specific_point_on_map import specific_main

def callback(msg):
	odometry_data = msg.pose.pose.position
	print(odometry_data[0])

def listener():
	rospy.init_node('listener', anonymous=True)
	odom_sub = rospy.Subscriber('/odometry/filtered', Odometry, callback)
	#rospy.spin()

def processor(odometry_data):
	x_coordinate = str(odometry_data.x)
	y_coordinate = str(odometry_data.y)
	print(x_coordinate, y_coordinate)
	specific_main(x_coordinate, y_coordinate)

listener()