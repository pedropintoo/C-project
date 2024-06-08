from antlr4 import *
from XAGLParser import XAGLParser
from XAGLParserVisitor import XAGLParserVisitor
from AGLClasses import *

class Interpreter(XAGLParserVisitor):
   def __init__(self, vars = {}):
      self.vars = vars

   def getVar(self, long_id):
      id_arr = long_id.split(".")
      var = None
      for id in id_arr:
         var = self.vars[id] if not var else var.Dict()[id]
      return var
   
   def setVar(self, long_id, value):
      id_arr = long_id.split(".")
      if len(id_arr) == 1:
            self.vars[id_arr[0]] = value
      else:
         var = self.vars[id_arr[0]]
         for id in id_arr[1:-1]:
            var = var.Dict()[id]
         var.Dict()[id_arr[-1]] = value

   def visitProgram(self, ctx:XAGLParser.ProgramContext):
      return self.visitChildren(ctx)

   def visitStat(self, ctx:XAGLParser.StatContext):
      return self.visitChildren(ctx)

   def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
      var = ctx.ID().getText()
      value = self.visit(ctx.simpleStatement())
      self.vars[var] = value

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
      return self.visitChildren(ctx)

   def visitExprString(self, ctx:XAGLParser.ExprStringContext):
      return ctx.STRING().getText()

   def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
      x = float(self.visit(ctx.x))
      y = float(self.visit(ctx.y))
      return (x,y)

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      value = ctx.BOOLEAN().getText()
      print(value)
      return True if value == "True" else False

   def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
      return self.visit(ctx.e)

   def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
      return self.visitChildren(ctx)

   def visitExprAndOr(self, ctx:XAGLParser.ExprAndOrContext):
      return self.visitChildren(ctx)

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      return self.visitChildren(ctx)

   def visitExprDeepCopy(self, ctx:XAGLParser.ExprDeepCopyContext):
      return self.visitChildren(ctx)

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      e1 = self.visit(ctx.e1)
      e2 = self.visit(ctx.e2)
      op = ctx.op
      if op == '+': r = e1 + e2
      elif op == '-': r = e1 - e2
      elif op == '*': r = e1 * e2
      elif op == '/': r = e1 / e2
      return r

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      return self.visitChildren(ctx)

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      return self.visitChildren(ctx)

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      return int(ctx.INT().getText()) if ctx.INT() else float(ctx.FLOAT().getText())

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      id = self.visit(ctx.identifier())
      print(id)
      return self.getVar(id)

   def visitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
      id = self.visit(ctx.identifier())
      var = self.getVar(id)
      delay = 0
      if ctx.AFTER():
         delay = self.visit(ctx.expression())
         if ctx.MS():
            delay = delay/1000         
   
      var.update(delay)
      return self.visitChildren(ctx)

   def visitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
      print(self.visit(ctx.expression()))

   def visitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
      return self.visitChildren(ctx)

   def visitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
      p = self.visit(ctx.expression())
      for id in ctx.identifier():
         var = self.getVar(self.visit(id))
         if ctx.BY():
            var.move_relative(p)
         else:
            var.move_absolute(p)

   def visitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
      return self.visitChildren(ctx)

   def visitEventTrigger(self, ctx:XAGLParser.EventTriggerContext):
      return self.visitChildren(ctx)

   def visitMouseTrigger(self, ctx:XAGLParser.MouseTriggerContext):
      return self.visitChildren(ctx)

   def visitForStatement(self, ctx:XAGLParser.ForStatementContext):
      return self.visitChildren(ctx)

   def visitNumber_range(self, ctx:XAGLParser.Number_rangeContext):
      return self.visitChildren(ctx)

   def visitWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
      return self.visitChildren(ctx)

   def visitRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
      return self.visitChildren(ctx)

   def visitWithStatement(self, ctx:XAGLParser.WithStatementContext):
      self.visit(ctx.identifier())
      self.visit(ctx.propertiesAssignment())

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      return self.visitChildren(ctx)

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      if ctx.INTEGER():
         default = 0
      elif ctx.STRING_():
         default = ""
      elif ctx.POINT() or ctx.VECTOR():
         default = (0.0, 0.0)
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
      if ctx.ID():
         id = ctx.ID().getText()
      if ctx.identifier():
         id += "."+self.visit(ctx.identifier())
      return id

