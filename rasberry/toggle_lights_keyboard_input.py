import RPi.GPIO as GPIO

PIN_RED = 17
PIN_YELLOW = 18
PIN_GREEN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    input_keyboard = input()
    if input_keyboard == "e":
        GPIO.output(PIN_RED, True)
        GPIO.output(PIN_YELLOW, True)
        GPIO.output(PIN_GREEN, True)
    if input_keyboard == "a":
        GPIO.output(PIN_RED, False)
        GPIO.output(PIN_YELLOW, False)
        GPIO.output(PIN_GREEN, False)
