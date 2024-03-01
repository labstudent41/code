import RPi.GPIO as GPIO
import time

pins = [3, 8, 12]
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pins, GPIO.OUT)

try:
    while True:
        for pin in pins:
            print()
            GPIO.output(pin, GPIO.HIGH)
            print(pin, "ON")
            time.sleep(1)
            GPIO.output(pin, GPIO.LOW)
            print(pin, "OFF")
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()