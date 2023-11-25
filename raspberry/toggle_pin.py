import RPi.GPIO as GPIO
import time

PIN_MOTOR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_MOTOR, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    GPIO.output(PIN_MOTOR, True)
    print(GPIO.input(PIN_MOTOR))
    time.sleep(2)
    GPIO.output(PIN_MOTOR, False)
    print(GPIO.input(PIN_MOTOR))
    time.sleep(2)
