'''Hello! This script is part of the larger Transient project, where we are trying to build swarm intelligence models
 for robots, inspired by transient ant swarms.
Check out the project at: https://github.com/SarthakJShetty/Transient

This script unifies the navigation stack together, and the different features can be evoked at once here.
Current flow of this script:
1. Initialize the node for the navigation_stack. - movement.py
2. Collect the P1(x, y) coordinates of the robot. - odometry.py
3. Provide a goal to be acheived. - goal_checker.py
4. Goal status goes to Goal pursued. - goal_checker.py
5. while loop in goal_checker get's triggered and activated. - goal_checker
6. Once goal status goes to Goal Acheived, while loop is exited. - goal_checker.py
7. P2(x, y) is noted down - odometry.py
8. Autonomous navigation is triggered - go_to_specific_point_on_map.py
9*. Declare a variable and hold sensor value in it. while sensor_value > threshold, proceed.
9'*. Else: execute evasive behaviour - goforward_and_avoid_obstacle.py '''

import rospy
from odometry import odometry_check
from goal_checker import goal_check
from autonomous_navigation import autonomous_routing
from goforward_and_avoid_obstacle import GoForwardAvoid
from scan import sensor_value
from mathwiz import calculator, waypoint_generator

def initialize_node():
	'''In this function, we initialize the node that will be utilized by the entire navigation stack'''
	rospy.init_node('navigation_stack_node', anonymous = True)

def movement_main():
	'''Declaring the main movement script here, which brings together the different parts of the navigation stack'''

	'''Initializing the navigation stack node here'''
	initialize_node()

	'''Grabbing p1(x, y), the initial point to go to once mapping has been performed'''
	p1_x, p1_y = odometry_check()

	'''Checking if agent has reached the goal provided via RViz interface'''
	while(goal_check() != " \"Goal reached.\""):
		rospy.loginfo("Goal Stauts:"+" " + str(goal_check()))

	'''This function extracts the final odometry of the robot once it has reached the goal'''
	p2_x, p2_y = odometry_check()

	'''This function returns the del_x and del_y calculator, which will be used to generate
	a series of way-points which will autonomously traversed.'''
	del_x, del_y = calculator(p1_x, p1_y, p2_x, p2_y)

	'''This function generates a set of waypoints that will be then sent over to the
	autonomous_routing() function.'''
	waypoints_x, waypoints_y = waypoint_generator(p1_x, p1_y, p2_x, p2_y, del_x, del_y)

	for waypoint_index in range(0, len(waypoints_x)):
		rospy.loginfo("Currently at waypoint:"+' '+str(waypoint_index))
		'''Checking if there's an obstacle up-ahead while moving through the waypoints'''
		if(sensor_value()<'1'):
			rospy.loginfo('Encountered Obstacle:'+' '+str(sensor_value()))
			'''If obstacle exists, GoForwardAvoid(), then go to destination'''
			GoForwardAvoid()
			autonomous_routing(waypoints_x[waypoint_index], waypoints_y[waypoint_index])
		else:
			'''If there is no obstacle, head over to the destination'''
			rospy.loginfo('No obstacle encountered')
			autonomous_routing(waypoints_x[waypoint_index], waypoints_y[waypoint_index])

movement_main()