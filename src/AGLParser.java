// Generated from AGLParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class AGLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LPAREN=1, RPAREN=2, LBRACE=3, RBRACE=4, LBRACK=5, RBRACK=6, COLON=7, EQUAL=8, 
		SEMI=9, COMMA=10, DOT=11, WITH=12, AT=13, INTEGER=14, NUMBER=15, STRING_=16, 
		POINT=17, VECTOR=18, ID=19, INT=20, FLOAT=21, STRING=22, WS=23, LINE_COMMENT=24, 
		COMMENT=25, ERROR=26;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_instantiation = 2, RULE_simpleStatement = 3, 
		RULE_expression = 4, RULE_propertiesAssignment = 5, RULE_assignment = 6, 
		RULE_value = 7, RULE_number = 8, RULE_point = 9, RULE_position = 10, RULE_typeID = 11, 
		RULE_primitiveType = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "instantiation", "simpleStatement", "expression", 
			"propertiesAssignment", "assignment", "value", "number", "point", "position", 
			"typeID", "primitiveType"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "';'", 
			"','", "'.'", "'with'", "'at'", "'Integer'", "'Number'", "'String'", 
			"'Point'", "'Vector'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COLON", 
			"EQUAL", "SEMI", "COMMA", "DOT", "WITH", "AT", "INTEGER", "NUMBER", "STRING_", 
			"POINT", "VECTOR", "ID", "INT", "FLOAT", "STRING", "WS", "LINE_COMMENT", 
			"COMMENT", "ERROR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "AGLParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AGLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(AGLParser.EOF, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1032192L) != 0)) {
				{
				{
				setState(26);
				stat();
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public InstantiationContext instantiation() {
			return getRuleContext(InstantiationContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStat(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(36);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				instantiation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(35);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstantiationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(AGLParser.COLON, 0); }
		public SimpleStatementContext simpleStatement() {
			return getRuleContext(SimpleStatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public InstantiationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instantiation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterInstantiation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitInstantiation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitInstantiation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InstantiationContext instantiation() throws RecognitionException {
		InstantiationContext _localctx = new InstantiationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_instantiation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(ID);
			setState(39);
			match(COLON);
			setState(42);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(40);
				simpleStatement();
				}
				break;
			case 2:
				{
				setState(41);
				expression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SimpleStatementContext extends ParserRuleContext {
		public TypeIDContext typeID() {
			return getRuleContext(TypeIDContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public SimpleStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterSimpleStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitSimpleStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitSimpleStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SimpleStatementContext simpleStatement() throws RecognitionException {
		SimpleStatementContext _localctx = new SimpleStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_simpleStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			typeID();
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(45);
				assignment();
				}
			}

			setState(48);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public TypeIDContext typeID() {
			return getRuleContext(TypeIDContext.class,0);
		}
		public TerminalNode WITH() { return getToken(AGLParser.WITH, 0); }
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public PropertiesAssignmentContext propertiesAssignment() {
			return getRuleContext(PropertiesAssignmentContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public TerminalNode AT() { return getToken(AGLParser.AT, 0); }
		public PositionContext position() {
			return getRuleContext(PositionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			typeID();
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AT) {
				{
				setState(51);
				match(AT);
				setState(52);
				position();
				}
			}

			setState(55);
			match(WITH);
			setState(56);
			match(LBRACE);
			setState(57);
			propertiesAssignment();
			setState(58);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PropertiesAssignmentContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(AGLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(AGLParser.ID, i);
		}
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(AGLParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(AGLParser.SEMI, i);
		}
		public PropertiesAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propertiesAssignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterPropertiesAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitPropertiesAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitPropertiesAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PropertiesAssignmentContext propertiesAssignment() throws RecognitionException {
		PropertiesAssignmentContext _localctx = new PropertiesAssignmentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_propertiesAssignment);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(ID);
			setState(61);
			assignment();
			setState(67);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(62);
					match(SEMI);
					setState(63);
					match(ID);
					setState(64);
					assignment();
					}
					} 
				}
				setState(69);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(70);
				match(SEMI);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(AGLParser.EQUAL, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(EQUAL);
			setState(74);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public PointContext point() {
			return getRuleContext(PointContext.class,0);
		}
		public TerminalNode STRING() { return getToken(AGLParser.STRING, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitValue(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_value);
		try {
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				number();
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(77);
				point();
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(78);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(79);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(AGLParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(AGLParser.FLOAT, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitNumber(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitNumber(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PointContext extends ParserRuleContext {
		public NumberContext x;
		public NumberContext y;
		public TerminalNode LPAREN() { return getToken(AGLParser.LPAREN, 0); }
		public TerminalNode COMMA() { return getToken(AGLParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(AGLParser.RPAREN, 0); }
		public List<NumberContext> number() {
			return getRuleContexts(NumberContext.class);
		}
		public NumberContext number(int i) {
			return getRuleContext(NumberContext.class,i);
		}
		public PointContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_point; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterPoint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitPoint(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitPoint(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PointContext point() throws RecognitionException {
		PointContext _localctx = new PointContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_point);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(LPAREN);
			setState(85);
			((PointContext)_localctx).x = number();
			setState(86);
			match(COMMA);
			setState(87);
			((PointContext)_localctx).y = number();
			setState(88);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PositionContext extends ParserRuleContext {
		public PointContext point() {
			return getRuleContext(PointContext.class,0);
		}
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public PositionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_position; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterPosition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitPosition(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitPosition(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PositionContext position() throws RecognitionException {
		PositionContext _localctx = new PositionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_position);
		try {
			setState(92);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				point();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeIDContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public PrimitiveTypeContext primitiveType() {
			return getRuleContext(PrimitiveTypeContext.class,0);
		}
		public TypeIDContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeID; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterTypeID(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitTypeID(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitTypeID(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeIDContext typeID() throws RecognitionException {
		TypeIDContext _localctx = new TypeIDContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_typeID);
		try {
			setState(96);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(ID);
				}
				break;
			case INTEGER:
			case NUMBER:
			case STRING_:
			case POINT:
			case VECTOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				primitiveType();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimitiveTypeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(AGLParser.INTEGER, 0); }
		public TerminalNode NUMBER() { return getToken(AGLParser.NUMBER, 0); }
		public TerminalNode STRING_() { return getToken(AGLParser.STRING_, 0); }
		public TerminalNode POINT() { return getToken(AGLParser.POINT, 0); }
		public TerminalNode VECTOR() { return getToken(AGLParser.VECTOR, 0); }
		public PrimitiveTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterPrimitiveType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitPrimitiveType(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitPrimitiveType(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrimitiveTypeContext primitiveType() throws RecognitionException {
		PrimitiveTypeContext _localctx = new PrimitiveTypeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_primitiveType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 507904L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001ae\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0005\u0000\u001c\b\u0000\n\u0000\f\u0000\u001f"+
		"\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001%"+
		"\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002+"+
		"\b\u0002\u0001\u0003\u0001\u0003\u0003\u0003/\b\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u00046\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005B\b\u0005\n\u0005"+
		"\f\u0005E\t\u0005\u0001\u0005\u0003\u0005H\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"Q\b\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0003\n]\b\n\u0001\u000b\u0001\u000b\u0003\u000ba\b"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0002\u0001\u0000\u0014"+
		"\u0015\u0001\u0000\u000e\u0012c\u0000\u001d\u0001\u0000\u0000\u0000\u0002"+
		"$\u0001\u0000\u0000\u0000\u0004&\u0001\u0000\u0000\u0000\u0006,\u0001"+
		"\u0000\u0000\u0000\b2\u0001\u0000\u0000\u0000\n<\u0001\u0000\u0000\u0000"+
		"\fI\u0001\u0000\u0000\u0000\u000eP\u0001\u0000\u0000\u0000\u0010R\u0001"+
		"\u0000\u0000\u0000\u0012T\u0001\u0000\u0000\u0000\u0014\\\u0001\u0000"+
		"\u0000\u0000\u0016`\u0001\u0000\u0000\u0000\u0018b\u0001\u0000\u0000\u0000"+
		"\u001a\u001c\u0003\u0002\u0001\u0000\u001b\u001a\u0001\u0000\u0000\u0000"+
		"\u001c\u001f\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000"+
		"\u001d\u001e\u0001\u0000\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f"+
		"\u001d\u0001\u0000\u0000\u0000 !\u0005\u0000\u0000\u0001!\u0001\u0001"+
		"\u0000\u0000\u0000\"%\u0003\u0004\u0002\u0000#%\u0003\b\u0004\u0000$\""+
		"\u0001\u0000\u0000\u0000$#\u0001\u0000\u0000\u0000%\u0003\u0001\u0000"+
		"\u0000\u0000&\'\u0005\u0013\u0000\u0000\'*\u0005\u0007\u0000\u0000(+\u0003"+
		"\u0006\u0003\u0000)+\u0003\b\u0004\u0000*(\u0001\u0000\u0000\u0000*)\u0001"+
		"\u0000\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,.\u0003\u0016\u000b"+
		"\u0000-/\u0003\f\u0006\u0000.-\u0001\u0000\u0000\u0000./\u0001\u0000\u0000"+
		"\u0000/0\u0001\u0000\u0000\u000001\u0005\t\u0000\u00001\u0007\u0001\u0000"+
		"\u0000\u000025\u0003\u0016\u000b\u000034\u0005\r\u0000\u000046\u0003\u0014"+
		"\n\u000053\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000067\u0001\u0000"+
		"\u0000\u000078\u0005\f\u0000\u000089\u0005\u0003\u0000\u00009:\u0003\n"+
		"\u0005\u0000:;\u0005\u0004\u0000\u0000;\t\u0001\u0000\u0000\u0000<=\u0005"+
		"\u0013\u0000\u0000=C\u0003\f\u0006\u0000>?\u0005\t\u0000\u0000?@\u0005"+
		"\u0013\u0000\u0000@B\u0003\f\u0006\u0000A>\u0001\u0000\u0000\u0000BE\u0001"+
		"\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000"+
		"DG\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000FH\u0005\t\u0000\u0000"+
		"GF\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000H\u000b\u0001\u0000"+
		"\u0000\u0000IJ\u0005\b\u0000\u0000JK\u0003\u000e\u0007\u0000K\r\u0001"+
		"\u0000\u0000\u0000LQ\u0003\u0010\b\u0000MQ\u0003\u0012\t\u0000NQ\u0005"+
		"\u0016\u0000\u0000OQ\u0005\u0013\u0000\u0000PL\u0001\u0000\u0000\u0000"+
		"PM\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PO\u0001\u0000\u0000"+
		"\u0000Q\u000f\u0001\u0000\u0000\u0000RS\u0007\u0000\u0000\u0000S\u0011"+
		"\u0001\u0000\u0000\u0000TU\u0005\u0001\u0000\u0000UV\u0003\u0010\b\u0000"+
		"VW\u0005\n\u0000\u0000WX\u0003\u0010\b\u0000XY\u0005\u0002\u0000\u0000"+
		"Y\u0013\u0001\u0000\u0000\u0000Z]\u0003\u0012\t\u0000[]\u0005\u0013\u0000"+
		"\u0000\\Z\u0001\u0000\u0000\u0000\\[\u0001\u0000\u0000\u0000]\u0015\u0001"+
		"\u0000\u0000\u0000^a\u0005\u0013\u0000\u0000_a\u0003\u0018\f\u0000`^\u0001"+
		"\u0000\u0000\u0000`_\u0001\u0000\u0000\u0000a\u0017\u0001\u0000\u0000"+
		"\u0000bc\u0007\u0001\u0000\u0000c\u0019\u0001\u0000\u0000\u0000\n\u001d"+
		"$*.5CGP\\`";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}