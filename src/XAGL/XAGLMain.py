import sys
from antlr4 import *
from XAGLLexer import XAGLLexer
from XAGLParser import XAGLParser
from Interpreter import Interpreter
from AGLClasses import *


def main(argv):
   r = Root()
   v = View(r, 0, 0, height=500, width=500)
   m = Rectangle(r,length=(50,50), fill='white', origin=(0,0))
   vars = {"m":m , "v":v}
   v.update()
   visitor0 = Interpreter(vars)
   input_stream = StdinStream()
   lexer = XAGLLexer(input_stream)
   stream = CommonTokenStream(lexer)
   parser = XAGLParser(stream)
   tree = parser.program()
   if parser.getNumberOfSyntaxErrors() == 0:
      visitor0.visit(tree)
      v.waitClick()

if __name__ == '__main__':
   main(sys.argv)
