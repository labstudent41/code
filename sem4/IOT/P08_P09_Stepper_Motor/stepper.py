import RPi.GPIO as GPIO
from time import sleep

pins = (29, 31, 33, 35)
GPIO.setwarnings(False)  # turn off warnings
GPIO.setmode(GPIO.BOARD)  # use board pins
GPIO.setup(pins, GPIO.OUT)  # setup pins for output

# 360 degrees = 512 steps = 2048 micro steps
# 1 step = 4 micro step

def rotate_clockwise(steps):
    for _ in range(steps):
        # take a step or 4 micro steps forward
        GPIO.output(pins, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW))
        sleep(0.002)
        GPIO.output(pins, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
        sleep(0.002)
        GPIO.output(pins, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        sleep(0.002)
        GPIO.output(pins, (GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(0.002)

def rotate_counter_clockwise(steps):
    for _ in range(steps):
        # take a step backward
        GPIO.output(pins, (GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH))
        sleep(0.002)
        GPIO.output(pins, (GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW))
        sleep(0.002)
        GPIO.output(pins, (GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW))
        sleep(0.002)
        GPIO.output(pins, (GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW))
        sleep(0.002)

# Main
while True:
    rotate_clockwise(256)  # rotate 180 degrees clockwise
    rotate_counter_clockwise(256)  # 180 degrees counter clockwise
