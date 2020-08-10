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

def angle(servo, angle):

    if servo == 1:
        servo = servo - 1
        trial = serv[servo]
        angle = angle
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 3:
        servo = servo - 1
        trial = serv[servo]
        angle = angle
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 5:
        servo = servo - 1
        trial = serv[servo]
        angle = angle
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    elif servo == 7:
        servo = servo - 1
        trial = serv[servo]
        angle = angle
        trial.ChangeDutyCycle(2+(angle/18))
        time.sleep(t)
        trial.ChangeDutyCycle(0)
    else:
        print("This Servo can't go foward")


while True:
    i = int(input())
    angle(7, i)

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
