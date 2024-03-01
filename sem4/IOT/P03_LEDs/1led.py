import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
while True:
    GPIO.output(3, True)
    print("3 enabled\n")
    time.sleep(1)
    GPIO.output(3, False)
    print("3 disabled\n")
    time.sleep(1)
    
