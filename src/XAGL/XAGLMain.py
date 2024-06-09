import sys
from antlr4 import *
from XAGLLexer import XAGLLexer
from XAGLParser import XAGLParser
from Interpreter import Interpreter
from Semantic import Semantic
from AGLClasses import *


def main():
   root = Root()
   v = View(root, 0, 0, height=500, width=500)
   m = Rectangle(root,length=(50,50), fill='white', origin=(0,0))
   vars = {"root":root, "m":m , "v":v}
   visitor0 = Semantic(vars)
   visitor1 = Interpreter(vars)
   file = "../../examples/new_examples/s0.xagl"
   input_stream = FileStream(file)
   lexer = XAGLLexer(input_stream)
   stream = CommonTokenStream(lexer)
   parser = XAGLParser(stream)
   tree = parser.program()
   if parser.getNumberOfSyntaxErrors() == 0:
      visitor0.visit(tree)
      if not visitor0.num_errors:
         visitor1.visit(tree)

if __name__ == '__main__':
   main()
