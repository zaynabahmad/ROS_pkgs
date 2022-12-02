#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import Int16
from nav_msgs.msg import Odometry
class computeOdometry():
    def __init__(self) :
        self.sub=rospy.Subscriber('/encoders', Float64 ,self.callback)
        self.odom_pub=rospy.Publisher('/odom',Odometry ,queue_size=10)
        self.PRE_TICKS=0.0
        self.Num_ticks=Float64()
        self.rate=rospy.Rate(10)


    def callback(self ,msg):
        self.Num_ticks=msg

    def pub_odom_data(self):
        while not rospy.is_shutdown():
            self.Cum_odom()
            self.odom_pub(self.D_c)
            self.rate.sleep()


    def Cum_odom(self):
        #l=0.05
        #r= 0.1
        #N=360
        D_l = (2*3.14*0.1*(self.Num_ticks- self.PRE_TICKS))/360
        D_r =(2*3.14*0.1*(self.Num_ticks- self.PRE_TICKS))/360

        self.D_c= ((D_l)+(D_r))/2
        


if __name__=='__main__':
    rospy.init_node('compute_odom', anonymous=True)
    rospy.loginfo("compute_odom has been initialized")
    cv=computeOdometry()
    cv.pub_odom_data