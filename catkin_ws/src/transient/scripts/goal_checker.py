'''Hello! This script is part of the larger Transient project, where are attempting to build swarm intelligence models,
inspired by transient behaviour seen in ant swarms.
Checkout the project at: https://GitHub.com/SarthakJShetty/Transient

This script is responsible for retreiving the goal status of the robot. Once the robot has reached the goal, 
which implies that it has explored the given area provided by the user, it has to go back to the initial point 
from where it had started.
This process, of intimation of goal acheived is carried out by this script.

Eventually, these scripts will be integrated into the movement.py script.

Cheers!
- Sarthak J. Shetty
(15/05/2019)'''

import rospy
from actionlib_msgs.msg import GoalStatusArray

def node_reader():
	'''This function reads what the move_base/status topic is publishing, in order to track an update to the goal status,
	and then send the status over to the initial function, where appropriate action will be taken.'''

	'''Here, we read the message being published by yhe move_base/status topic. Note, the format of the message is GoalStatusArray,
	 which is obtained from the actionlib_msgs.msg library'''
	message = rospy.wait_for_message('move_base/status', GoalStatusArray)

	'''This block of code processes the message retrieved and only sends the goal status over the wire to the intial node.'''
	message_str = str(message.status_list[0]).split(':')[7]
	return message_str

def goal_check():
	'''This is the main node where the different functions are sequentially executed to retrieve the goal_status.
	Eventually, this function will be called over in the movement.py script.'''

	'''Reading the current goal status, before action is taken.'''
	status_text = node_reader()
	'''Return status_text as read by the node reader'''
	return status_text