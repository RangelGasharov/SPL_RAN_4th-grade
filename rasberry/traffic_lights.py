import RPi.GPIO as GPIO
import time
import signal
import sys

PIN_RED = 17
PIN_YELLOW = 18
PIN_GREEN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)


def allLightsOff(signal, frame):
    GPIO.output(PIN_RED, False)
    GPIO.output(PIN_YELLOW, False)
    GPIO.output(PIN_GREEN, False)
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, allLightsOff)

while True:
    GPIO.output(PIN_RED, True)
    time.sleep(3)

    GPIO.output(PIN_YELLOW, True)
    time.sleep(1)

    GPIO.output(PIN_RED, False)
    GPIO.output(PIN_YELLOW, False)
    GPIO.output(PIN_GREEN, True)
    time.sleep(3)
    for i in range(0, 3):
        GPIO.output(PIN_GREEN, False)
        time.sleep(0.5)
        GPIO.output(PIN_GREEN, True)
        time.sleep(0.5)

    GPIO.output(PIN_GREEN, False)
    GPIO.output(PIN_RED, True)
    time.sleep(2)

    GPIO.output(PIN_YELLOW, False)
