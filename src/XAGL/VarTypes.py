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
   

class Var():
    def __init__(self, value):
        self.type = value if type(value) == Type else type(value)

    def Dict(self):
        #TODO
        if self.type == View:
            return {"Ox":Type.Number, "Oy":Type.Number}
        elif self.type == Line or self.type == Rectangle or self.type == Ellipse:
            return {"length":Type.Vector, "fill":Type.String, "state":Type.String}
        else:
            return {}

    
        