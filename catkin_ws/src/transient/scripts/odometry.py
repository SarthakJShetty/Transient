#!/usr/bin/env python

'''This script is part of the larger Transient project. Check it out here: https://github.com/SarthakJShetty/Transient. We are trying 
build swarm intelligence models inspired by transient ant swarms.

In this script, we initialize a node to subscribe to the odometry/filtered topic. For now, we evoke the functions at two different points:
1. Initial start point: P1
2. Goal final point: P2

- Sarthak J. Shetty

(09/05/2019)'''

import rospy
from nav_msgs.msg import Odometry

def read_coordinates():
	'''This function reads the coordinates from the odometry node and transfers it over to the odometry_main() function.'''

	'''Initializing the subscriber node here, which retrieves odometry data from the /odometry/filtered topic'''
	#rospy.init_node('odometry_subscriber', anonymous = True)
	'''The wait_for_message() function makes sure that the node runs until one message is retrieved, and stops after one message is retrieved.'''
	message = rospy.wait_for_message('/odometry/filtered', Odometry)
	'''Rounding the coordinates to 3 decimals places using the round() function'''
	return round(message.pose.pose.position.x, 3), round(message.pose.pose.position.y, 3)

def odometry_check():
	'''This function receives the coordinates from the read_coordinates() function and stores them for eventual use while rerouting to P1, from P2, P3...P(n).
	Workflow for the rest of the code:
	1. Return P1, initital point where the robot spawns within the Gazebo world.
	2. Until Frontier Exploration goal (P2) is reached, don't retrieve coordinates.
	3. Once P2 is reached, evoke autonomous navigation script once you reach it.'''

	p1_x_coordinates, p1_y_coordinates = read_coordinates()
	rospy.loginfo("Coordinates (%s, %s)", str(p1_x_coordinates), str(p1_y_coordinates))
	return p1_x_coordinates, p1_y_coordinates