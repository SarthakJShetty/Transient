'''Hello! This code is part of my bachelor's thesis on transiently informed robotic swarms.
The project is in it's nascency. Hence, the code is neither stable nor complete.

This bit of the script shall serve as the basis of the navigation stack.
Once complete the following tasks (1 -> 4) are expected of this module:

1. Autonomously map a given terrain (For this project we generate a simple map to be navigated) by scout.
1'. Autonomously map a given terrain, with little to no human intervention.
2. Grab co-ordinates of the initial point (P1) and final point (P2), upon completition of the mapping.
3. Autonomously navigate back to P1.
4. Navigate back to P2 (best possible path) with rest of the swarm.

- Sarthak J. Shetty
26/04/2019'''


'''Importing the required libraries here
rospy is the main library required, containing functions to publish and interact with the agents in Gazebo.'''
import rospy
'''Twist enables us to code the movements of the Husky including linear and angular movements, 
highlighted by linear & angular classes.'''
from geometry_msgs.msg import Twist

def movement_forward():
	'''This is the forward function where the movement of the bot is controlled from.'''

	'''/husky_velocity_controller/cmd_vel is the publisher to which the movement is sent to for control.
	 Two types of topics are published here, a) linear (x, y, z) & b) angular (x, y, z)'''
	cmd_vel = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)

	'''Rate at which the nodes are pinged with the velocity; i.e. 10Hz'''
	r = rospy.Rate(10)
	'''Here, we call the Twist variable move_cmd'''
	move_cmd = Twist()
	'''Linear movement of the bot has been coded here. The units are m/s.'''
	move_cmd.linear.x = 1.0
	'''Declaring the Z value of the angular velocity as 0 to avoid spin.'''
	move_cmd.angular.z = 0.0

	'''As long as the roscore has not been shutdown, publishing will occur at the rate of 10 Hz.'''
	while not rospy.is_shutdown():
		'''Publishing the commands here.'''
		cmd_vel.publish(move_cmd)
		'''Recheck the earlier condition'''
		r.sleep()

def movement_main():
	'''This is the main function where the node is declared and initialized, then the movement_forward() code is invoked.'''
	rospy.init_node('GoForward', anonymous = False)
	movement_forward()

'''Calling the main function for execution.'''
movement_main()