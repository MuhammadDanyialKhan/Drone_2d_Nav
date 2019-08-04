# Hector Quadrotor 2d Navigation

This project focuses on simulating a quadrotor aerial vehicle for the development of flight control systems, autonomous navigation, obstacle avoidance, and path planning. This software relies on the Robot Operating System (ROS) software. ROS provides hardware abstraction, device drivers, libraries, visualizers, message-passing, package management, and more. Along with ROS, Gazebo is used for simulation. Gazebo offers the ability to accurately and efficiently simulate populations of robots in complex indoor and outdoor environments.

This project begins with simple manual control of the quadrotor with a keyboard. It then evolves to simulating GPS waypoint navigation. Once the quadrotor can follow a series of waypoints, it is possible to develop 2D maps of the environment. These maps are used for 2D and 3D path planning and obstacle avoidance.
## Getting Started

These instructions will cover the installation of ROS, Gazebo, and several other basic packages required for this software to run.
This first section installs ROS, and a few additional dependencies and compiled packages required for the Ardupilot simulation.

## Install ROS and primary pacakges

```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key 0xB01FA116
$ sudo apt-get update
```
In case there was a missing dependency, you may try the following line. However, be careful not to attempt to desinstall-reinstall libgl1-mesa,for it sometimes messes up the ubuntu installation.
```
$ sudo apt-get -y install libgl1-mesa-dev-lts-utopic
```
Install ROS Kinetic
```
$ sudo apt-get -y install ros-kinetic-desktop-full
$ sudo rosdep init
$ rosdep update
```
Setup environment variables
```
$ sudo sh -c 'echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc'
$ source ~/.bashrc
```
Get rosinstall and some additional dependencies

```
$ sudo apt-get -y install python-rosinstall          \
                        ros-kinetic-octomap-msgs    \
                        ros-kinetic-joy             \
                        ros-kinetic-geodesy         \
                        ros-kinetic-octomap-ros     \
			            unzip
```
Install catkin tool kit

```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
$ wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
$ sudo apt-get update
$ sudo apt-get install python-catkin-tools
```

### 

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

