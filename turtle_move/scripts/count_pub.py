#!/usr/bin/env python3
import rospy 
from std_msgs.msg import Float32

def send():
   init_v=0
   sum_=0

   rospy.init_node('count_pub',anonymous=True)
   pub =rospy.Publisher('_count_',Float32,queue_size=10)
   rate=rospy.Rate(10)
   pose=Float32()
   while not rospy.is_shutdown():
    sum_=sum_+init_v
    init_v=init_v+1
    rospy.loginfo(init_v)
    
    pub.publish(pose)
    rate.sleep()
   
if __name__=='__main__':
 try:
  send()
 except rospy.ROSInterruptException:
  pass
   
   
