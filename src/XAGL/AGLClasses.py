from tkinter import *
import time
import copy
import math


class Root:

    def __init__(self, views, last_view):
        self.tk = Tk()
        self.objects = []

        self.mouseX = None
        self.mouseY = None

        self.views = views
        self.last_view = last_view

        self.tk.withdraw()

        self.objects = []
        self.views = []
        self.last_refresh = time.time()
        self.REFRESH_RATE = 0.001       

    def add_object(self, obj):
        self.objects.append(obj)

    def onClick(self, event, view):
        self.mouseX = event.x - view.width/2 + view.Ox
        self.mouseY = view.height/2 + view.Oy - event.y

    def getMouse(self):
        for v in self.views:
            v.canvas.pack()
            v.canvas.update()
        self.last_view.canvas.pack()
        self.last_view.canvas.update()

        self.mouseX = None; self.mouseY = None
        while self.mouseX == None:
            time.sleep(.1)

            for v in self.views:
                v.canvas.update()
            self.last_view.canvas.update()

    def waitClick(self):
        for v in self.views:
            v.canvas.bind("<Button-1>", lambda event, view=v : self.onClick(event,view))
        self.last_view.canvas.bind("<Button-1>", lambda event, view=self.last_view : self.onClick(event,view))    
        self.getMouse()    
        return self.mouseX, self.mouseY


class View:

    def __init__(self, root: Root, Ox=0, Oy=0, height=201, width=201, title="No title", background="black"):
        self.root = root
        self.top = Toplevel(self.root.tk)
        self.Ox = Ox
        self.Oy = Oy
        self.height = height
        self.width = width
        self.title = title
        self.background = background

        self.mouseX = None
        self.mouseY = None

        self.canvas = None
        
        self.objectsDrawn = []
        #self.canvas = Canvas(self.top, height=self.height, width=self.width, background=self.background)

        self.root.views.append(self)

    def update(self, delay = 0):
        if not self.canvas:
            self.canvas = Canvas(self.top, height=self.height, width=self.width, background=self.background) 
        if delay:
            while (time.time() - self.root.last_refresh <= delay):
                time.sleep(self.root.REFRESH_RATE)

        self.root.last_refresh = time.time()
        self.top.title(self.title)
        self.canvas.config(height=self.height, width=self.width, background=self.background)
        self.canvas.pack()
        for o in self.objectsDrawn:
            self.canvas.delete(o)
        for o in self.root.objects:
            o.create_object(self)
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

    def rectangle(self, origin, length, angle):
        angle_rad = math.radians(-angle)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)

        p0 = (origin[0] - length[0] * cos_angle - length[1] * sin_angle, origin[1] - length[0] * sin_angle + length[1] * cos_angle)
        p1 = (origin[0] + length[0] * cos_angle - length[1] * sin_angle, origin[1] + length[0] * sin_angle + length[1] * cos_angle)
        p2 = (origin[0] + length[0] * cos_angle + length[1] * sin_angle, origin[1] + length[0] * sin_angle - length[1] * cos_angle)
        p3 = (origin[0] - length[0] * cos_angle + length[1] * sin_angle, origin[1] - length[0] * sin_angle - length[1] * cos_angle)
        return p0,p1,p2,p3,p0

    def ellipse(self, origin, length):
        return (origin[0]-length[0], origin[1]-length[1]), (origin[0]+length[0], origin[1]+length[1])

    def poly_oval(self, x0, y0, x1, y1, start = 0, extent = 360, steps=250, rotation=0):
        a = (x1 - x0) / 2.0
        b = (y1 - y0) / 2.0

        xc = x0 + a
        yc = y0 + b

        point_list = []

        start_rad = math.radians(start)
        extent_rad = math.radians(extent)
        rotation_rad = math.radians(rotation)

        for i in range(steps):

            theta = start_rad + (extent_rad * i / steps)

            x1 = a * math.cos(theta)
            y1 = b * math.sin(theta)

            x = (x1 * math.cos(rotation_rad)) + (y1 * math.sin(rotation_rad))
            y = (y1 * math.cos(rotation_rad)) - (x1 * math.sin(rotation_rad))

            point_list.append(round(x + xc))
            point_list.append(round(y + yc))

        return point_list

    def close(self):
        self.canvas.destroy()
        self.top.destroy()
    
    def rotateByOrigin(self, angle, originRef, originObject):
        """
        Rotate an origin of a object by a given angle around a given origin.
        This function will calculate the new position of the origin of the object by rotating the vector from the given origin 
        to the origin of the object by the given angle.
        """
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)
        vector_from_origin = (originObject[0] - originRef[0], originObject[1] - originRef[1])
        # rotate the vector_from_origin around the origin by the angle
        new_x = cos_val * vector_from_origin[0] - sin_val * vector_from_origin[1]
        new_y = sin_val * vector_from_origin[0] + cos_val * vector_from_origin[1]
        return (originRef[0] + new_x, originRef[1] + new_y)

    def rotateLength(self, length, angle):
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)

        rel_x = length[0]
        rel_y = length[1]

        new_x = cos_val * rel_x - sin_val * rel_y
        new_y = sin_val * rel_x + cos_val * rel_y

        return (new_x, new_y)
    
    def Dict(self):
        return vars(self)

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

    def Dict(self):
        return vars(self)
    
