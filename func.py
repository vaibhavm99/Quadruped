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

# Define the values
# one = [25,105,180]
# two = [0,180]
# three = [25,105,180]
# four = [0,180]
# five = [25,105,180]
# six = [0,180]
# seven = [70,155,200]
# eight = [0,180]

serv = [servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8]
t = 0.2
def down(servo):

    if servo % 2 == 0:
        servo = servo - 1
        trial = serv[servo]
        angle = 0
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    else:
        print("This Servo can't go down")

def up(servo):

    if servo % 2 == 0:
        servo = servo - 1
        trial = serv[servo]
        angle = 150
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        # trial.ChangeDutyCycle(0)
    else:
        print("This Servo can't go up")

def up_all():
    angle = 150
    servo2.ChangeDutyCycle(2+(angle/18))
    servo4.ChangeDutyCycle(2+(angle/18))
    servo6.ChangeDutyCycle(2+(angle/18))
    servo8.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    # servo2.ChangeDutyCycle(0)
    # servo4.ChangeDutyCycle(0)
    # servo6.ChangeDutyCycle(0)
    # servo8.ChangeDutyCycle(0)

def down_all():
    angle = 0
    servo2.ChangeDutyCycle(2+(angle/18))
    servo4.ChangeDutyCycle(2+(angle/18))
    servo6.ChangeDutyCycle(2+(angle/18))
    servo8.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    servo2.ChangeDutyCycle(0)
    servo4.ChangeDutyCycle(0)
    servo6.ChangeDutyCycle(0)
    servo8.ChangeDutyCycle(0)

def up_right():
    angle = 150
    servo4.ChangeDutyCycle(2+(angle/18))
    servo6.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    # servo4.ChangeDutyCycle(0)
    # servo6.ChangeDutyCycle(0)

def down_right():
    angle = 0
    servo4.ChangeDutyCycle(2+(angle/18))
    servo6.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    servo4.ChangeDutyCycle(0)
    servo6.ChangeDutyCycle(0)

def up_left():
    angle = 150
    servo2.ChangeDutyCycle(2+(angle/18))
    servo8.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    # servo2.ChangeDutyCycle(0)
    # servo8.ChangeDutyCycle(0)

def down_left():
    angle = 0
    servo2.ChangeDutyCycle(2+(angle/18))
    servo8.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    servo2.ChangeDutyCycle(0)
    servo8.ChangeDutyCycle(0)



def up_front():
    angle = 150
    servo2.ChangeDutyCycle(2+(angle/18))
    servo4.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    # servo2.ChangeDutyCycle(0)
    # servo4.ChangeDutyCycle(0)


def down_front():
    angle = 0
    servo2.ChangeDutyCycle(2+(angle/18))
    servo4.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    servo2.ChangeDutyCycle(0)
    servo4.ChangeDutyCycle(0)



def up_rear():
    angle = 150
    servo6.ChangeDutyCycle(2+(angle/18))
    servo8.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    # servo6.ChangeDutyCycle(0)
    # servo8.ChangeDutyCycle(0)


def down_rear():
    angle = 0
    servo6.ChangeDutyCycle(2+(angle/18))
    servo8.ChangeDutyCycle(2+(angle/18))
    time.sleep(t)
    servo6.ChangeDutyCycle(0)
    servo8.ChangeDutyCycle(0)

def leg_outward(servo):

    if servo == 1:
        servo = servo - 1
        trial = serv[servo]
        angle = 100
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 3:
        servo = servo - 1
        trial = serv[servo]
        angle = 100
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 5:
        servo = servo - 1
        trial = serv[servo]
        angle = 100
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 7:
        servo = servo - 1
        trial = serv[servo]
        angle = 150
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    else:
        print("This Servo can't go foward")

def leg_mid(servo):

    if servo == 1:
        servo = servo - 1
        trial = serv[servo]
        angle = 150
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 3:
        servo = servo - 1
        trial = serv[servo]
        angle = 50
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 5:
        servo = servo - 1
        trial = serv[servo]
        angle = 140
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 7:
        servo = servo - 1
        trial = serv[servo]
        angle = 110
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    else:
        print("This Servo can't go foward")

