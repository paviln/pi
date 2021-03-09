import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

outputs = [4, 18, 22, 23, 24, 27]
GPIO.setup(outputs, GPIO.OUT)

sleep = 1

while True:
    GPIO.output(18, True)
    time.sleep(sleep)
    GPIO.output(18, False)
    GPIO.output(23, True)
    time.sleep(sleep)
    GPIO.output(23, False)
    GPIO.output(24, True)
    GPIO.output(22, False)
    GPIO.output(4, True)
    time.sleep(sleep)
    GPIO.output(4, False)
    GPIO.output(27, True)
    time.sleep(sleep)
    GPIO.output(27, False)
    GPIO.output(22, True)
    GPIO.output(24, False)

