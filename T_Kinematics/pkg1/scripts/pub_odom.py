#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from tf.msg import *
odom_data=Odometry()
def pub_move (getpose_):
    rospy.init_node('pub_odom',anonymous=True)
    pub=rospy.Publisher('/odom',Odometry,queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        odom_data.pose=getpose_
        pub.publish(odom_data)
        rospy.loginfo('pose:%f'%odom_data.pose)
        rate.sleep()



        
if __name__=='__main__':
    try:
        pub_move(float(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass


