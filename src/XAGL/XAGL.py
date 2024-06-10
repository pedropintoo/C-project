from antlr4 import *
from src.XAGL.XAGLParserParser import XAGLParserParser
from src.XAGL.XAGLParserVisitor import XAGLParserVisitor

class XAGL(XAGLParserVisitor):
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
      return self.visitChildren(ctx)

   def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
      return self.visitChildren(ctx)

   def visitIn_assignment(self, ctx:XAGLParser.In_assignmentContext):
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

   def visitExprAndOr(self, ctx:XAGLParser.ExprAndOrContext):
      return self.visitChildren(ctx)

   def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
      return self.visitChildren(ctx)

   def visitExprDeepCopy(self, ctx:XAGLParser.ExprDeepCopyContext):
      return self.visitChildren(ctx)

   def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
      return self.visitChildren(ctx)

   def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
      return self.visitChildren(ctx)

   def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
      return self.visitChildren(ctx)

   def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
      return self.visitChildren(ctx)

   def visitExprID(self, ctx:XAGLParser.ExprIDContext):
      return self.visitChildren(ctx)

   def visitPoint(self, ctx:XAGLParser.PointContext):
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
      return self.visitChildren(ctx)

