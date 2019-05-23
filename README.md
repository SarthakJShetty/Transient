# Transient

Developing swarm intelligence models for robots inspired by transient behaviour of ant swarms.

:warning: **Code is buggy** :warning:

### Introduction:

This repository contains code & resources for thesis research project, titled **"Transiently Informed Robotic Swarms for Search & Rescue"**, being undertaken at the <a title="IISc" href="https://iisc.ac.in" target="_blank">Indian Institute of Science</a>, Bengaluru.

**Thesis Advisors:** <a title="Professor Guttal" href="https://teelabiisc.wordpress.com/curriculum-vitae/" target="_blank">Dr. Vishwesha Guttal</a> **[1]** & <a title="Professor Ghose" href="http://www.aero.iisc.ernet.in/people/debasish-ghose/" target="_blank">Dr. Debasish Ghose</a> **[2]**.

**[1]** - <a title="CES, IISc" href="http://ces.iisc.ernet.in" target="_blank">Center for Ecological Sciences</a>, Indian Institute of Science, Bengaluru.
<br>
**[2]** - <a title="Aerospace Engineering, IISc" href="http://www.aero.iisc.ernet.in" target="_blank">Department of Aerospace Engineering</a>, Indian Institute of Science, Bengaluru.

- The main purpose of this package is to design a navigation stack for swarm robots, inspired by transient behaviour as seen in ant groups. <a title="Gelblum et al" href="https://www.nature.com/articles/ncomms8729" target="_blank">**[3]**</a>

- We hypothesize, that such an architecture will bring about a reduction in the amount of energy expended by the entire swarm, all the while being directed along the optimal path to the destination, in-turn set by a user.

- Currently, this repository contains ```catkin_ws```, which is the ```catkin``` workspace for the project. It contains the ```transient``` package which in-turn comprises of the (launch) [https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/launch] files and [scripts](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/scripts).

### Pacakge Overview:

#### 1. [Scripts](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/scripts)
	
- [Movement](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/movement.py): This script brings together the different parts of the navigation stack together, and acts as the central script triggered at the start of the autonomous simulations.

- [Odometry](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/odometry.py): This script subscribes to the odometry data being published by the ```/odom``` topic. The coordinates are then passed over to the ```goal_checker.py``` script.
	
- [Autonomous Navigation](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/autonomous_navigation.py) - This script charts a path to a given set of coordinates from the mapping data accumlated by the ```gmapping``` module. The robot then autonomously traverses this path.
	
- [Goal Checker](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/goal_checker.py): This script subscribes to the ```/move_base/goal``` topic and checks if the robot has reached the coordinates specified by the user.

#### 2. [Launch Files](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/launch)

- [Gazebo Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient_gazebo.launch): This ```.launch``` file triggers the Gazebo environment and the ```playpen``` configuration of the prototyping world.
	
- [RViz Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient_rviz.launch): This ```.launch``` file spawns the control panel for the robot interaction tools.
	
- [Exploration Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient_exploration.launch): This ```.launch``` file evokes the environment exploration package, which enables the robot to map an unknown portion of the surroundings, utilizing 3 smaller packages: 1. [Adaptive Monte Carlo Localization (AMCL)](http://wiki.ros.org/amcl) 2. [move_base](http://wiki.ros.org/move_base) 3. [Frontier Exploration](http://wiki.ros.org/frontier_exploration)

- [Transient Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient.launch): This ```.launch``` file calls the three previous ```.launch``` files at once, instead of running 3 seperate launch files in 3 different terminals.

### Usage:

1. We initialize the preinstalled Husky ```playpen``` environment to test of the scripts. Previously, the scripts were tested out in the ```empty_world``` environment, but we have since shifted to ```playpen```.
		
		roslaunch transient transient.launch

2. Once the <a title="Gazebo" href="http://gazebosim.org/" target="_blank">Gazebo</a> world has launched with the <a title="Husky!" href="https://www.clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/" target="_blank">Husky</a> at the center, we invoke the ```movement.py``` script, which triggers the navigation stack.
		
		python movement.py

### Known Issues:

- Currently, the repository contains basic movement <a title="Movement Code!" href="https://github.com/SarthakJShetty/Transient/blob/master/movement.py">scripts</a>. Other packages are lined up, and will ne integrated with ```rospy``` before being pushed here to the repository.

- ROS code requires ```python2.x``` to function and not ```python3.x```. Hence, take make sure that <a title="Python 2.x" href="https://github.com/SarthakJShetty/Transient#usage">these</a> commands are syntactically correct at execution.

- The [Frontier Exploration](http://wiki.ros.org/husky_navigation/Tutorials/Husky%20Frontier%20Exploration%20Demo) stack which is a part of this package is pretty buggy. At times the exploration of a given region can fail, due to a number of different reasons, which are currently being worked out.