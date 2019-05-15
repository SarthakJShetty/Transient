'''Hello! This script is part of the larger Transient project, where are attempting to build '''

import rospy
from actionlib_msgs.msg import GoalStatusArray

def initialize_node():
	rospy.init_node('goal_reader', anonymous = True)

def node_reader():
	message = rospy.wait_for_message('move_base/status', GoalStatusArray)
	message_str = str(message.status_list[0])
	message_list = message_str.split(':')
	status_text = message_list[7]
	return status_text

def initial():
	initialize_node()
	status_text = node_reader()
	default_text = " \"Goal reached.\""
	while (status_text != default_text):
		print(status_text)
		status_text = node_reader()

initial()