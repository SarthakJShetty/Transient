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
9*. Declare a variable and hold sensor value in it. while sensorvalue > threshold, proceed.
9'*. Else: execute evasive behaviour - goforward_and_avoid_obstacle.py '''

import rospy
from odometry import odometry_main
from goal_checker import initial
from go_to_specific_point_on_map import location_main

def initialize_node():
	'''In this function, we initialize the node that will be utilized by the entire navigation stack'''
	rospy.init_node('navigation_stack_node', anonymous = True)

def movement_main():
	'''Main function where individual bits of the stack are evoked one-by-one'''
	initialize_node()
	p1_x, p1_y = odometry_main()
	initial()
	p2_x, p2_y = odometry_main()
	location_main(p1_x, p1_y)

movement_main()