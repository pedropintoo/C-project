from antlr4 import *
from src.XAGL.XAGLParser import XAGLParser
from src.XAGL.XAGLParserVisitor import XAGLParserVisitor
from src.XAGL.VarTypes import *
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
               temp[member.name.replace("var__agl__", "")] = Var(member)

         if value.type == Type.Model:
            for attr in value.Dict().values():
               if attr.type == Type.Enum:
                  for member in attr.var.__class__:
                     temp[member.name.replace("var__agl__", "")] = Var(member)

      self.vars.update(temp)


   def getVar(self, long_id):
      id_arr = long_id.split(".")
      var = None
      for id in id_arr:
         if '[' in id:
            var = self.array_GetValue(id, self.vars if not var else var.Dict())
         else:
            var = self.vars.get(id) if not var else var.Dict().get(id)
         if not self.error:
            if var is None:
               if id_arr.index(id) > 1:
                  self.SemanticError(f"'{id_arr[id_arr.index(id)-1]}' object has no attribute '{id}'")
               else:
                  self.SemanticError(f"Object '{id}' does not exist")
      return var
   
   def array_GetValue(self, array, dict):
      index = array.index('[')
      array_name = array[:index]
      var = dict.get(array_name)
      if var and var.element:
         return var.element
      self.SemanticError("Object array not assigned")

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
         if not self.error:
            if var not in self.vars:
               self.setVar(var, value)
            else:
               self.SemanticError(f"Object {var} already declared!")

   def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
      if not self.error:
         type = self.visit(ctx.typeID())
         if not self.error:
            if ctx.assignment():
               value = self.visit(ctx.assignment())
               if not self.error:
                  if type.canAssign(value):
                     return type
                  self.SemanticError(f"Can not assign a '{value.type}' object to a '{type.type}' object")
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
         x = self.visit(ctx.x)
         y = self.visit(ctx.y)
         if not self.error:
            if x.isNumeric() and y.isNumeric():
               return Var(Type.ImplicitPoint)

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      if not self.error:
         return Var(Type.Boolean)

   def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
      if not self.error:
         return self.visit(ctx.e)

   def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
      if not self.error:
         e1 = self.visit(ctx.e1)
         e2 = self.visit(ctx.e2)
         if not self.error:
            if e1.canCompare(e2):
               return Var(Type.Boolean)
            else:
               self.SemanticError(f"Can not compare {e1.type} and {e2.type}")

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      if not self.error:
         element_type = self.visit(ctx.expression(0))
         for expr in ctx.expression():
            type = self.visit(expr)
            if not element_type.canAssign(type):
               self.SemanticError(f"Can not assign a '{element_type.type}' object to a '{type.type}' object")
         var = Var(Type.Array)
         var.element = element_type
         return var

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      if not self.error:
         e1 = self.visit(ctx.e1)
         e2 = self.visit(ctx.e2)
         if not self.error:
            
            if ctx.PLUS() or ctx.MINUS():
               r = e1.sum_sub(e2)
               if r:
                  return Var(r) 
               self.SemanticError(f"Error: Operand does not exist beetween {e1.type} and {e2.type}")

            elif ctx.MUL():
               r = e1.mult(e2)
               if r:
                  return Var(r)
               self.SemanticError(f"Error: Operand does not exist beetween {e1.type} and {e2.type}")
               
            elif ctx.DIV():
               if ctx.e2.getText() != '0':
                  r = e1.div(e2)
                  if r:
                     return Var(r)
                  self.SemanticError(f"Error: Operand does not exist beetween {e1.type} and {e2.type}")
               else:
                  self.SemanticError("Error: Can not divide by")

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      if not self.error:
         deg = self.visit(ctx.deg)
         length = self.visit(ctx.length)
         if not self.error:
            if deg.isNumeric() and length.isNumeric():
               return Var(Type.Vector)

   def visitExprAnd(self, ctx:XAGLParser.ExprAndContext):
      if not self.error:
         e1 = self.visit(ctx.e1)
         e2 = self.visit(ctx.e2)
         if not self.error:
            if e1.isBoolean() and e2.isBoolean():
               return Var(Type.Boolean)

   def visitExprOr(self, ctx:XAGLParser.ExprOrContext):
      if not self.error:
         e1 = self.visit(ctx.e1)
         e2 = self.visit(ctx.e2)
         if not self.error:
            if e1.isBoolean() and e2.isBoolean():
               return Var(Type.Boolean)

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      if not self.error:
         e = self.visit(ctx.expression())
         if not self.error:
            if ctx.MINUS() or ctx.PLUS():
               if e.isNumeric():
                  return e
               else:
                  self.SemanticError(f"Invalid Operand for {e.type}")
               
            elif ctx.NOT():
               if e.type == Type.Boolean:
                  return e
               else:
                  self.SemanticError(f"Invalid Operand for {e.type}")

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      if not self.error:
         return Var(Type.Integer) if ctx.INT() else Var(Type.Number)

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      if not self.error:
         id = self.visit(ctx.identifier())
         var = self.getVar(id)
         if not self.error:
            if var:
               return Var(var) if var.__class__ != Var else var
            self.SemanticError(f"Object '{id}' does not exist")
   
   def visitExprInput(self, ctx:XAGLParser.ExprInputContext):
      if not self.error:
         return Var(Type.String)
   
   def visitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
      if not self.error:
         id = self.visit(ctx.identifier())
         if not self.error:
            var = self.getVar(id)
            if not self.error:
               if var.isView():
                  if ctx.AFTER():
                     delay = self.visit(ctx.expression())
                     if not self.error:
                        if not delay.isDelay():
                           self.SemanticError("Error: invalid expression type in refresh command (must be a number, integer or time type!)")
               else:
                  self.SemanticError("Error: invalid type in refresh command (must be a view type!)")

   def visitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
      if not self.error:
         self.visit(ctx.expression())

   def visitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
      if not self.error:
         id = self.visit(ctx.identifier())
         if not self.error:
            var = self.getVar(id)
            if not self.error:
               if not var.isView():
                  self.SemanticError("Error: invalid type in close command (must be a view type!)")

   def visitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
      if not self.error:
         for id in ctx.identifier():
            var = self.visit(id)
            if not self.error:
               type = self.getVar(var)
               if not self.error:
                  if not type.isModel():
                     self.SemanticError("Error: invalid type in move command (must be a model or view type!)")
         if not self.error:
            e = self.visit(ctx.expression())
            if not self.error:
               if ctx.BY():
                  if not e.isVector():
                     self.SemanticError("Error: invalid expression type in move command (must be a vector!)")
               elif ctx.TO():
                  if not e.isPoint():
                     self.SemanticError("Error: invalid expression type in move command (must be a point!)")


   def visitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
      if not self.error:
         for id in ctx.identifier():
            var = self.visit(id)
            if not self.error:
               type = self.getVar(var)
               if not self.error:
                  if not type.isModel():
                     self.SemanticError("Error: invalid type in move command (must be a model or view type!)")
         if not self.error:
            e = self.visit(ctx.expression())
            if not self.error:
               if not e.isNumeric():
                  self.SemanticError("Error: invalid expression type in rotate command (must be a number!)")

   def visitForStatement(self, ctx:XAGLParser.ForStatementContext):
      if not self.error:
         id = ctx.ID().getText()
         if id in self.vars:
            self.SemanticError(f"Object {id} already declared!")
         else:
            self.visit(ctx.number_range())
            if not self.error:
               self.visit(ctx.stat())

   def visitNumber_range(self, ctx:XAGLParser.Number_rangeContext):
      if not self.error:
         for expr in ctx.expression():
            e = self.visit(expr)
            if e.type != Type.Integer:
               self.SemanticError("Number_range must have Integer Object")
               break

   def visitWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
      if not self.error:
         condition =  self.visit(ctx.expression())
         if condition.isBoolean():
            self.visit(ctx.stat)
         else:
            self.SemanticError("Error: The expression in the while statement has to be a boolean")

   def visitRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
      if not self.error:
         condition =  self.visit(ctx.expression())
         self.visit(ctx.stat)
         if not self.error:
            if not condition.isBoolean():
               self.SemanticError("Error: The expression in the repeat statement has to be a boolean")

   def visitWithStatement(self, ctx:XAGLParser.WithStatementContext):
      if not self.error:
         id = self.visit(ctx.identifier())
         if not self.error:
            if self.getVar(id):
               self.visit(ctx.propertiesAssignment())

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      if not self.error:
         condition =  self.visit(ctx.expression())
         if condition.isBoolean():
            self.visit(ctx.stat())
         else:
            self.SemanticError("Error: The expression in the while statement has to be a boolean")
         if not self.error:
            if ctx.elseStatement():
               self.visit(ctx.elseStatement())
   
   def visitElseIfStat(self, ctx:XAGLParser.ElseIfStatContext):
      if not self.error:
         self.visit(ctx.ifStatement())

   def visitElseStat(self, ctx:XAGLParser.ElseStatContext):
      if not self.error:
         self.visit(ctx.stat())

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      if not self.error:
         if ctx.INTEGER():
            type = Var(Type.Integer)
         elif ctx.STRING_():
            type = Var(Type.String)
         elif ctx.POINT():
            type = Var(Type.Point)
         elif ctx.VECTOR():
            type = Var(Type.Vector)
         elif ctx.NUMBER():
            type = Var(Type.Number)
         elif ctx.BOOLEAN_():
            type = Var(Type.Boolean)
         elif ctx.TIME():
            type = Var(Type.Time)
         elif ctx.ARRAY():
            type = Var(Type.Array)
            type.element = self.visit(ctx.typeID())
         return type

   def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
      if not self.error:
         id = ctx.ID().getText()

         if ctx.expression():
            for expr in ctx.expression():
               e = self.visit(expr)
               if e.type == Type.Integer:
                  id += f'[]'
               else:
                  self.SemanticError("Index must be Integer")
            
         if ctx.identifier():
               id += "."+self.visit(ctx.identifier())

         return id

