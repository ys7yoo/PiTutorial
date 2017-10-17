# import required libraries 
import RPi.GPIO as GPIO
import time

# set up the GPIO 18 for output
portNo = 12 # GPIO 18 is on physical port 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(portNo, GPIO.OUT)

# blink the LED
for i in range(3):
    GPIO.output(portNo,True)
    time.sleep(1)
    GPIO.output(portNo,False)
    time.sleep(1)

# clean up GPIO settings
GPIO.cleanup()
