#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def pose_listener():
    while not rospy.is_shutdown():  # While loop while rospy is not shutdown
        rospy.init_node('listener', anonymous=True) # Initializing the listener code
        rospy.Subscriber("/turtle1/pose", Pose, turtle_callback)    # Making a subscriber that subscribes to turtle1/pose
        rospy.Subscriber("/turtlesim/Pose", Vector3, callback)  # Making a subscriber that subscribes to turtlesim/Pose
        global pub
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)     # Publishing to turtle1/cmd_vel
        rospy.spin()    # Keeps the code from exiting until this node is stopped

def turtle_callback(data):  # Recieving the data of where the turtle is and making the variable global
    pose = data
    global currentPosX  # Making the variable global
    global currentPosY
    currentPosX = pose.x
    currentPosY = pose.y

def callback(position): # Showing where I want the turtle to be at and running cmd_listener
    rate = rospy.Rate(5)    # The rate the loop goes at
    rospy.loginfo(position) # Showing the position
    errorX = position.x - currentPosX    # The calculation
    errorY = position.y - currentPosY
    cmd_vel = Twist()           # Declaring the variable is a Twist message type
    cmd_vel.linear.x = errorX   # Moving the turtle
    cmd_vel.linear.y = errorY
    pub.publish(cmd_vel)    # Publishing the velocity to turtle1/cmd_vel using Twist
    rate.sleep()
        
        
if __name__ == '__main__':
    pose_listener()