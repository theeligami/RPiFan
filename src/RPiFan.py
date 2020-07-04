import RPi.GPIO as GPIO
import time
import os

FAN = 14        # Fan GPIO

FAN_MIN = 60    # Minimum value for PWM duty cycle to turn the fan on.
                # Please adjust this value if you have issues with the fan not
                # turning on on the lower duty cycle settings.

FAN_MAX = 100   # Fan maximum duty cycle
FAN_25 = FAN_MIN + (FAN_MAX - FAN_MIN) * 0.25
FAN_50 = FAN_MIN + (FAN_MAX - FAN_MIN) * 0.5
FAN_75 = FAN_MIN + (FAN_MAX - FAN_MIN) * 0.75
duty = 0        # Duty cycle

# Setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN, GPIO.OUT)

# Get CPU temperature
def get_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return float(cpu_temp.replace("temp=", "").replace("'C\n", ""))

def main():
    p = GPIO.PWM(FAN, 100)
    p.start(duty)

    while 1:
        temp = get_temp()
        if (temp < 38.0):
            p.ChangeDutyCycle(0)
        elif (temp >= 40.0 and temp < 50.0):
            p.ChangeDutyCycle(FAN_25)
        elif (temp >= 50.0 and temp < 60.0):
            p.ChangeDutyCycle(FAN_50)
        elif (temp >= 60.0 and temp < 70.0):
            p.ChangeDutyCycle(FAN_75)
        else:
            p.ChangeDutyCycle(FAN_MAX)
        time.sleep(1)

if __name__=="__main__":
    main()
