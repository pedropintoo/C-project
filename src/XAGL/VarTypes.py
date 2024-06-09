from enum import Enum
from AGLClasses import *
import re
import numpy

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
        self.var = var # Para models e enum

    def getType(self, var):
        if type(var) == Type:
            return var
        
        elif type(var) in (View, Line, Rectangle, Ellipse, Arc, ArcChord, PieSlice, Polygon, Spline, Polygon, Blob, Text, Dot):
            return type(var)
        
        elif issubclass(type(var), Model):
            return Type.Model
        
        elif issubclass(type(var), Enum):
            return Type.Enum
        
        elif type(var) == int:
            return Type.Integer
        
        elif type(var) == float:
            return Type.Number
        
        elif type(var) == numpy.ndarray:
            return Type.Point
        
        elif type(var) == str and re.fullmatch(r"\d+ m?s", var):
            return Type.Time
        
        elif type(var) == str:
            return Type.String
        
        elif type(var) == list:
            return Type.Array
        
        elif type(var) == bool:
            return Type.Boolean


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
        
        elif self.type == Type.Model:
            return {attr:Var(value) for attr, value in self.var.attributes.items()}
        
        elif type(self.type) == Type or self.type == Type.Enum: 
            return {}
        

    def canAssign(self, var):
      var1 = self.var
      var2 = var.var
      type1 = self.type
      type2 = var.type
      print(type1, var1, type2, var2)
      return ( type1 == Type.Enum and type2 == Type.Enum and type(var1) == type(var2) or # verificar se os enums são do mesmo tipo
               type1 == type2 and type1 != Type.Enum or
               type1 == Type.Number and type2 == Type.Integer or    # Number pode recber Number ou Integer
               type1 == Type.Point and type2 == Type.ImplicitPoint or # ImplicitPoint pode ser atribuido em Point e Vector
               type1 == Type.Vector and type2 == Type.ImplicitPoint
            )
    
        