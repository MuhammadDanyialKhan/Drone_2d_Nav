#!/usr/bin/env python
import getch
import roslib; roslib.load_manifest('p3dx_mover')
import sys
import rospy
import math


from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

#########Publisher

pub_r1 = rospy.Publisher('/r1/cmd_vel', Twist)
pub_r2 = rospy.Publisher('/r2/cmd_vel', Twist)
rospy.init_node('p3dx_mover')
twist_r1 = Twist()
twist_r2 = Twist()

########Variables
i=0
rate = rospy.Rate(rospy.get_param('~hz', 10))

s_min = 0.3                         #minimum space between slave & master
s_max = 2                           #maximum space between slave & master
v_max = 0.4                         #maximum velocity of slave
alpha = v_max / (s_max - s_min)     #slope of the velocity function
b = alpha*s_max - v_max             #intercept of the velocity function

#########Subscriber

def callback(msg):
    rospy.loginfo("Sonar 4 detects something at %s m" % round(msg.range,3))
    if msg.range < 0.22:
        rospy.loginfo("Obstacle too close ! Not normal, vehicule stopped (You might want to revise the code)")
        twistr_r1.linear.x = 0
        pub_r1.publish(twist)
        rospy.signal_shutdown("Simulation end")

    beta = alpha*msg.range - b
    gamma = min(beta,v_max)
    twist_r1.linear.x = max(0, gamma)

sub = rospy.Subscriber("/r1/sonar4/scan", Range, callback)

#########Loop

while not rospy.is_shutdown() :

    twist_r2.linear.x = (math.cos(i) +2)/8
    i+=0.1
    rospy.loginfo("r1 velocity is "+ str(round(twist_r1.linear.x,3))+ " m/s" )
    rospy.loginfo("r2 velocity is "+ str(round(twist_r2.linear.x,3))+ " m/s" )
    pub_r1.publish(twist_r1)
    pub_r2.publish(twist_r2)
    rate.sleep()
