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
	 * Visit a parse tree produced by {@link AGLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStat(AGLParser.StatContext ctx);
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
	 * Visit a parse tree produced by {@link AGLParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(AGLParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#propertiesAssignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(AGLParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(AGLParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#number}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumber(AGLParser.NumberContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#point}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPoint(AGLParser.PointContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#position}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPosition(AGLParser.PositionContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#typeID}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeID(AGLParser.TypeIDContext ctx);
	/**
	 * Visit a parse tree produced by {@link AGLParser#primitiveType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitiveType(AGLParser.PrimitiveTypeContext ctx);
}