import RPI.GPIO as GPIO
import time
import os

FAN = 14    # Fan GPIO
duty = 0    # Duty cycle

# Setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN, GPIO.OUT)

# Get CPU temperature
def get_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "").replace("'C\n", "")

def main():
    p = GPIO.PWM(FAN, 100)
    p.start(duty)

    while 1:
        temp = get_temp()
        if (temp < 38.0):
            p.ChangeDutyCycle(0)
        elif (temp >= 40.0 and temp < 50.0):
            p.ChangeDutyCycle(25)
        elif (temp >= 50.0 and temp < 60.0):
            p.ChangeDutyCycle(50)
        elif (temp >= 60.0 and temp < 70.0):
            p.ChangeDutyCycle(75)
        else:
            p.ChangeDutyCycle(100)
        time.sleep(1)
