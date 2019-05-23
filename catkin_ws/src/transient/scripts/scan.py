import rospy
from sensor_msgs.msg import LaserScan

def callback(message):
	rospy.loginfo("\nValue at 0: %s \nValue at 90:%s \nValue at 180:%s \n", str(message.ranges[0]), str(message.ranges[360]), str(message.ranges[719]))

def main_function():
	rospy.init_node('laser_scanner', anonymous=True)
	sub = rospy.wait_for_message('/scan', LaserScan)
	callback(sub)
main_function()