from tkinter import *
import time

class Root:

    def __init__(self):
        self.root = Tk()
        self.objects = []

        self.root.withdraw()

    def add_object(self, obj):
        self.objects.append(obj)

class View:

    def __init__(self, root: Root, top=None, Ox=0, Oy=0, height=201, width=201, title="No title", background="black"):
        self.root = root
        self.top = top
        self.Ox = Ox
        self.Oy = Oy
        self.height = height
        self.width = width
        self.title = title
        self.background = background

        self.mouseX = None
        self.mouseY = None

        self.canvas = None
        #self.create_canvas()
        
    def create_canvas(self):
        if not self.top: self.top = Toplevel(self.root.root)
        self.top.title(self.title)
        self.canvas = Canvas(self.top, height=self.height, width=self.width, background=self.background)
        self.canvas.pack()
        for o in self.root.objects:
            o.create_object(self)

    def update(self):
        if self.canvas: self.canvas.destroy()
        self.create_canvas()
        self.root.root.update()

    def move_relative(self, point):
        x, y = point
        self.Ox += x
        self.Oy += y

    def move_absolute(self, point):
        x, y = point
        self.Ox = x
        self.Oy = y

    def coord(self, point):
        x, y = point
        return (self.width/2-self.Ox+x, self.height/2+self.Oy-y)

    def line(self, origin, point):
        return (origin[0],origin[1]),(origin[0]+point[0], origin[1]-point[1])

    def rectangle(self, origin, length):
        p0 = (origin[0]-length[0]/2,origin[1]-length[1]/2)
        p1 = (origin[0]+length[0]/2,origin[1]-length[1]/2)
        p2 = (origin[0]+length[0]/2,origin[1]+length[1]/2)
        p3 = (origin[0]-length[0]/2,origin[1]+length[1]/2)
        return p0,p1,p2,p3,p0

    def ellipse(self, origin, length):
        return (origin[0]-length[0]/2,origin[1]-length[1]/2),(origin[0]+length[0]/2,origin[1]+length[1]/2)

    def onClick(self, event):
        self.mouseX, self.mouseY = event.x, event.y

    def getMouse(self):
        self.top.update()
        self.mouseX = None; self.mouseY = None
        while self.mouseX == None:
            time.sleep(.1)
            self.top.update()

    def waitClick(self):
        self.top.bind("<Button-1>", self.onClick)
        self.getMouse()
        return self.mouseX-self.width/2+self.Ox, self.height/2+self.Oy-self.mouseY
    
    def add_object(self, obj):
        self.objects.append(obj)

    def close(self):
        self.canvas.destroy()

# ---------------------------------------------------------------
# AGL Objects
# ---------------------------------------------------------------

class Object:

    def __init__(self, root: Root, view: View, origin, state):
        self.root = root
        self.view = view
        self.origin = origin
        self.state = state

        self.root.add_object(self)

    def waitClick(self):
        return self.view.waitClick()  

    def move_relative(self, vector):
        self.origin = (self.origin[0] + vector[0], self.origin[1] + vector[1])

    def move_absolute(self, vector):
        self.origin=(vector[0], vector[1])

class Line(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.line(self.view.coord(self.origin), self.length), fill=self.fill, state=DISABLED)

class PolyLine(Object):
    """
    PolyLine is a line that needs to pass through a list of points.
    It has an origin, and, if no points are given, it will have a default length of (1,1).
    """

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), points=[(1,1)], fill="black"):
        super().__init__(root, view, origin, state)
        self.points = points
        self.fill = fill

        self.object = None
        #self.create_object()
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, state=self.state)

class Rectangle(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill
        self.state = NORMAL

        self.object = None
        #self.create_object()
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.rectangle(self.view.coord(self.origin), self.length), fill=self.fill, state=self.state)

class Ellipse(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_oval(self.view.ellipse(self.view.coord(self.origin), self.length), fill=self.fill, state=self.state)

class Arc(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, outline="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.outline = outline

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.view.coord(self.origin), self.length), style=ARC, start=self.start, extent=self.extent, outline=self.outline, state=self.state)

class ArcChord(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.view.coord(self.origin), self.length), style=CHORD, start=self.start, extent=self.extent, fill=self.fill, state=self.state)


class PieSlice(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill  

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.view.coord(self.origin), self.length), style=PIESLICE, start=self.start, extent=self.extent, fill=self.fill, state=self.state)


class Text(Object):
    
    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), text="No text", fill="black"):
        super().__init__(root, view, origin, state)
        self.text = text
        self.fill = fill

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_text(self.view.coord(self.origin), text=self.text, fill=self.fill, state=self.state)


class Dot(Object):

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), fill="black"):
        super().__init__(root, view, origin, state)
        self.fill = fill

        self.object = None
        #self.create_object()

    def create_object(self, view):
        self.view = view
        origin_coord = self.view.coord(self.origin)
        self.object = self.view.canvas.create_oval(origin_coord, origin_coord, fill=self.fill, state=self.state)
