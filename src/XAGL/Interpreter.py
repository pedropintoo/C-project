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
            self.vars[id] = value
      else:
         var = self.vars[id_arr[0]]
         for id in id_arr[1:-1]:
            var = var.Dict()[id]
         var.Dict()[id_arr[-1]] = value

   def visitProgram(self, ctx:XAGLParser.ProgramContext):
      return self.visitChildren(ctx)

   def visitStatInstantiation(self, ctx:XAGLParser.StatInstantiationContext):
      return self.visitChildren(ctx)

   def visitStatModelInstantiation(self, ctx:XAGLParser.StatModelInstantiationContext):
      return self.visitChildren(ctx)

   def visitStatBlockStatement(self, ctx:XAGLParser.StatBlockStatementContext):
      return self.visitChildren(ctx)

   def visitStatLongAssignment(self, ctx:XAGLParser.StatLongAssignmentContext):
      return self.visitChildren(ctx)

   def visitStatWithStatement(self, ctx:XAGLParser.StatWithStatementContext):
      return self.visitChildren(ctx)

   def visitRepForStatement(self, ctx:XAGLParser.RepForStatementContext):
      return self.visitChildren(ctx)

   def visitRepWhileStatement(self, ctx:XAGLParser.RepWhileStatementContext):
      return self.visitChildren(ctx)

   def visitRepRepeatStatement(self, ctx:XAGLParser.RepRepeatStatementContext):
      return self.visitChildren(ctx)

   def visitStatIfStatement(self, ctx:XAGLParser.StatIfStatementContext):
      return self.visitChildren(ctx)

   def visitStatCommand(self, ctx:XAGLParser.StatCommandContext):
      return self.visitChildren(ctx)

   def visitStatBlock(self, ctx:XAGLParser.StatBlockContext):
      return self.visitChildren(ctx)

   def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
      return self.visitChildren(ctx)

   def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
      return self.visitChildren(ctx)

   def visitBlockStatement(self, ctx:XAGLParser.BlockStatementContext):
      return self.visitChildren(ctx)

   def visitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
      return self.visitChildren(ctx)

   def visitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
      id = self.visit(ctx.identifier())
      e = self.visit(ctx.assignment())
      self.setVar(id, e)

   def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
      return self.visit(ctx.expression())

   def visitIn_assignment(self, ctx:XAGLParser.In_assignmentContext):
      return self.visitChildren(ctx)

   def visitExprWait(self, ctx:XAGLParser.ExprWaitContext):
      return self.visitChildren(ctx)

   def visitExprString(self, ctx:XAGLParser.ExprStringContext):
      return ctx.STRING().getText()

   def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
      x = float(self.visit(ctx.x))
      y = float(self.visit(ctx.y))
      return (x,y)

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      return self.visitChildren(ctx)

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
      return self.visitChildren(ctx)

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
      return self.visitChildren(ctx)

   def visitPlayStatement(self, ctx:XAGLParser.PlayStatementContext):
      return self.visitChildren(ctx)

   def visitModelInstantiation(self, ctx:XAGLParser.ModelInstantiationContext):
      return self.visitChildren(ctx)

   def visitModelStatInstantiation(self, ctx:XAGLParser.ModelStatInstantiationContext):
      return self.visitChildren(ctx)

   def visitModelStatBlockStatement(self, ctx:XAGLParser.ModelStatBlockStatementContext):
      return self.visitChildren(ctx)

   def visitModelStatLongAssignment(self, ctx:XAGLParser.ModelStatLongAssignmentContext):
      return self.visitChildren(ctx)

   def visitModelStatAction(self, ctx:XAGLParser.ModelStatActionContext):
      return self.visitChildren(ctx)

   def visitAction(self, ctx:XAGLParser.ActionContext):
      return self.visitChildren(ctx)

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      return self.visitChildren(ctx)

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      return self.visitChildren(ctx)

   def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
      if ctx.ID():
         id = ctx.ID().getText()
      if ctx.identifier():
         id += "."+self.visit(ctx.identifier())
      return id

