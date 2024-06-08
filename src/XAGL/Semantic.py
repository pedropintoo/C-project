from antlr4 import *
from XAGLParser import XAGLParser
from XAGLParserVisitor import XAGLParserVisitor

class Semantic(XAGLParserVisitor):
   def __init__(self):
      self.num_errors = 0

   def visitProgram(self, ctx:XAGLParser.ProgramContext):
      return self.visitChildren(ctx)

   def visitStat(self, ctx:XAGLParser.StatContext):
      return self.visitChildren(ctx)

   def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
      return self.visitChildren(ctx)

   def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
      return self.visitChildren(ctx)

   def visitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
      return self.visitChildren(ctx)

   def visitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
      return self.visitChildren(ctx)

   def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
      return self.visitChildren(ctx)

   def visitExprWait(self, ctx:XAGLParser.ExprWaitContext):
      return self.visitChildren(ctx)

   def visitExprString(self, ctx:XAGLParser.ExprStringContext):
      return self.visitChildren(ctx)

   def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
      return self.visitChildren(ctx)

   def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
      return self.visitChildren(ctx)

   def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
      return self.visitChildren(ctx)

   def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
      return self.visitChildren(ctx)

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      return self.visitChildren(ctx)

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      return self.visitChildren(ctx)

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      return self.visitChildren(ctx)

   def visitExprAnd(self, ctx:XAGLParser.ExprAndContext):
      return self.visitChildren(ctx)

   def visitExprOr(self, ctx:XAGLParser.ExprOrContext):
      return self.visitChildren(ctx)

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      return self.visitChildren(ctx)

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      return self.visitChildren(ctx)

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      return self.visitChildren(ctx)

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

   def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
      return self.visitChildren(ctx)

   def visitElseStatement(self, ctx:XAGLParser.ElseStatementContext):
      return self.visitChildren(ctx)

   def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
      return self.visitChildren(ctx)

   def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
      return self.visitChildren(ctx)

