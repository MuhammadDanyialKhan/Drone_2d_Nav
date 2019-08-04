#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

PI = 3.1415926535897

class movement_uav1 :

    def __init__(self):
        rospy.init_node('move_robot_node', anonymous=False)

        self.pub_move = rospy.Publisher("/uav1/cmd_vel",Twist,queue_size=10)
        self.move = Twist()

    def publish_vel(self):
        self.pub_move.publish(self.move)

    def move_forward(self):        
        self.move.linear.x=10
        self.move.angular.z=0.0

    def move_backward(self):      
        self.move.linear.x=-1
        self.move.angular.z=0.0

    def stop(self):        
        self.move.linear.x=0
        self.move.angular.z=0.0  

class movement_uav2 :

    def __init__(self):
        
        self.pub_move = rospy.Publisher("/uav2/cmd_vel",Twist,queue_size=10)
        self.move = Twist()

    def publish_vel(self):
        self.pub_move.publish(self.move)

    def move_forward(self):        
        self.move.linear.x=10
        self.move.angular.z=0.0

    def move_backward(self):      
        self.move.linear.x=-1
        self.move.angular.z=0.0

    def stop(self):        
        self.move.linear.x=0
        self.move.angular.z=0.0  


if __name__ == "__main__":

    mov1 = movement_uav1()
    mov2 = movement_uav2()
    rate = rospy.Rate(1)

    while not rospy.is_shutdown() :

        movement = raw_input('Enter desired movement: ')

        if movement == 'forward':
            mov1.move_forward()
	    mov2.move_forward()

        if movement == 'backward':
            mov1.move_backward()
	    mov2.move_backward()

        if movement == 'stop':
            mov1.stop()
            mov2.stop()

        mov1.publish_vel()
        mov2.publish_vel()
        rate.sleep()
