from drawings import *

pen = draw
shape = shapes

turt = myTurtle

#variable that takes to create smooth circle
smoothCircle = 3

i = 30
curIndex = 0

#sets turtle color
turt.color(0.5, 0, 0)
while curIndex != i:
    pen.angle(smoothCircle, smoothCircle, smoothCircle, smoothCircle, smoothCircle)
    curIndex += 1