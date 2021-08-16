import time
from tkinter import Tcl, TclError
import turtle




myTurtle = turtle.Turtle()


class draw:
    
    def angleDrawAdvanced(x, angle0, angle1, angle2, angle3, doDrawForward1, angle4, doDrawForward2):


        angle = [angle0, angle1, angle2]

        #Rotations are made to go right if u want to go left u will need to use -DEG like -90DEG


        #Logic If User Put None As Index 4 or 5
        canDraw4 = False
        canDraw5 = False

        #If Statements based on what you inputed in this function

        if(angle3 != None):
            #We Append Array
            angle.append(angle3)
            canDraw4 = True
        if(angle3 != False):
            angle.append(angle3)
            canDraw4 = True
        if(angle4 != None):
            angle.append(angle4)
            canDraw5 = True
        if(angle4 != False):
            angle.append(angle4)
            canDraw5 = True


        myTurtle.right(angle[0])
        myTurtle.forward(x)
        myTurtle.right(angle[1])
        myTurtle.forward(x)
        myTurtle.right(angle[2])


        #We Draw Those Indexes If CanDraw is True
        if(canDraw4):
            myTurtle.right(angle[3])
            myTurtle.forward(x)
        if(canDraw5):
            myTurtle.right(angle[4])
            myTurtle.forward(100)


        #Logic to say Are WE Drawing
        if(doDrawForward1 != False or None):
            myTurtle.forward(100)
        if(doDrawForward2 != False or None):
            myTurtle.forward(100)



    def draw(x, angle, times, max):
        while(times != max):
            myTurtle.forward(x)
            myTurtle.right(angle)
            times += 1
    def angle(x, r0, r1, r2, r3):
        doRotation4 = False
        if(r3 != False):
            doRotation4 = True
        if(r3 != None):
            doRotation4 = True

        myTurtle.right(r0)
        myTurtle.forward(x)
        myTurtle.right(r1)
        myTurtle.forward(x)
        myTurtle.right(r2)
        myTurtle.forward(x)


        if(doRotation4):
            myTurtle.right(r3)
            myTurtle.forward(x)         
class shapes:
    def square(x, loopDraw):
        startLoop = False     
        if(loopDraw != None):
            startLoop = True
        if(loopDraw != False):
            startLoop = True
        
        myTurtle.forward(x) 
        myTurtle.right(90)
        myTurtle.forward(x)    
        myTurtle.right(90)    
        myTurtle.forward(x)
        myTurtle.right(90)
        myTurtle.forward(x)
        if(startLoop):
            myTurtle.forward(x)
    def normalSquare(x):
        myTurtle.forward(x)
        myTurtle.right(90)
        myTurtle.forward(x)
        myTurtle.right(90)
        myTurtle.forward(x)
        myTurtle.right(90)
        myTurtle.forward(x)