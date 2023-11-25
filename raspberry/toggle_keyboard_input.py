import RPi.GPIO as GPIO

PIN_MOTOR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_MOTOR, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    input_keyboard = input()
    if input_keyboard == "e":
        GPIO.output(PIN_MOTOR, False)
        print("Ein")
    if input_keyboard == "a":
        GPIO.output(PIN_MOTOR, True)
        print("Aus")
