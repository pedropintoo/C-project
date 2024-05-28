// Generated from AGLParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link AGLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface AGLParserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link AGLParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(AGLParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatInstantiation}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatInstantiation(AGLParser.StatInstantiationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatModelInstantiation}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatModelInstantiation(AGLParser.StatModelInstantiationContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatBlockStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatBlockStatement(AGLParser.StatBlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatLongAssignment}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatLongAssignment(AGLParser.StatLongAssignmentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatWithStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatWithStatement(AGLParser.StatWithStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatPlayStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatPlayStatement(AGLParser.StatPlayStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatRepetitiveStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatRepetitiveStatement(AGLParser.StatRepetitiveStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatIfStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatIfStatement(AGLParser.StatIfStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatCommand}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatCommand(AGLParser.StatCommandContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatBlock}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatBlock(AGLParser.StatBlockContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RepForStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepForStatement(AGLParser.RepForStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RepWhileStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepWhileStatement(AGLParser.RepWhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by the {@code RepRepeatStatement}
	 * labeled alternative in {@link AGLParser#repetitiveStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepRepeatStatement(AGLParser.RepRepeatStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#instantiation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInstantiation(AGLParser.InstantiationContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#simpleStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSimpleStatement(AGLParser.SimpleStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#blockStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlockStatement(AGLParser.BlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#propertiesAssignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#longAssignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLongAssignment(AGLParser.LongAssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(AGLParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#in_assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIn_assignment(AGLParser.In_assignmentContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprWait}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprWait(AGLParser.ExprWaitContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprString}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprString(AGLParser.ExprStringContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprAddSubMultDivAndOr}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprAddSubMultDivAndOr(AGLParser.ExprAddSubMultDivAndOrContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprPoint}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprPoint(AGLParser.ExprPointContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprBoolean}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprBoolean(AGLParser.ExprBooleanContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprParenthesis}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprParenthesis(AGLParser.ExprParenthesisContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprRelational}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprRelational(AGLParser.ExprRelationalContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprArray}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprArray(AGLParser.ExprArrayContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprVector}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprVector(AGLParser.ExprVectorContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprScript}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprScript(AGLParser.ExprScriptContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprUnary}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprUnary(AGLParser.ExprUnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprNumber}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprNumber(AGLParser.ExprNumberContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprID}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprID(AGLParser.ExprIDContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CommandRefresh}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandRefresh(AGLParser.CommandRefreshContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CommandPrint}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandPrint(AGLParser.CommandPrintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CommandClose}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandClose(AGLParser.CommandCloseContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CommandMove}
	 * labeled alternative in {@link AGLParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandMove(AGLParser.CommandMoveContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#eventTrigger}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEventTrigger(AGLParser.EventTriggerContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#mouseTrigger}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMouseTrigger(AGLParser.MouseTriggerContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#forStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStatement(AGLParser.ForStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#number_range}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber_range(AGLParser.Number_rangeContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#whileStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStatement(AGLParser.WhileStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#repeatStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepeatStatement(AGLParser.RepeatStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#withStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWithStatement(AGLParser.WithStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#playStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPlayStatement(AGLParser.PlayStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#modelInstantiation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModelInstantiation(AGLParser.ModelInstantiationContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#action}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAction(AGLParser.ActionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(AGLParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#typeID}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeID(AGLParser.TypeIDContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(AGLParser.IdentifierContext ctx);
}