import board
import busio
import adafruit_am2320
import time
import json
from json import JSONEncoder
from datetime import datetime
import enum
import RPi.GPIO as GPIO

# Global constants.
WAITINGLED = 16
LOGGINGLED = 20
STOPPEDLED = 21

# Global Variables
log = None

# Entry point of the programm.
def main():
    pin_setup()
    ShowStatus(Status.Waiting)
    start_time = input("Start time (dd:hh:mm): ")
    log_interval = int(input("Log interval (mm): "))
    stop_time = input("Stop time (number or dd:hh:mm): ")
    global log
    log = Log(start_time, log_interval, stop_time, [])
    Logger()

# Configure the IO pins of the Raspberry Pi.
def pin_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(WAITINGLED, GPIO.OUT)
    GPIO.output(WAITINGLED, False)
    GPIO.setup(LOGGINGLED, GPIO.OUT)
    GPIO.output(LOGGINGLED, False)
    GPIO.setup(STOPPEDLED, GPIO.OUT)
    GPIO.output(STOPPEDLED, False)

# Handle input data.
def Logger():
    if(log.stop_time.isdigit()):
        StartMessurement(int(log.stop_time))
    else:
        # Calculate messurement repetitions from datatime difference/interval.
        time_now = datetime.now()
        start_time = datetime.strptime(log.start_time, "%d:%H:%M")
        start_time = start_time.replace(year=time_now.year, month=time_now.month)
        time_end = datetime.strptime(log.stop_time, "%d:%H:%M")
        time_end = time_end.replace(year=time_now.year, month=time_now.month)
        if(time_end > start_time):
            repetitions = (time_end - start_time).total_seconds() / 60
            StartMessurement(repetitions)

# Writes messurements to file, based on the log information.
def StartMessurement(number):

    # Stop programm execution until start time
    time_now = datetime.now()
    start_time = datetime.strptime(log.start_time, "%d:%H:%M")
    start_time = start_time.replace(year=time_now.year, month=time_now.month)
    sleep_time = (start_time - time_now).total_seconds()
    time.sleep(sleep_time)
    ShowStatus(Status.Logging)

    # Write messurements
    file_name = datetime.now().strftime("%m.%d.%Y, %H:%M:%S") + ".txt"
    current_messurement = 0
    while(current_messurement <= number):
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_am2320.AM2320(i2c)
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        measurement = Measurement(date_time, sensor.temperature, sensor.relative_humidity)
        log.measurements.append(measurement)

        with open(file_name, 'w+') as outfile:
            json.dump(log, outfile, indent=4, cls=LogEncoder)

        current_messurement = current_messurement + 1
        time.sleep(log.log_interval * 60)
    
    ShowStatus(Status.Stopped)

# Turn on led to show status.
def ShowStatus(status):
    GPIO.output(WAITINGLED, False)
    GPIO.output(LOGGINGLED, False)
    GPIO.output(STOPPEDLED, False)

    if(status == Status.Waiting):
        GPIO.output(WAITINGLED, True)
    elif(status == Status.Logging):
        GPIO.output(LOGGINGLED, True)
    elif(status == Status.Stopped):
        GPIO.output(STOPPEDLED, True)

class Log:
    def __init__(self, start_time, log_interval, stop_time, measurements):
        self.start_time = start_time
        self.log_interval = log_interval
        self.stop_time = stop_time
        self.measurements = measurements

# Log JSONEncoder.
class LogEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class Measurement:
    def __init__(self, datetime, temperature, humidity):
        self.datetime = datetime
        self.temperature = temperature
        self.humidity = humidity

class Status(enum.Enum):
   Waiting = 1
   Logging = 2
   Stopped = 3

# Invokes the main method, if the programm is run directly.
if __name__ == "__main__":
    main()