class Model(Object):
    
    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0)):
        super().__init__(root, view, origin, state)
        self.objects = []
        self.attributes = {}

    def addAttributes(self, attr, value):
        self.attributes[attr] = value

    def Dict(self):
        return self.attributes   

    def copyAttributesTo(self, new_model):
        new_model.objects = []

        for k,v in self.__dict__.items():
            if k == "objects":
                continue
            if isinstance(v, Root) or isinstance(v, View):
                new_model.__dict__[k] = v
            else:
                new_model.__dict__[k] = copy.deepcopy(v)
            if isinstance(v, Object) and not k.startswith("last"):
                # print(self.__class__.__name__ + "." + k)
                new_model.objects.append(new_model.__dict__[k])
            

    def fixCoords(self):
        for o in self.objects:
            old_relative = o.origin
            o.move_absolute(self.origin)
            o.move_relative(old_relative)

    def add_object(self, obj):
        self.objects.append(obj)

    def create_object(self, view):
        for o in self.objects:
            o.state = self.state if self.state != "normal" else o.state

        for o in self.objects:
            o.create_object(view)

    def move_relative(self, vector):
        for o in self.objects:
            o.move_relative(vector)
        self.origin = (self.origin[0] + vector[0], self.origin[1] + vector[1])    

    def move_absolute(self, point):
        for o in self.objects:
            old_relative = (o.origin[0] - self.origin[0], o.origin[1] - self.origin[1])
            o.move_absolute(point) 
            o.move_relative(old_relative) 
        self.origin = point   

    def rotate(self, angle, origin=None):
        if origin is None:
            origin = self.origin

        for o in self.objects:
            o.rotate(angle, origin)


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
        self.view = view # TODO: this id is for specific view!!! cannot be used in other views
        self.object = self.view.canvas.create_line(self.view.line(self.view.coord(self.origin), self.length), fill=self.fill, state=self.state)
        self.view.objectsDrawn.append(self.object)
    
    def rotate(self, angle, origin=None):
        self.length = self.view.rotateLength(self.length, angle)
        
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class Polyline(Object):
    """
    Polyline is a line that needs to pass through a list of points.
    It has an origin, and, if no points are given, it will have a default point of (1,1).
    """

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), points=[(1,1)], fill="black"):
        super().__init__(root, view, origin, state)
        self.points = points
        self.fill = fill
    
    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_polyline = Polyline(self.root, self.view, self.state, self.origin, self.points, self.fill)   
        return new_polyline
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, state=self.state)
        self.view.objectsDrawn.append(self.object)

    def move_relative(self, vector):
        super().move_relative(vector)  # move the origin point
        
        # move the points
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + vector[0], self.points[i][1] + vector[1])

    def move_absolute(self, point):
        temp_origin = self.origin  # save the origin point
        super().move_absolute(point)  # move the origin point
        move_vector = (self.origin[0] - temp_origin[0], self.origin[1] - temp_origin[1])  # take the resultant vector
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + move_vector[0], self.points[i][1] + move_vector[1])
    
    def rotate(self, angle, origin=None):
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)

        for i in range(len(self.points)):
            if origin != None:
                self.points[i] = self.view.rotateByOrigin(angle, origin, self.points[i])
            else:
                self.points[i] = (cos_val * self.points[i][0] - sin_val * self.points[i][1], sin_val * self.points[i][0] + cos_val * self.points[i][1])
        
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

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
        self.view.objectsDrawn.append(self.object)

    def move_relative(self, vector):
        super().move_relative(vector)
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + vector[0], self.points[i][1] + vector[1])
    
    def move_absolute(self, point):
        temp_origin = self.origin 
        super().move_absolute(point)  
        move_vector = (self.origin[0] - temp_origin[0], self.origin[1] - temp_origin[1]) 
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + move_vector[0], self.points[i][1] + move_vector[1])
    
    def rotate(self, angle, origin=None):
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)

        for i in range(len(self.points)):
            if origin != None:
                self.points[i] = self.view.rotateByOrigin(angle, origin, self.points[i])
            else:
                self.points[i] = (cos_val * self.points[i][0] - sin_val * self.points[i][1], sin_val * self.points[i][0] + cos_val * self.points[i][1])
        
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class Polygon(Object):
    """
    Polygon is a shape that is defined by a series of points.
    It can be filled or not.
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
        new_polygon = Polygon(self.root, self.view, self.state, self.origin, self.points, self.fill, self.outline)   
        return new_polygon    
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_polygon(self.view.coord(self.origin), *[self.view.coord(p) for p in self.points], fill=self.fill, outline=self.outline, state=self.state)
        self.view.objectsDrawn.append(self.object)

    def move_relative(self, vector):
        super().move_relative(vector)
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + vector[0], self.points[i][1] + vector[1])
    
    def move_absolute(self, point):
        temp_origin = self.origin 
        super().move_absolute(point)  
        move_vector = (self.origin[0] - temp_origin[0], self.origin[1] - temp_origin[1]) 
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + move_vector[0], self.points[i][1] + move_vector[1])
    
    def rotate(self, angle, origin=None):
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)

        for i in range(len(self.points)):
            if origin != None:
                self.points[i] = self.view.rotateByOrigin(angle, origin, self.points[i])
            else:
                self.points[i] = (cos_val * self.points[i][0] - sin_val * self.points[i][1], sin_val * self.points[i][0] + cos_val * self.points[i][1])
        
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

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
        self.view.objectsDrawn.append(self.object)

    def move_relative(self, vector):
        super().move_relative(vector)
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + vector[0], self.points[i][1] + vector[1])
    
    def move_absolute(self, point):
        temp_origin = self.origin 
        super().move_absolute(point)  
        move_vector = (self.origin[0] - temp_origin[0], self.origin[1] - temp_origin[1]) 
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + move_vector[0], self.points[i][1] + move_vector[1])
    
    def rotate(self, angle, origin=None):
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)

        for i in range(len(self.points)):
            if origin != None:
                self.points[i] = self.view.rotateByOrigin(angle, origin, self.points[i])
            else:
                self.points[i] = (cos_val * self.points[i][0] - sin_val * self.points[i][1], sin_val * self.points[i][0] + cos_val * self.points[i][1])
        
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class Rectangle(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill
        self.angle = 0
        self.array = []
    
    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_rectangle = Rectangle(self.root, self.view, self.state, self.origin, self.length, self.fill)   
        new_rectangle.angle = self.angle
        return new_rectangle
    
    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_line(self.view.rectangle(self.view.coord(self.origin), self.length, self.angle), fill=self.fill, state=self.state)
        self.view.objectsDrawn.append(self.object)
    
    def rotate(self, angle, origin=None):
        self.angle += angle

        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class Ellipse(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), fill="black", outline="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.fill = fill
        self.outline = outline
        self.angle = 0

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_ellipse = Ellipse(self.root, self.view, self.state, self.origin, self.length, self.fill, self.outline)   
        new_ellipse.angle = self.angle
        return new_ellipse

    def create_object(self, view):
        self.view = view
        top_left, bottom_right = self.view.ellipse(self.view.coord(self.origin), self.length)
        self.object = self.view.canvas.create_polygon(tuple(self.view.poly_oval(top_left[0], top_left[1], bottom_right[0], bottom_right[1], steps=250, rotation=self.angle)), fill=self.fill, state=self.state, smooth=True, outline=self.outline)
        self.view.objectsDrawn.append(self.object)
    
    def rotate(self, angle, origin=None):
        self.angle += angle
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class Arc(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, outline="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.outline = outline
        self.angle = 0

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_arc = Arc(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.outline)   
        new_arc.angle = self.angle
        return new_arc

    def create_object(self, view):
        self.view = view
        top_left, bottom_right = self.view.ellipse(self.view.coord(self.origin), self.length)
        self.object = self.view.canvas.create_line(tuple(self.view.poly_oval(top_left[0], top_left[1], bottom_right[0], bottom_right[1], start=self.start, extent=self.extent, steps=250, rotation=self.angle)), fill = self.outline, state=self.state, smooth=True)
        self.view.objectsDrawn.append(self.object)
    
    def rotate(self, angle, origin=None):
        self.angle += angle

        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class ArcChord(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black", outline="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill
        self.angle = 0
        self.outline = outline

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_arcchord = ArcChord(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.fill)   
        new_arcchord.angle = self.angle
        return new_arcchord

    def create_object(self, view):
        self.view = view
        top_left, bottom_right = self.view.ellipse(self.view.coord(self.origin), self.length)
        self.object = self.view.canvas.create_polygon(tuple(self.view.poly_oval(top_left[0], top_left[1], bottom_right[0], bottom_right[1], start=self.start, extent=self.extent, steps=250, rotation=self.angle)), fill=self.fill, state=self.state, outline=self.outline)
        self.view.objectsDrawn.append(self.object)

    def rotate(self, angle, origin=None):
        self.angle += angle
        
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class PieSlice(Object):

    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), length=(1,1), start=0, extent=100, fill="black", outline="black"):
        super().__init__(root, view, origin, state)
        self.length = length
        self.start = start
        self.extent = extent   
        self.fill = fill  
        self.outline = outline
        self.angle = 0

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_pieslice = PieSlice(self.root, self.view, self.state, self.origin, self.length, self.start, self.extent, self.fill)   
        new_pieslice.angle = self.angle
        return new_pieslice

    def create_object(self, view):
        self.view = view
        top_left, bottom_right = self.view.ellipse(self.view.coord(self.origin), self.length)   
        self.object = self.view.canvas.create_polygon(self.view.coord(self.origin), tuple(self.view.poly_oval(top_left[0], top_left[1], bottom_right[0], bottom_right[1], start=self.start, extent=self.extent, steps=250, rotation=self.angle)), fill=self.fill, state=self.state, outline=self.outline)
        self.view.objectsDrawn.append(self.object)

    def rotate(self, angle, origin=None):
        self.angle += angle

        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)

class Text(Object):
    
    def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0), text="No text", fill="black"):
        super().__init__(root, view, origin, state)
        self.text = text
        self.fill = fill
        self.angle = 0

    def __deepcopy__(self, memo=None):
        """Create a deep copy of the model."""
        if memo is None:
            memo = {}
        new_text = Text(self.root, self.view, self.state, self.origin, self.text, self.fill) 
        new_text.angle = self.angle;  
        return new_text    

    def create_object(self, view):
        self.view = view
        self.object = self.view.canvas.create_text(self.view.coord(self.origin), text=self.text, fill=self.fill, state=self.state, angle=self.angle)
        self.view.objectsDrawn.append(self.object)
    
    def rotate(self, angle, origin=None):
        self.angle += angle

        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)


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
        self.view.objectsDrawn.append(self.object)
    
    def rotate(self, angle, origin=None):
        # Should a dot be rotated?
        if origin != None:
            self.origin = self.view.rotateByOrigin(angle, origin, self.origin)
