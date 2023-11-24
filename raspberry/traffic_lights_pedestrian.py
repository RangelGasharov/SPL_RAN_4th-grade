import RPi.GPIO as GPIO

PIN_RED = 17
PIN_GREEN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    input()
    if GPIO.input(PIN_RED) == 0:
        GPIO.output(PIN_RED, True)
        GPIO.output(PIN_GREEN, False)
    else:
        GPIO.output(PIN_RED, False)
        GPIO.output(PIN_GREEN, True)
