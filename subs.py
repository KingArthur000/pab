#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import pygame
#import os


def talker():
    pubx = rospy.Publisher('left', Int32, queue_size=10)
    puby = rospy.Publisher('right',Int32,queue_size=10)
    global pub
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('joystick', anonymous=True)
    rate = rospy.Rate(30) # 10hz
    while not rospy.is_shutdown():
    	pygame.init()
    	done = False
	
    	pygame.joystick.init()
    	
    	while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done=True 

            joystick_count = pygame.joystick.get_count()


            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                name = joystick.get_name()
                buttons = joystick.get_numbuttons()
		button= []
		for i in range(8):
			button.append(joystick.get_button(i))
		print ("buttons")
		print (button)
		a=int(joystick.get_button(0))#back
    		b=int(joystick.get_button(1))#right
    		c=int(joystick.get_button(2))#forward
    		d=int(joystick.get_button(3))#left
    		e=int(joystick.get_button(4))#actuator
    		f=int(joystick.get_button(5))#stop
		g=int(joystick.get_button(6))#kill
		h=int(joystick.get_button(7))#kill
    		hello_str = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
    		pub.publish(hello_str)
    		rospy.loginfo(hello_str)
		
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
