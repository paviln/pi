import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

sleep = input("Sleep time? ")
flash = input("Flash time: ")

while (True):
    GPIO.output(18,True)
    time.sleep(flash)
    GPIO.output(18,False)
    time.sleep(sleep)
