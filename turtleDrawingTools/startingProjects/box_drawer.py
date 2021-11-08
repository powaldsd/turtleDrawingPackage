import drawings

shape = drawings.shapes
turtle = drawings.myTurtle
turtle.speed(2)
red = 0.2
blue = 0
green = 1
turtle.color(red, blue, green)

j = 3
x = 100
for i in range(23):
    shape.normalSquare(x)
    
    if(i == 3):
        x += 10
    if(i == 7):
        x += 10
    if(i == 10):
        x += 10   
    if(i == 13):
        x += 10
    if(i == 16):
        x += 10
    if(i == 19):
        x += 10
    if(i == 22):
        x += 10
    
