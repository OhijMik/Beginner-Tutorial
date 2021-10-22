#!/usr/bin/python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


wantedPosX = 3.0    # The coordinates of where you want the turtle to be at
wantedPosY = 3.0

currentPosX = 5.54
currentPosY = 5.54


def cmd_vel_talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cmd_vel = Twist()
        cmd_vel.linear.x = posX
        cmd_vel.linear.y = posY
        cmd_vel.angular.z = 0.0
        rospy.loginfo(cmd_vel)
        pub.publish(cmd_vel)
        rate.sleep()
        break


def pose_talker():
    pub = rospy.Publisher('/turtlesim/Pose', Vector3, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz    
    while not rospy.is_shutdown():
        position = Vector3()
        position.x = currentPosX
        position.y = currentPosY
        position.z = 0.0
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
        break


if __name__ == '__main__':
    try:
        
        posX = wantedPosX - currentPosX    
        posY = wantedPosY - currentPosY
        cmd_vel_talker()
        pose_talker()
        currentPosX = currentPosX + posX
        currentPosY = currentPosY + posY
        cmd_vel_talker()
        pose_talker()

    except rospy.ROSInterruptException:
        pass

