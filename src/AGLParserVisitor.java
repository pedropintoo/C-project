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
	 * Visit a parse tree produced by the {@code StatCommand}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatCommand(AGLParser.StatCommandContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatForLoop}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatForLoop(AGLParser.StatForLoopContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatWithStatement}
	 * labeled alternative in {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatWithStatement(AGLParser.StatWithStatementContext ctx);
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
	 * Visit a parse tree produced by the {@code ExprPoint}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprPoint(AGLParser.ExprPointContext ctx);
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
	 * Visit a parse tree produced by the {@code ExprParenthesis}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprParenthesis(AGLParser.ExprParenthesisContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprID}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprID(AGLParser.ExprIDContext ctx);
	/**
	 * Visit a parse tree produced by the {@code ExprAddSubMultDiv}
	 * labeled alternative in {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx);
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
	 * Visit a parse tree produced by {@link AGLParser#for_loop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_loop(AGLParser.For_loopContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#withStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWithStatement(AGLParser.WithStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#typeID}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeID(AGLParser.TypeIDContext ctx);
}