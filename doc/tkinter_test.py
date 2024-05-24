from tkinter import *
import time

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

mouseX = None
mouseY = None
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

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    
    top = Toplevel(root)
    Ox = 0
    Oy = 0
    height = 601
    width = 601
    bg = 'alice blue'

    top.title("Illustrating the minimum level graphical models")
    canvas = Canvas(top, height=height, width=width, background=bg)

    canvas.pack()

    cellsize = 200.0

    origin = coord((-cellsize,cellsize))
    len = length(origin,50,50)
    color = 'red'
    canvas.create_line(origin, len, fill=color,)

    origin2 = coord((0,cellsize))
    len2 = (50,50)
    color2 = 'orange'
    canvas.create_line(rectangle(origin2, len2), fill=color2)

    origin3 = coord((cellsize,cellsize))
    len3 = (40,60)
    color3 = 'blue'
    canvas.create_oval(ellipse(origin3,len3), fill=color3)

    origin4 = coord((-cellsize,0))
    len4 = (50,50)
    color4 = 'tomato'
    canvas.create_arc(ellipse(origin4,len4),extent=100,start=30,style=ARC,outline=color4)

    origin5 = coord((cellsize,0))
    len5 = (50,50)
    color5 = 'cyan'
    canvas.create_arc(ellipse(origin5,len5),extent=150,start=30,style=CHORD,fill=color5)

    origin6 = coord((-cellsize,-cellsize))
    len6 = (50,50)
    color6 = 'blue'
    pie = canvas.create_arc(ellipse(origin6,len6),extent=300,start=30,style=PIESLICE,fill=color6)

    origin7 = coord((0,-cellsize))
    text = 'Bla bla ...'
    color7 = 'purple'
    canvas.create_text(origin7,text=text, fill=color7)

    origin8 = coord((cellsize,-cellsize))
    color8 = 'black'
    canvas.create_rectangle(origin8,origin8, fill=color8, state=HIDDEN)
    
    print(ellipse(origin6,len6))
    print(canvas.itemconfig(pie))

    top.update()

    output = 'Press any mouse button to quit'
    print(output)

    p = waitClick()
    print(p)

    canvas.destroy()
