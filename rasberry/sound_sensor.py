import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN)


setup()

while True:
    print(GPIO.INPUT(18))
    time.sleep(0.25)
