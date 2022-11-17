#a node to publish a random complex number


#!/usr/bin/env python3
import rospy 
import random
from turtle_move.msg import complex

def send():
   init_v=0
   sum_=0

   rospy.init_node('count_pub',anonymous=True)
   pub =rospy.Publisher('_count_',comlex,queue_size=10)
   rate=rospy.Rate(10)
   NUM=complex()
   while not rospy.is_shutdown():
    num=0.0
   rospy.loginfo(str(1*random.random())+"+"+str(1*random.random())+"i")
    
    pub.publish(NUM)
    rate.sleep()
   
if __name__=='__main__':
 try:
  send()
 except rospy.ROSInterruptException:
  pass
