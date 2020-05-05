#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('pab')
import sys
import rospy
import cv2
import os
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def image_saver(image,count):
  filename = 'pic'
  exten = '.jpg'
  if count%10==0:
    cv2.imwrite(filename+str(count/10)+exten,image)
  count = count + 1
  print("image has been saved")
  return count

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.count = 0
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("usb_cam/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      self.count  = image_saver(cv_image, self.count)
    except CvBridgeError as e:
      print(e)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)  

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  os.chdir("/home/sathya-prakash/catkin_ws/src/pab/images/")
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
