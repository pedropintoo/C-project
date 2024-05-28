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
		SEMI=9, COMMA=10, TWODOTS=11, DOT=12, DOUBLECOLON=13, INTEGER=14, NUMBER=15, 
		STRING_=16, POINT=17, VECTOR=18, TIME=19, BOOLEAN_=20, VIEW=21, LINE=22, 
		RECTANGLE=23, ELLIPSE=24, ARC=25, ARCHORD=26, PIESLICE=27, TEXT=28, DOTTYPE=29, 
		POLYLINE=30, SPLINE=31, POLYGON=32, BLOB=33, Model=34, Enum=35, SCRIPT=36, 
		WITH=37, AT=38, PRINT=39, REFRESH=40, CLOSE=41, MOUSE=42, CLICK=43, WAIT=44, 
		INPUT=45, LOAD=46, PLAY=47, FOR=48, WHILE=49, REPEAT=50, UNTIL=51, IF=52, 
		ELSE=53, IN=54, DO=55, AFTER=56, MS=57, S=58, MOVE=59, BY=60, TO=61, ACTION=62, 
		ON=63, PLUS=64, MINUS=65, MUL=66, DIV=67, RELATIONAL_OPERATOR=68, AND=69, 
		OR=70, NOT=71, ID=72, NAME=73, BOOLEAN=74, INT=75, FLOAT=76, STRING=77, 
		LINE_COMMENT=78, COMMENT=79, WS=80, ERROR=81;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_repetitiveStatement = 2, RULE_instantiation = 3, 
		RULE_simpleStatement = 4, RULE_blockStatement = 5, RULE_propertiesAssignment = 6, 
		RULE_longAssignment = 7, RULE_assignment = 8, RULE_in_assignment = 9, 
		RULE_expression = 10, RULE_command = 11, RULE_eventTrigger = 12, RULE_mouseTrigger = 13, 
		RULE_forStatement = 14, RULE_number_range = 15, RULE_whileStatement = 16, 
		RULE_repeatStatement = 17, RULE_withStatement = 18, RULE_playStatement = 19, 
		RULE_modelInstantiation = 20, RULE_action = 21, RULE_ifStatement = 22, 
		RULE_typeID = 23, RULE_identifier = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "repetitiveStatement", "instantiation", "simpleStatement", 
			"blockStatement", "propertiesAssignment", "longAssignment", "assignment", 
			"in_assignment", "expression", "command", "eventTrigger", "mouseTrigger", 
			"forStatement", "number_range", "whileStatement", "repeatStatement", 
			"withStatement", "playStatement", "modelInstantiation", "action", "ifStatement", 
			"typeID", "identifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "';'", 
			"','", "'..'", "'.'", "'::'", "'Integer'", "'Number'", "'String'", "'Point'", 
			"'Vector'", "'Time'", "'Boolean'", "'View'", "'Line'", "'Rectangle'", 
			"'Ellipse'", "'Arc'", "'ArcChord'", "'PieSlice'", "'Text'", "'Dot'", 
			"'PolyLine'", "'Spline'", "'Polygon'", "'Blob'", "'Model'", "'Enum'", 
			"'Script'", "'with'", "'at'", "'print'", "'refresh'", "'close'", "'mouse'", 
			"'click'", "'wait'", "'input'", "'load'", "'play'", "'for'", "'while'", 
			"'repeat'", "'until'", "'if'", "'else'", "'in'", "'do'", "'after'", "'ms'", 
			"'s'", "'move'", "'by'", "'to'", "'action'", "'on'", "'+'", "'-'", "'*'", 
			"'/'", null, "'&&'", "'||'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COLON", 
			"EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "DOUBLECOLON", "INTEGER", 
			"NUMBER", "STRING_", "POINT", "VECTOR", "TIME", "BOOLEAN_", "VIEW", "LINE", 
			"RECTANGLE", "ELLIPSE", "ARC", "ARCHORD", "PIESLICE", "TEXT", "DOTTYPE", 
			"POLYLINE", "SPLINE", "POLYGON", "BLOB", "Model", "Enum", "SCRIPT", "WITH", 
			"AT", "PRINT", "REFRESH", "CLOSE", "MOUSE", "CLICK", "WAIT", "INPUT", 
			"LOAD", "PLAY", "FOR", "WHILE", "REPEAT", "UNTIL", "IF", "ELSE", "IN", 
			"DO", "AFTER", "MS", "S", "MOVE", "BY", "TO", "ACTION", "ON", "PLUS", 
			"MINUS", "MUL", "DIV", "RELATIONAL_OPERATOR", "AND", "OR", "NOT", "ID", 
			"NAME", "BOOLEAN", "INT", "FLOAT", "STRING", "LINE_COMMENT", "COMMENT", 
			"WS", "ERROR"
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


	static protected Map<String, Symbol> symbolTable = new HashMap<>();

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
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 583079520244842504L) != 0) || _la==ID) {
				{
				{
				setState(50);
				stat();
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
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
	public static class StatBlockContext extends StatContext {
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public StatBlockContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatBlock(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatIfStatementContext extends StatContext {
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public StatIfStatementContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatIfStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatIfStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatIfStatement(this);
			else return visitor.visitChildren(this);
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
	public static class StatWithStatementContext extends StatContext {
		public WithStatementContext withStatement() {
			return getRuleContext(WithStatementContext.class,0);
		}
		public StatWithStatementContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatWithStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatWithStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatWithStatement(this);
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
	@SuppressWarnings("CheckReturnValue")
	public static class StatRepetitiveStatementContext extends StatContext {
		public RepetitiveStatementContext repetitiveStatement() {
			return getRuleContext(RepetitiveStatementContext.class,0);
		}
		public StatRepetitiveStatementContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatRepetitiveStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatRepetitiveStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatRepetitiveStatement(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatPlayStatementContext extends StatContext {
		public PlayStatementContext playStatement() {
			return getRuleContext(PlayStatementContext.class,0);
		}
		public StatPlayStatementContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatPlayStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatPlayStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatPlayStatement(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatModelInstantiationContext extends StatContext {
		public ModelInstantiationContext modelInstantiation() {
			return getRuleContext(ModelInstantiationContext.class,0);
		}
		public StatModelInstantiationContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterStatModelInstantiation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitStatModelInstantiation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitStatModelInstantiation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		int _la;
		try {
			setState(77);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new StatInstantiationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(58);
				instantiation();
				}
				break;
			case 2:
				_localctx = new StatModelInstantiationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				modelInstantiation();
				}
				break;
			case 3:
				_localctx = new StatBlockStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(60);
				blockStatement();
				}
				break;
			case 4:
				_localctx = new StatLongAssignmentContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(61);
				longAssignment();
				setState(62);
				match(SEMI);
				}
				break;
			case 5:
				_localctx = new StatWithStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(64);
				withStatement();
				}
				break;
			case 6:
				_localctx = new StatPlayStatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(65);
				playStatement();
				}
				break;
			case 7:
				_localctx = new StatRepetitiveStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(66);
				repetitiveStatement();
				}
				break;
			case 8:
				_localctx = new StatIfStatementContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(67);
				ifStatement();
				}
				break;
			case 9:
				_localctx = new StatCommandContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(68);
				command();
				}
				break;
			case 10:
				_localctx = new StatBlockContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(69);
				match(LBRACE);
				setState(71); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(70);
					stat();
					}
					}
					setState(73); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 583079520244842504L) != 0) || _la==ID );
				setState(75);
				match(RBRACE);
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
	public static class RepetitiveStatementContext extends ParserRuleContext {
		public RepetitiveStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repetitiveStatement; }
	 
		public RepetitiveStatementContext() { }
		public void copyFrom(RepetitiveStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RepWhileStatementContext extends RepetitiveStatementContext {
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public RepWhileStatementContext(RepetitiveStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterRepWhileStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitRepWhileStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitRepWhileStatement(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RepForStatementContext extends RepetitiveStatementContext {
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public RepForStatementContext(RepetitiveStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterRepForStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitRepForStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitRepForStatement(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RepRepeatStatementContext extends RepetitiveStatementContext {
		public RepeatStatementContext repeatStatement() {
			return getRuleContext(RepeatStatementContext.class,0);
		}
		public RepRepeatStatementContext(RepetitiveStatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterRepRepeatStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitRepRepeatStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitRepRepeatStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RepetitiveStatementContext repetitiveStatement() throws RecognitionException {
		RepetitiveStatementContext _localctx = new RepetitiveStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_repetitiveStatement);
		try {
			setState(82);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FOR:
				_localctx = new RepForStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				forStatement();
				}
				break;
			case WHILE:
				_localctx = new RepWhileStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				whileStatement();
				}
				break;
			case REPEAT:
				_localctx = new RepRepeatStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(81);
				repeatStatement();
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
		enterRule(_localctx, 6, RULE_instantiation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(ID);
			setState(85);
			match(COLON);
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(86);
				simpleStatement();
				}
				break;
			case 2:
				{
				setState(87);
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
		public In_assignmentContext in_assignment() {
			return getRuleContext(In_assignmentContext.class,0);
		}
		public TerminalNode AT() { return getToken(AGLParser.AT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
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
		enterRule(_localctx, 8, RULE_simpleStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			typeID();
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AT) {
				{
				setState(91);
				match(AT);
				setState(92);
				expression(0);
				}
			}

			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUAL:
			case SEMI:
				{
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EQUAL) {
					{
					setState(95);
					assignment();
					}
				}

				setState(98);
				match(SEMI);
				}
				break;
			case IN:
				{
				setState(99);
				in_assignment();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class BlockStatementContext extends ParserRuleContext {
		public String varName;
		public TypeIDContext typeID() {
			return getRuleContext(TypeIDContext.class,0);
		}
		public TerminalNode WITH() { return getToken(AGLParser.WITH, 0); }
		public PropertiesAssignmentContext propertiesAssignment() {
			return getRuleContext(PropertiesAssignmentContext.class,0);
		}
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
		enterRule(_localctx, 10, RULE_blockStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			typeID();
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AT) {
				{
				setState(103);
				match(AT);
				setState(104);
				expression(0);
				}
			}

			setState(107);
			match(WITH);
			setState(108);
			propertiesAssignment();
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
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public List<LongAssignmentContext> longAssignment() {
			return getRuleContexts(LongAssignmentContext.class);
		}
		public LongAssignmentContext longAssignment(int i) {
			return getRuleContext(LongAssignmentContext.class,i);
		}
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
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
		enterRule(_localctx, 12, RULE_propertiesAssignment);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(LBRACE);
			setState(111);
			longAssignment();
			setState(116);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(112);
					match(SEMI);
					setState(113);
					longAssignment();
					}
					} 
				}
				setState(118);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(119);
				match(SEMI);
				}
			}

			setState(122);
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
	public static class LongAssignmentContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
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
		enterRule(_localctx, 14, RULE_longAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			identifier();
			setState(125);
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
		public Type eType;
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
		enterRule(_localctx, 16, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(EQUAL);
			setState(128);
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
	public static class In_assignmentContext extends ParserRuleContext {
		public TerminalNode IN() { return getToken(AGLParser.IN, 0); }
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public List<TerminalNode> ID() { return getTokens(AGLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(AGLParser.ID, i);
		}
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AGLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AGLParser.COMMA, i);
		}
		public In_assignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_in_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterIn_assignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitIn_assignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitIn_assignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final In_assignmentContext in_assignment() throws RecognitionException {
		In_assignmentContext _localctx = new In_assignmentContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_in_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(IN);
			setState(131);
			match(LBRACE);
			setState(132);
			match(ID);
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(133);
				match(COMMA);
				setState(134);
				match(ID);
				}
				}
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(140);
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
	public static class ExpressionContext extends ParserRuleContext {
		public Type eType;
		public String varName;
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
			this.eType = ctx.eType;
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
	public static class ExprAddSubMultDivAndOrContext extends ExpressionContext {
		public ExpressionContext e1;
		public Token op;
		public ExpressionContext e2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(AGLParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(AGLParser.DIV, 0); }
		public TerminalNode AND() { return getToken(AGLParser.AND, 0); }
		public TerminalNode PLUS() { return getToken(AGLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AGLParser.MINUS, 0); }
		public TerminalNode OR() { return getToken(AGLParser.OR, 0); }
		public ExprAddSubMultDivAndOrContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprAddSubMultDivAndOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprAddSubMultDivAndOr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprAddSubMultDivAndOr(this);
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
	public static class ExprBooleanContext extends ExpressionContext {
		public TerminalNode BOOLEAN() { return getToken(AGLParser.BOOLEAN, 0); }
		public ExprBooleanContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprBoolean(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprBoolean(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprBoolean(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprParenthesisContext extends ExpressionContext {
		public ExpressionContext e;
		public TerminalNode LPAREN() { return getToken(AGLParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(AGLParser.RPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
	public static class ExprRelationalContext extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RELATIONAL_OPERATOR() { return getToken(AGLParser.RELATIONAL_OPERATOR, 0); }
		public ExprRelationalContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprRelational(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprRelational(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprRelational(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprArrayContext extends ExpressionContext {
		public TerminalNode LBRACK() { return getToken(AGLParser.LBRACK, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RBRACK() { return getToken(AGLParser.RBRACK, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AGLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AGLParser.COMMA, i);
		}
		public ExprArrayContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprArray(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprArray(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprVectorContext extends ExpressionContext {
		public ExpressionContext x;
		public ExpressionContext y;
		public TerminalNode LPAREN() { return getToken(AGLParser.LPAREN, 0); }
		public TerminalNode COLON() { return getToken(AGLParser.COLON, 0); }
		public TerminalNode RPAREN() { return getToken(AGLParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ExprVectorContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprVector(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprVector(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprVector(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprScriptContext extends ExpressionContext {
		public Token op;
		public TerminalNode STRING() { return getToken(AGLParser.STRING, 0); }
		public TerminalNode INPUT() { return getToken(AGLParser.INPUT, 0); }
		public TerminalNode LOAD() { return getToken(AGLParser.LOAD, 0); }
		public ExprScriptContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprScript(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprScript(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprScript(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprUnaryContext extends ExpressionContext {
		public Token sign;
		public ExpressionContext e;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(AGLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(AGLParser.MINUS, 0); }
		public TerminalNode NOT() { return getToken(AGLParser.NOT, 0); }
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
	public static class ExprIDContext extends ExpressionContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
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

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				_localctx = new ExprUnaryContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(143);
				((ExprUnaryContext)_localctx).sign = _input.LT(1);
				_la = _input.LA(1);
				if ( !(((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 131L) != 0)) ) {
					((ExprUnaryContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(144);
				((ExprUnaryContext)_localctx).e = expression(14);
				}
				break;
			case 2:
				{
				_localctx = new ExprParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(145);
				match(LPAREN);
				setState(146);
				((ExprParenthesisContext)_localctx).e = expression(0);
				setState(147);
				match(RPAREN);
				}
				break;
			case 3:
				{
				_localctx = new ExprPointContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(149);
				match(LPAREN);
				setState(150);
				((ExprPointContext)_localctx).x = expression(0);
				setState(151);
				match(COMMA);
				setState(152);
				((ExprPointContext)_localctx).y = expression(0);
				setState(153);
				match(RPAREN);
				}
				break;
			case 4:
				{
				_localctx = new ExprVectorContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(155);
				match(LPAREN);
				setState(156);
				((ExprVectorContext)_localctx).x = expression(0);
				setState(157);
				match(COLON);
				setState(158);
				((ExprVectorContext)_localctx).y = expression(0);
				setState(159);
				match(RPAREN);
				}
				break;
			case 5:
				{
				_localctx = new ExprArrayContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(161);
				match(LBRACK);
				setState(162);
				expression(0);
				setState(167);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(163);
					match(COMMA);
					setState(164);
					expression(0);
					}
					}
					setState(169);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(170);
				match(RBRACK);
				}
				break;
			case 6:
				{
				_localctx = new ExprNumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(172);
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
			case 7:
				{
				_localctx = new ExprBooleanContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(173);
				match(BOOLEAN);
				}
				break;
			case 8:
				{
				_localctx = new ExprStringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(174);
				match(STRING);
				}
				break;
			case 9:
				{
				_localctx = new ExprIDContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(175);
				identifier();
				}
				break;
			case 10:
				{
				_localctx = new ExprWaitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(176);
				match(WAIT);
				setState(177);
				eventTrigger();
				}
				break;
			case 11:
				{
				_localctx = new ExprScriptContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(178);
				((ExprScriptContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==INPUT || _la==LOAD) ) {
					((ExprScriptContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(179);
				match(STRING);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(193);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(191);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new ExprAddSubMultDivAndOrContext(new ExpressionContext(_parentctx, _parentState));
						((ExprAddSubMultDivAndOrContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(182);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(183);
						((ExprAddSubMultDivAndOrContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 11L) != 0)) ) {
							((ExprAddSubMultDivAndOrContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(184);
						((ExprAddSubMultDivAndOrContext)_localctx).e2 = expression(13);
						}
						break;
					case 2:
						{
						_localctx = new ExprAddSubMultDivAndOrContext(new ExpressionContext(_parentctx, _parentState));
						((ExprAddSubMultDivAndOrContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(185);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(186);
						((ExprAddSubMultDivAndOrContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 67L) != 0)) ) {
							((ExprAddSubMultDivAndOrContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(187);
						((ExprAddSubMultDivAndOrContext)_localctx).e2 = expression(12);
						}
						break;
					case 3:
						{
						_localctx = new ExprRelationalContext(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(188);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(189);
						match(RELATIONAL_OPERATOR);
						setState(190);
						expression(8);
						}
						break;
					}
					} 
				}
				setState(195);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
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
	public static class CommandMoveContext extends CommandContext {
		public Token type;
		public TerminalNode MOVE() { return getToken(AGLParser.MOVE, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public TerminalNode BY() { return getToken(AGLParser.BY, 0); }
		public TerminalNode TO() { return getToken(AGLParser.TO, 0); }
		public CommandMoveContext(CommandContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterCommandMove(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitCommandMove(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitCommandMove(this);
			else return visitor.visitChildren(this);
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
		public Token suffix;
		public TerminalNode REFRESH() { return getToken(AGLParser.REFRESH, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public TerminalNode AFTER() { return getToken(AGLParser.AFTER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode MS() { return getToken(AGLParser.MS, 0); }
		public TerminalNode S() { return getToken(AGLParser.S, 0); }
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
		enterRule(_localctx, 22, RULE_command);
		int _la;
		try {
			setState(218);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REFRESH:
				_localctx = new CommandRefreshContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(REFRESH);
				setState(197);
				match(ID);
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AFTER) {
					{
					setState(198);
					match(AFTER);
					setState(199);
					expression(0);
					setState(200);
					((CommandRefreshContext)_localctx).suffix = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==MS || _la==S) ) {
						((CommandRefreshContext)_localctx).suffix = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(204);
				match(SEMI);
				}
				break;
			case PRINT:
				_localctx = new CommandPrintContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(205);
				match(PRINT);
				setState(206);
				expression(0);
				setState(207);
				match(SEMI);
				}
				break;
			case CLOSE:
				_localctx = new CommandCloseContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(209);
				match(CLOSE);
				setState(210);
				match(ID);
				setState(211);
				match(SEMI);
				}
				break;
			case MOVE:
				_localctx = new CommandMoveContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(212);
				match(MOVE);
				setState(213);
				identifier();
				setState(214);
				((CommandMoveContext)_localctx).type = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==BY || _la==TO) ) {
					((CommandMoveContext)_localctx).type = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(215);
				expression(0);
				setState(216);
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
		enterRule(_localctx, 24, RULE_eventTrigger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(MOUSE);
			setState(221);
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
		enterRule(_localctx, 26, RULE_mouseTrigger);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
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
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(AGLParser.FOR, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode IN() { return getToken(AGLParser.IN, 0); }
		public Number_rangeContext number_range() {
			return getRuleContext(Number_rangeContext.class,0);
		}
		public TerminalNode DO() { return getToken(AGLParser.DO, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterForStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitForStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitForStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_forStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(FOR);
			setState(226);
			match(ID);
			setState(227);
			match(IN);
			setState(228);
			number_range();
			setState(229);
			match(DO);
			setState(230);
			stat();
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
	public static class Number_rangeContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> TWODOTS() { return getTokens(AGLParser.TWODOTS); }
		public TerminalNode TWODOTS(int i) {
			return getToken(AGLParser.TWODOTS, i);
		}
		public Number_rangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number_range; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterNumber_range(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitNumber_range(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitNumber_range(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Number_rangeContext number_range() throws RecognitionException {
		Number_rangeContext _localctx = new Number_rangeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_number_range);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			expression(0);
			setState(233);
			match(TWODOTS);
			setState(234);
			expression(0);
			setState(237);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TWODOTS) {
				{
				setState(235);
				match(TWODOTS);
				setState(236);
				expression(0);
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
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(AGLParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DO() { return getToken(AGLParser.DO, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterWhileStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitWhileStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitWhileStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(WHILE);
			setState(240);
			expression(0);
			setState(241);
			match(DO);
			setState(242);
			stat();
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
	public static class RepeatStatementContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(AGLParser.REPEAT, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public TerminalNode UNTIL() { return getToken(AGLParser.UNTIL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RepeatStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeatStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterRepeatStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitRepeatStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitRepeatStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RepeatStatementContext repeatStatement() throws RecognitionException {
		RepeatStatementContext _localctx = new RepeatStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_repeatStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			match(REPEAT);
			setState(245);
			stat();
			setState(246);
			match(UNTIL);
			setState(247);
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
	public static class WithStatementContext extends ParserRuleContext {
		public TerminalNode WITH() { return getToken(AGLParser.WITH, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode DO() { return getToken(AGLParser.DO, 0); }
		public PropertiesAssignmentContext propertiesAssignment() {
			return getRuleContext(PropertiesAssignmentContext.class,0);
		}
		public WithStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_withStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterWithStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitWithStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitWithStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WithStatementContext withStatement() throws RecognitionException {
		WithStatementContext _localctx = new WithStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_withStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			match(WITH);
			setState(250);
			identifier();
			setState(251);
			match(DO);
			setState(252);
			propertiesAssignment();
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
	public static class PlayStatementContext extends ParserRuleContext {
		public TerminalNode PLAY() { return getToken(AGLParser.PLAY, 0); }
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode WITH() { return getToken(AGLParser.WITH, 0); }
		public PropertiesAssignmentContext propertiesAssignment() {
			return getRuleContext(PropertiesAssignmentContext.class,0);
		}
		public PlayStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_playStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterPlayStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitPlayStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitPlayStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PlayStatementContext playStatement() throws RecognitionException {
		PlayStatementContext _localctx = new PlayStatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_playStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(PLAY);
			setState(255);
			match(ID);
			setState(256);
			match(WITH);
			setState(257);
			propertiesAssignment();
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
	public static class ModelInstantiationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode DOUBLECOLON() { return getToken(AGLParser.DOUBLECOLON, 0); }
		public TerminalNode Model() { return getToken(AGLParser.Model, 0); }
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public List<InstantiationContext> instantiation() {
			return getRuleContexts(InstantiationContext.class);
		}
		public InstantiationContext instantiation(int i) {
			return getRuleContext(InstantiationContext.class,i);
		}
		public List<BlockStatementContext> blockStatement() {
			return getRuleContexts(BlockStatementContext.class);
		}
		public BlockStatementContext blockStatement(int i) {
			return getRuleContext(BlockStatementContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
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
		public ModelInstantiationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modelInstantiation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterModelInstantiation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitModelInstantiation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitModelInstantiation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ModelInstantiationContext modelInstantiation() throws RecognitionException {
		ModelInstantiationContext _localctx = new ModelInstantiationContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_modelInstantiation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(ID);
			setState(260);
			match(DOUBLECOLON);
			setState(261);
			match(Model);
			setState(262);
			match(LBRACE);
			setState(269); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(269);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
				case 1:
					{
					setState(263);
					instantiation();
					}
					break;
				case 2:
					{
					setState(264);
					blockStatement();
					}
					break;
				case 3:
					{
					setState(265);
					action();
					}
					break;
				case 4:
					{
					setState(266);
					longAssignment();
					setState(267);
					match(SEMI);
					}
					break;
				}
				}
				setState(271); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( ((((_la - 14)) & ~0x3f) == 0 && ((1L << (_la - 14)) & 288511851135762431L) != 0) );
			setState(273);
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
	public static class ActionContext extends ParserRuleContext {
		public TerminalNode ACTION() { return getToken(AGLParser.ACTION, 0); }
		public TerminalNode ON() { return getToken(AGLParser.ON, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitAction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitAction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_action);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(ACTION);
			setState(276);
			match(ON);
			setState(277);
			identifier();
			setState(278);
			stat();
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
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(AGLParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> DO() { return getTokens(AGLParser.DO); }
		public TerminalNode DO(int i) {
			return getToken(AGLParser.DO, i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(AGLParser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterIfStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitIfStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitIfStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			match(IF);
			setState(281);
			expression(0);
			setState(282);
			match(DO);
			setState(283);
			stat();
			setState(287);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(284);
				match(ELSE);
				setState(285);
				match(DO);
				setState(286);
				stat();
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
	public static class TypeIDContext extends ParserRuleContext {
		public Type res;
		public TerminalNode INTEGER() { return getToken(AGLParser.INTEGER, 0); }
		public TerminalNode STRING_() { return getToken(AGLParser.STRING_, 0); }
		public TerminalNode POINT() { return getToken(AGLParser.POINT, 0); }
		public TerminalNode NUMBER() { return getToken(AGLParser.NUMBER, 0); }
		public TerminalNode VECTOR() { return getToken(AGLParser.VECTOR, 0); }
		public TerminalNode TIME() { return getToken(AGLParser.TIME, 0); }
		public TerminalNode BOOLEAN_() { return getToken(AGLParser.BOOLEAN_, 0); }
		public TerminalNode VIEW() { return getToken(AGLParser.VIEW, 0); }
		public TerminalNode LINE() { return getToken(AGLParser.LINE, 0); }
		public TerminalNode RECTANGLE() { return getToken(AGLParser.RECTANGLE, 0); }
		public TerminalNode ELLIPSE() { return getToken(AGLParser.ELLIPSE, 0); }
		public TerminalNode ARC() { return getToken(AGLParser.ARC, 0); }
		public TerminalNode ARCHORD() { return getToken(AGLParser.ARCHORD, 0); }
		public TerminalNode PIESLICE() { return getToken(AGLParser.PIESLICE, 0); }
		public TerminalNode TEXT() { return getToken(AGLParser.TEXT, 0); }
		public TerminalNode DOTTYPE() { return getToken(AGLParser.DOTTYPE, 0); }
		public TerminalNode POLYLINE() { return getToken(AGLParser.POLYLINE, 0); }
		public TerminalNode SPLINE() { return getToken(AGLParser.SPLINE, 0); }
		public TerminalNode POLYGON() { return getToken(AGLParser.POLYGON, 0); }
		public TerminalNode BLOB() { return getToken(AGLParser.BLOB, 0); }
		public TerminalNode SCRIPT() { return getToken(AGLParser.SCRIPT, 0); }
		public TerminalNode Enum() { return getToken(AGLParser.Enum, 0); }
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
		enterRule(_localctx, 46, RULE_typeID);
		try {
			setState(334);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(289);
				match(INTEGER);
				((TypeIDContext)_localctx).res =  new IntegerType();
				}
				break;
			case STRING_:
				enterOuterAlt(_localctx, 2);
				{
				setState(291);
				match(STRING_);
				((TypeIDContext)_localctx).res =  new StringType();
				}
				break;
			case POINT:
				enterOuterAlt(_localctx, 3);
				{
				setState(293);
				match(POINT);
				((TypeIDContext)_localctx).res =  new PointType();
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 4);
				{
				setState(295);
				match(NUMBER);
				((TypeIDContext)_localctx).res =  new NumberType();
				}
				break;
			case VECTOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(297);
				match(VECTOR);
				((TypeIDContext)_localctx).res =  new VectorType();
				}
				break;
			case TIME:
				enterOuterAlt(_localctx, 6);
				{
				setState(299);
				match(TIME);
				((TypeIDContext)_localctx).res =  new TimeType();
				}
				break;
			case BOOLEAN_:
				enterOuterAlt(_localctx, 7);
				{
				setState(301);
				match(BOOLEAN_);
				((TypeIDContext)_localctx).res =  new BooleanType();
				}
				break;
			case VIEW:
				enterOuterAlt(_localctx, 8);
				{
				setState(303);
				match(VIEW);
				((TypeIDContext)_localctx).res =  new ObjectType("View");
				}
				break;
			case LINE:
				enterOuterAlt(_localctx, 9);
				{
				setState(305);
				match(LINE);
				((TypeIDContext)_localctx).res =  new ObjectType("Line");
				}
				break;
			case RECTANGLE:
				enterOuterAlt(_localctx, 10);
				{
				setState(307);
				match(RECTANGLE);
				((TypeIDContext)_localctx).res =  new ObjectType("Rectangle");
				}
				break;
			case ELLIPSE:
				enterOuterAlt(_localctx, 11);
				{
				setState(309);
				match(ELLIPSE);
				((TypeIDContext)_localctx).res =  new ObjectType("Ellipse");
				}
				break;
			case ARC:
				enterOuterAlt(_localctx, 12);
				{
				setState(311);
				match(ARC);
				((TypeIDContext)_localctx).res =  new ObjectType("Arc");
				}
				break;
			case ARCHORD:
				enterOuterAlt(_localctx, 13);
				{
				setState(313);
				match(ARCHORD);
				((TypeIDContext)_localctx).res =  new ObjectType("ArcChord");
				}
				break;
			case PIESLICE:
				enterOuterAlt(_localctx, 14);
				{
				setState(315);
				match(PIESLICE);
				((TypeIDContext)_localctx).res =  new ObjectType("PieSlice");
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 15);
				{
				setState(317);
				match(TEXT);
				((TypeIDContext)_localctx).res =  new ObjectType("Text");
				}
				break;
			case DOTTYPE:
				enterOuterAlt(_localctx, 16);
				{
				setState(319);
				match(DOTTYPE);
				((TypeIDContext)_localctx).res =  new ObjectType("Dot");
				}
				break;
			case POLYLINE:
				enterOuterAlt(_localctx, 17);
				{
				setState(321);
				match(POLYLINE);
				((TypeIDContext)_localctx).res =  new ObjectType("PolyLine");
				}
				break;
			case SPLINE:
				enterOuterAlt(_localctx, 18);
				{
				setState(323);
				match(SPLINE);
				((TypeIDContext)_localctx).res =  new ObjectType("Spline");
				}
				break;
			case POLYGON:
				enterOuterAlt(_localctx, 19);
				{
				setState(325);
				match(POLYGON);
				((TypeIDContext)_localctx).res =  new ObjectType("Polygon");
				}
				break;
			case BLOB:
				enterOuterAlt(_localctx, 20);
				{
				setState(327);
				match(BLOB);
				((TypeIDContext)_localctx).res =  new ObjectType("Blob");
				}
				break;
			case SCRIPT:
				enterOuterAlt(_localctx, 21);
				{
				setState(329);
				match(SCRIPT);
				((TypeIDContext)_localctx).res =  new ObjectType("Script");
				}
				break;
			case Enum:
				enterOuterAlt(_localctx, 22);
				{
				setState(331);
				match(Enum);
				((TypeIDContext)_localctx).res =  new ObjectType("Enum");
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 23);
				{
				setState(333);
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
	public static class IdentifierContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(AGLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(AGLParser.ID, i);
		}
		public List<TerminalNode> DOT() { return getTokens(AGLParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(AGLParser.DOT, i);
		}
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitIdentifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_identifier);
		try {
			int _alt;
			setState(344);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(336);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(337);
				match(ID);
				setState(340); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(338);
						match(DOT);
						setState(339);
						match(ID);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(342); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 12);
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001Q\u015b\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0001\u0000\u0005\u00004\b\u0000\n\u0000\f\u00007\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0004\u0001H\b\u0001\u000b\u0001\f\u0001I\u0001"+
		"\u0001\u0001\u0001\u0003\u0001N\b\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002S\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003Y\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004^\b\u0004\u0001\u0004\u0003\u0004a\b\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004e\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"j\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0005\u0006s\b\u0006\n\u0006\f\u0006v\t\u0006"+
		"\u0001\u0006\u0003\u0006y\b\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0005\t\u0088\b\t\n\t\f\t\u008b\t\t\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u00a6\b\n\n\n\f\n\u00a9"+
		"\t\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u00b5\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\n\u00c0\b\n\n\n\f\n\u00c3\t\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u00cb\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00db\b\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00ee\b\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0004\u0014\u010e"+
		"\b\u0014\u000b\u0014\f\u0014\u010f\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016"+
		"\u0120\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u014f\b\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0004\u0018\u0155\b\u0018"+
		"\u000b\u0018\f\u0018\u0156\u0003\u0018\u0159\b\u0018\u0001\u0018\u0000"+
		"\u0001\u0014\u0019\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.0\u0000\u0007\u0002\u0000@AGG\u0001"+
		"\u0000KL\u0001\u0000-.\u0002\u0000BCEE\u0002\u0000@AFF\u0001\u00009:\u0001"+
		"\u0000<=\u0186\u00005\u0001\u0000\u0000\u0000\u0002M\u0001\u0000\u0000"+
		"\u0000\u0004R\u0001\u0000\u0000\u0000\u0006T\u0001\u0000\u0000\u0000\b"+
		"Z\u0001\u0000\u0000\u0000\nf\u0001\u0000\u0000\u0000\fn\u0001\u0000\u0000"+
		"\u0000\u000e|\u0001\u0000\u0000\u0000\u0010\u007f\u0001\u0000\u0000\u0000"+
		"\u0012\u0082\u0001\u0000\u0000\u0000\u0014\u00b4\u0001\u0000\u0000\u0000"+
		"\u0016\u00da\u0001\u0000\u0000\u0000\u0018\u00dc\u0001\u0000\u0000\u0000"+
		"\u001a\u00df\u0001\u0000\u0000\u0000\u001c\u00e1\u0001\u0000\u0000\u0000"+
		"\u001e\u00e8\u0001\u0000\u0000\u0000 \u00ef\u0001\u0000\u0000\u0000\""+
		"\u00f4\u0001\u0000\u0000\u0000$\u00f9\u0001\u0000\u0000\u0000&\u00fe\u0001"+
		"\u0000\u0000\u0000(\u0103\u0001\u0000\u0000\u0000*\u0113\u0001\u0000\u0000"+
		"\u0000,\u0118\u0001\u0000\u0000\u0000.\u014e\u0001\u0000\u0000\u00000"+
		"\u0158\u0001\u0000\u0000\u000024\u0003\u0002\u0001\u000032\u0001\u0000"+
		"\u0000\u000047\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u000056\u0001"+
		"\u0000\u0000\u000068\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u0000"+
		"89\u0005\u0000\u0000\u00019\u0001\u0001\u0000\u0000\u0000:N\u0003\u0006"+
		"\u0003\u0000;N\u0003(\u0014\u0000<N\u0003\n\u0005\u0000=>\u0003\u000e"+
		"\u0007\u0000>?\u0005\t\u0000\u0000?N\u0001\u0000\u0000\u0000@N\u0003$"+
		"\u0012\u0000AN\u0003&\u0013\u0000BN\u0003\u0004\u0002\u0000CN\u0003,\u0016"+
		"\u0000DN\u0003\u0016\u000b\u0000EG\u0005\u0003\u0000\u0000FH\u0003\u0002"+
		"\u0001\u0000GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IG\u0001"+
		"\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000"+
		"KL\u0005\u0004\u0000\u0000LN\u0001\u0000\u0000\u0000M:\u0001\u0000\u0000"+
		"\u0000M;\u0001\u0000\u0000\u0000M<\u0001\u0000\u0000\u0000M=\u0001\u0000"+
		"\u0000\u0000M@\u0001\u0000\u0000\u0000MA\u0001\u0000\u0000\u0000MB\u0001"+
		"\u0000\u0000\u0000MC\u0001\u0000\u0000\u0000MD\u0001\u0000\u0000\u0000"+
		"ME\u0001\u0000\u0000\u0000N\u0003\u0001\u0000\u0000\u0000OS\u0003\u001c"+
		"\u000e\u0000PS\u0003 \u0010\u0000QS\u0003\"\u0011\u0000RO\u0001\u0000"+
		"\u0000\u0000RP\u0001\u0000\u0000\u0000RQ\u0001\u0000\u0000\u0000S\u0005"+
		"\u0001\u0000\u0000\u0000TU\u0005H\u0000\u0000UX\u0005\u0007\u0000\u0000"+
		"VY\u0003\b\u0004\u0000WY\u0003\n\u0005\u0000XV\u0001\u0000\u0000\u0000"+
		"XW\u0001\u0000\u0000\u0000Y\u0007\u0001\u0000\u0000\u0000Z]\u0003.\u0017"+
		"\u0000[\\\u0005&\u0000\u0000\\^\u0003\u0014\n\u0000][\u0001\u0000\u0000"+
		"\u0000]^\u0001\u0000\u0000\u0000^d\u0001\u0000\u0000\u0000_a\u0003\u0010"+
		"\b\u0000`_\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000ab\u0001\u0000"+
		"\u0000\u0000be\u0005\t\u0000\u0000ce\u0003\u0012\t\u0000d`\u0001\u0000"+
		"\u0000\u0000dc\u0001\u0000\u0000\u0000e\t\u0001\u0000\u0000\u0000fi\u0003"+
		".\u0017\u0000gh\u0005&\u0000\u0000hj\u0003\u0014\n\u0000ig\u0001\u0000"+
		"\u0000\u0000ij\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000kl\u0005"+
		"%\u0000\u0000lm\u0003\f\u0006\u0000m\u000b\u0001\u0000\u0000\u0000no\u0005"+
		"\u0003\u0000\u0000ot\u0003\u000e\u0007\u0000pq\u0005\t\u0000\u0000qs\u0003"+
		"\u000e\u0007\u0000rp\u0001\u0000\u0000\u0000sv\u0001\u0000\u0000\u0000"+
		"tr\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000"+
		"\u0000vt\u0001\u0000\u0000\u0000wy\u0005\t\u0000\u0000xw\u0001\u0000\u0000"+
		"\u0000xy\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z{\u0005\u0004"+
		"\u0000\u0000{\r\u0001\u0000\u0000\u0000|}\u00030\u0018\u0000}~\u0003\u0010"+
		"\b\u0000~\u000f\u0001\u0000\u0000\u0000\u007f\u0080\u0005\b\u0000\u0000"+
		"\u0080\u0081\u0003\u0014\n\u0000\u0081\u0011\u0001\u0000\u0000\u0000\u0082"+
		"\u0083\u00056\u0000\u0000\u0083\u0084\u0005\u0003\u0000\u0000\u0084\u0089"+
		"\u0005H\u0000\u0000\u0085\u0086\u0005\n\u0000\u0000\u0086\u0088\u0005"+
		"H\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0088\u008b\u0001\u0000"+
		"\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000"+
		"\u0000\u0000\u008a\u008c\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000"+
		"\u0000\u0000\u008c\u008d\u0005\u0004\u0000\u0000\u008d\u0013\u0001\u0000"+
		"\u0000\u0000\u008e\u008f\u0006\n\uffff\uffff\u0000\u008f\u0090\u0007\u0000"+
		"\u0000\u0000\u0090\u00b5\u0003\u0014\n\u000e\u0091\u0092\u0005\u0001\u0000"+
		"\u0000\u0092\u0093\u0003\u0014\n\u0000\u0093\u0094\u0005\u0002\u0000\u0000"+
		"\u0094\u00b5\u0001\u0000\u0000\u0000\u0095\u0096\u0005\u0001\u0000\u0000"+
		"\u0096\u0097\u0003\u0014\n\u0000\u0097\u0098\u0005\n\u0000\u0000\u0098"+
		"\u0099\u0003\u0014\n\u0000\u0099\u009a\u0005\u0002\u0000\u0000\u009a\u00b5"+
		"\u0001\u0000\u0000\u0000\u009b\u009c\u0005\u0001\u0000\u0000\u009c\u009d"+
		"\u0003\u0014\n\u0000\u009d\u009e\u0005\u0007\u0000\u0000\u009e\u009f\u0003"+
		"\u0014\n\u0000\u009f\u00a0\u0005\u0002\u0000\u0000\u00a0\u00b5\u0001\u0000"+
		"\u0000\u0000\u00a1\u00a2\u0005\u0005\u0000\u0000\u00a2\u00a7\u0003\u0014"+
		"\n\u0000\u00a3\u00a4\u0005\n\u0000\u0000\u00a4\u00a6\u0003\u0014\n\u0000"+
		"\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000"+
		"\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000"+
		"\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000"+
		"\u00aa\u00ab\u0005\u0006\u0000\u0000\u00ab\u00b5\u0001\u0000\u0000\u0000"+
		"\u00ac\u00b5\u0007\u0001\u0000\u0000\u00ad\u00b5\u0005J\u0000\u0000\u00ae"+
		"\u00b5\u0005M\u0000\u0000\u00af\u00b5\u00030\u0018\u0000\u00b0\u00b1\u0005"+
		",\u0000\u0000\u00b1\u00b5\u0003\u0018\f\u0000\u00b2\u00b3\u0007\u0002"+
		"\u0000\u0000\u00b3\u00b5\u0005M\u0000\u0000\u00b4\u008e\u0001\u0000\u0000"+
		"\u0000\u00b4\u0091\u0001\u0000\u0000\u0000\u00b4\u0095\u0001\u0000\u0000"+
		"\u0000\u00b4\u009b\u0001\u0000\u0000\u0000\u00b4\u00a1\u0001\u0000\u0000"+
		"\u0000\u00b4\u00ac\u0001\u0000\u0000\u0000\u00b4\u00ad\u0001\u0000\u0000"+
		"\u0000\u00b4\u00ae\u0001\u0000\u0000\u0000\u00b4\u00af\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b0\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b5\u00c1\u0001\u0000\u0000\u0000\u00b6\u00b7\n\f\u0000\u0000"+
		"\u00b7\u00b8\u0007\u0003\u0000\u0000\u00b8\u00c0\u0003\u0014\n\r\u00b9"+
		"\u00ba\n\u000b\u0000\u0000\u00ba\u00bb\u0007\u0004\u0000\u0000\u00bb\u00c0"+
		"\u0003\u0014\n\f\u00bc\u00bd\n\u0007\u0000\u0000\u00bd\u00be\u0005D\u0000"+
		"\u0000\u00be\u00c0\u0003\u0014\n\b\u00bf\u00b6\u0001\u0000\u0000\u0000"+
		"\u00bf\u00b9\u0001\u0000\u0000\u0000\u00bf\u00bc\u0001\u0000\u0000\u0000"+
		"\u00c0\u00c3\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001\u0000\u0000\u0000"+
		"\u00c1\u00c2\u0001\u0000\u0000\u0000\u00c2\u0015\u0001\u0000\u0000\u0000"+
		"\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c4\u00c5\u0005(\u0000\u0000\u00c5"+
		"\u00ca\u0005H\u0000\u0000\u00c6\u00c7\u00058\u0000\u0000\u00c7\u00c8\u0003"+
		"\u0014\n\u0000\u00c8\u00c9\u0007\u0005\u0000\u0000\u00c9\u00cb\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c6\u0001\u0000\u0000\u0000\u00ca\u00cb\u0001\u0000"+
		"\u0000\u0000\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u00db\u0005\t\u0000"+
		"\u0000\u00cd\u00ce\u0005\'\u0000\u0000\u00ce\u00cf\u0003\u0014\n\u0000"+
		"\u00cf\u00d0\u0005\t\u0000\u0000\u00d0\u00db\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d2\u0005)\u0000\u0000\u00d2\u00d3\u0005H\u0000\u0000\u00d3\u00db\u0005"+
		"\t\u0000\u0000\u00d4\u00d5\u0005;\u0000\u0000\u00d5\u00d6\u00030\u0018"+
		"\u0000\u00d6\u00d7\u0007\u0006\u0000\u0000\u00d7\u00d8\u0003\u0014\n\u0000"+
		"\u00d8\u00d9\u0005\t\u0000\u0000\u00d9\u00db\u0001\u0000\u0000\u0000\u00da"+
		"\u00c4\u0001\u0000\u0000\u0000\u00da\u00cd\u0001\u0000\u0000\u0000\u00da"+
		"\u00d1\u0001\u0000\u0000\u0000\u00da\u00d4\u0001\u0000\u0000\u0000\u00db"+
		"\u0017\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005*\u0000\u0000\u00dd\u00de"+
		"\u0003\u001a\r\u0000\u00de\u0019\u0001\u0000\u0000\u0000\u00df\u00e0\u0005"+
		"+\u0000\u0000\u00e0\u001b\u0001\u0000\u0000\u0000\u00e1\u00e2\u00050\u0000"+
		"\u0000\u00e2\u00e3\u0005H\u0000\u0000\u00e3\u00e4\u00056\u0000\u0000\u00e4"+
		"\u00e5\u0003\u001e\u000f\u0000\u00e5\u00e6\u00057\u0000\u0000\u00e6\u00e7"+
		"\u0003\u0002\u0001\u0000\u00e7\u001d\u0001\u0000\u0000\u0000\u00e8\u00e9"+
		"\u0003\u0014\n\u0000\u00e9\u00ea\u0005\u000b\u0000\u0000\u00ea\u00ed\u0003"+
		"\u0014\n\u0000\u00eb\u00ec\u0005\u000b\u0000\u0000\u00ec\u00ee\u0003\u0014"+
		"\n\u0000\u00ed\u00eb\u0001\u0000\u0000\u0000\u00ed\u00ee\u0001\u0000\u0000"+
		"\u0000\u00ee\u001f\u0001\u0000\u0000\u0000\u00ef\u00f0\u00051\u0000\u0000"+
		"\u00f0\u00f1\u0003\u0014\n\u0000\u00f1\u00f2\u00057\u0000\u0000\u00f2"+
		"\u00f3\u0003\u0002\u0001\u0000\u00f3!\u0001\u0000\u0000\u0000\u00f4\u00f5"+
		"\u00052\u0000\u0000\u00f5\u00f6\u0003\u0002\u0001\u0000\u00f6\u00f7\u0005"+
		"3\u0000\u0000\u00f7\u00f8\u0003\u0014\n\u0000\u00f8#\u0001\u0000\u0000"+
		"\u0000\u00f9\u00fa\u0005%\u0000\u0000\u00fa\u00fb\u00030\u0018\u0000\u00fb"+
		"\u00fc\u00057\u0000\u0000\u00fc\u00fd\u0003\f\u0006\u0000\u00fd%\u0001"+
		"\u0000\u0000\u0000\u00fe\u00ff\u0005/\u0000\u0000\u00ff\u0100\u0005H\u0000"+
		"\u0000\u0100\u0101\u0005%\u0000\u0000\u0101\u0102\u0003\f\u0006\u0000"+
		"\u0102\'\u0001\u0000\u0000\u0000\u0103\u0104\u0005H\u0000\u0000\u0104"+
		"\u0105\u0005\r\u0000\u0000\u0105\u0106\u0005\"\u0000\u0000\u0106\u010d"+
		"\u0005\u0003\u0000\u0000\u0107\u010e\u0003\u0006\u0003\u0000\u0108\u010e"+
		"\u0003\n\u0005\u0000\u0109\u010e\u0003*\u0015\u0000\u010a\u010b\u0003"+
		"\u000e\u0007\u0000\u010b\u010c\u0005\t\u0000\u0000\u010c\u010e\u0001\u0000"+
		"\u0000\u0000\u010d\u0107\u0001\u0000\u0000\u0000\u010d\u0108\u0001\u0000"+
		"\u0000\u0000\u010d\u0109\u0001\u0000\u0000\u0000\u010d\u010a\u0001\u0000"+
		"\u0000\u0000\u010e\u010f\u0001\u0000\u0000\u0000\u010f\u010d\u0001\u0000"+
		"\u0000\u0000\u010f\u0110\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000"+
		"\u0000\u0000\u0111\u0112\u0005\u0004\u0000\u0000\u0112)\u0001\u0000\u0000"+
		"\u0000\u0113\u0114\u0005>\u0000\u0000\u0114\u0115\u0005?\u0000\u0000\u0115"+
		"\u0116\u00030\u0018\u0000\u0116\u0117\u0003\u0002\u0001\u0000\u0117+\u0001"+
		"\u0000\u0000\u0000\u0118\u0119\u00054\u0000\u0000\u0119\u011a\u0003\u0014"+
		"\n\u0000\u011a\u011b\u00057\u0000\u0000\u011b\u011f\u0003\u0002\u0001"+
		"\u0000\u011c\u011d\u00055\u0000\u0000\u011d\u011e\u00057\u0000\u0000\u011e"+
		"\u0120\u0003\u0002\u0001\u0000\u011f\u011c\u0001\u0000\u0000\u0000\u011f"+
		"\u0120\u0001\u0000\u0000\u0000\u0120-\u0001\u0000\u0000\u0000\u0121\u0122"+
		"\u0005\u000e\u0000\u0000\u0122\u014f\u0006\u0017\uffff\uffff\u0000\u0123"+
		"\u0124\u0005\u0010\u0000\u0000\u0124\u014f\u0006\u0017\uffff\uffff\u0000"+
		"\u0125\u0126\u0005\u0011\u0000\u0000\u0126\u014f\u0006\u0017\uffff\uffff"+
		"\u0000\u0127\u0128\u0005\u000f\u0000\u0000\u0128\u014f\u0006\u0017\uffff"+
		"\uffff\u0000\u0129\u012a\u0005\u0012\u0000\u0000\u012a\u014f\u0006\u0017"+
		"\uffff\uffff\u0000\u012b\u012c\u0005\u0013\u0000\u0000\u012c\u014f\u0006"+
		"\u0017\uffff\uffff\u0000\u012d\u012e\u0005\u0014\u0000\u0000\u012e\u014f"+
		"\u0006\u0017\uffff\uffff\u0000\u012f\u0130\u0005\u0015\u0000\u0000\u0130"+
		"\u014f\u0006\u0017\uffff\uffff\u0000\u0131\u0132\u0005\u0016\u0000\u0000"+
		"\u0132\u014f\u0006\u0017\uffff\uffff\u0000\u0133\u0134\u0005\u0017\u0000"+
		"\u0000\u0134\u014f\u0006\u0017\uffff\uffff\u0000\u0135\u0136\u0005\u0018"+
		"\u0000\u0000\u0136\u014f\u0006\u0017\uffff\uffff\u0000\u0137\u0138\u0005"+
		"\u0019\u0000\u0000\u0138\u014f\u0006\u0017\uffff\uffff\u0000\u0139\u013a"+
		"\u0005\u001a\u0000\u0000\u013a\u014f\u0006\u0017\uffff\uffff\u0000\u013b"+
		"\u013c\u0005\u001b\u0000\u0000\u013c\u014f\u0006\u0017\uffff\uffff\u0000"+
		"\u013d\u013e\u0005\u001c\u0000\u0000\u013e\u014f\u0006\u0017\uffff\uffff"+
		"\u0000\u013f\u0140\u0005\u001d\u0000\u0000\u0140\u014f\u0006\u0017\uffff"+
		"\uffff\u0000\u0141\u0142\u0005\u001e\u0000\u0000\u0142\u014f\u0006\u0017"+
		"\uffff\uffff\u0000\u0143\u0144\u0005\u001f\u0000\u0000\u0144\u014f\u0006"+
		"\u0017\uffff\uffff\u0000\u0145\u0146\u0005 \u0000\u0000\u0146\u014f\u0006"+
		"\u0017\uffff\uffff\u0000\u0147\u0148\u0005!\u0000\u0000\u0148\u014f\u0006"+
		"\u0017\uffff\uffff\u0000\u0149\u014a\u0005$\u0000\u0000\u014a\u014f\u0006"+
		"\u0017\uffff\uffff\u0000\u014b\u014c\u0005#\u0000\u0000\u014c\u014f\u0006"+
		"\u0017\uffff\uffff\u0000\u014d\u014f\u0005H\u0000\u0000\u014e\u0121\u0001"+
		"\u0000\u0000\u0000\u014e\u0123\u0001\u0000\u0000\u0000\u014e\u0125\u0001"+
		"\u0000\u0000\u0000\u014e\u0127\u0001\u0000\u0000\u0000\u014e\u0129\u0001"+
		"\u0000\u0000\u0000\u014e\u012b\u0001\u0000\u0000\u0000\u014e\u012d\u0001"+
		"\u0000\u0000\u0000\u014e\u012f\u0001\u0000\u0000\u0000\u014e\u0131\u0001"+
		"\u0000\u0000\u0000\u014e\u0133\u0001\u0000\u0000\u0000\u014e\u0135\u0001"+
		"\u0000\u0000\u0000\u014e\u0137\u0001\u0000\u0000\u0000\u014e\u0139\u0001"+
		"\u0000\u0000\u0000\u014e\u013b\u0001\u0000\u0000\u0000\u014e\u013d\u0001"+
		"\u0000\u0000\u0000\u014e\u013f\u0001\u0000\u0000\u0000\u014e\u0141\u0001"+
		"\u0000\u0000\u0000\u014e\u0143\u0001\u0000\u0000\u0000\u014e\u0145\u0001"+
		"\u0000\u0000\u0000\u014e\u0147\u0001\u0000\u0000\u0000\u014e\u0149\u0001"+
		"\u0000\u0000\u0000\u014e\u014b\u0001\u0000\u0000\u0000\u014e\u014d\u0001"+
		"\u0000\u0000\u0000\u014f/\u0001\u0000\u0000\u0000\u0150\u0159\u0005H\u0000"+
		"\u0000\u0151\u0154\u0005H\u0000\u0000\u0152\u0153\u0005\f\u0000\u0000"+
		"\u0153\u0155\u0005H\u0000\u0000\u0154\u0152\u0001\u0000\u0000\u0000\u0155"+
		"\u0156\u0001\u0000\u0000\u0000\u0156\u0154\u0001\u0000\u0000\u0000\u0156"+
		"\u0157\u0001\u0000\u0000\u0000\u0157\u0159\u0001\u0000\u0000\u0000\u0158"+
		"\u0150\u0001\u0000\u0000\u0000\u0158\u0151\u0001\u0000\u0000\u0000\u0159"+
		"1\u0001\u0000\u0000\u0000\u00195IMRX]`ditx\u0089\u00a7\u00b4\u00bf\u00c1"+
		"\u00ca\u00da\u00ed\u010d\u010f\u011f\u014e\u0156\u0158";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}