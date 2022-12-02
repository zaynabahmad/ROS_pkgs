#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
class ConvertVelocites():
    def __init__(self) :
        self.sub=rospy.Subscriber('/cmd_vel', Twist ,self.callback)
        self.right_wheel_pub=rospy.Publisher('/right_wheel_controller/command',Float64 ,queue_size=10)
        self.left_wheel_pub=rospy.Publisher('/left_wheel_controller/command',Float64 ,queue_size=10)
        self.twist_vels=Twist()
        self.rate=rospy.Rate(10)


    def callback(self ,msg):
        self.twist_vels=msg

    def pub_wheel_vels(self):
        while not rospy.is_shutdown():
            self.convert_velocities()
            self.right_wheel_pub(self.vr)
            self.left_wheel_pub(self.vl)
            self.rate.sleep()


    def convert_velocities(self):
        # l=0.05
        #r= 0.1
        self.vr =((2*self.twist_vels.linear.x)+(self.twist_vels.angular.z*0.05))/(2*0.1)
        self.vl =((2*self.twist_vels.linear.x)-(self.twist_vels.angular.z*0.05))/(2*0.1)


if __name__=='__main__':
    rospy.init_node('convert_vels', anonymous=True)
    rospy.loginfo('convert_vel_node has been initialized')
    cv=ConvertVelocites()
    cv.pub_wheel_vels


       
