// Generated from AGLParser.g4 by ANTLR 4.13.1

import java.util.Map;
import java.util.HashMap;

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
		SEMI=9, COMMA=10, TWODOTS=11, DOT=12, PRIMITIVE_TYPE=13, INTEGER=14, NUMBER=15, 
		STRING_=16, POINT=17, VECTOR=18, WITH=19, AT=20, PRINT=21, REFRESH=22, 
		CLOSE=23, MOUSE=24, CLICK=25, WAIT=26, FOR=27, IN=28, DO=29, AFTER=30, 
		MS=31, PLUS=32, MINUS=33, MUL=34, DIV=35, ID=36, INT=37, FLOAT=38, NUMBER_RANGE=39, 
		STRING=40, LINE_COMMENT=41, COMMENT=42, WS=43, ERROR=44;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_instantiation = 2, RULE_simpleStatement = 3, 
		RULE_blockStatement = 4, RULE_propertiesAssignment = 5, RULE_longAssignment = 6, 
		RULE_assignment = 7, RULE_expression = 8, RULE_command = 9, RULE_eventTrigger = 10, 
		RULE_mouseTrigger = 11, RULE_for_loop = 12, RULE_typeID = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "instantiation", "simpleStatement", "blockStatement", 
			"propertiesAssignment", "longAssignment", "assignment", "expression", 
			"command", "eventTrigger", "mouseTrigger", "for_loop", "typeID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "';'", 
			"','", "'..'", "'.'", null, "'Integer'", "'Number'", "'String'", "'Point'", 
			"'Vector'", "'with'", "'at'", "'print'", "'refresh'", "'close'", "'mouse'", 
			"'click'", "'wait'", "'for'", "'in'", "'do'", "'after'", "'ms'", "'+'", 
			"'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COLON", 
			"EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "PRIMITIVE_TYPE", "INTEGER", 
			"NUMBER", "STRING_", "POINT", "VECTOR", "WITH", "AT", "PRINT", "REFRESH", 
			"CLOSE", "MOUSE", "CLICK", "WAIT", "FOR", "IN", "DO", "AFTER", "MS", 
			"PLUS", "MINUS", "MUL", "DIV", "ID", "INT", "FLOAT", "NUMBER_RANGE", 
			"STRING", "LINE_COMMENT", "COMMENT", "WS", "ERROR"
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


	static protected Map<String,Number> symbolTable = new HashMap<>();

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
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 68868382720L) != 0)) {
				{
				{
				setState(28);
				stat();
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(34);
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
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatCommandContext extends StatContext {
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public StatCommandContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatCommand(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatCommand(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatForLoopContext extends StatContext {
		public For_loopContext for_loop() {
			return getRuleContext(For_loopContext.class,0);
		}
		public StatForLoopContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatForLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatForLoop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatForLoop(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatInstantiationContext extends StatContext {
		public InstantiationContext instantiation() {
			return getRuleContext(InstantiationContext.class,0);
		}
		public StatInstantiationContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatInstantiation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatInstantiation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatInstantiation(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatBlockStatementContext extends StatContext {
		public BlockStatementContext blockStatement() {
			return getRuleContext(BlockStatementContext.class,0);
		}
		public StatBlockStatementContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatBlockStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatBlockStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatBlockStatement(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatLongAssignmentContext extends StatContext {
		public LongAssignmentContext longAssignment() {
			return getRuleContext(LongAssignmentContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public StatLongAssignmentContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatLongAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatLongAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatLongAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new StatInstantiationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				instantiation();
				}
				break;
			case 2:
				_localctx = new StatBlockStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(37);
				blockStatement();
				}
				break;
			case 3:
				_localctx = new StatLongAssignmentContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				longAssignment();
				setState(39);
				match(SEMI);
				}
				break;
			case 4:
				_localctx = new StatCommandContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(41);
				command();
				}
				break;
			case 5:
				_localctx = new StatForLoopContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(42);
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
			setState(45);
			match(ID);
			setState(46);
			match(COLON);
			setState(49);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(47);
				simpleStatement();
				}
				break;
			case 2:
				{
				setState(48);
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
		public String varName;
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
			setState(51);
			typeID();
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(52);
				assignment();
				}
			}

			setState(55);
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
		public String varName;
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
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			typeID();
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AT) {
				{
				setState(58);
				match(AT);
				setState(59);
				expression(0);
				}
			}

			setState(62);
			match(WITH);
			setState(63);
			match(LBRACE);
			setState(64);
			propertiesAssignment();
			setState(65);
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
		public List<LongAssignmentContext> longAssignment() {
			return getRuleContexts(LongAssignmentContext.class);
		}
		public LongAssignmentContext longAssignment(int i) {
			return getRuleContext(LongAssignmentContext.class,i);
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
			setState(67);
			longAssignment();
			setState(72);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(68);
					match(SEMI);
					setState(69);
					longAssignment();
					}
					} 
				}
				setState(74);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(75);
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
	public static class LongAssignmentContext extends ParserRuleContext {
		public Token attr;
		public List<TerminalNode> ID() { return getTokens(AGLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(AGLParser.ID, i);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode DOT() { return getToken(AGLParser.DOT, 0); }
		public LongAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_longAssignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterLongAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitLongAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitLongAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LongAssignmentContext longAssignment() throws RecognitionException {
		LongAssignmentContext _localctx = new LongAssignmentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_longAssignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(ID);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DOT) {
				{
				setState(79);
				match(DOT);
				setState(80);
				((LongAssignmentContext)_localctx).attr = match(ID);
				}
			}

			setState(83);
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
		public String varName;
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
			setState(85);
			match(EQUAL);
			setState(86);
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
		public String varName;
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
			this.varName = ctx.varName;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprWaitContext extends ExpressionContext {
		public TerminalNode WAIT() { return getToken(AGLParser.WAIT, 0); }
		public EventTriggerContext eventTrigger() {
			return getRuleContext(EventTriggerContext.class,0);
		}
		public ExprWaitContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprWait(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprWait(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprWait(this);
			else return visitor.visitChildren(this);
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
	public static class ExprPointContext extends ExpressionContext {
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
	public static class ExprUnaryContext extends ExpressionContext {
		public Token sign;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(AGLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AGLParser.MINUS, 0); }
		public ExprUnaryContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprUnary(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprNumberContext extends ExpressionContext {
		public Token number;
		public TerminalNode INT() { return getToken(AGLParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(AGLParser.FLOAT, 0); }
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
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				_localctx = new ExprUnaryContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(89);
				((ExprUnaryContext)_localctx).sign = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
					((ExprUnaryContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(90);
				expression(9);
				}
				break;
			case 2:
				{
				_localctx = new ExprParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(91);
				match(LPAREN);
				setState(92);
				expression(0);
				setState(93);
				match(RPAREN);
				}
				break;
			case 3:
				{
				_localctx = new ExprPointContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(95);
				match(LPAREN);
				setState(96);
				((ExprPointContext)_localctx).x = expression(0);
				setState(97);
				match(COMMA);
				setState(98);
				((ExprPointContext)_localctx).y = expression(0);
				setState(99);
				match(RPAREN);
				}
				break;
			case 4:
				{
				_localctx = new ExprNumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(101);
				((ExprNumberContext)_localctx).number = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==INT || _la==FLOAT) ) {
					((ExprNumberContext)_localctx).number = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 5:
				{
				_localctx = new ExprStringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(102);
				match(STRING);
				}
				break;
			case 6:
				{
				_localctx = new ExprIDContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(103);
				match(ID);
				}
				break;
			case 7:
				{
				_localctx = new ExprWaitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(104);
				match(WAIT);
				setState(105);
				eventTrigger();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(116);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(114);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						_localctx = new ExprAddSubMultDivContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(108);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(109);
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
						setState(110);
						expression(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprAddSubMultDivContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(111);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(112);
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
						setState(113);
						expression(7);
						}
						break;
					}
					} 
				}
				setState(118);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
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
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	 
		public CommandContext() { }
		public void copyFrom(CommandContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CommandPrintContext extends CommandContext {
		public TerminalNode PRINT() { return getToken(AGLParser.PRINT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public CommandPrintContext(CommandContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterCommandPrint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitCommandPrint(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitCommandPrint(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CommandCloseContext extends CommandContext {
		public TerminalNode CLOSE() { return getToken(AGLParser.CLOSE, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public CommandCloseContext(CommandContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterCommandClose(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitCommandClose(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitCommandClose(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CommandRefreshContext extends CommandContext {
		public Token number;
		public TerminalNode REFRESH() { return getToken(AGLParser.REFRESH, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public TerminalNode AFTER() { return getToken(AGLParser.AFTER, 0); }
		public TerminalNode MS() { return getToken(AGLParser.MS, 0); }
		public TerminalNode INT() { return getToken(AGLParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(AGLParser.FLOAT, 0); }
		public CommandRefreshContext(CommandContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterCommandRefresh(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitCommandRefresh(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitCommandRefresh(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_command);
		int _la;
		try {
			setState(134);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REFRESH:
				_localctx = new CommandRefreshContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(119);
				match(REFRESH);
				setState(120);
				match(ID);
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AFTER) {
					{
					setState(121);
					match(AFTER);
					setState(122);
					((CommandRefreshContext)_localctx).number = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==INT || _la==FLOAT) ) {
						((CommandRefreshContext)_localctx).number = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(123);
					match(MS);
					}
				}

				setState(126);
				match(SEMI);
				}
				break;
			case PRINT:
				_localctx = new CommandPrintContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				match(PRINT);
				setState(128);
				expression(0);
				setState(129);
				match(SEMI);
				}
				break;
			case CLOSE:
				_localctx = new CommandCloseContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(131);
				match(CLOSE);
				setState(132);
				match(ID);
				setState(133);
				match(SEMI);
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
		enterRule(_localctx, 20, RULE_eventTrigger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(MOUSE);
			setState(137);
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
		enterRule(_localctx, 22, RULE_mouseTrigger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
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
		public TerminalNode DO() { return getToken(AGLParser.DO, 0); }
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
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
		enterRule(_localctx, 24, RULE_for_loop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(FOR);
			setState(142);
			match(ID);
			setState(143);
			match(IN);
			setState(144);
			match(NUMBER_RANGE);
			setState(145);
			match(DO);
			setState(146);
			match(LBRACE);
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 68868382720L) != 0)) {
				{
				{
				setState(147);
				stat();
				}
				}
				setState(152);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(153);
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
	public static class TypeIDContext extends ParserRuleContext {
		public Token type;
		public TerminalNode PRIMITIVE_TYPE() { return getToken(AGLParser.PRIMITIVE_TYPE, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
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
		enterRule(_localctx, 26, RULE_typeID);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			((TypeIDContext)_localctx).type = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==PRIMITIVE_TYPE || _la==ID) ) {
				((TypeIDContext)_localctx).type = (Token)_errHandler.recoverInline(this);
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
		"\u0004\u0001,\u009e\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0005\u0000\u001e\b\u0000\n\u0000"+
		"\f\u0000!\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001,\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u00022\b"+
		"\u0002\u0001\u0003\u0001\u0003\u0003\u00036\b\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004=\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0005\u0005G\b\u0005\n\u0005\f\u0005J\t\u0005\u0001"+
		"\u0005\u0003\u0005M\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006R\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\bk\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0005\bs\b\b\n\b\f\bv\t\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003"+
		"\t}\b\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0003\t\u0087\b\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f\u0095\b\f\n"+
		"\f\f\f\u0098\t\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0000\u0001\u0010"+
		"\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018"+
		"\u001a\u0000\u0004\u0001\u0000 !\u0001\u0000%&\u0001\u0000\"#\u0002\u0000"+
		"\r\r$$\u00a6\u0000\u001f\u0001\u0000\u0000\u0000\u0002+\u0001\u0000\u0000"+
		"\u0000\u0004-\u0001\u0000\u0000\u0000\u00063\u0001\u0000\u0000\u0000\b"+
		"9\u0001\u0000\u0000\u0000\nC\u0001\u0000\u0000\u0000\fN\u0001\u0000\u0000"+
		"\u0000\u000eU\u0001\u0000\u0000\u0000\u0010j\u0001\u0000\u0000\u0000\u0012"+
		"\u0086\u0001\u0000\u0000\u0000\u0014\u0088\u0001\u0000\u0000\u0000\u0016"+
		"\u008b\u0001\u0000\u0000\u0000\u0018\u008d\u0001\u0000\u0000\u0000\u001a"+
		"\u009b\u0001\u0000\u0000\u0000\u001c\u001e\u0003\u0002\u0001\u0000\u001d"+
		"\u001c\u0001\u0000\u0000\u0000\u001e!\u0001\u0000\u0000\u0000\u001f\u001d"+
		"\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 \"\u0001\u0000"+
		"\u0000\u0000!\u001f\u0001\u0000\u0000\u0000\"#\u0005\u0000\u0000\u0001"+
		"#\u0001\u0001\u0000\u0000\u0000$,\u0003\u0004\u0002\u0000%,\u0003\b\u0004"+
		"\u0000&\'\u0003\f\u0006\u0000\'(\u0005\t\u0000\u0000(,\u0001\u0000\u0000"+
		"\u0000),\u0003\u0012\t\u0000*,\u0003\u0018\f\u0000+$\u0001\u0000\u0000"+
		"\u0000+%\u0001\u0000\u0000\u0000+&\u0001\u0000\u0000\u0000+)\u0001\u0000"+
		"\u0000\u0000+*\u0001\u0000\u0000\u0000,\u0003\u0001\u0000\u0000\u0000"+
		"-.\u0005$\u0000\u0000.1\u0005\u0007\u0000\u0000/2\u0003\u0006\u0003\u0000"+
		"02\u0003\b\u0004\u00001/\u0001\u0000\u0000\u000010\u0001\u0000\u0000\u0000"+
		"2\u0005\u0001\u0000\u0000\u000035\u0003\u001a\r\u000046\u0003\u000e\u0007"+
		"\u000054\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000067\u0001\u0000"+
		"\u0000\u000078\u0005\t\u0000\u00008\u0007\u0001\u0000\u0000\u00009<\u0003"+
		"\u001a\r\u0000:;\u0005\u0014\u0000\u0000;=\u0003\u0010\b\u0000<:\u0001"+
		"\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000"+
		">?\u0005\u0013\u0000\u0000?@\u0005\u0003\u0000\u0000@A\u0003\n\u0005\u0000"+
		"AB\u0005\u0004\u0000\u0000B\t\u0001\u0000\u0000\u0000CH\u0003\f\u0006"+
		"\u0000DE\u0005\t\u0000\u0000EG\u0003\f\u0006\u0000FD\u0001\u0000\u0000"+
		"\u0000GJ\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HI\u0001\u0000"+
		"\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000KM\u0005"+
		"\t\u0000\u0000LK\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000M\u000b"+
		"\u0001\u0000\u0000\u0000NQ\u0005$\u0000\u0000OP\u0005\f\u0000\u0000PR"+
		"\u0005$\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000"+
		"RS\u0001\u0000\u0000\u0000ST\u0003\u000e\u0007\u0000T\r\u0001\u0000\u0000"+
		"\u0000UV\u0005\b\u0000\u0000VW\u0003\u0010\b\u0000W\u000f\u0001\u0000"+
		"\u0000\u0000XY\u0006\b\uffff\uffff\u0000YZ\u0007\u0000\u0000\u0000Zk\u0003"+
		"\u0010\b\t[\\\u0005\u0001\u0000\u0000\\]\u0003\u0010\b\u0000]^\u0005\u0002"+
		"\u0000\u0000^k\u0001\u0000\u0000\u0000_`\u0005\u0001\u0000\u0000`a\u0003"+
		"\u0010\b\u0000ab\u0005\n\u0000\u0000bc\u0003\u0010\b\u0000cd\u0005\u0002"+
		"\u0000\u0000dk\u0001\u0000\u0000\u0000ek\u0007\u0001\u0000\u0000fk\u0005"+
		"(\u0000\u0000gk\u0005$\u0000\u0000hi\u0005\u001a\u0000\u0000ik\u0003\u0014"+
		"\n\u0000jX\u0001\u0000\u0000\u0000j[\u0001\u0000\u0000\u0000j_\u0001\u0000"+
		"\u0000\u0000je\u0001\u0000\u0000\u0000jf\u0001\u0000\u0000\u0000jg\u0001"+
		"\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000kt\u0001\u0000\u0000\u0000"+
		"lm\n\u0007\u0000\u0000mn\u0007\u0002\u0000\u0000ns\u0003\u0010\b\bop\n"+
		"\u0006\u0000\u0000pq\u0007\u0000\u0000\u0000qs\u0003\u0010\b\u0007rl\u0001"+
		"\u0000\u0000\u0000ro\u0001\u0000\u0000\u0000sv\u0001\u0000\u0000\u0000"+
		"tr\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000u\u0011\u0001\u0000"+
		"\u0000\u0000vt\u0001\u0000\u0000\u0000wx\u0005\u0016\u0000\u0000x|\u0005"+
		"$\u0000\u0000yz\u0005\u001e\u0000\u0000z{\u0007\u0001\u0000\u0000{}\u0005"+
		"\u001f\u0000\u0000|y\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000"+
		"}~\u0001\u0000\u0000\u0000~\u0087\u0005\t\u0000\u0000\u007f\u0080\u0005"+
		"\u0015\u0000\u0000\u0080\u0081\u0003\u0010\b\u0000\u0081\u0082\u0005\t"+
		"\u0000\u0000\u0082\u0087\u0001\u0000\u0000\u0000\u0083\u0084\u0005\u0017"+
		"\u0000\u0000\u0084\u0085\u0005$\u0000\u0000\u0085\u0087\u0005\t\u0000"+
		"\u0000\u0086w\u0001\u0000\u0000\u0000\u0086\u007f\u0001\u0000\u0000\u0000"+
		"\u0086\u0083\u0001\u0000\u0000\u0000\u0087\u0013\u0001\u0000\u0000\u0000"+
		"\u0088\u0089\u0005\u0018\u0000\u0000\u0089\u008a\u0003\u0016\u000b\u0000"+
		"\u008a\u0015\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u0019\u0000\u0000"+
		"\u008c\u0017\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u001b\u0000\u0000"+
		"\u008e\u008f\u0005$\u0000\u0000\u008f\u0090\u0005\u001c\u0000\u0000\u0090"+
		"\u0091\u0005\'\u0000\u0000\u0091\u0092\u0005\u001d\u0000\u0000\u0092\u0096"+
		"\u0005\u0003\u0000\u0000\u0093\u0095\u0003\u0002\u0001\u0000\u0094\u0093"+
		"\u0001\u0000\u0000\u0000\u0095\u0098\u0001\u0000\u0000\u0000\u0096\u0094"+
		"\u0001\u0000\u0000\u0000\u0096\u0097\u0001\u0000\u0000\u0000\u0097\u0099"+
		"\u0001\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0099\u009a"+
		"\u0005\u0004\u0000\u0000\u009a\u0019\u0001\u0000\u0000\u0000\u009b\u009c"+
		"\u0007\u0003\u0000\u0000\u009c\u001b\u0001\u0000\u0000\u0000\u000e\u001f"+
		"+15<HLQjrt|\u0086\u0096";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}