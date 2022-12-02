#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *

from tf.msg import *
msg=Odometry()
def subO():
    rospy.init_node('sub_odom',anonymous=True)
    pub=rospy.Subscriber('/odom',Odometry,callback)
    rate=rospy.Rate(10)
    rospy.spin()

def callback(msg):
    print (msg.pose.pose)


if __name__=='__main__':
    try:
        subO()
    except rospy.ROSInterruptException:
        pass


