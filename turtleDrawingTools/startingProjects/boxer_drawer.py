import drawings
from turtle import *
import time
 

#drawings.draw.angleDrawAdvanced(100, -45, 90, 90, 18, False , 80, True)

draw = drawings.shapes
x = 100
limit = 242

running = True

while(running):
    while(x < limit):
        draw.square(x, True)
        draw.square(x, False)
        if(x < limit):
            x += 20
        while(x > 241):
            x -= 20
    if not running:
        break
if(x == limit):
    time.sleep(5)

    


	