import rospy
from sensor_msgs.msg import LaserScan
from goforward_and_avoid_obstacle import GoForwardAvoid

'''def callback(message):
	return str(message.ranges[360])'''

def sensor_value():
	'''rospy.init_node('laser_scanner', anonymous=True)'''
	sub = rospy.wait_for_message('/scan', LaserScan)
	return str(sub.ranges[360])