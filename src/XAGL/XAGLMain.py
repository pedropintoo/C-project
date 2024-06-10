import sys
from antlr4 import *
from XAGLLexer import XAGLLexer
from XAGLParser import XAGLParser
from Interpreter import Interpreter
from Semantic import Semantic
from AGLClasses import *
from VarTypes import *
from enum import Enum, auto


class Pacman(Model):

   def __init__(self, root: Root = None, view: View = None, state="normal", origin=(0,0)):
      super().__init__(root, view, state, origin)
         
      class mouth(Enum):
         Open = auto()
         Close = auto()

      class color(Enum):
         Red = auto()
         Blue = auto()

      # print([mouth(id.value) for id in mouth])
      x = mouth(1)
      y = color(1)
      self.attributes = {"mouth":x, "color":y}

def main():
   root = Root()
   v = View(root, 0, 0, height=500, width=500)
   m = Rectangle(root,length=(50,50), fill='white', origin=(0,0))
   m1 = Pacman()
   m1.add_object(m)
   
   file = "../../examples/new_examples/s0.xagl"
   vars0 = {"m":Var(m1), "v":Var(v)}
   vars1 = {"root":root, "m":m1 , "v":v}
   visitor0 = Semantic(vars0)
   visitor1 = Interpreter(vars1)
   input_stream = FileStream(file)
   lexer = XAGLLexer(input_stream)
   stream = CommonTokenStream(lexer)
   parser = XAGLParser(stream)
   tree = parser.program()
   if parser.getNumberOfSyntaxErrors() == 0:
      visitor0.visit(tree)
      if not visitor0.error:
         visitor1.visit(tree)
if __name__ == '__main__':
   main()
