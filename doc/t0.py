from tkinter import *
import time, os, sys
from tkinter import *

root = Tk()
root.withdraw()
root.title("C-Project Compiler")

top = Toplevel(root)
a = Canvas(top, background="wheat", height=450, width=700)
a.pack()
canvas = a

b = Canvas(top, background="wheat", height=450, width=700)
b.pack()

def drawPolyline():
    # A Tk line accepts 2 or more pairs of coordinates.
    # Origin is at the top-left corner, not the same as required by the AGL language,
    # so a transformation is required.
    # AGL Line and Polyline primitives may be based on this canvas method.
    line = canvas.create_line(10,10, 100,100, 500,100, fill='black', width=5)

def drawSpline():
    # tk line may also be used to implement the Spline primitive.
    # Coordinates may be given as a list.
    # Clipping is automatic.
    splineCoords = [ -200,200, 770,500, 100,100, 10,400 ]
    spline = canvas.create_line(splineCoords, smooth=True, fill="purple", width=3)

def drawArc():
    # tk arc allows to implement AGL Arc, ArcChord, and PieSlice.
    # Coordinates may also be given as a list of tuples
    # Overlapping depend on order of creation
    arcPoints = [ (10,500), (240,210) ]
    global arc
    arc = canvas.create_arc(arcPoints, start=0, extent=150, fill="cyan", outline='')

mouseX = None
mouseY = None
def onClick(event):
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y

def getMouse():
    global mouseX, mouseY
    canvas.update()
    mouseX = None; mouseY = None
    while mouseX == None:
        time.sleep(.1)
        canvas.update()

top.bind("<Button-1>", onClick)

drawPolyline()
root.update()

time.sleep(1)

drawArc()
root.update()

time.sleep(1)

canvas.itemconfig(arc, fill="yellow")
canvas.move(arc, 400, 0)
drawSpline()
root.update()

print('Press mouse to quit')
getMouse()
print('Button: {}, {}'.format(mouseX, mouseY))

