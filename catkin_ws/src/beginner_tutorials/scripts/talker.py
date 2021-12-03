#!/usr/bin/python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Vector3


def pose_talker():
    pub = rospy.Publisher('/turtlesim/Pose', Vector3, queue_size=10)    # Publishing to turtlesim/Pose
    rospy.init_node('talker', anonymous=True)   # Initializing this code
    rate = rospy.Rate(10)
    position = Vector3()
    position.x = 9
    position.y = 9
    rospy.loginfo(position)
    pub.publish(position)
    rate.sleep()
        

if __name__ == '__main__':
    try: 
        pose_talker()
            
    except rospy.ROSInterruptException:
        pass
