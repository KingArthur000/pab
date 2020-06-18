# PAB (Precision Agriculture Bot)
Robust four wheel drive robot for spraying organic growth enhancer on plants and for deweeding purposes.
The bot can be of great use to farmers who spend a lot of money on manual labour for deweeding and spraying of manures and fertilizers.
# AIM
The final aim of the bot is to manuever the field on its own, while simultaneously scan the land near it for plants and weeds through a camera. Then deweed the unwanted plants through a mechanical arm and spray organic growth enhancers on the crops. 
# PAB in detail
All the individual modules of the bot are run on ROS (Robotic Operating System), as the framework relies on parallelism individual modules can run on its own irrespective of their relation with other modules. This greatly helps in acheiving a decent frame rate for the camera.
There are several nodes declared in the framework for our project, some of them are arduino_node, camera_node, RCNN_node, etc.
The motors are controlled through 30-A smartelex motor drivers which are in turn controlled using PWM (Pulse Width Modulation) signals from Arduino MEGA and are programmed in embedded C.
