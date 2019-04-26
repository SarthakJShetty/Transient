# Transient
Developing swarm intelligence models for robots inspired by transient behaviour of ant swarms.

:warning: **Code is buggy** :warning:

## Introduction:

This repository contains code & resources for thesis research project, titled **"Transiently Informed Robotic Swarms for Search & Rescue"**, being undertaken at the <a title="IISc" href="https://iisc.ac.in" target="_blank">Indian Institute of Science</a>, Bengaluru.

**Thesis Advisors:** <a title="Professor Guttal" href="https://teelabiisc.wordpress.com/curriculum-vitae/" target="_blank">Dr. Vishwesha Guttal</a> **[1]** & <a title="Professor Ghose" href="http://www.aero.iisc.ernet.in/people/debasish-ghose/" target="_blank">Dr. Debasish Ghose</a> **[2]**.

**[1]** - <a title="CES, IISc" href="http://ces.iisc.ernet.in" target="_blank">Center for Ecological Sciences</a>, Indian Institute of Science, Bengaluru.
<br>
**[2]** - <a title="Aerospace Engineering, IISc" href="http://www.aero.iisc.ernet.in" target="_blank">Department of Aerospace Engineering</a>, Indian Institute of Science, Bengaluru.

- The main purpose of this package is to design a navigation stack for swarm robots, inspired by transient behaviour as seen in ant groups. <a title="Gelblum et al" href="https://www.nature.com/articles/ncomms8729" target="_blank">**[3]**</a>

- We hypothesize, that such an architecture will bring about a reduction in the amount of energy expended by the entire swarm, all the while being directed along the right path to the destination.

## Usage:

- We initialize a ```empty_world``` to test of the scripts. As the complexity of the environment improves, we will add further levels of complications in the form of obstacles.
		
		roslaunch husky_gazebo husky_empty_world.launch

- Once the <a title="Gazebo" href="http://gazebosim.org/" target="_blank">Gazebo</a> world has launched with the <a title="Husky!" href="https://www.clearpathrobotics.com/husky-unmanned-ground-vehicle-robot/" target="_blank">Husky</a> at the center, we invoke the movement.py script, which in-turn generates the GoForward nodes etc.
		
		python movement.py

## Known Issues:

1. Currently, the repository contains basic movement <a title="Movement Code!" href="https://github.com/SarthakJShetty/Transient/blob/master/movement.py">scripts</a>. Other packages are lined up, and will ne integrated with ```rospy``` before being pushed here to the repository.

2. ROS code requires ```python2.x``` to function and not ```python3.x```. Hence, take make sure that <a title="Python 2.x" href="https://github.com/SarthakJShetty/Transient#usage">these</a> commands are syntactically correct at execution.