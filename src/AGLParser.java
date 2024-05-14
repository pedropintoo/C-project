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
		SEMI=9, COMMA=10, TWODOTS=11, DOT=12, INTEGER=13, NUMBER=14, STRING_=15, 
		POINT=16, VECTOR=17, WITH=18, AT=19, PRINT=20, REFRESH=21, CLOSE=22, MOUSE=23, 
		CLICK=24, WAIT=25, FOR=26, IN=27, DO=28, AFTER=29, MS=30, PLUS=31, MINUS=32, 
		MUL=33, DIV=34, ID=35, INT=36, FLOAT=37, NUMBER_RANGE=38, STRING=39, LINE_COMMENT=40, 
		COMMENT=41, WS=42, ERROR=43;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_instantiation = 2, RULE_simpleStatement = 3, 
		RULE_blockStatement = 4, RULE_propertiesAssignment = 5, RULE_propertie = 6, 
		RULE_assignment = 7, RULE_expression = 8, RULE_command = 9, RULE_waitFor = 10, 
		RULE_eventTrigger = 11, RULE_mouseTrigger = 12, RULE_for_loop = 13, RULE_number = 14, 
		RULE_point = 15, RULE_typeID = 16, RULE_primitiveType = 17, RULE_operator = 18, 
		RULE_sign = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "instantiation", "simpleStatement", "blockStatement", 
			"propertiesAssignment", "propertie", "assignment", "expression", "command", 
			"waitFor", "eventTrigger", "mouseTrigger", "for_loop", "number", "point", 
			"typeID", "primitiveType", "operator", "sign"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "';'", 
			"','", "'..'", "'.'", "'Integer'", "'Number'", "'String'", "'Point'", 
			"'Vector'", "'with'", "'at'", "'print'", "'refresh'", "'close'", "'mouse'", 
			"'click'", "'wait'", "'for'", "'in'", "'do'", "'after'", "'ms'", "'+'", 
			"'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COLON", 
			"EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "INTEGER", "NUMBER", "STRING_", 
			"POINT", "VECTOR", "WITH", "AT", "PRINT", "REFRESH", "CLOSE", "MOUSE", 
			"CLICK", "WAIT", "FOR", "IN", "DO", "AFTER", "MS", "PLUS", "MINUS", "MUL", 
			"DIV", "ID", "INT", "FLOAT", "NUMBER_RANGE", "STRING", "LINE_COMMENT", 
			"COMMENT", "WS", "ERROR"
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
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 34434441216L) != 0)) {
				{
				{
				setState(40);
				stat();
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
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
		public BlockStatementContext blockStatement() {
			return getRuleContext(BlockStatementContext.class,0);
		}
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public For_loopContext for_loop() {
			return getRuleContext(For_loopContext.class,0);
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
			setState(52);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				instantiation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				blockStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				command();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(51);
				for_loop();
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
		public BlockStatementContext blockStatement() {
			return getRuleContext(BlockStatementContext.class,0);
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
			setState(54);
			match(ID);
			setState(55);
			match(COLON);
			setState(58);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(56);
				simpleStatement();
				}
				break;
			case 2:
				{
				setState(57);
				blockStatement();
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
			setState(60);
			typeID();
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(61);
				assignment();
				}
			}

			setState(64);
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
	public static class BlockStatementContext extends ParserRuleContext {
		public List<TypeIDContext> typeID() {
			return getRuleContexts(TypeIDContext.class);
		}
		public TypeIDContext typeID(int i) {
			return getRuleContext(TypeIDContext.class,i);
		}
		public TerminalNode WITH() { return getToken(AGLParser.WITH, 0); }
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public PropertiesAssignmentContext propertiesAssignment() {
			return getRuleContext(PropertiesAssignmentContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public TerminalNode AT() { return getToken(AGLParser.AT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> DOT() { return getTokens(AGLParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(AGLParser.DOT, i);
		}
		public List<PropertieContext> propertie() {
			return getRuleContexts(PropertieContext.class);
		}
		public PropertieContext propertie(int i) {
			return getRuleContext(PropertieContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(AGLParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(AGLParser.SEMI, i);
		}
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public BlockStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterBlockStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitBlockStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitBlockStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockStatementContext blockStatement() throws RecognitionException {
		BlockStatementContext _localctx = new BlockStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_blockStatement);
		int _la;
		try {
			int _alt;
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				typeID();
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AT) {
					{
					setState(67);
					match(AT);
					setState(68);
					expression(0);
					}
				}

				setState(71);
				match(WITH);
				setState(72);
				match(LBRACE);
				setState(73);
				propertiesAssignment();
				setState(74);
				match(RBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(81); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(76);
						typeID();
						setState(77);
						match(DOT);
						setState(78);
						propertie();
						setState(79);
						match(SEMI);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(83); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(86); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(85);
						command();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(88); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class PropertiesAssignmentContext extends ParserRuleContext {
		public List<PropertieContext> propertie() {
			return getRuleContexts(PropertieContext.class);
		}
		public PropertieContext propertie(int i) {
			return getRuleContext(PropertieContext.class,i);
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
			setState(92);
			propertie();
			setState(97);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(93);
					match(SEMI);
					setState(94);
					propertie();
					}
					} 
				}
				setState(99);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(100);
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
	public static class PropertieContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public PropertieContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_propertie; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterPropertie(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitPropertie(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitPropertie(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PropertieContext propertie() throws RecognitionException {
		PropertieContext _localctx = new PropertieContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_propertie);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(ID);
			setState(104);
			assignment();
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
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
		enterRule(_localctx, 14, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(EQUAL);
			setState(107);
			expression(0);
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
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprStringContext extends ExpressionContext {
		public TerminalNode STRING() { return getToken(AGLParser.STRING, 0); }
		public ExprStringContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprString(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprString(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprWaitForContext extends ExpressionContext {
		public WaitForContext waitFor() {
			return getRuleContext(WaitForContext.class,0);
		}
		public ExprWaitForContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprWaitFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprWaitFor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprWaitFor(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprPointContext extends ExpressionContext {
		public PointContext point() {
			return getRuleContext(PointContext.class,0);
		}
		public SignContext sign() {
			return getRuleContext(SignContext.class,0);
		}
		public ExprPointContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprPoint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprPoint(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprPoint(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprNumberContext extends ExpressionContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public SignContext sign() {
			return getRuleContext(SignContext.class,0);
		}
		public ExprNumberContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprNumber(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprNumber(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprParenthesisContext extends ExpressionContext {
		public TerminalNode LPAREN() { return getToken(AGLParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(AGLParser.RPAREN, 0); }
		public SignContext sign() {
			return getRuleContext(SignContext.class,0);
		}
		public ExprParenthesisContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprParenthesis(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprParenthesis(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprParenthesis(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprIDContext extends ExpressionContext {
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public SignContext sign() {
			return getRuleContext(SignContext.class,0);
		}
		public ExprIDContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprID(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprID(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprID(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprAddSubMultDivContext extends ExpressionContext {
		public Token op;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(AGLParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(AGLParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(AGLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AGLParser.MINUS, 0); }
		public ExprAddSubMultDivContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprAddSubMultDiv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprAddSubMultDiv(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprAddSubMultDiv(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				_localctx = new ExprParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(111);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(110);
					sign();
					}
				}

				setState(113);
				match(LPAREN);
				setState(114);
				expression(0);
				setState(115);
				match(RPAREN);
				}
				break;
			case 2:
				{
				_localctx = new ExprPointContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(117);
					sign();
					}
				}

				setState(120);
				point();
				}
				break;
			case 3:
				{
				_localctx = new ExprNumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(121);
					sign();
					}
				}

				setState(124);
				number();
				}
				break;
			case 4:
				{
				_localctx = new ExprStringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(125);
				match(STRING);
				}
				break;
			case 5:
				{
				_localctx = new ExprIDContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(126);
					sign();
					}
				}

				setState(129);
				match(ID);
				}
				break;
			case 6:
				{
				_localctx = new ExprWaitForContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(130);
				waitFor();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(141);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(139);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						_localctx = new ExprAddSubMultDivContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(133);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(134);
						((ExprAddSubMultDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((ExprAddSubMultDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(135);
						expression(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprAddSubMultDivContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(136);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(137);
						((ExprAddSubMultDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((ExprAddSubMultDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(138);
						expression(7);
						}
						break;
					}
					} 
				}
				setState(143);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public TerminalNode REFRESH() { return getToken(AGLParser.REFRESH, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public TerminalNode AFTER() { return getToken(AGLParser.AFTER, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public TerminalNode MS() { return getToken(AGLParser.MS, 0); }
		public TerminalNode PRINT() { return getToken(AGLParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CLOSE() { return getToken(AGLParser.CLOSE, 0); }
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitCommand(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitCommand(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_command);
		try {
			setState(161);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(144);
				match(REFRESH);
				setState(145);
				match(ID);
				setState(146);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				match(REFRESH);
				setState(148);
				match(ID);
				setState(149);
				match(AFTER);
				setState(150);
				number();
				setState(151);
				match(MS);
				setState(152);
				match(SEMI);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(154);
				match(PRINT);
				setState(155);
				expression(0);
				setState(156);
				match(SEMI);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(158);
				match(CLOSE);
				setState(159);
				match(ID);
				setState(160);
				match(SEMI);
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
	public static class WaitForContext extends ParserRuleContext {
		public TerminalNode WAIT() { return getToken(AGLParser.WAIT, 0); }
		public EventTriggerContext eventTrigger() {
			return getRuleContext(EventTriggerContext.class,0);
		}
		public WaitForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_waitFor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterWaitFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitWaitFor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitWaitFor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WaitForContext waitFor() throws RecognitionException {
		WaitForContext _localctx = new WaitForContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_waitFor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(WAIT);
			setState(164);
			eventTrigger();
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
	public static class EventTriggerContext extends ParserRuleContext {
		public TerminalNode MOUSE() { return getToken(AGLParser.MOUSE, 0); }
		public MouseTriggerContext mouseTrigger() {
			return getRuleContext(MouseTriggerContext.class,0);
		}
		public EventTriggerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eventTrigger; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterEventTrigger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitEventTrigger(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitEventTrigger(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EventTriggerContext eventTrigger() throws RecognitionException {
		EventTriggerContext _localctx = new EventTriggerContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_eventTrigger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(MOUSE);
			setState(167);
			mouseTrigger();
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
	public static class MouseTriggerContext extends ParserRuleContext {
		public TerminalNode CLICK() { return getToken(AGLParser.CLICK, 0); }
		public MouseTriggerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mouseTrigger; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterMouseTrigger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitMouseTrigger(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitMouseTrigger(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MouseTriggerContext mouseTrigger() throws RecognitionException {
		MouseTriggerContext _localctx = new MouseTriggerContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_mouseTrigger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(CLICK);
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
	public static class For_loopContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(AGLParser.FOR, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode IN() { return getToken(AGLParser.IN, 0); }
		public TerminalNode NUMBER_RANGE() { return getToken(AGLParser.NUMBER_RANGE, 0); }
		public For_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterFor_loop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitFor_loop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitFor_loop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final For_loopContext for_loop() throws RecognitionException {
		For_loopContext _localctx = new For_loopContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_for_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(FOR);
			setState(172);
			match(ID);
			setState(173);
			match(IN);
			setState(174);
			match(NUMBER_RANGE);
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
		enterRule(_localctx, 28, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
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
		public ExpressionContext x;
		public ExpressionContext y;
		public TerminalNode LPAREN() { return getToken(AGLParser.LPAREN, 0); }
		public TerminalNode COMMA() { return getToken(AGLParser.COMMA, 0); }
		public TerminalNode RPAREN() { return getToken(AGLParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
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
		enterRule(_localctx, 30, RULE_point);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(LPAREN);
			setState(179);
			((PointContext)_localctx).x = expression(0);
			setState(180);
			match(COMMA);
			setState(181);
			((PointContext)_localctx).y = expression(0);
			setState(182);
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
		enterRule(_localctx, 32, RULE_typeID);
		try {
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
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
				setState(185);
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
		enterRule(_localctx, 34, RULE_primitiveType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 253952L) != 0)) ) {
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
	public static class OperatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(AGLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AGLParser.MINUS, 0); }
		public TerminalNode MUL() { return getToken(AGLParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(AGLParser.DIV, 0); }
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitOperator(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitOperator(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 32212254720L) != 0)) ) {
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
	public static class SignContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(AGLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AGLParser.MINUS, 0); }
		public SignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterSign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitSign(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitSign(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SignContext sign() throws RecognitionException {
		SignContext _localctx = new SignContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_sign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			_la = _input.LA(1);
			if ( !(_la==PLUS || _la==MINUS) ) {
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001+\u00c3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0005\u0000*\b\u0000\n\u0000\f\u0000"+
		"-\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u00015\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002;\b\u0002\u0001\u0003\u0001\u0003\u0003\u0003"+
		"?\b\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004F\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0004\u0004R\b\u0004\u000b\u0004\f\u0004S\u0001\u0004\u0004\u0004W\b"+
		"\u0004\u000b\u0004\f\u0004X\u0003\u0004[\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0005\u0005`\b\u0005\n\u0005\f\u0005c\t\u0005\u0001\u0005"+
		"\u0003\u0005f\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0003\bp\b\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0003\bw\b\b\u0001\b\u0001\b\u0003\b{\b\b\u0001"+
		"\b\u0001\b\u0001\b\u0003\b\u0080\b\b\u0001\b\u0001\b\u0003\b\u0084\b\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u008c\b\b\n\b"+
		"\f\b\u008f\t\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0003\t\u00a2\b\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0003\u0010\u00bb\b\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0000\u0001\u0010\u0014\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&\u0000\u0005\u0001"+
		"\u0000!\"\u0001\u0000\u001f \u0001\u0000$%\u0001\u0000\r\u0011\u0001\u0000"+
		"\u001f\"\u00ca\u0000+\u0001\u0000\u0000\u0000\u00024\u0001\u0000\u0000"+
		"\u0000\u00046\u0001\u0000\u0000\u0000\u0006<\u0001\u0000\u0000\u0000\b"+
		"Z\u0001\u0000\u0000\u0000\n\\\u0001\u0000\u0000\u0000\fg\u0001\u0000\u0000"+
		"\u0000\u000ej\u0001\u0000\u0000\u0000\u0010\u0083\u0001\u0000\u0000\u0000"+
		"\u0012\u00a1\u0001\u0000\u0000\u0000\u0014\u00a3\u0001\u0000\u0000\u0000"+
		"\u0016\u00a6\u0001\u0000\u0000\u0000\u0018\u00a9\u0001\u0000\u0000\u0000"+
		"\u001a\u00ab\u0001\u0000\u0000\u0000\u001c\u00b0\u0001\u0000\u0000\u0000"+
		"\u001e\u00b2\u0001\u0000\u0000\u0000 \u00ba\u0001\u0000\u0000\u0000\""+
		"\u00bc\u0001\u0000\u0000\u0000$\u00be\u0001\u0000\u0000\u0000&\u00c0\u0001"+
		"\u0000\u0000\u0000(*\u0003\u0002\u0001\u0000)(\u0001\u0000\u0000\u0000"+
		"*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000"+
		"\u0000,.\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000./\u0005\u0000"+
		"\u0000\u0001/\u0001\u0001\u0000\u0000\u000005\u0003\u0004\u0002\u0000"+
		"15\u0003\b\u0004\u000025\u0003\u0012\t\u000035\u0003\u001a\r\u000040\u0001"+
		"\u0000\u0000\u000041\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u0000"+
		"43\u0001\u0000\u0000\u00005\u0003\u0001\u0000\u0000\u000067\u0005#\u0000"+
		"\u00007:\u0005\u0007\u0000\u00008;\u0003\u0006\u0003\u00009;\u0003\b\u0004"+
		"\u0000:8\u0001\u0000\u0000\u0000:9\u0001\u0000\u0000\u0000;\u0005\u0001"+
		"\u0000\u0000\u0000<>\u0003 \u0010\u0000=?\u0003\u000e\u0007\u0000>=\u0001"+
		"\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000"+
		"@A\u0005\t\u0000\u0000A\u0007\u0001\u0000\u0000\u0000BE\u0003 \u0010\u0000"+
		"CD\u0005\u0013\u0000\u0000DF\u0003\u0010\b\u0000EC\u0001\u0000\u0000\u0000"+
		"EF\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GH\u0005\u0012\u0000"+
		"\u0000HI\u0005\u0003\u0000\u0000IJ\u0003\n\u0005\u0000JK\u0005\u0004\u0000"+
		"\u0000K[\u0001\u0000\u0000\u0000LM\u0003 \u0010\u0000MN\u0005\f\u0000"+
		"\u0000NO\u0003\f\u0006\u0000OP\u0005\t\u0000\u0000PR\u0001\u0000\u0000"+
		"\u0000QL\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000SQ\u0001\u0000"+
		"\u0000\u0000ST\u0001\u0000\u0000\u0000T[\u0001\u0000\u0000\u0000UW\u0003"+
		"\u0012\t\u0000VU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000XV\u0001"+
		"\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y[\u0001\u0000\u0000\u0000"+
		"ZB\u0001\u0000\u0000\u0000ZQ\u0001\u0000\u0000\u0000ZV\u0001\u0000\u0000"+
		"\u0000[\t\u0001\u0000\u0000\u0000\\a\u0003\f\u0006\u0000]^\u0005\t\u0000"+
		"\u0000^`\u0003\f\u0006\u0000_]\u0001\u0000\u0000\u0000`c\u0001\u0000\u0000"+
		"\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000be\u0001\u0000"+
		"\u0000\u0000ca\u0001\u0000\u0000\u0000df\u0005\t\u0000\u0000ed\u0001\u0000"+
		"\u0000\u0000ef\u0001\u0000\u0000\u0000f\u000b\u0001\u0000\u0000\u0000"+
		"gh\u0005#\u0000\u0000hi\u0003\u000e\u0007\u0000i\r\u0001\u0000\u0000\u0000"+
		"jk\u0005\b\u0000\u0000kl\u0003\u0010\b\u0000l\u000f\u0001\u0000\u0000"+
		"\u0000mo\u0006\b\uffff\uffff\u0000np\u0003&\u0013\u0000on\u0001\u0000"+
		"\u0000\u0000op\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qr\u0005"+
		"\u0001\u0000\u0000rs\u0003\u0010\b\u0000st\u0005\u0002\u0000\u0000t\u0084"+
		"\u0001\u0000\u0000\u0000uw\u0003&\u0013\u0000vu\u0001\u0000\u0000\u0000"+
		"vw\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000x\u0084\u0003\u001e"+
		"\u000f\u0000y{\u0003&\u0013\u0000zy\u0001\u0000\u0000\u0000z{\u0001\u0000"+
		"\u0000\u0000{|\u0001\u0000\u0000\u0000|\u0084\u0003\u001c\u000e\u0000"+
		"}\u0084\u0005\'\u0000\u0000~\u0080\u0003&\u0013\u0000\u007f~\u0001\u0000"+
		"\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0005#\u0000\u0000\u0082\u0084\u0003\u0014\n"+
		"\u0000\u0083m\u0001\u0000\u0000\u0000\u0083v\u0001\u0000\u0000\u0000\u0083"+
		"z\u0001\u0000\u0000\u0000\u0083}\u0001\u0000\u0000\u0000\u0083\u007f\u0001"+
		"\u0000\u0000\u0000\u0083\u0082\u0001\u0000\u0000\u0000\u0084\u008d\u0001"+
		"\u0000\u0000\u0000\u0085\u0086\n\u0007\u0000\u0000\u0086\u0087\u0007\u0000"+
		"\u0000\u0000\u0087\u008c\u0003\u0010\b\b\u0088\u0089\n\u0006\u0000\u0000"+
		"\u0089\u008a\u0007\u0001\u0000\u0000\u008a\u008c\u0003\u0010\b\u0007\u008b"+
		"\u0085\u0001\u0000\u0000\u0000\u008b\u0088\u0001\u0000\u0000\u0000\u008c"+
		"\u008f\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d"+
		"\u008e\u0001\u0000\u0000\u0000\u008e\u0011\u0001\u0000\u0000\u0000\u008f"+
		"\u008d\u0001\u0000\u0000\u0000\u0090\u0091\u0005\u0015\u0000\u0000\u0091"+
		"\u0092\u0005#\u0000\u0000\u0092\u00a2\u0005\t\u0000\u0000\u0093\u0094"+
		"\u0005\u0015\u0000\u0000\u0094\u0095\u0005#\u0000\u0000\u0095\u0096\u0005"+
		"\u001d\u0000\u0000\u0096\u0097\u0003\u001c\u000e\u0000\u0097\u0098\u0005"+
		"\u001e\u0000\u0000\u0098\u0099\u0005\t\u0000\u0000\u0099\u00a2\u0001\u0000"+
		"\u0000\u0000\u009a\u009b\u0005\u0014\u0000\u0000\u009b\u009c\u0003\u0010"+
		"\b\u0000\u009c\u009d\u0005\t\u0000\u0000\u009d\u00a2\u0001\u0000\u0000"+
		"\u0000\u009e\u009f\u0005\u0016\u0000\u0000\u009f\u00a0\u0005#\u0000\u0000"+
		"\u00a0\u00a2\u0005\t\u0000\u0000\u00a1\u0090\u0001\u0000\u0000\u0000\u00a1"+
		"\u0093\u0001\u0000\u0000\u0000\u00a1\u009a\u0001\u0000\u0000\u0000\u00a1"+
		"\u009e\u0001\u0000\u0000\u0000\u00a2\u0013\u0001\u0000\u0000\u0000\u00a3"+
		"\u00a4\u0005\u0019\u0000\u0000\u00a4\u00a5\u0003\u0016\u000b\u0000\u00a5"+
		"\u0015\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005\u0017\u0000\u0000\u00a7"+
		"\u00a8\u0003\u0018\f\u0000\u00a8\u0017\u0001\u0000\u0000\u0000\u00a9\u00aa"+
		"\u0005\u0018\u0000\u0000\u00aa\u0019\u0001\u0000\u0000\u0000\u00ab\u00ac"+
		"\u0005\u001a\u0000\u0000\u00ac\u00ad\u0005#\u0000\u0000\u00ad\u00ae\u0005"+
		"\u001b\u0000\u0000\u00ae\u00af\u0005&\u0000\u0000\u00af\u001b\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b1\u0007\u0002\u0000\u0000\u00b1\u001d\u0001\u0000"+
		"\u0000\u0000\u00b2\u00b3\u0005\u0001\u0000\u0000\u00b3\u00b4\u0003\u0010"+
		"\b\u0000\u00b4\u00b5\u0005\n\u0000\u0000\u00b5\u00b6\u0003\u0010\b\u0000"+
		"\u00b6\u00b7\u0005\u0002\u0000\u0000\u00b7\u001f\u0001\u0000\u0000\u0000"+
		"\u00b8\u00bb\u0005#\u0000\u0000\u00b9\u00bb\u0003\"\u0011\u0000\u00ba"+
		"\u00b8\u0001\u0000\u0000\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb"+
		"!\u0001\u0000\u0000\u0000\u00bc\u00bd\u0007\u0003\u0000\u0000\u00bd#\u0001"+
		"\u0000\u0000\u0000\u00be\u00bf\u0007\u0004\u0000\u0000\u00bf%\u0001\u0000"+
		"\u0000\u0000\u00c0\u00c1\u0007\u0001\u0000\u0000\u00c1\'\u0001\u0000\u0000"+
		"\u0000\u0013+4:>ESXZaeovz\u007f\u0083\u008b\u008d\u00a1\u00ba";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}