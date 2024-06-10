from antlr4 import *
from src.XAGL.XAGLParser import XAGLParser
from src.XAGL.XAGLParserVisitor import XAGLParserVisitor
from src.XAGL.AGLClasses import *
import numpy as np
import re
from enum import Enum


class Interpreter(XAGLParserVisitor):
   def __init__(self, vars = {}):
      self.vars = vars
      self.handle_enum()

   def handle_enum(self):
      temp = {}
      for value in self.vars.values():
         if issubclass(type(value), Enum):
            for member in value.__class__:
               temp[member.name.replace("var__agl__", "")] = member

         if issubclass(type(value), Model):
            for attr in value.Dict().values():
               if issubclass(type(attr), Enum):
                  for member in attr.__class__:
                     temp[member.name.replace("var__agl__", "")] = member

      self.vars.update(temp)

   def getVar(self, long_id):
      id_arr = long_id.split(".")
      var = None
      for id in id_arr:
         if '[' in id:
            var = self.array_GetValue(id, self.vars if not var else var.Dict())
         else:
            var = self.vars[id] if not var else var.Dict()[id]
      return var
   
   def array_GetValue(self, array, dict):
      array = re.split(r'\[|\]', array)
      array_name = array[0]
      index = int(array[1])
      var = dict[array_name]
      return var[index]

   def setVar(self, long_id, value):
      id_arr = long_id.split(".")
      if len(id_arr) == 1:
            id = id_arr[0]
            if '[' in id:
               self.array_SetValue(id, value, self.vars)
            else:
               self.vars[id] = value
      else:
         var = self.vars[id_arr[0]]
         for id in id_arr[1:-1]:
            if '[' in id:
               var = self.array_GetValue(id, var.Dict())
            else:
               var = var.Dict()[id]

         id = id_arr[-1]
         if '[' in id:
               self.array_SetValue(id, value, var.Dict())
         else:
            d = var.__dict__
            id = "var__agl__"+id if issubclass(type(value), Enum) else id
            d.update({id: value})

   def array_SetValue(self, array, value, dict):
      array = re.split(r'\[|\]', array)
      array_name = array[0]
      index = int(array[1])
      var = dict[array_name]
      var[index] = value

   def visitProgram(self, ctx:XAGLParser.ProgramContext):
      return self.visitChildren(ctx)

   def visitStat(self, ctx:XAGLParser.StatContext):
      return self.visitChildren(ctx)

   def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
      var = ctx.ID().getText()
      value = self.visit(ctx.simpleStatement())
      self.setVar(var, value)

   def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
      if ctx.assignment():
         value = self.visit(ctx.assignment())
      else:
         value = self.visit(ctx.typeID())
      return value

   def visitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
      for assign in ctx.longAssignment():
         self.visit(assign)

   def visitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
      var = self.visit(ctx.identifier())
      e = self.visit(ctx.assignment())
      id = var if not ctx.varName else ctx.varName+"."+var
      self.setVar(id, e)

   def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
      return self.visit(ctx.expression())

   def visitExprWait(self, ctx:XAGLParser.ExprWaitContext):
      root = self.getVar("root")
      x, y = root.waitClick()
      return np.array((x,y))

   def visitExprString(self, ctx:XAGLParser.ExprStringContext):
      return ctx.STRING().getText()[1:-1]

   def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
      x = float(self.visit(ctx.x))
      y = float(self.visit(ctx.y))
      return np.array((x,y))

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      value = ctx.BOOLEAN().getText()
      return True if value == "True" else False

   def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
      return self.visit(ctx.e)

   def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
      e1 = self.visit(ctx.e1)
      e2 = self.visit(ctx.e2)
      if ctx.GT(): r = e1 > e2
      elif ctx.LT(): r = e1 < e2
      elif ctx.GTE(): r = e1 >= e2
      elif ctx.LTE(): r = e1 <= e2
      elif ctx.EQ(): r = e1 == e2
      elif ctx.NEQ(): r = e1 != e2
      return r

   def visitExprAnd(self, ctx:XAGLParser.ExprAndContext):
      e1 = self.visit(ctx.e1)
      e2 = self.visit(ctx.e2)
      return e1 and e2
   
   def visitExprOr(self, ctx:XAGLParser.ExprOrContext):
      e1 = self.visit(ctx.e1)
      e2 = self.visit(ctx.e2)
      return e1 or e2

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      arr = []
      for expr in ctx.expression():
         arr.append(self.visit(expr)) 
      return arr

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      e1 = self.visit(ctx.e1)
      e2 = self.visit(ctx.e2)
      if ctx.PLUS(): r = e1 + e2
      elif ctx.MINUS(): r = e1 - e2
      elif ctx.MUL(): r = e1 * e2
      elif ctx.DIV(): r = e1 / e2
      return r

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      deg = float(self.visit(ctx.deg))
      length = float(self.visit(ctx.length))
      ang = math.radians(deg)
      x = length * math.cos(ang)
      y = length * math.sin(ang)
      return np.array((x,y))

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      e = self.visit(ctx.expression())
      if ctx.MINUS(): r = -e
      if ctx.NOT(): r = not r
      return r

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      return int(ctx.INT().getText()) if ctx.INT() else float(ctx.FLOAT().getText())

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      id = self.visit(ctx.identifier())
      return self.getVar(id)
   
   def visitExprInput(self, ctx:XAGLParser.ExprInputContext):
      str = ctx.STRING().getText()
      res = input(str)
      return res

   def visitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
      id = self.visit(ctx.identifier())
      var = self.getVar(id)
      delay = 0
      if ctx.AFTER():
         delay = self.visit(ctx.expression())
         if ctx.MS():
            delay = delay/1000         
   
      var.update(delay)

   def visitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
      print(self.visit(ctx.expression()))

   def visitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
      id = self.visit(ctx.identifier())
      var = self.getVar(id)
      var.close()
      self.setVar(id,None)      

   def visitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
      p = self.visit(ctx.expression())
      for id in ctx.identifier():
         var = self.getVar(self.visit(id))
         if ctx.BY():
            var.move_relative(p)
         else:
            var.move_absolute(p)

   def visitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
      angle = self.visit(ctx.expression())
      for id in ctx.identifier():
         var = self.getVar(self.visit(id))
         var.rotate(angle)

   def visitForStatement(self, ctx:XAGLParser.ForStatementContext):
      rnge = self.visit(ctx.number_range())
      id = ctx.ID().getText()
      for i in rnge:
         self.setVar(id, i)
         self.visit(ctx.stat())

   def visitNumber_range(self, ctx:XAGLParser.Number_rangeContext):
      e1 = self.visit(ctx.expression(0))
      e2 = self.visit(ctx.expression(1))
      if ctx.expression(2):
         e3 = self.visit(ctx.expression(2))
         rnge = range(e1,e2,e3)
      else:
         rnge = range(e1,e2)
      return rnge

   def visitWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
      condition = self.visit(ctx.expression())
      while condition:
         self.visit(ctx.stat())
         condition = self.visit(ctx.expression())

   def visitRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
      while True:
         self.visit(ctx.stat())
         condition = self.visit(ctx.expression())
         if condition:
            break

   def visitWithStatement(self, ctx:XAGLParser.WithStatementContext):
      self.visit(ctx.identifier())
      self.visit(ctx.propertiesAssignment())

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      condition = self.visit(ctx.expression())
      if condition:
         self.visit(ctx.stat())
      elif ctx.elseStatement():
         self.visit(ctx.elseStatement())

   def visitElseIfStat(self, ctx:XAGLParser.ElseIfStatContext):
      self.visit(ctx.ifStatement())

   def visitElseStat(self, ctx:XAGLParser.ElseStatContext):
      self.visit(ctx.stat())

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      if ctx.INTEGER():
         default = 0
      elif ctx.STRING_():
         default = ""
      elif ctx.POINT() or ctx.VECTOR():
         default = np.array((0.0, 0.0))
      elif ctx.NUMBER():
         default = 0.0
      elif ctx.BOOLEAN_():
         default = None
      elif ctx.TIME():
         default = None
      elif ctx.ARRAY():
         default = []
      return default

   def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
      id = ctx.ID().getText()

      if ctx.expression():
         for expr in ctx.expression():
            e = self.visit(expr)
            id += f'[{e}]'
         
      if ctx.identifier():
            id += "."+self.visit(ctx.identifier())

      return id

