from tkinter import *
import time, os, sys

#################################################################
## Auxiliar
#################################################################
REFRESH_RATE = 0.1
last_refresh = time.time()
canvas_global = None
mouseX = None
mouseY = None
#################################################################
def coord(point):
    x = point[0]
    y = point[1]
    return (width/2-Ox+x, height/2+Oy-y)

def length(origin, x, y):
    return (origin[0]+x, origin[1]-y)

def rectangle(origin, length):
    p0 = (origin[0]-length[0]/2,origin[1]-length[1]/2)
    p1 = (origin[0]+length[0]/2,origin[1]-length[1]/2)
    p2 = (origin[0]+length[0]/2,origin[1]+length[1]/2)
    p3 = (origin[0]-length[0]/2,origin[1]+length[1]/2)
    return p0,p1,p2,p3,p0

def ellipse(origin, length):
    return (origin[0]-length[0]/2,origin[1]-length[1]/2),(origin[0]+length[0]/2,origin[1]+length[1]/2)

def onClick(event):
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y

def getMouse():
    global mouseX, mouseY
    top.update()
    mouseX = None; mouseY = None
    while mouseX == None:
        time.sleep(.1)
        top.update()

def waitClick():
    top.bind("<Button-1>", onClick)
    getMouse()
    return mouseX-width/2+Ox, height/2+Oy-mouseY
#################################################################


if __name__ == "__main__":
    root = Tk()
    root.withdraw()

    # default View values
    top = Toplevel(root)
    Ox = 0
    Oy = 0
    width = 201
    height = 201
    top.title("No title") 
    background = "black"

    v0 = 601
    v1 = v0
    v2 = v1
    v3 = 601
    v4 = v3
    v5 = v4
    v6 = "Illustrating the minimum level graphical models"
    v7 = v6
    v8 = v7
    v9 = "alice blue"
    v10 = v9
    v11 = v10

    height=v5
    width=v2
    top.title(v8)
    background=v11

    v12 = Canvas(top, height=height, width=width, background=background)
    v12.pack()
    canvas_global = v12
    view = v12
    v13 = 200
    v14 = v13
    v15 = v14
    cellSize = v15
    v17 = cellSize
    v18 = - v17
    v19 = cellSize
    v16 = (v18 , v19)
    v21 = 50
    v22 = 50
    v20 = (v21 , v22)
    v23 = v20
    v24 = v23
    v25 = "red"
    v26 = v25
    v27 = v26

    origin = coord(v16)
    length = v24
    canvas_global.create_line(rectangle(origin, length), fill=v27)
    v28 = 1
    v29 = 10
    for i in range(v28, v29, 1):
        v30 = "pedro "
        print(v30)
        v31 = i
        print(v31)
    v32 = waitClick()
    v33 = v32
    v34 = v33
    p = v34
    v35 = p
    print(v35)
