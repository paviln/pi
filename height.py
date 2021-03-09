# -----------------------------------------------------------
# The program measures the height of a person, and validates it against a user defined minimum height reqirement.
# -----------------------------------------------------------

import RPi.GPIO as GPIO
import time
from os import system, name

# Global constants.
TRIG = 26
ECHO = 19
GREENLED = 20
REDLED = 21
BUZZER = 25
BUTTON = 18

# Entry point of the programm.
def main():
    pin_setup()

    while True:
        if GPIO.input(BUTTON) == True:
            # User input minimum height.
            minHeight = input("Minimum height: ")

            # Find sensor height.
            sensorHeight = measure_distance()
            GPIO.output(GREENLED, True)
            time.sleep(4)
            
            # Calculate the actual person height.
            distance = measure_distance()
            height = SENSORHEIGHT - distance

            # Validate the height, and give the appropriate feedback.
            print "\nMinimum height: " + str(minHeight) + "cm"
            print "Person height: " + str(height) + "cm"
            if (height >= minHeight):
                GPIO.output(GREENLED, True)
                time.sleep(4)
                GPIO.output(GREENLED, False)
            else:
                GPIO.output(REDLED, True)
                GPIO.output(BUZZER, True)
                time.sleep(4)
                GPIO.output(REDLED, False)
                GPIO.output(BUZZER, False)

            clear()

# Configure the IO pins of the Raspberry Pi.
def pin_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    GPIO.setup(GREENLED, GPIO.OUT)
    GPIO.output(GREENLED, False)
    GPIO.setup(REDLED, GPIO.OUT)
    GPIO.output(REDLED, False)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.output(BUZZER, False)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Gets the distence between the sensor and the object(person).
def measure_distance():
    distance = 0
    
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time() 
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
    
    return distance

# Clears the console
def clear():
    if (name == 'nt'):
        os.system('cls')
    else:
        system('clear')

# Invokes the main method, if the programm is run directly.
if __name__ == "__main__":
    main()