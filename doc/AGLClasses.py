from tkinter import *
import time
import copy

class Root:

    def __init__(self):
        self.tk = Tk()
        self.objects = []

        self.tk.withdraw()

    def add_object(self, obj):
        self.objects.append(obj)

class View:

    def __init__(self, root: Root, Ox=0, Oy=0, height=201, width=201, title="No title", background="black"):
        self.root = root
        self.top = None
        self.Ox = Ox
        self.Oy = Oy
        self.height = height
        self.width = width
        self.title = title
        self.background = background

        self.mouseX = None
        self.mouseY = None

        self.canvas = None
        
    def create_canvas(self):
        if not self.top: self.top = Toplevel(self.root.tk)
        self.top.title(self.title)
        self.canvas = Canvas(self.top, height=self.height, width=self.width, background=self.background)
        self.canvas.pack()
        for o in self.root.objects:
            o.create_object(self)

    def update(self):
        if self.canvas: self.canvas.destroy()
        self.create_canvas()
        self.top.update()

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
        return (origin[0]-length[0],origin[1]-length[1]),(origin[0]+length[0],origin[1]+length[1])

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
        self.object = None                

        if self.root is not None:
            self.root.add_object(self)        

    def move_relative(self, vector):
        self.origin = (self.origin[0] + vector[0], self.origin[1] + vector[1])

    def move_absolute(self, point):
        self.origin = (point[0], point[1])

class Model(Object):
    
    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0)):
        super().__init__(root, view, origin, state)
        self.objects = []

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {} # this is required by the deepcopy protocol
        new_model = Model(self.root, self.view, self.state, self.origin)

        # copy all the attributes of the model
        copied_objects = []
        for k, v in self.__dict__.items():
            if not hasattr(new_model, k):
                copied_objects.append(v)
                object_copy = copy.deepcopy(v)
                old_relative = object_copy.origin
                object_copy.move_absolute(self.origin)
                object_copy.move_relative(old_relative)
                setattr(new_model, k, object_copy) # deepcopy of the object
                new_model.add_object(object_copy)

        for o in self.objects:
            if o not in copied_objects:
                object_copy = copy.deepcopy(o)
                new_model.add_object(object_copy)
                old_relative = object_copy.origin
                object_copy.move_absolute(self.origin)
                object_copy.move_relative(old_relative)
                
        return new_model

    def add_object(self, obj):
        print(self.objects)
        self.objects.append(obj)

    def create_object(self, view):
        print(self.objects)
        for o in self.objects:
            o.create_object(view)

    def move_relative(self, vector):
        for o in self.objects:
            o.move_relative(vector)

    def move_absolute(self, point):
        for o in self.objects:
            o.move_absolute(point)  
            o.move_relative(o.origin)              

# TODO: override move_relative and move_absolute

class Line(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_line = Line(self.root, self.view, self.state, self.origin, self.length, self.fill)   
        return new_line 

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.line(self.view.coord(self.origin), self.length), fill=self.fill, state=self.state)

class PolyLine(Object):
    """
    PolyLine is a line that needs to pass through a list of points.
    It has an origin, and, if no points are given, it will have a default length of (1,1).
    """

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), points=[(1,1)], fill="black"):
        super().__init__(root, view, origin, state)
        self.points = points
        self.fill = fill
    
    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_polyline = PolyLine(self.root, self.view, self.state, self.origin, self.points, self.fill)   
        return new_polyline
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, state=self.state)

    # TODO: override move_relative and move_absolute

class Spline(Object):
    """
    Spline is a smooth curve that is defined by a series of control points.
    It has an origin, and, if no points are given, it will have a default end point of (1,1).
    """

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), points=[(1,1)], fill="black"):
        super().__init__(root, view, origin, state)
        self.points = points
        self.fill = fill

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_spline = Spline(self.root, self.view, self.state, self.origin, self.points, self.fill)   
        return new_spline

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, state=self.state, smooth=True)

    # TODO: override move_relative and move_absolute

class Polygon(Object):
    """
    Polygon is a shape that is defined by a series of points.
    It can be filled or not.
    """

    def __init__(self, root: Root, view: View = None, state="normal", origin=(0,0), points=[(1,1)], fill="black", outline="black"):
        super().__init__(root, view, origin, state)
        self.points = points
        self.fill = fill
        self.outline = outline

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_polygon = Polygon(self.root, self.view, self.state, self.origin, self.points, self.fill, self.outline)   
        return new_polygon    
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_polygon(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, outline=self.outline, state=self.state)

    # TODO: override move_relative and move_absolute

class Blob(Object):
    """
    Blob is a shape that can be interpreted as drawing an irregular, free-form shape.
    It is basically a smooth polygon.
    """

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), points=[(1,1)], fill="black", outline="black"):
        super().__init__(root, view, origin, state)
        self.points = points
        self.fill = fill
        self.outline = outline

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_blob = Blob(self.root, self.view, self.state, self.origin, self.points, self.fill, self.outline)   
        return new_blob 
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_polygon(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, outline=self.outline, state=self.state, smooth=True)

    # TODO: override move_relative and move_absolute

class Rectangle(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill  
    
    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_rectangle = Rectangle(self.root, self.view, self.state, self.origin, self.length, self.fill)   
        return new_rectangle
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.rectangle(self.view.coord(self.origin), self.length), fill=self.fill, state=self.state)

class Ellipse(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_ellipse = Ellipse(self.root, self.view, self.state, self.origin, self.length, self.fill)   
        return new_ellipse

    def create_object(self, view):
        self.view = view
        calc = self.view.ellipse(self.origin, self.length)
        res = (self.view.coord(calc[0]), self.view.coord(calc[1]))
        print(res)
        self.object = self.view.canvas.create_oval(self.view.coord(calc[0]), self.view.coord(calc[1]), fill="red", state=self.state)
        print(self.view.ellipse(self.view.coord(self.origin), self.length))
        #self.object = self.view.canvas.create_oval(self.view.ellipse(self.view.coord(self.origin), self.length), fill=self.fill, state=self.state)

class Arc(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, outline="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.outline = outline

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_arc = Arc(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.outline)   
        return new_arc

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.view.coord(self.origin), self.length), style=ARC, start=self.start, extent=self.extent, outline=self.outline, state=self.state)

class ArcChord(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_arcchord = ArcChord(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.fill)   
        return new_arcchord

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.view.coord(self.origin), self.length), style=CHORD, start=self.start, extent=self.extent, fill=self.fill, state=self.state)


class PieSlice(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill  

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_pieslice = PieSlice(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.fill)   
        return new_pieslice

    def create_object(self, view):
        self.view = view
        print(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.fill)
        self.object = self.view.canvas.create_arc(self.view.ellipse(self.view.coord(self.origin), self.length), style=PIESLICE, start=self.start, extent=self.extent, fill=self.fill, state=self.state)


class Text(Object):
    
    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), text="No text", fill="black"):
        super().__init__(root, view, origin, state)
        self.text = text
        self.fill = fill

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_text = Text(self.root, self.view, self.state, self.origin, self.text, self.fill)   
        return new_text    

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_text(self.view.coord(self.origin), text=self.text, fill=self.fill, state=self.state)


class Dot(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), fill="black"):
        super().__init__(root, view, origin, state)
        self.fill = fill

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_dot = Dot(self.root, self.view, self.state, self.origin, self.fill)   
        return new_dot

    def create_object(self, view):
        self.view = view
        origin_coord = self.view.coord(self.origin)
        self.object = self.view.canvas.create_oval(origin_coord, origin_coord, fill=self.fill, state=self.state)
