# Quadruped
This project is for 8 DOF Spiderbot(Quadruped) robot.
The bot recognises the palm using OpenCV and moves with its movement. Fist is used to make it sit and stand.


# Files
Hand_Gesture_Remote.py is for Laptop to detect hand gestures and simulate keyboard command presses.\
The files named 'yolov3-tiny-obj.cfg' and 'yolov3-tiny-obj_7000.weights' are the configuration and weights files for the Yolo model respectively, they are to be saved in the same folder as the Hand_Gesture_Remote.py file.\
Rest all files are for controlling the Raspberry Pi.\
The Raspberyy Pi and Laptop should be connected to each other.\
The main_ssh.py file is to be run, this file accepts input such was 'w', 'a', 's', 'd', etc from the Laptop Keyboard and the Bot in the required direction.

# Hand Gesture
Hand Gestures are detected by training a Tiny Yolo v3 Algorithm. This Detectes the palm and fist. Then the position of their mid point on frame image is used to find out where to move the Bot.
