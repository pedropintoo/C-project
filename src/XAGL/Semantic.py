from antlr4 import *
from XAGLParser import XAGLParser
from XAGLParserVisitor import XAGLParserVisitor
from VarTypes import *
import re

class Semantic(XAGLParserVisitor):
   def __init__(self, vars):
      self.vars = vars
      self.num_errors = 0

   def getVar(self, long_id):
      id_arr = long_id.split(".")
      var = None
      for id in id_arr:
         if '[' in id:
            var = self.array_GetValue(id, self.vars if not var else var.Dict())
         else:
            var = self.vars.get(id) if not var else var.Dict().get(id)

         if var is None:
            self.SemanticError(f"'{id_arr[id_arr.index(id)-1]}' object has no attribute '{id}'")
      return var
   
   def array_GetValue(self, array, dict):
      array = re.split(r'\[|\]', array)
      array_name = array[0]
      index = int(array[1])
      var = dict.get(array_name)
      return var[index] if var else None

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
            var.Dict()[id] = value

   def array_SetValue(self, array, value, dict):
      array = re.split(r'\[|\]', array)
      array_name = array[0]
      index = int(array[1])
      var = dict[array_name]
      var[index] = value

   def SemanticError(self, message):
      self.num_errors = self.num_errors+1
      print(message)

   def compatible(self, type1, type2):
      return ( type1 == type2 or
               type1 == Type.Number and type2 == Type.Integer or
               type1 == Type.Point and type2 == Type.ImplicitPoint or 
               type1 == Type.Vector and type2 == Type.ImplicitPoint
            )

   def visitProgram(self, ctx:XAGLParser.ProgramContext):
      return self.visitChildren(ctx)

   def visitStat(self, ctx:XAGLParser.StatContext):
      return self.visitChildren(ctx)

   def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
      var = ctx.ID().getText()
      value = self.visit(ctx.simpleStatement())
      if var not in self.vars:
         self.setVar(var, Var(value))
      else:
         self.SemanticError(f"Object '{var}' already instantiated")

   def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
      type = self.visit(ctx.typeID())
      if ctx.assignment():
         value = self.visit(ctx.assignment())
         if self.compatible(type, value):
            return type
         self.SemanticError(f"Can not assign a '{value}' object to a '{type}' object")
      else:
         return type

   def visitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
      for assign in ctx.longAssignment():
         self.visit(assign)

   def visitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
      var = self.visit(ctx.identifier())
      value = self.visit(ctx.assignment())
      id = var if not ctx.varName else ctx.varName+"."+var
      type = self.getVar(id)
      if type and self.compatible(type, value):
         self.setVar(id, Var(value))
      else:
         self.SemanticError(f"Can not assign a '{value}' object to a '{type}' object")

   def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
      return self.visitChildren(ctx)

   def visitExprWait(self, ctx:XAGLParser.ExprWaitContext):
      return Type.Point

   def visitExprString(self, ctx:XAGLParser.ExprStringContext):
      return Type.String

   def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
      return Type.ImplicitPoint

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      return Type.Boolean

   def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
      return self.visit(ctx.e)

   def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
      return self.visitChildren(ctx)

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      return Type.Array

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      return self.visitChildren(ctx)

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      return Type.Vector

   def visitExprAnd(self, ctx:XAGLParser.ExprAndContext):
      return self.visitChildren(ctx)

   def visitExprOr(self, ctx:XAGLParser.ExprOrContext):
      return self.visitChildren(ctx)

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      return self.visitChildren(ctx)

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      return Type.Integer if ctx.INT() else Type.Number

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      id = self.visit(ctx.identifier())
      var = self.getVar(id)
      if var:
         return var
      self.SemanticError(f"Object '{id}' does not exist")
   
   def visitExprInput(self, ctx:XAGLParser.ExprInputContext):
      return Type.String
   
   def visitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
      return self.visitChildren(ctx)

   def visitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
      return self.visitChildren(ctx)

   def visitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
      return self.visitChildren(ctx)

   def visitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
      return self.visitChildren(ctx)

   def visitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
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
      return self.visitChildren(ctx)

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      return self.visitChildren(ctx)
   
   def visitElseIfStat(self, ctx:XAGLParser.ElseIfStatContext):
      return self.visitChildren(ctx)

   def visitElseStat(self, ctx:XAGLParser.ElseStatContext):
      return self.visitChildren(ctx)

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      if ctx.INTEGER():
         type = Type.Integer
      elif ctx.STRING_():
         type = Type.String
      elif ctx.POINT():
         type = Type.Point
      elif ctx.VECTOR():
         type = Type.Vector
      elif ctx.NUMBER():
         type = Type.Number
      elif ctx.BOOLEAN_():
         type = Type.Boolean
      elif ctx.TIME():
         type = Type.Time
      elif ctx.ARRAY():
         type = Type.Array
      return type

   def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
      id = ctx.ID().getText()

      if ctx.expression():
         for expr in ctx.expression():
            e = self.visit(expr)
            id += f'[{e}]'
         
      if ctx.identifier():
            id += "."+self.visit(ctx.identifier())

      return id

