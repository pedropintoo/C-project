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
	 * Enter a parse tree produced by {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(AGLParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(AGLParser.StatContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(AGLParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(AGLParser.ExpressionContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(AGLParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(AGLParser.ValueContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#position}.
	 * @param ctx the parse tree
	 */
	void enterPosition(AGLParser.PositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#position}.
	 * @param ctx the parse tree
	 */
	void exitPosition(AGLParser.PositionContext ctx);
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
	 * Enter a parse tree produced by {@link AGLParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveType(AGLParser.PrimitiveTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link AGLParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveType(AGLParser.PrimitiveTypeContext ctx);
}