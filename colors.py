import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

outputs = [18, 23, 24]
GPIO.setup(outputs, GPIO.OUT)

def green():
    GPIO.output(18, True)

def yellow():
    GPIO.output(23, True)

def red():
    GPIO.output(24, True)

def color():
    input = raw_input("Turn on/of (green, yellow or red): ")
    if (input == "green"):
        green()
    elif (input == "yellow"):
        yellow()
    elif (input == "red"):
        red()
while (True):
    color()