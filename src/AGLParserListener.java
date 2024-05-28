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
	 * Enter a parse tree produced by the {@code StatModelInstantiation}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatModelInstantiation(AGLParser.StatModelInstantiationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatModelInstantiation}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatModelInstantiation(AGLParser.StatModelInstantiationContext ctx);
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
	 * Enter a parse tree produced by the {@code StatLongAssignment}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatLongAssignment(AGLParser.StatLongAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatLongAssignment}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatLongAssignment(AGLParser.StatLongAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatWithStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatWithStatement(AGLParser.StatWithStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatWithStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatWithStatement(AGLParser.StatWithStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatPlayStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatPlayStatement(AGLParser.StatPlayStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatPlayStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatPlayStatement(AGLParser.StatPlayStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatRepetitiveStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatRepetitiveStatement(AGLParser.StatRepetitiveStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatRepetitiveStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatRepetitiveStatement(AGLParser.StatRepetitiveStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatIfStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatIfStatement(AGLParser.StatIfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatIfStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatIfStatement(AGLParser.StatIfStatementContext ctx);
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
	 * Enter a parse tree produced by the {@code StatBlock}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatBlock(AGLParser.StatBlockContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatBlock}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatBlock(AGLParser.StatBlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RepForStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 */
	void enterRepForStatement(AGLParser.RepForStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RepForStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 */
	void exitRepForStatement(AGLParser.RepForStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RepWhileStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 */
	void enterRepWhileStatement(AGLParser.RepWhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RepWhileStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 */
	void exitRepWhileStatement(AGLParser.RepWhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RepRepeatStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 */
	void enterRepRepeatStatement(AGLParser.RepRepeatStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RepRepeatStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 */
	void exitRepRepeatStatement(AGLParser.RepRepeatStatementContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#longAssignment}.
	 * @param ctx the parse tree
	 */
	void enterLongAssignment(AGLParser.LongAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#longAssignment}.
	 * @param ctx the parse tree
	 */
	void exitLongAssignment(AGLParser.LongAssignmentContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#in_assignment}.
	 * @param ctx the parse tree
	 */
	void enterIn_assignment(AGLParser.In_assignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#in_assignment}.
	 * @param ctx the parse tree
	 */
	void exitIn_assignment(AGLParser.In_assignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprWait}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprWait(AGLParser.ExprWaitContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprWait}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprWait(AGLParser.ExprWaitContext ctx);
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
	 * Enter a parse tree produced by the {@code ExprAddSubMultDivAndOr}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprAddSubMultDivAndOr(AGLParser.ExprAddSubMultDivAndOrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprAddSubMultDivAndOr}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprAddSubMultDivAndOr(AGLParser.ExprAddSubMultDivAndOrContext ctx);
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
	 * Enter a parse tree produced by the {@code ExprBoolean}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprBoolean(AGLParser.ExprBooleanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprBoolean}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprBoolean(AGLParser.ExprBooleanContext ctx);
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
	 * Enter a parse tree produced by the {@code ExprRelational}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprRelational(AGLParser.ExprRelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprRelational}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprRelational(AGLParser.ExprRelationalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprArray}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprArray(AGLParser.ExprArrayContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprArray}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprArray(AGLParser.ExprArrayContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprVector}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprVector(AGLParser.ExprVectorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprVector}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprVector(AGLParser.ExprVectorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprScript}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprScript(AGLParser.ExprScriptContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprScript}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprScript(AGLParser.ExprScriptContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprUnary}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExprUnary(AGLParser.ExprUnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprUnary}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExprUnary(AGLParser.ExprUnaryContext ctx);
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
	 * Enter a parse tree produced by the {@code CommandMove}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommandMove(AGLParser.CommandMoveContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CommandMove}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommandMove(AGLParser.CommandMoveContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(AGLParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(AGLParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#number_range}.
	 * @param ctx the parse tree
	 */
	void enterNumber_range(AGLParser.Number_rangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#number_range}.
	 * @param ctx the parse tree
	 */
	void exitNumber_range(AGLParser.Number_rangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(AGLParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(AGLParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#repeatStatement}.
	 * @param ctx the parse tree
	 */
	void enterRepeatStatement(AGLParser.RepeatStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#repeatStatement}.
	 * @param ctx the parse tree
	 */
	void exitRepeatStatement(AGLParser.RepeatStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#withStatement}.
	 * @param ctx the parse tree
	 */
	void enterWithStatement(AGLParser.WithStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#withStatement}.
	 * @param ctx the parse tree
	 */
	void exitWithStatement(AGLParser.WithStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#playStatement}.
	 * @param ctx the parse tree
	 */
	void enterPlayStatement(AGLParser.PlayStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#playStatement}.
	 * @param ctx the parse tree
	 */
	void exitPlayStatement(AGLParser.PlayStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#modelInstantiation}.
	 * @param ctx the parse tree
	 */
	void enterModelInstantiation(AGLParser.ModelInstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#modelInstantiation}.
	 * @param ctx the parse tree
	 */
	void exitModelInstantiation(AGLParser.ModelInstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(AGLParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(AGLParser.ActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link AGLParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(AGLParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(AGLParser.IfStatementContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(AGLParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(AGLParser.IdentifierContext ctx);
}