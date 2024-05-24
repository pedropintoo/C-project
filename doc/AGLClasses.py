from tkinter import *
import time

class View:

    def __init__(self, top, Ox=0, Oy=0, height=201, width=201, title="No title", background="black"):
        self.top = top
        self.Ox = Ox
        self.Oy = Oy
        self.height = height
        self.width = width
        self.title = title
        self.background = background

        self.mouseX = None
        self.mouseY = None

        self.objects = []

        self.canvas = None
        self.create_canvas()
        
    def create_canvas(self):
        self.top.title(self.title)
        self.canvas = Canvas(self.top, height=self.height, width=self.width, background=self.background)
        self.canvas.pack()
        for o in self.objects:
            o.create_object()

    def change(self, Ox=None, Oy=None, height=None, width=None, title=None, background=None):
        self.Ox = Ox if Ox else self.Ox
        self.Oy = Oy if Oy else self.Oy
        self.height = height if height else self.height
        self.width = width if width else self.width
        self.title = title if title else self.title
        self.background = background if background else self.background
        # next update will change the canvas
        self.top.title(self.title)
        self.canvas.config(height=self.height, width=self.width, background=self.background)

    def update(self):
        for o in self.objects:
            self.canvas.delete(o.object)
            o.create_object()
        self.top.update()

    def coord(self, point):
        x = point[0]
        y = point[1]
        return (self.width/2-self.Ox+x, self.height/2+self.Oy-y)

    def length(self, origin, point):
        return (origin[0]+point[0], origin[1]-point[1])

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

    def __init__(self, view: View, state):
        self.view = view
        self.state = state

    def waitClick(self):
        return self.view.waitClick()  

class Line(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.length = view.length(self.origin, length)
        self.fill = fill

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_line(self.origin, self.length, fill=self.fill, state=self.state)

    def change(self, state=None, origin=None, length=None, fill=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.length = self.view.length(self.origin, length) if length else self.length
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas

class Rectangle(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.length = length
        self.fill = fill
        self.state = NORMAL

        self.object = None
        self.create_object()
    
    def create_object(self):
        self.object = self.view.canvas.create_line(self.view.rectangle(self.origin, self.length), fill=self.fill, state=self.state)

    def change(self, state=None, origin=None, length=None, fill=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.length = length if length else self.length
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas

class Ellipse(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.length = length
        self.fill = fill

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_oval(self.view.ellipse(self.origin, self.length), fill=self.fill, state=self.state)

    def change(self, origin=None, length=None, fill=None, state=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.length = length if length else self.length
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas

class Arc(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, outline="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.length = length
        self.start = start
        self.extent = extent   
        self.outline = outline

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.origin, self.length), style=ARC, start=self.start, extent=self.extent, outline=self.outline, state=self.state)

    def change(self, origin=None, length=None, start=None, extent=None, outline=None, state=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.length = length if length else self.length
        self.start = start if start else self.start
        self.extent = extent if extent else self.extent
        self.outline = outline if outline else self.outline
        self.state = state if state else self.state
        # next update will change the canvas

class ArcChord(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.origin, self.length), style=CHORD, start=self.start, extent=self.extent, fill=self.fill, state=self.state)

    def change(self, origin=None, length=None, start=None, extent=None, fill=None, state=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.length = length if length else self.length
        self.start = start if start else self.start
        self.extent = extent if extent else self.extent
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas

class PieSlice(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill  

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.origin, self.length), style=PIESLICE, start=self.start, extent=self.extent, fill=self.fill, state=self.state)

    def change(self, origin=None, length=None, start=None, extent=None, fill=None, state=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.length = length if length else self.length
        self.start = start if start else self.start
        self.extent = extent if extent else self.extent
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas

class Text(Object):
    
    def __init__(self, view: View, state="normal", origin=(0,0), text="No text", fill="black"):
        super().__init__(view, state)
        self.origin = view.coord(origin)
        self.text = text
        self.fill = fill

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_text(self.origin, text=self.text, fill=self.fill, state=self.state)

    def change(self, origin=None, text=None, fill=None, state=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.text = text if text else self.text
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas

class Dot(Object):

    def __init__(self, view: View, state="normal", origin=(0,0), fill="black"):
        super().__init__( view, state)
        self.origin = view.coord(origin)
        self.fill = fill

        self.object = None
        self.create_object()

    def create_object(self):
        self.object = self.view.canvas.create_oval(self.origin, self.origin, fill=self.fill, state=self.state)

    def change(self, origin=None, fill=None, state=None):
        self.origin = self.view.coord(origin) if origin else self.origin
        self.fill = fill if fill else self.fill
        self.state = state if state else self.state
        # next update will change the canvas