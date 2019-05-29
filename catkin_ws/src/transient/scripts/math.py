'''Hello! This script is part of the larger Transient project, which you can 
check out here: https:github.com/SarthakJShetty/Transient.

-29/05/2019
Sarthak

Loop to be implemented in this script:
	1. Get P2 co-ordinates
	2. Calculate del(x)=|P1_x - P2_x|/10 & del(y)=|P1_y - P2_y|/10
	3. Intermittent values from P1 to P2 store two lists
	4. Loop through each member of the list
	5. Plug into autonomous_routing
	6. Run goal_checker() at the end of each
	7*. rospy.sleep(10) to flush goal status before moving onto the next set of points'''

def calculator(p1_x, p1_y, p2_x, p2_y):
	'''This function calculates the increments which will be appended to p1(x, y)'''
	'''Calculating the mod of the difference and returning it back to the movement script'''
	del_x = float(abs(int(p1_x) - int(p2_x)))/10
	del_y = float(abs(int(p1_y) - int(p2_y)))/10
	print(del_x, del_y)
	return del_x, del_y

def waypoint_generator(p1_x, p1_y, del_x, del_y):
	'''This function generates a set of 10 waypoints which will be then sent to the autonomous_routing()
	 function. This list is then sent over to the movement script.'''
	waypoints_x = []
	waypoints_y = []

	'''Here, we are looping through the increments added to p1(x, y)'''
	for waypoint_counter in range(0, 10):
		'''Incrementing the value of p1(x, y) using a simple linear function'''
		temp_p1_x = p1_x + (waypoint_counter + 1)*del_x
		temp_p1_y = p1_y + (waypoint_counter + 1)*del_y
		'''Rounding the value so that the robot does not get stuck in infinite loops'''
		temp_p1_x = round(temp_p1_x, 2)
		temp_p1_y = round(temp_p1_y, 2)
		'''Appending the acquired to a list which will be then passed to the autonomous routing function'''
		waypoints_x.append(temp_p1_x)
		waypoints_y.append(temp_p1_y)
	
	return waypoints_x, waypoints_y