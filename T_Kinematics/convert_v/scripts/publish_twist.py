#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
vel=Twist()
def pub_vel ():
    rospy.init_node('pub_twist',anonymous=True)
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    vel.linear.x=0.2
    vel.angular.z=0.2
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(vel)

        #rospy.loginfo('vel:'%vel.linear.x)
        rate.sleep()



        
if __name__=='__main__':
    try:
        pub_vel()
    except rospy.ROSInterruptException:
        pass