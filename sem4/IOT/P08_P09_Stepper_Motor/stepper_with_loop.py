import RPi.GPIO as GPIO
from time import sleep

pins = (29, 31, 33, 35)
GPIO.setwarnings(False)  # turn off warnings
GPIO.setmode(GPIO.BOARD)  # use board pins
GPIO.setup(pins, GPIO.OUT)  # setup pins for output

def stepMotor(stepId): # take a micro step
    for i in range(4):
        if i == stepId:
            GPIO.output(pins[i], GPIO.HIGH)
        else:
            GPIO.output(pins[i], GPIO.LOW)

while True:

    # 360 degrees = 512 steps = 2048 micro steps
    # 1 step = 4 micro step

    for _ in range(256): # rotate 180 degrees clockwise
        for i in range(4): # take full step or 4 micro step forward
            stepMotor(i)
            sleep(0.002)

    for _ in range(256):  # 180 degrees counter clockwise
        for i in range(3, -1, -1):  # take full step backward
            stepMotor(i)
            sleep(0.002)
