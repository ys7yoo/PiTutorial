# import required libraries
import RPi.GPIO as GPIO
import time

# set up the GPIO 16 for input
portNo=16
GPIO.setmode(GPIO.BCM)		# you can set up with BCM
GPIO.setup(portNo, GPIO.IN)

# read the state of the push button
for i in range(30):
    print(GPIO.input(portNo))
    time.sleep(0.2)

GPIO.cleanup()

