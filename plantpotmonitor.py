#!/usr/bin/python

# import modules
import RPi.GPIO as GPIO
from time import sleep
import mcp3008

# set up variables
red1 = 17
green1 = 22
yellow1 = 23
red2 = 24
green2 = 14
yellow2 = 15

# set up GPIO
print "Setting up GPIO"

GPIO.setmode(GPIO.BCM)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(yellow1, GPIO.OUT)
GPIO.setup(green1, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(yellow2, GPIO.OUT)
GPIO.setup(green2, GPIO.OUT)


# define led function
#def enable_led(should_enable):
#	if should_enable:
#		GPIO.output(led_pin, True)
#	else:
#		GPIO.output(led_pin, False)


while True:

    # read moisture sensors
    m1 = mcp3008.readadc(1)
    m2 = mcp3008.readadc(5)
    print "Moisture level 1: {:>5} ".format(m1)
    print "Moisture level 2: {:>5} ".format(m2)
    sleep(.5)

    #clear leds
    GPIO.output(red1, False)
    GPIO.output(green1, False)
    GPIO.output(yellow1, False)
    GPIO.output(red2, False)
    GPIO.output(green2, False)
    GPIO.output(yellow2, False)

    # set led for sensor 1

    if (m1 > 600):
        print "Plant 1 overwatered!"
        GPIO.output(red1, True)
        GPIO.output(green1, True)
    elif (m1 < 600) and (m1 > 300):
        print "Plant 1 okay"
        GPIO.output(green1, True)
    elif (m1 < 300) and (m1 >100):
        print "Plant 1 needs watering"
        GPIO.output(yellow1, True)
    else:
        print "Danger Will Robinson!"
        GPIO.output(red1, True)

    # set led for sensor 2

    if (m2 > 600):
        print "Plant 2 overwatered!"
        GPIO.output(red2, True)
        GPIO.output(green2, True)
    elif (m2 < 600) and (m2 > 300):
        print "Plant 2 okay"
        GPIO.output(green2, True)
    elif (m2 < 300) and (m2 >100):
        print "Plant 2 needs watering"
        GPIO.output(yellow2, True)
    else:
        print "Danger Will Robinson!"
        GPIO.output(red2, True)

    sleep(10)

 
