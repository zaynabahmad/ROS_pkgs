#!/usr/bin/env python3
import rospy 
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('move_turtle',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(10)
    
    vel=Twist()
    while not rospy.is_shutdown():
       
       vel.linear.x=0.5
       vel.angular.z=0.2
        
       pub.publish(vel)
       rospy.loginfo("publish the turtle with linear_vel=%f: angualr_vel=%f" ,vel.linear.x ,vel.angular.z)
       rate.sleep()



if __name__=='__main__':
  try:
    move()
  except rospy.ROSInterruptException:
    pass
       

