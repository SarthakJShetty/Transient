
# Transient

Developing a navigagation stack for swarm robots.

:warning: **Code is buggy** :warning:

### 1.0 Introduction:

This repository contains code & resources for thesis research project, titled **"Transiently Informed Robotic Swarms for Search & Rescue"**, being undertaken at the <a title="IISc" href="https://iisc.ac.in" target="_blank">Indian Institute of Science</a>, Bengaluru.

**1.1 Thesis Advisors:** <a title="Professor Guttal" href="https://teelabiisc.wordpress.com/curriculum-vitae/" target="_blank">Dr. Vishwesha Guttal</a> **[1]** & <a title="Professor Ghose" href="http://aero.iisc.ac.in/people/debasish-ghose/" target="_blank">Dr. Debasish Ghose</a> **[2]**.

**[1]** - <a title="CES, IISc" href="http://ces.iisc.ernet.in" target="_blank">Center for Ecological Sciences</a>, Indian Institute of Science, Bengaluru.
<br>
**[2]** - <a title="Aerospace Engineering, IISc" href="http://www.aero.iisc.ernet.in" target="_blank">Department of Aerospace Engineering</a>, Indian Institute of Science, Bengaluru.

- The main purpose of this package is to design a navigation stack for swarm robots, inspired by transient behaviour as seen in ant groups. <a title="Gelblum et al" href="https://www.nature.com/articles/ncomms8729" target="_blank">**[3]**</a>

- We hypothesize, that such an architecture will bring about a reduction in the amount of energy expended by the entire swarm, all the while being directed along the optimal path to the destination, in-turn set by a user.

- Currently, this repository contains ```catkin_ws```, which is the ```catkin``` workspace for the project. It contains the ```transient``` package which in-turn comprises of the [launch](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/launch) files and [scripts](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/scripts).

### 2.0 Pacakge Overview:

#### 2.1. [Scripts](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/scripts)
	
- 2.1.1 [Movement](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/movement.py): This script brings together the different parts of the navigation stack together, and acts as the central script triggered at the start of the autonomous simulations.

- 2.1.2 [Odometry](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/odometry.py): This script subscribes to the odometry data being published by the ```/odom``` topic. The coordinates are then passed over to the ```goal_checker.py``` script.
	
- 2.1.3 [Autonomous Navigation](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/autonomous_navigation.py) - This script charts a path to a given set of coordinates from the mapping data accumlated by the ```gmapping``` module. The robot then autonomously traverses this path.
	
- 2.1.4 [Goal Checker](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/goal_checker.py): This script subscribes to the ```/move_base/goal``` topic and checks if the robot has reached the coordinates specified by the user.

#### 2.2 [Launch Files](https://github.com/SarthakJShetty/Transient/tree/master/catkin_ws/src/transient/launch)

- **2.2.1** [Gazebo Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient_gazebo.launch): This ```.launch``` file triggers the Gazebo environment and the ```playpen``` configuration of the prototyping world.
	
- **2.2.2** [RViz Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient_rviz.launch): This ```.launch``` file spawns the control panel for the robot interaction tools.
	
- **2.2.3** [Exploration Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient_exploration.launch): This ```.launch``` file evokes the environment exploration package, which enables the robot to map an unknown portion of the surroundings, utilizing 3 smaller packages: 1. [Adaptive Monte Carlo Localization (AMCL)](http://wiki.ros.org/amcl) 2. [move_base](http://wiki.ros.org/move_base) 3. [Frontier Exploration](http://wiki.ros.org/frontier_exploration)

- **2.2.4** [Transient Launch](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/launch/transient.launch): This ```.launch``` file calls the three previous ```.launch``` files at once, instead of running 3 seperate launch files in 3 different terminals.

### 3.0 Usage:

**3.1** We initialize the preinstalled Husky ```playpen``` environment to test of the scripts. Previously, the scripts were tested out in the ```empty_world``` environment, but we have since shifted to ```playpen```.
		
		roslaunch transient transient.launch

**3.2** Once the <a title="Gazebo" href="http://gazebosim.org/" target="_blank">Gazebo</a> world has launched with the <a title="Husky!" href="https://www.clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/" target="_blank">Husky</a> at the center, we invoke the [```movement.py```](https://github.com/SarthakJShetty/Transient/blob/master/catkin_ws/src/transient/scripts/movement.py) script, which triggers the navigation stack.
		
		python movement.py

**3.3** To debug the package and the stack during run-time we genereate an [```RQT_GRAPH```](http://wiki.ros.org/rqt_graph) to check the transaction of topics between the individual nodes.

		rosrun rqt_graph rqt_graph

![RQT_GRAPH](https://raw.githubusercontent.com/SarthakJShetty/Transient/master/pictures/RQT_Graph.png "RQT_GRAPH")

### 4.0 Snapshots:

#### 4.1 Frontier Exploration Progression:

- **Fig 4.1.1**
Initially provided a 4-sided polygon for exploration.

![Frontier Exploration 1](https://raw.githubusercontent.com/SarthakJShetty/Transient/master/pictures/Map_1.png "Frontier Exploration 1")

- **Fig 4.1.2**
Due to delays in the map updating process, there is a mismatch between the map being generated and the pointclouds being provided by  the LiDAR.

![Frontier Exploration 2](https://raw.githubusercontent.com/SarthakJShetty/Transient/master/pictures/Map_2.png "Frontier Exploration 2")

- **Fig 4.1.3**
The initially provided 4-sided polygon area has been explored by the agent. With enough number of iterations, the map update syncs up with the pointclouds being generated.

![Frontier Exploration 3](https://raw.githubusercontent.com/SarthakJShetty/Transient/master/pictures/Map_3.png "Frontier Exploration 3")

### 5.0 Known Issues:

- **5.1** Currently, the repository contains basic movement <a title="Movement Code!" href="https://github.com/SarthakJShetty/Transient/blob/master/movement.py">scripts</a>. Other packages are lined up, and will ne integrated with ```rospy``` before being pushed here to the repository.

- **5.2** ROS code requires ```python2.x``` to function and not ```python3.x```. Hence, take make sure that <a title="Python 2.x" href="https://github.com/SarthakJShetty/Transient#usage">these</a> commands are syntactically correct at execution.

- **5.3** The [Frontier Exploration](http://wiki.ros.org/husky_navigation/Tutorials/Husky%20Frontier%20Exploration%20Demo) stack which is a part of this package is pretty buggy. At times the exploration of a given region can fail, due to a number of different reasons, which are currently being worked out.