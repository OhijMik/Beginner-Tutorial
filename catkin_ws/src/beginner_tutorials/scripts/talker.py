#!/usr/bin/python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/turtle1/command_velocity', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = self.__slots__ = '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass