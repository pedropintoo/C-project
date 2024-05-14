// Generated from AGLParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link AGLParser}.
 */
public interface AGLParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link AGLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(AGLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(AGLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatInstantiation}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatInstantiation(AGLParser.StatInstantiationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatInstantiation}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatInstantiation(AGLParser.StatInstantiationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatBlockStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatBlockStatement(AGLParser.StatBlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatBlockStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatBlockStatement(AGLParser.StatBlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatCommand}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatCommand(AGLParser.StatCommandContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatCommand}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatCommand(AGLParser.StatCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#instantiation}.
	 * @param ctx the parse tree
	 */
	void enterInstantiation(AGLParser.InstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#instantiation}.
	 * @param ctx the parse tree
	 */
	void exitInstantiation(AGLParser.InstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void enterSimpleStatement(AGLParser.SimpleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#simpleStatement}.
	 * @param ctx the parse tree
	 */
	void exitSimpleStatement(AGLParser.SimpleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void enterBlockStatement(AGLParser.BlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#blockStatement}.
	 * @param ctx the parse tree
	 */
	void exitBlockStatement(AGLParser.BlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#propertiesAssignment}.
	 * @param ctx the parse tree
	 */
	void enterPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#propertiesAssignment}.
	 * @param ctx the parse tree
	 */
	void exitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#propertiy}.
	 * @param ctx the parse tree
	 */
	void enterPropertiy(AGLParser.PropertiyContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#propertiy}.
	 * @param ctx the parse tree
	 */
	void exitPropertiy(AGLParser.PropertiyContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(AGLParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(AGLParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprString}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprString(AGLParser.ExprStringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprString}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprString(AGLParser.ExprStringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprWaitFor}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprWaitFor(AGLParser.ExprWaitForContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprWaitFor}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprWaitFor(AGLParser.ExprWaitForContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprPoint}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprPoint(AGLParser.ExprPointContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprPoint}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprPoint(AGLParser.ExprPointContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprNumber}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprNumber(AGLParser.ExprNumberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprNumber}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprNumber(AGLParser.ExprNumberContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprParenthesis}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprParenthesis(AGLParser.ExprParenthesisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprParenthesis}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprParenthesis(AGLParser.ExprParenthesisContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprID}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprID(AGLParser.ExprIDContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprID}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprID(AGLParser.ExprIDContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprAddSubMultDiv}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprAddSubMultDiv}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CommandRefresh}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommandRefresh(AGLParser.CommandRefreshContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CommandRefresh}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommandRefresh(AGLParser.CommandRefreshContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CommandPrint}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommandPrint(AGLParser.CommandPrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CommandPrint}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommandPrint(AGLParser.CommandPrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CommandClose}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommandClose(AGLParser.CommandCloseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CommandClose}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommandClose(AGLParser.CommandCloseContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#waitFor}.
	 * @param ctx the parse tree
	 */
	void enterWaitFor(AGLParser.WaitForContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#waitFor}.
	 * @param ctx the parse tree
	 */
	void exitWaitFor(AGLParser.WaitForContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#eventTrigger}.
	 * @param ctx the parse tree
	 */
	void enterEventTrigger(AGLParser.EventTriggerContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#eventTrigger}.
	 * @param ctx the parse tree
	 */
	void exitEventTrigger(AGLParser.EventTriggerContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#mouseTrigger}.
	 * @param ctx the parse tree
	 */
	void enterMouseTrigger(AGLParser.MouseTriggerContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#mouseTrigger}.
	 * @param ctx the parse tree
	 */
	void exitMouseTrigger(AGLParser.MouseTriggerContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(AGLParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(AGLParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#point}.
	 * @param ctx the parse tree
	 */
	void enterPoint(AGLParser.PointContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#point}.
	 * @param ctx the parse tree
	 */
	void exitPoint(AGLParser.PointContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#typeID}.
	 * @param ctx the parse tree
	 */
	void enterTypeID(AGLParser.TypeIDContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#typeID}.
	 * @param ctx the parse tree
	 */
	void exitTypeID(AGLParser.TypeIDContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(AGLParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(AGLParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#sign}.
	 * @param ctx the parse tree
	 */
	void enterSign(AGLParser.SignContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#sign}.
	 * @param ctx the parse tree
	 */
	void exitSign(AGLParser.SignContext ctx);
}