import rospy
from sensor_msgs.msg import LaserScan
from goforward_and_avoid_obstacle import GoForwardAvoid

def scan_init_node():
	rospy.init_node('laser_scanner', anonymous=True)

def sensor_value():
	sub = rospy.wait_for_message('/scan', LaserScan)
	return str(sub.ranges[360])