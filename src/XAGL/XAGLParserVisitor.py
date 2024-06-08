# Generated from XAGLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .XAGLParser import XAGLParser
else:
    from XAGLParser import XAGLParser

# This class defines a complete generic visitor for a parse tree produced by XAGLParser.

class XAGLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XAGLParser#program.
    def visitProgram(self, ctx:XAGLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#stat.
    def visitStat(self, ctx:XAGLParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#instantiation.
    def visitInstantiation(self, ctx:XAGLParser.InstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#simpleStatement.
    def visitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#propertiesAssignment.
    def visitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#longAssignment.
    def visitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#assignment.
    def visitAssignment(self, ctx:XAGLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprWait.
    def visitExprWait(self, ctx:XAGLParser.ExprWaitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprString.
    def visitExprString(self, ctx:XAGLParser.ExprStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprPoint.
    def visitExprPoint(self, ctx:XAGLParser.ExprPointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprBoolean.
    def visitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprParenthesis.
    def visitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprRelational.
    def visitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprAndOr.
    def visitExprAndOr(self, ctx:XAGLParser.ExprAndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprArray.
    def visitExprArray(self, ctx:XAGLParser.ExprArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprDeepCopy.
    def visitExprDeepCopy(self, ctx:XAGLParser.ExprDeepCopyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprAddSubMultDiv.
    def visitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprVector.
    def visitExprVector(self, ctx:XAGLParser.ExprVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprUnary.
    def visitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprNumber.
    def visitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ExprID.
    def visitExprID(self, ctx:XAGLParser.ExprIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#CommandRefresh.
    def visitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#CommandPrint.
    def visitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#CommandClose.
    def visitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#CommandMove.
    def visitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#CommandRotate.
    def visitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#eventTrigger.
    def visitEventTrigger(self, ctx:XAGLParser.EventTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#mouseTrigger.
    def visitMouseTrigger(self, ctx:XAGLParser.MouseTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#forStatement.
    def visitForStatement(self, ctx:XAGLParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#number_range.
    def visitNumber_range(self, ctx:XAGLParser.Number_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#whileStatement.
    def visitWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#repeatStatement.
    def visitRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#withStatement.
    def visitWithStatement(self, ctx:XAGLParser.WithStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#ifStatement.
    def visitIfStatement(self, ctx:XAGLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#typeID.
    def visitTypeID(self, ctx:XAGLParser.TypeIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XAGLParser#identifier.
    def visitIdentifier(self, ctx:XAGLParser.IdentifierContext):
        return self.visitChildren(ctx)



del XAGLParser