from func import *
import time
import keyboard
import readchar
# Define pins
one = 29
two = 31
three = 33
four = 35
five = 37
six = 36
seven = 38
eight = 40
# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(one, GPIO.OUT)
GPIO.setup(two, GPIO.OUT)
GPIO.setup(three, GPIO.OUT)
GPIO.setup(four, GPIO.OUT)
GPIO.setup(five, GPIO.OUT)
GPIO.setup(six, GPIO.OUT)
GPIO.setup(seven, GPIO.OUT)

GPIO.setup(eight, GPIO.OUT)

servo1 = GPIO.PWM(one, 50)
servo2 = GPIO.PWM(two, 50)
servo3 = GPIO.PWM(three, 50)
servo4 = GPIO.PWM(four, 50)
servo5 = GPIO.PWM(five, 50)
servo6 = GPIO.PWM(six, 50)
servo7 = GPIO.PWM(seven, 50)
servo8 = GPIO.PWM(eight, 50)

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)
servo5.start(0)
servo6.start(0)
servo7.start(0)
servo8.start(0)


serv = [servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8]
t = 0.4

def home():
    up_all()
    time.sleep(1)
    down(2)
    leg_outward(1)
    up(2)
    down(4)
    leg_outward(3)
    up(4)
    down(6)
    leg_outward(5)
    up(6)
    down(8)
    leg_outward(7)
    up(8)
    up_all()





def left():
    # Left Side
    left_forward()
    # down(8)
    # # time.sleep(1)
    leg_inward(7)
    # up(8)
    #
    down(2)
    leg_mid(1)
    up(2)
    #
    #
    # down(8)
    leg_mid(7)
    # up(8)




def right():
    # Right Side
    right_forward()
    # down(6)
    leg_inward(5)
    # up(6)

    down(4)
    leg_mid(3)
    up(4)


    # down(6)
    leg_mid(5)
    # up(6)


def backward():
    # Right Side
    right_backward()

    down(4)
    leg_mid(3)
    up(4)

    leg_mid(5)

    # Left Side
    left_backward()

    down(2)
    leg_mid(1)
    up(2)

    leg_mid(7)



def forward():
    right()
    left()


up_all()
time.sleep(1)
while True:
    key = readchar.readkey()
    if key == 'w':
        print('forward')
        forward()
    elif key == 's':
        print('backward')
        backward()
    elif key == 'q':
        print('Shut down')
        down_all()
        break
    elif key == 'd':
        print('left')
        left()
    elif key == 'a':
        print('right')
        right()
    else:
        up_all()


servo1.stop(0)
servo2.stop(0)
servo3.stop(0)
servo4.stop(0)
servo5.stop(0)
servo6.stop(0)
servo7.stop(0)
servo8.stop(0)

GPIO.cleanup()
