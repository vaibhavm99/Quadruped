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

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)
trial = servo7
while True:
    i = raw_input()
    if i == 'q':
        break

#Ask user for angle and turn servo to it
angle = 70
trial.ChangeDutyCycle(2+(angle/18))
time.sleep(0.5)
trial.ChangeDutyCycle(0)

angle = 155
trial.ChangeDutyCycle(2+(angle/18))
time.sleep(0.5)
trial.ChangeDutyCycle(0)

angle = 200
trial.ChangeDutyCycle(2+(angle/18))
time.sleep(0.5)
trial.ChangeDutyCycle(0)



#Clean things up at the end
trial.stop()
GPIO.cleanup()
