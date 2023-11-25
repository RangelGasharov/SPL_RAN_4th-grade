import RPi.GPIO as GPIO
import time

PORT_SENSOR = 17
PORT_MOTOR = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT_SENSOR, GPIO.IN)
GPIO.setup(PORT_MOTOR, GPIO.OUT)

a = 0

while 1:
    if GPIO.input(PORT_SENSOR) == GPIO.LOW:
        if a == 0:
            GPIO.output(PORT_MOTOR, GPIO.LOW)
            time.sleep(0.05)
            print("aus")
            a = 1
        else:
            GPIO.output(PORT_MOTOR, GPIO.HIGH)
            time.sleep(0.05)
            print("ein")
            a = 0
