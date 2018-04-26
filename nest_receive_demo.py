# -*- coding: utf-8 -*-

# CSC3722 Group Project - Team 11 - NEST Home Device
# A script demonstrating receipt and clearing of a message via gesture
# Team 11: Adele Cooper, Emma Wilson, Oliver McNally, Zhaoran Wang

import time
 
from grovepi import *
from grove_rgb_lcd import *
 
# Connections
led_green = 3           # Port D3
led_blue = 4            # Port D4
ultrasonic_ranger = 7   # Port D7
 
# Set LEDs to outputs
pinMode(led_green, "OUTPUT")
pinMode(led_blue, "OUTPUT")
 
try:
    # Set display colours and initial text
    setRGB(0,128,64)
    setRGB(0,255,0)
    setText("(Ollie):  can I borrow some milk")
 
    # Until an object is within 10cm of ultrasonic ranger
    while ultrasonicRead(ultrasonic_ranger) >= 10:
        # Flash the blue LED once per second
        print "Notification showing"
        digitalWrite(led_blue,1)
        time.sleep(0.5)
        digitalWrite(led_blue,0)
        time.sleep(0.5)      
 
    # Change LCD text, turn off blue LED, set green LED to solid on
    print "Notification cleared"
    digitalWrite(led_blue,0)
    digitalWrite(led_green,1)
    setText("Message cleared")
 
    # Wait 10 seconds then clear hardware state and exit
    time.sleep(10)
    print "Terminating program"
    digitalWrite(led_green,0)
    setRGB(0,0,0)
    setText("")
 
except (IOError,TypeError):
    print sys.exc_info()
