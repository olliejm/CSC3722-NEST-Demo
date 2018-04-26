# -*- coding: utf-8 -*-

# CSC3722 Group Project - Team 11 - NEST Home Device
# A script demonstrating sending a message through voice command
# Team 11: Adele Cooper, Emma Wilson, Oliver McNally, Zhaoran Wang

import time
import grovepi
 
# Connections
led_green = 3           # Port D3
led_blue = 4            # Port D4
ultrasonic_ranger = 7   # Port D7
sound_sensor = 0        # Port A0
 
# Set LEDs to outputs
grovepi.pinMode(led_green, "OUTPUT")
grovepi.pinMode(led_blue, "OUTPUT")
 
try:
    # Set green LED to solid on to indicate resting status
    grovepi.digitalWrite(led_green,1)

    # Until a distinctively louder sound is detected, wait
    while True:
        print "Listening..."
        if grovepi.analogRead(sound_sensor) >= 300:
            break 
 
    # Set blue LED to solid on to indicate recording
    grovepi.digitalWrite(led_green,0)
    grovepi.digitalWrite(led_blue,1)

    # Wait until sound returns to ambient level
    while True:
        print "Recording..."
        time.sleep(5)
        if grovepi.analogRead(sound_sensor) <= 100:
            break

    # Flash blue LED three times to indicate message sending
    print "Sending..."
    for x in range (0, 3):
        grovepi.digitalWrite(led_blue,0)
        time.sleep(0.5)
        grovepi.digitalWrite(led_blue,1)
        time.sleep(0.5)

    # Turn off blue LED and return to green LED resting state
    grovepi.digitalWrite(led_blue,0)
    grovepi.digitalWrite(led_green,1)
 
    # Wait 10 seconds then clear hardware state and exit
    time.sleep(10)
    print "Terminating program"
    grovepi.digitalWrite(led_green,0)
 
except (IOError,TypeError):
    print sys.exc_info()
  
