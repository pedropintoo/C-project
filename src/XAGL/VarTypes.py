from enum import Enum
from src.XAGL.AGLClasses import *
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
        self.var = var # Para models, enum e array
        self.element = None

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
      return ( type1 == Type.Enum and type2 == Type.Enum and type(var1) == type(var2) or # verificar se os enums são do mesmo tipo
               type1 == Type.Array and type2 == Type.Array and self.element.type == var.element.type or
               type1 == type2 and type1 != Type.Enum and type1 != Type.Array or
               type1 == Type.Number and type2 == Type.Integer or    # Number pode receber Number ou Integer
               type1 == Type.Time and var.isNumeric() or
               type1 == Type.Point and type2 == Type.ImplicitPoint or # ImplicitPoint pode ser atribuido em Point e Vector
               type1 == Type.Vector and type2 == Type.ImplicitPoint
            )
    
    def isNumeric(self):
        return (self.type == Type.Integer or
                self.type == Type.Number
                )
    
    def isPoint(self):
        return (self.type == Type.Point or
                self.type == Type.ImplicitPoint)
    
    def isVector(self):
        return (self.type == Type.Vector or
                self.type == Type.ImplicitPoint)
    
    def isBoolean(self):
        return self.type == Type.Boolean
    
    def isView(self):
        return self.type == View
    
    def isModel(self):
        return (self.type in (View, Line, Rectangle, Ellipse, Arc, ArcChord, PieSlice, Polygon, Spline, Polygon, Blob, Text, Dot, Type.Model)
                )
    
    def isDelay(self):
        return (self.type == Type.Integer or
                self.type == Type.Number or
                self.type == Type.Time)
    
    def sum_sub(self, var):
        type1 = self.type
        type2 = var.type
        if (type1 == Type.Integer and type2 == Type.Integer):
            return Type.Integer
        
        if  (type1 == Type.Integer and type2 == Type.Number or 
             type1 == Type.Number and type2 == Type.Integer or
             type1 == Type.Number and type2 == Type.Number):
            return Type.Number
        
        if (self.isVector() and var.isVector()):
            return Type.Vector
        
        if (self.isVector() and var.isPoint() or
            self.isPoint() and var.isVector()):
            return Type.Point
        
    def mult(self, var):
        type1 = self.type
        type2 = var.type
        if (type1 == Type.Integer and type2 == Type.Integer):
            return Type.Integer
        
        if  (type1 == Type.Integer and type2 == Type.Number or 
             type1 == Type.Number and type2 == Type.Integer or
             type1 == Type.Number and type2 == Type.Number):
            return Type.Number
        
        if (type1 == Type.ImplicitPoint and type2 == Type.ImplicitPoint or
            type1 == Type.ImplicitPoint and var.isNumeric() or
            self.isNumeric() and type2 == Type.ImplicitPoint):
            return Type.ImplicitPoint
        
        if (type1 == Type.Vector and type2 == Type.Vector or
            type1 == Type.Vector and var.isNumeric() or
            self.isNumeric() and type2 == Type.Vector):
            return Type.Vector
        
        if (type1 == Type.Point and var.isNumeric() or
            self.isNumeric() and type2 == Type.Point or
            self.isVector() and var.isPoint() or
            self.isPoint() and var.isVector()):
            return Type.Point
        
    def div(self, var):
        type1 = self.type
        type2 = var.type
        if (type1 == Type.Integer and type2 == Type.Integer):
            return Type.Integer
        
        if  (type1 == Type.Integer and type2 == Type.Number or 
             type1 == Type.Number and type2 == Type.Integer or
             type1 == Type.Number and type2 == Type.Number):
            return Type.Number
        
        if (type1 == Type.ImplicitPoint and type2 == Type.ImplicitPoint or
            type1 == Type.ImplicitPoint and var.isNumeric()):
            return Type.ImplicitPoint
        
        if (type1 == Type.Vector and var.isNumeric()):
            return Type.Vector
        
        if (type1 == Type.Point and var.isNumeric() or
            self.isVector() and var.isPoint() or
            self.isPoint() and var.isVector()):
            return Type.Point
        
    def canCompare(self, var):
        var1 = self.var
        var2 = var.var
        type1 = self.type
        type2 = var.type
        return (type1 == Type.Enum and type2 == Type.Enum and type(var1) == type(var2) or
                self.isNumeric() and var.isNumeric())
    
        