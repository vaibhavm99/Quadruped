# Quadruped
This project is for 8 DOF Spiderbot(Quadruped) robot.
The bot recognises the palm using OpenCV and moves with its movement. Fist is used to make it sit and stand.


# Files
Hand_Gesture_Remote.py is for Laptop to detect hand gestures and simulate keyboard command presses.\
Rest all files are for controlling the Raspberry Pi.\
The Raspberyy Pi and Laptop should be connected to each other.\
The main_ssh.py file is to be run, this file accepts input such was 'w', 'a', 's', 'd', etc from the Laptop Keyboard and the Bot in the required direction.\