def leg_inward(servo):

    if servo == 1:
        servo = servo - 1
        trial = serv[servo]
        angle = 180
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 3:
        servo = servo - 1
        trial = serv[servo]
        angle = 15
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 5:
            servo = servo - 1
            trial = serv[servo]
            angle = 180
            trial.ChangeDutyCycle(2+(angle/18))
            time.sleep(t)
            trial.ChangeDutyCycle(0)
    elif servo == 7:
            servo = servo - 1
            trial = serv[servo]
            angle = 50
            trial.ChangeDutyCycle(2+(angle/18))
            time.sleep(t)
            trial.ChangeDutyCycle(0)
    else:
        print("This Servo can't go foward")

def left_forward():
    angle1 = 180
    angle2 = 150
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo7.ChangeDutyCycle(2+(angle2/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)

def left_backward():
    angle1 = 100
    angle2 = 20
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo7.ChangeDutyCycle(2+(angle2/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)

def right_forward():
    angle1 = 15
    angle2 = 100
    servo3.ChangeDutyCycle(2+(angle1/18))
    servo5.ChangeDutyCycle(2+(angle2/18))
    time.sleep(t)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)


def right_backward():
    angle1 = 100
    angle2 = 180
    servo3.ChangeDutyCycle(2+(angle1/18))
    servo5.ChangeDutyCycle(2+(angle2/18))
    time.sleep(t)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)

def whole_forward():
    angle1 = 15
    angle2 = 100
    angle3 = 180
    angle4 = 150
    servo3.ChangeDutyCycle(2+(angle1/18))
    servo5.ChangeDutyCycle(2+(angle2/18))
    servo1.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo1.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)


def whole_forward():
    angle1 = 15
    angle2 = 100
    angle3 = 180
    angle4 = 150
    servo3.ChangeDutyCycle(2+(angle1/18))
    servo5.ChangeDutyCycle(2+(angle2/18))
    servo1.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo1.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)

def whole_backward():
    angle1 = 100
    angle2 = 180
    angle3 = 100
    angle4 = 50
    servo3.ChangeDutyCycle(2+(angle1/18))
    servo5.ChangeDutyCycle(2+(angle2/18))
    servo1.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo1.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)

def whole_mid():
    angle1 = 150
    angle2 = 50
    angle3 = 140
    angle4 = 110
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo3.ChangeDutyCycle(2+(angle2/18))
    servo5.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)


def left_mid():
    angle1 = 150
    angle4 = 100
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)

def right_mid():
    angle2 = 50
    angle3 = 145
    servo3.ChangeDutyCycle(2+(angle2/18))
    servo5.ChangeDutyCycle(2+(angle3/18))
    time.sleep(t)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)

def whole_outward():
    angle1 = 100
    angle2 = 100
    angle3 = 100
    angle4 = 150
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo3.ChangeDutyCycle(2+(angle2/18))
    servo5.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)



def whole_inward():
    angle1 = 180
    angle2 = 15
    angle3 = 180
    angle4 = 50
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo3.ChangeDutyCycle(2+(angle2/18))
    servo5.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)
def step():
    angle1 = 150
    angle2 = 50
    angle3 = 100
    angle4 = 150
    servo1.ChangeDutyCycle(2+(angle1/18))
    servo3.ChangeDutyCycle(2+(angle2/18))
    servo5.ChangeDutyCycle(2+(angle3/18))
    servo7.ChangeDutyCycle(2+(angle4/18))
    time.sleep(t)
    servo1.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    servo5.ChangeDutyCycle(0)
    servo7.ChangeDutyCycle(0)





# while True:
#     i = raw_input()
#     if i == 'q':
#         break
# up(2)
# up(4)
# up(6)
# up(8)
# down(2)
# down(4)
# down(6)
# down(8)
# up_all()
# down_all()
# up_left()
# down_left()
# up_right()
# down_right()
# up_front()
# down_front()
# up_rear()
# down_rear()
# leg_outward(1)
# leg_mid(1)
# leg_inward(1)
# leg_outward(3)
# leg_mid(3)
# leg_inward(3)
# leg_outward(5)
# leg_mid(5)
# leg_inward(5)
# leg_outward(7)
# leg_mid(7)
# leg_inward(7)
# left_forward()
# left_backward()
# right_forward()
# right_backward()
# whole_forward()
# whole_backward()
# left_mid()
# right_mid()
# whole_mid()
# whole_outward()
# whole_inward()



# while True:
#     i = raw_input()
#     if i == 'q':
#         break

#Clean things up at the end
servo1.stop(0)
servo2.stop(0)
servo3.stop(0)
servo4.stop(0)
servo5.stop(0)
servo6.stop(0)
servo7.stop(0)
servo8.stop(0)

GPIO.cleanup()
