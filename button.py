import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
y=0.2
x=0.2
input_state = True
while input_state == True:
    GPIO.output(26, True)
    GPIO.output(21, False)
    time.sleep(y)
    GPIO.output(26, False)
    GPIO.output(21, True)
    time.sleep(x)
    input_state = GPIO.input(18)
GPIO.cleanup()