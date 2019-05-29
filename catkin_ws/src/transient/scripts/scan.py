''' This script is part of the larger Transient project, which you can check out here: https://github.com/SarthakJShetty/Transient
This script is designed to retrieve the readings of the LiDAR unit mounted on the Clearpath Husky. 

-27/05/2019
Sarthak'''

import rospy
from sensor_msgs.msg import LaserScan
from goforward_and_avoid_obstacle import GoForwardAvoid

def scan_init_node():
	'''Initializing the nodes here if we use this unit independently of the movement.py script.'''
	rospy.init_node('laser_scanner', anonymous=True)

def sensor_value():
	'''This function retrieves the LiDAR readings over to the movement.py script.
	We use a wait_for_message() to make sure there is a message waiting at the other end'''
	sub = rospy.wait_for_message('/scan', LaserScan)
	'''Specifically tapping into the 360 degree laser scan reading, which gives the stream from the 
	array up front.'''
	return str(sub.ranges[360])