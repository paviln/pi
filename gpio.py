import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    com = raw_input("Input command: ")
    if com == "ON":
        GPIO.output(18, True)
    elif com == "OFF":
        GPIO.output(18, False)
    elif com == "EXIT":
        break
