# Generated from XAGLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .XAGLParser import XAGLParser
else:
    from XAGLParser import XAGLParser

# This class defines a complete listener for a parse tree produced by XAGLParser.
class XAGLParserListener(ParseTreeListener):

    # Enter a parse tree produced by XAGLParser#program.
    def enterProgram(self, ctx:XAGLParser.ProgramContext):
        pass

    # Exit a parse tree produced by XAGLParser#program.
    def exitProgram(self, ctx:XAGLParser.ProgramContext):
        pass


    # Enter a parse tree produced by XAGLParser#stat.
    def enterStat(self, ctx:XAGLParser.StatContext):
        pass

    # Exit a parse tree produced by XAGLParser#stat.
    def exitStat(self, ctx:XAGLParser.StatContext):
        pass


    # Enter a parse tree produced by XAGLParser#instantiation.
    def enterInstantiation(self, ctx:XAGLParser.InstantiationContext):
        pass

    # Exit a parse tree produced by XAGLParser#instantiation.
    def exitInstantiation(self, ctx:XAGLParser.InstantiationContext):
        pass


    # Enter a parse tree produced by XAGLParser#simpleStatement.
    def enterSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by XAGLParser#simpleStatement.
    def exitSimpleStatement(self, ctx:XAGLParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by XAGLParser#propertiesAssignment.
    def enterPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
        pass

    # Exit a parse tree produced by XAGLParser#propertiesAssignment.
    def exitPropertiesAssignment(self, ctx:XAGLParser.PropertiesAssignmentContext):
        pass


    # Enter a parse tree produced by XAGLParser#longAssignment.
    def enterLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
        pass

    # Exit a parse tree produced by XAGLParser#longAssignment.
    def exitLongAssignment(self, ctx:XAGLParser.LongAssignmentContext):
        pass


    # Enter a parse tree produced by XAGLParser#assignment.
    def enterAssignment(self, ctx:XAGLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by XAGLParser#assignment.
    def exitAssignment(self, ctx:XAGLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprWait.
    def enterExprWait(self, ctx:XAGLParser.ExprWaitContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprWait.
    def exitExprWait(self, ctx:XAGLParser.ExprWaitContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprString.
    def enterExprString(self, ctx:XAGLParser.ExprStringContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprString.
    def exitExprString(self, ctx:XAGLParser.ExprStringContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprPoint.
    def enterExprPoint(self, ctx:XAGLParser.ExprPointContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprPoint.
    def exitExprPoint(self, ctx:XAGLParser.ExprPointContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprBoolean.
    def enterExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprBoolean.
    def exitExprBoolean(self, ctx:XAGLParser.ExprBooleanContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprParenthesis.
    def enterExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprParenthesis.
    def exitExprParenthesis(self, ctx:XAGLParser.ExprParenthesisContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprRelational.
    def enterExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprRelational.
    def exitExprRelational(self, ctx:XAGLParser.ExprRelationalContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprAndOr.
    def enterExprAndOr(self, ctx:XAGLParser.ExprAndOrContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprAndOr.
    def exitExprAndOr(self, ctx:XAGLParser.ExprAndOrContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprArray.
    def enterExprArray(self, ctx:XAGLParser.ExprArrayContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprArray.
    def exitExprArray(self, ctx:XAGLParser.ExprArrayContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprDeepCopy.
    def enterExprDeepCopy(self, ctx:XAGLParser.ExprDeepCopyContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprDeepCopy.
    def exitExprDeepCopy(self, ctx:XAGLParser.ExprDeepCopyContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprAddSubMultDiv.
    def enterExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprAddSubMultDiv.
    def exitExprAddSubMultDiv(self, ctx:XAGLParser.ExprAddSubMultDivContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprVector.
    def enterExprVector(self, ctx:XAGLParser.ExprVectorContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprVector.
    def exitExprVector(self, ctx:XAGLParser.ExprVectorContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprUnary.
    def enterExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprUnary.
    def exitExprUnary(self, ctx:XAGLParser.ExprUnaryContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprNumber.
    def enterExprNumber(self, ctx:XAGLParser.ExprNumberContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprNumber.
    def exitExprNumber(self, ctx:XAGLParser.ExprNumberContext):
        pass


    # Enter a parse tree produced by XAGLParser#ExprID.
    def enterExprID(self, ctx:XAGLParser.ExprIDContext):
        pass

    # Exit a parse tree produced by XAGLParser#ExprID.
    def exitExprID(self, ctx:XAGLParser.ExprIDContext):
        pass


    # Enter a parse tree produced by XAGLParser#CommandRefresh.
    def enterCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
        pass

    # Exit a parse tree produced by XAGLParser#CommandRefresh.
    def exitCommandRefresh(self, ctx:XAGLParser.CommandRefreshContext):
        pass


    # Enter a parse tree produced by XAGLParser#CommandPrint.
    def enterCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
        pass

    # Exit a parse tree produced by XAGLParser#CommandPrint.
    def exitCommandPrint(self, ctx:XAGLParser.CommandPrintContext):
        pass


    # Enter a parse tree produced by XAGLParser#CommandClose.
    def enterCommandClose(self, ctx:XAGLParser.CommandCloseContext):
        pass

    # Exit a parse tree produced by XAGLParser#CommandClose.
    def exitCommandClose(self, ctx:XAGLParser.CommandCloseContext):
        pass


    # Enter a parse tree produced by XAGLParser#CommandMove.
    def enterCommandMove(self, ctx:XAGLParser.CommandMoveContext):
        pass

    # Exit a parse tree produced by XAGLParser#CommandMove.
    def exitCommandMove(self, ctx:XAGLParser.CommandMoveContext):
        pass


    # Enter a parse tree produced by XAGLParser#CommandRotate.
    def enterCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
        pass

    # Exit a parse tree produced by XAGLParser#CommandRotate.
    def exitCommandRotate(self, ctx:XAGLParser.CommandRotateContext):
        pass


    # Enter a parse tree produced by XAGLParser#eventTrigger.
    def enterEventTrigger(self, ctx:XAGLParser.EventTriggerContext):
        pass

    # Exit a parse tree produced by XAGLParser#eventTrigger.
    def exitEventTrigger(self, ctx:XAGLParser.EventTriggerContext):
        pass


    # Enter a parse tree produced by XAGLParser#mouseTrigger.
    def enterMouseTrigger(self, ctx:XAGLParser.MouseTriggerContext):
        pass

    # Exit a parse tree produced by XAGLParser#mouseTrigger.
    def exitMouseTrigger(self, ctx:XAGLParser.MouseTriggerContext):
        pass


    # Enter a parse tree produced by XAGLParser#forStatement.
    def enterForStatement(self, ctx:XAGLParser.ForStatementContext):
        pass

    # Exit a parse tree produced by XAGLParser#forStatement.
    def exitForStatement(self, ctx:XAGLParser.ForStatementContext):
        pass


    # Enter a parse tree produced by XAGLParser#number_range.
    def enterNumber_range(self, ctx:XAGLParser.Number_rangeContext):
        pass

    # Exit a parse tree produced by XAGLParser#number_range.
    def exitNumber_range(self, ctx:XAGLParser.Number_rangeContext):
        pass


    # Enter a parse tree produced by XAGLParser#whileStatement.
    def enterWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by XAGLParser#whileStatement.
    def exitWhileStatement(self, ctx:XAGLParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by XAGLParser#repeatStatement.
    def enterRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by XAGLParser#repeatStatement.
    def exitRepeatStatement(self, ctx:XAGLParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by XAGLParser#withStatement.
    def enterWithStatement(self, ctx:XAGLParser.WithStatementContext):
        pass

    # Exit a parse tree produced by XAGLParser#withStatement.
    def exitWithStatement(self, ctx:XAGLParser.WithStatementContext):
        pass


    # Enter a parse tree produced by XAGLParser#ifStatement.
    def enterIfStatement(self, ctx:XAGLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by XAGLParser#ifStatement.
    def exitIfStatement(self, ctx:XAGLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by XAGLParser#typeID.
    def enterTypeID(self, ctx:XAGLParser.TypeIDContext):
        pass

    # Exit a parse tree produced by XAGLParser#typeID.
    def exitTypeID(self, ctx:XAGLParser.TypeIDContext):
        pass


    # Enter a parse tree produced by XAGLParser#identifier.
    def enterIdentifier(self, ctx:XAGLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by XAGLParser#identifier.
    def exitIdentifier(self, ctx:XAGLParser.IdentifierContext):
        pass



del XAGLParser