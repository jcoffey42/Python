#!/usr/bin/python
######################################################
## Create  a pulsing spiral lighting each led       ##
## Version 1 using a method I saw in another script ##
##                                                  ##
######################################################

# Import needed modules
import time
from piglow import PiGlow

# An alias, so you can type piglow rather than PiGlow()
piglow = PiGlow()

q = 0.0003   # Delay for time.sleep in seconds
x = 1        # Iniialize x, 0 causes .led to turn them off
             # Used to define led and brightness
       
y = 1        # Initialize y for main loop

piglow.all(0) # turn off all led, 

while y > 0:              # Begin the pulse loop
    
    for x in range(255):  # Start the brighten loop     

        m = (x % 19)      # Make sure to only have 1-18 for led
                          # by dividing by 19 and using the remainder

        if m == 0:        # LED can't be zero so if it is, set to 1
           m= m + 1

        n = (x % 255)     # Make sure the brightness value does not exceed 255
                          # by dividing by 255 and using the remainder
        
        piglow.led(m,n)   # Set the led m=led, n=brightness 

        time.sleep(q)     # Delay the loop by q

        x = x + 1         # Add one to x and loop

    while x > 0:          # Start the dimming loop

        m = (x % 19)
        
        if m == 0:      # LED can't be zero so if it is set to 1
           m= m + 1

        n = (x % 255)   # Make sure the brightness value does not exceed 255
        
        
        time.sleep(q)      # Delay the loop by q

        piglow.led(m,n)    # Set the led m=led, n=brightness 

        x = x - 1          # Decrease x by 1

