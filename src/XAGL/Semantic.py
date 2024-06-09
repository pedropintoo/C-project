from antlr4 import *
from XAGLParser import XAGLParser
from XAGLParserVisitor import XAGLParserVisitor
from VarTypes import *
import re
import sys

class Semantic(XAGLParserVisitor):
   def __init__(self, vars = {}):
      self.vars = vars
      self.error = False
      self.handle_enum()

   def handle_enum(self):
      temp = {}
      for value in self.vars.values():
         if value.type == Type.Enum:
            for member in value.var.__class__:
               temp[member.name] = Var(member)

         if value.type == Type.Model:
            for attr in value.Dict().values():
               if attr.type == Type.Enum:
                  for member in attr.var.__class__:
                     temp[member.name] = Var(member)

      self.vars.update(temp)


   def getVar(self, long_id):
      id_arr = long_id.split(".")
      var = None
      for id in id_arr:
         if '[' in id:
            var = self.array_GetValue(id, self.vars if not var else var.Dict())
         else:
            var = self.vars.get(id) if not var else var.Dict().get(id)

         if var is None:
            if id_arr.index(id) > 1:
               self.SemanticError(f"'{id_arr[id_arr.index(id)-1]}' object has no attribute '{id}'")
            else:
               self.SemanticError(f"Object '{id}' does not exist")
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
      self.error = True
      print(message)
      
   def visitProgram(self, ctx:XAGLParser.ProgramContext):
      return self.visitChildren(ctx)

   def visitStat(self, ctx:XAGLParser.StatContext):
      return self.visitChildren(ctx)

   def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
      if not self.error:
         var = ctx.ID().getText()
         value = self.visit(ctx.simpleStatement())
         if var not in self.vars:
            self.setVar(var, value)
         else:
            self.SemanticError(f"Object '{var}' already instantiated")

   def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
      if not self.error:
         type = self.visit(ctx.typeID())
         if ctx.assignment():
            value = self.visit(ctx.assignment())
            if type.canAssign(value):
               return type
            self.SemanticError(f"Can not assign a '{value}' object to a '{type}' object")
         else:
            return type

   def visitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
      if not self.error:
         for assign in ctx.longAssignment():
            self.visit(assign)

   def visitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
      if not self.error:
         var = self.visit(ctx.identifier())
         value = self.visit(ctx.assignment())
         id = var if not ctx.varName else ctx.varName+"."+var
         type = self.getVar(id)
         if not self.error:
            type = Var(type) if type.__class__ != Var else type
            if type.canAssign(value):
               self.setVar(id, value)
            else:
               self.SemanticError(f"Can not assign a '{value.type}' object to a '{type.type}' object")

   def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
      if not self.error:
         return self.visit(ctx.expression())

   def visitExprWait(self, ctx:XAGLParser.ExprWaitContext):
      if not self.error:
         return Var(Type.Point)

   def visitExprString(self, ctx:XAGLParser.ExprStringContext):
      if not self.error:
         return Var(Type.String)

   def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
      if not self.error:
         return Var(Type.ImplicitPoint)

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      if not self.error:
         return Var(Type.Boolean)

   def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
      if not self.error:
         return self.visit(ctx.e)

   def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      if not self.error:
         return Var(Type.Array)

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      if not self.error:
         return Var(Type.Vector)

   def visitExprAnd(self, ctx:XAGLParser.ExprAndContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitExprOr(self, ctx:XAGLParser.ExprOrContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      if not self.error:
         return Var(Type.Integer) if ctx.INT() else Var(Type.Number)

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      if not self.error:
         id = self.visit(ctx.identifier())
         var = self.getVar(id)
         if not self.error:
            if var:
               return var
            self.SemanticError(f"Object '{id}' does not exist")
   
   def visitExprInput(self, ctx:XAGLParser.ExprInputContext):
      if not self.error:
         return Var(Type.String)
   
   def visitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
      return self.visitChildren(ctx)

   def visitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitForStatement(self, ctx:XAGLParser.ForStatementContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitNumber_range(self, ctx:XAGLParser.Number_rangeContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitWithStatement(self, ctx:XAGLParser.WithStatementContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      if not self.error:
         return self.visitChildren(ctx)
   
   def visitElseIfStat(self, ctx:XAGLParser.ElseIfStatContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitElseStat(self, ctx:XAGLParser.ElseStatContext):
      if not self.error:
         return self.visitChildren(ctx)

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      if not self.error:
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
         return Var(type)

   def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
      if not self.error:
         id = ctx.ID().getText()

         if ctx.expression():
            for expr in ctx.expression():
               e = self.visit(expr)
               id += f'[{e}]'
            
         if ctx.identifier():
               id += "."+self.visit(ctx.identifier())

         return id

