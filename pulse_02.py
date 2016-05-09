#!/usr/bin/python
######################################################
## create  a pulsing spiral lighing each led        ##
## an alternate method that eliminate some          ##
## uneven changes visable                           ##
##                                                  ##
######################################################

import time
from piglow import PiGlow

piglow = PiGlow()

q = 0.001   # Delay for time.sleep seconds

x = 1      # Iniialize x, 0 causes .led to turn them off
           # Used to define led and brightness
maxbrite = 100 # The maximum brightness to use, absolute max is 255       
y = 1      # Initialize y for main loop

m = 0      # Initialize key for led list selection loop

           # LED selection list is below
           # Odd then even leds
#l=[1,3,5,7,9,11,13,14,17,2,4,6,8,10,12,14,16,18]

           # An alternate writing pattern that starts at center and moves
           # out, around the center counter clockwise.
           # Uncomment only one at a time
l=[12,6,18,11,5,17,10,4,16,9,3,15,8,2,14,7,1,13

piglow.all(0) # Turn off all led, just a housekeeping line

while y > 0:              # Begin the pulse loop
    
    while x < maxbrite :  # Start the brighten loop. The max is 255 for brightness of led    
   
        for m in range(18):      # Loop to set the leds to current brightness
            piglow.led(l[m],x)   # Set the led l[m]=led, n=brightness 
            m = m + 1            # Move to next in list l
        
        time.sleep(q) # Delay the loop by q
        
        x = x + 1         # Add one to x and loop


    while x > 0 :  # Start the dimming loop     
       

        for m in range(18):     # Loop to set the leds to current brightness
            piglow.led(l[m],x)  # Set the led l[m]=led, n=brightness  
            m = m + 1           # Move to next in list l
        
        time.sleep(q) # Delay the loop by q

        
        x = x - 1         # Add one x and loop

