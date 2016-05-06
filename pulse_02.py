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

q = 0.001   # delay for time.sleep seconds

x = 1      # iniialize x, 0 causes .led to turn them off
           # used to define led and brightness
maxbrite = 100 # the maximum brightness to use, absolute max is 255       
y = 1      # initialize y for main loop

m = 0      # initialize key for led list selection loop

           # led selection list is below
           # odd the even leds
#l=[1,3,5,7,9,11,13,14,17,2,4,6,8,10,12,14,16,18]

           # an alternate writing pattern that starts at center and moves
           # out, around the center counter clockwise.
           # uncomment only one at a time
l=[12,6,18,11,5,17,10,4,16,9,3,15,8,2,14,7,1,13

piglow.all(0) # turn off all led, just a housekeeping line

while y > 0:              # begin the pulse loop
    
    while x < maxbrite :  # Start the brighten loop. The max is 255 for brightness of led    
   
        for m in range(18):      # loop to set the leds to current brightness
            piglow.led(l[m],x)   # Set the led l[m]=led, n=brightness 
            m = m + 1            # move to next in list l
        
        time.sleep(q) # delay the loop by q
        
        x = x + 1         # add one to x and loop


    while x > 0 :  # Start the dimming loop     
       

        for m in range(18):     # loop to set the leds to current brightness
            piglow.led(l[m],x)  # Set the led l[m]=led, n=brightness  
            m = m + 1           # move to next in list l
        
        time.sleep(q) # delay the loop by q

        
        x = x - 1         # add one x and loop

