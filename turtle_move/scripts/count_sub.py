#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
def recieve():
   rospy.init_node('count_sub',anonymous=True)
   sub=rospy.Subscriber('_count_',Float32,callback)
   rospy.spin()
   
   
def callback(data):
 rospy.loginfo('the sum_ :', data.data)
 
if __name__=='__main__':
 recieve()
