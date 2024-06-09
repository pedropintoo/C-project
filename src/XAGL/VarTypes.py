from enum import Enum
from AGLClasses import *

class Type(Enum):
    Integer = 0
    Number = 1
    String = 2
    Point = 3
    Vector = 4
    Time = 5
    Boolean = 6
    Array = 7
    ImplicitPoint = 8 # pode ser um vector ou um ponto, usado para expressões que não possuem declaração
    Enum = 9
    Model = 10

class Var():
    def __init__(self, var):
        self.type = self.getType(var)
        self.var = var # Para models

    def getType(self, var):
        if type(var) == Type:
            return var
        
        elif type(var) in (View, Line, Rectangle, Ellipse, Arc, ArcChord, PieSlice, Polygon, Spline, Polygon, Blob, Text, Dot):
            return type(var)
        
        elif issubclass(type(var), Model):
            return Type.Model
        
        elif issubclass(type(var), Enum):
            return Type.Enum

    def Dict(self):
        if self.type == View:
            return {"Ox":Type.Number,
                    "Oy":Type.Number,
                    "width":Type.Integer,
                    "height":Type.Integer, 
                    "title":Type.String, 
                    "background":Type.String}
        
        elif self.type == Line or self.type == Rectangle or self.type == Ellipse:
            return {"length":Type.Vector, 
                    "fill":Type.String, 
                    "state":Type.String}
        
        elif self.type == Arc:
            return {"length:":Type.Vector,
                    "outline":Type.String,
                    "state":Type.String,
                    "start":Type.Integer,
                    "extent":Type.Integer,
                    }
        
        elif self.type == ArcChord or self.type == PieSlice:
            return {"length:":Type.Vector,
                    "fill":Type.String,
                    "state":Type.String,
                    "start":Type.Integer,
                    "extent":Type.Integer,
                    }
        elif self.type == Text:
            return {"text":Type.String,
                    "fill":Type.String,
                    "state":Type.String
                    }
        
        elif self.type == Dot:
            return {"text":Type.String,
                    "state":Type.String
                    }
        
        elif self.type == Polyline or self.type == Spline:
            return {"points":Type.Array,
                    "fill":Type.String,
                    "state":Type.String
                    }

        elif self.type == Polygon or self.type == Blob:
            return {"points":Type.Array,
                    "fill":Type.String,
                    "outline":Type.String,
                    "state":Type.String
                    }
        elif type(self.type) == Type or self.type == Enum: 
            return {}
    
        elif self.type == Model:
            return {attr:Var(value) for attr, value in self.var.attributes}
        

    def canAssign(self, var):
      type1 = self.type
      type2 = var.type
      return ( type1 == type2 or
               type1 == Type.Number and type2 == Type.Integer or
               type1 == Type.Point and type2 == Type.ImplicitPoint or 
               type1 == Type.Vector and type2 == Type.ImplicitPoint
            )
    
        