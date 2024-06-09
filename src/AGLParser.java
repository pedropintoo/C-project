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
		POLYLINE=30, SPLINE=31, POLYGON=32, BLOB=33, Model=34, Enum=35, ARRAY=36, 
		SCRIPT=37, WITH=38, AT=39, PRINT=40, REFRESH=41, CLOSE=42, MOUSE=43, CLICK=44, 
		WAIT=45, DEEPCOPY=46, INPUT=47, LOAD=48, PLAY=49, FOR=50, WHILE=51, REPEAT=52, 
		UNTIL=53, IF=54, ELSE=55, IN=56, DO=57, AFTER=58, MS=59, S=60, MOVE=61, 
		ROTATE=62, BY=63, TO=64, ACTION=65, ON=66, PLUS=67, MINUS=68, MUL=69, 
		DIV=70, GT=71, LT=72, GTE=73, LTE=74, EQ=75, NEQ=76, AND=77, OR=78, NOT=79, 
		BOOLEAN=80, ID=81, NAME=82, INT=83, FLOAT=84, STRING=85, LINE_COMMENT=86, 
		COMMENT=87, WS=88, ERROR=89;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_repetitiveStatement = 2, RULE_instantiation = 3, 
		RULE_simpleStatement = 4, RULE_blockStatement = 5, RULE_propertiesAssignment = 6, 
		RULE_longAssignment = 7, RULE_assignment = 8, RULE_in_assignment = 9, 
		RULE_expression = 10, RULE_command = 11, RULE_eventTrigger = 12, RULE_mouseTrigger = 13, 
		RULE_forStatement = 14, RULE_number_range = 15, RULE_whileStatement = 16, 
		RULE_repeatStatement = 17, RULE_withStatement = 18, RULE_playStatement = 19, 
		RULE_modelStat = 20, RULE_modelInstantiation = 21, RULE_action = 22, RULE_ifStatement = 23, 
		RULE_typeID = 24, RULE_identifier = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "repetitiveStatement", "instantiation", "simpleStatement", 
			"blockStatement", "propertiesAssignment", "longAssignment", "assignment", 
			"in_assignment", "expression", "command", "eventTrigger", "mouseTrigger", 
			"forStatement", "number_range", "whileStatement", "repeatStatement", 
			"withStatement", "playStatement", "modelStat", "modelInstantiation", 
			"action", "ifStatement", "typeID", "identifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "';'", 
			"','", "'..'", "'.'", "'::'", "'Integer'", "'Number'", "'String'", "'Point'", 
			"'Vector'", "'Time'", "'Boolean'", "'View'", "'Line'", "'Rectangle'", 
			"'Ellipse'", "'Arc'", "'ArcChord'", "'PieSlice'", "'Text'", "'Dot'", 
			"'Polyline'", "'Spline'", "'Polygon'", "'Blob'", "'Model'", "'Enum'", 
			"'Array'", "'Script'", "'with'", "'at'", "'print'", "'refresh'", "'close'", 
			"'mouse'", "'click'", "'wait'", "'deepcopy'", "'input'", "'load'", "'play'", 
			"'for'", "'while'", "'repeat'", "'until'", "'if'", "'else'", "'in'", 
			"'do'", "'after'", "'ms'", "'s'", "'move'", "'rotate'", "'by'", "'to'", 
			"'action'", "'on'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'>='", 
			"'<='", "'=='", "'!='", "'and'", "'or'", "'not'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COLON", 
			"EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "DOUBLECOLON", "INTEGER", 
			"NUMBER", "STRING_", "POINT", "VECTOR", "TIME", "BOOLEAN_", "VIEW", "LINE", 
			"RECTANGLE", "ELLIPSE", "ARC", "ARCHORD", "PIESLICE", "TEXT", "DOTTYPE", 
			"POLYLINE", "SPLINE", "POLYGON", "BLOB", "Model", "Enum", "ARRAY", "SCRIPT", 
			"WITH", "AT", "PRINT", "REFRESH", "CLOSE", "MOUSE", "CLICK", "WAIT", 
			"DEEPCOPY", "INPUT", "LOAD", "PLAY", "FOR", "WHILE", "REPEAT", "UNTIL", 
			"IF", "ELSE", "IN", "DO", "AFTER", "MS", "S", "MOVE", "ROTATE", "BY", 
			"TO", "ACTION", "ON", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "GTE", 
			"LTE", "EQ", "NEQ", "AND", "OR", "NOT", "BOOLEAN", "ID", "NAME", "INT", 
			"FLOAT", "STRING", "LINE_COMMENT", "COMMENT", "WS", "ERROR"
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
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 6943995904609206280L) != 0) || _la==ID) {
				{
				{
				setState(52);
				stat();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(58);
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
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new StatInstantiationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				instantiation();
				}
				break;
			case 2:
				_localctx = new StatModelInstantiationContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				modelInstantiation();
				}
				break;
			case 3:
				_localctx = new StatBlockStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(62);
				blockStatement();
				}
				break;
			case 4:
				_localctx = new StatLongAssignmentContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(63);
				longAssignment();
				setState(64);
				match(SEMI);
				}
				break;
			case 5:
				_localctx = new StatWithStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(66);
				withStatement();
				}
				break;
			case 6:
				_localctx = new StatPlayStatementContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(67);
				playStatement();
				}
				break;
			case 7:
				_localctx = new StatRepetitiveStatementContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(68);
				repetitiveStatement();
				}
				break;
			case 8:
				_localctx = new StatIfStatementContext(_localctx);
				enterOuterAlt(_localctx, 8);
				{
				setState(69);
				ifStatement();
				}
				break;
			case 9:
				_localctx = new StatCommandContext(_localctx);
				enterOuterAlt(_localctx, 9);
				{
				setState(70);
				command();
				}
				break;
			case 10:
				_localctx = new StatBlockContext(_localctx);
				enterOuterAlt(_localctx, 10);
				{
				setState(71);
				match(LBRACE);
				setState(73); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(72);
					stat();
					}
					}
					setState(75); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 6943995904609206280L) != 0) || _la==ID );
				setState(77);
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
			setState(84);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FOR:
				_localctx = new RepForStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				forStatement();
				}
				break;
			case WHILE:
				_localctx = new RepWhileStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(82);
				whileStatement();
				}
				break;
			case REPEAT:
				_localctx = new RepRepeatStatementContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(83);
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
			setState(86);
			match(ID);
			setState(87);
			match(COLON);
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(88);
				simpleStatement();
				}
				break;
			case 2:
				{
				setState(89);
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
		public TerminalNode AT() { return getToken(AGLParser.AT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public In_assignmentContext in_assignment() {
			return getRuleContext(In_assignmentContext.class,0);
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
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(92);
				typeID();
				setState(96);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AT:
					{
					setState(93);
					match(AT);
					setState(94);
					expression(0);
					}
					break;
				case EQUAL:
					{
					setState(95);
					assignment();
					}
					break;
				case SEMI:
					break;
				default:
					break;
				}
				setState(98);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(100);
				typeID();
				setState(101);
				in_assignment();
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
			setState(105);
			typeID();
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AT) {
				{
				setState(106);
				match(AT);
				setState(107);
				expression(0);
				}
			}

			setState(110);
			match(WITH);
			setState(111);
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
		public String idToAssign;
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
			setState(113);
			match(LBRACE);
			setState(114);
			longAssignment();
			setState(119);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(115);
					match(SEMI);
					setState(116);
					longAssignment();
					}
					} 
				}
				setState(121);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMI) {
				{
				setState(122);
				match(SEMI);
				}
			}

			setState(125);
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
			setState(127);
			identifier();
			setState(128);
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
			setState(130);
			match(EQUAL);
			setState(131);
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
		public Type eType;
		public String varName;
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
			setState(133);
			match(IN);
			setState(134);
			match(LBRACE);
			setState(135);
			match(ID);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(136);
				match(COMMA);
				setState(137);
				match(ID);
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(143);
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
		public ExpressionContext e1;
		public Token op;
		public ExpressionContext e2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode GT() { return getToken(AGLParser.GT, 0); }
		public TerminalNode LT() { return getToken(AGLParser.LT, 0); }
		public TerminalNode GTE() { return getToken(AGLParser.GTE, 0); }
		public TerminalNode LTE() { return getToken(AGLParser.LTE, 0); }
		public TerminalNode EQ() { return getToken(AGLParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(AGLParser.NEQ, 0); }
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
	public static class ExprAndOrContext extends ExpressionContext {
		public ExpressionContext e1;
		public ExpressionContext e2;
		public TerminalNode AND() { return getToken(AGLParser.AND, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(AGLParser.OR, 0); }
		public ExprAndOrContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprAndOr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprAndOr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprAndOr(this);
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
	public static class ExprDeepCopyContext extends ExpressionContext {
		public TerminalNode DEEPCOPY() { return getToken(AGLParser.DEEPCOPY, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode TO() { return getToken(AGLParser.TO, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExprDeepCopyContext(ExpressionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterExprDeepCopy(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitExprDeepCopy(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitExprDeepCopy(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprAddSubMultDivContext extends ExpressionContext {
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
	@SuppressWarnings("CheckReturnValue")
	public static class ExprVectorContext extends ExpressionContext {
		public ExpressionContext deg;
		public ExpressionContext length;
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
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				_localctx = new ExprUnaryContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(146);
				((ExprUnaryContext)_localctx).sign = _input.LT(1);
				_la = _input.LA(1);
				if ( !(((((_la - 67)) & ~0x3f) == 0 && ((1L << (_la - 67)) & 4099L) != 0)) ) {
					((ExprUnaryContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(147);
				((ExprUnaryContext)_localctx).e = expression(18);
				}
				break;
			case 2:
				{
				_localctx = new ExprParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(148);
				match(LPAREN);
				setState(149);
				((ExprParenthesisContext)_localctx).e = expression(0);
				setState(150);
				match(RPAREN);
				}
				break;
			case 3:
				{
				_localctx = new ExprPointContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(152);
				match(LPAREN);
				setState(153);
				((ExprPointContext)_localctx).x = expression(0);
				setState(154);
				match(COMMA);
				setState(155);
				((ExprPointContext)_localctx).y = expression(0);
				setState(156);
				match(RPAREN);
				}
				break;
			case 4:
				{
				_localctx = new ExprVectorContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(158);
				match(LPAREN);
				setState(159);
				((ExprVectorContext)_localctx).deg = expression(0);
				setState(160);
				match(COLON);
				setState(161);
				((ExprVectorContext)_localctx).length = expression(0);
				setState(162);
				match(RPAREN);
				}
				break;
			case 5:
				{
				_localctx = new ExprArrayContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(164);
				match(LBRACK);
				setState(165);
				expression(0);
				setState(170);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(166);
					match(COMMA);
					setState(167);
					expression(0);
					}
					}
					setState(172);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(173);
				match(RBRACK);
				}
				break;
			case 6:
				{
				_localctx = new ExprNumberContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(175);
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
				setState(176);
				match(BOOLEAN);
				}
				break;
			case 8:
				{
				_localctx = new ExprStringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(177);
				match(STRING);
				}
				break;
			case 9:
				{
				_localctx = new ExprIDContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(178);
				identifier();
				}
				break;
			case 10:
				{
				_localctx = new ExprWaitContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(179);
				match(WAIT);
				setState(180);
				eventTrigger();
				}
				break;
			case 11:
				{
				_localctx = new ExprDeepCopyContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(181);
				match(DEEPCOPY);
				setState(182);
				identifier();
				setState(183);
				match(TO);
				setState(184);
				expression(2);
				}
				break;
			case 12:
				{
				_localctx = new ExprScriptContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(186);
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
				setState(187);
				match(STRING);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(210);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(208);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
					case 1:
						{
						_localctx = new ExprAddSubMultDivContext(new ExpressionContext(_parentctx, _parentState));
						((ExprAddSubMultDivContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(190);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(191);
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
						setState(192);
						((ExprAddSubMultDivContext)_localctx).e2 = expression(17);
						}
						break;
					case 2:
						{
						_localctx = new ExprAddSubMultDivContext(new ExpressionContext(_parentctx, _parentState));
						((ExprAddSubMultDivContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(193);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(194);
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
						setState(195);
						((ExprAddSubMultDivContext)_localctx).e2 = expression(16);
						}
						break;
					case 3:
						{
						_localctx = new ExprRelationalContext(new ExpressionContext(_parentctx, _parentState));
						((ExprRelationalContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(196);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(197);
						((ExprRelationalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(((((_la - 71)) & ~0x3f) == 0 && ((1L << (_la - 71)) & 15L) != 0)) ) {
							((ExprRelationalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(198);
						((ExprRelationalContext)_localctx).e2 = expression(15);
						}
						break;
					case 4:
						{
						_localctx = new ExprRelationalContext(new ExpressionContext(_parentctx, _parentState));
						((ExprRelationalContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(199);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(200);
						((ExprRelationalContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==EQ || _la==NEQ) ) {
							((ExprRelationalContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(201);
						((ExprRelationalContext)_localctx).e2 = expression(14);
						}
						break;
					case 5:
						{
						_localctx = new ExprAndOrContext(new ExpressionContext(_parentctx, _parentState));
						((ExprAndOrContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(202);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(203);
						match(AND);
						setState(204);
						((ExprAndOrContext)_localctx).e2 = expression(13);
						}
						break;
					case 6:
						{
						_localctx = new ExprAndOrContext(new ExpressionContext(_parentctx, _parentState));
						((ExprAndOrContext)_localctx).e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(205);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(206);
						match(OR);
						setState(207);
						((ExprAndOrContext)_localctx).e2 = expression(12);
						}
						break;
					}
					} 
				}
				setState(212);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
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
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public TerminalNode BY() { return getToken(AGLParser.BY, 0); }
		public TerminalNode TO() { return getToken(AGLParser.TO, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AGLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AGLParser.COMMA, i);
		}
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
	public static class CommandRotateContext extends CommandContext {
		public TerminalNode ROTATE() { return getToken(AGLParser.ROTATE, 0); }
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public TerminalNode BY() { return getToken(AGLParser.BY, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AGLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AGLParser.COMMA, i);
		}
		public CommandRotateContext(CommandContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterCommandRotate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitCommandRotate(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitCommandRotate(this);
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
		public List<TerminalNode> ID() { return getTokens(AGLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(AGLParser.ID, i);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AGLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AGLParser.COMMA, i);
		}
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
		public List<TerminalNode> ID() { return getTokens(AGLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(AGLParser.ID, i);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(AGLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(AGLParser.COMMA, i);
		}
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
			setState(269);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REFRESH:
				_localctx = new CommandRefreshContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				match(REFRESH);
				setState(214);
				match(ID);
				setState(219);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(215);
					match(COMMA);
					setState(216);
					match(ID);
					}
					}
					setState(221);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(226);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==AFTER) {
					{
					setState(222);
					match(AFTER);
					setState(223);
					expression(0);
					setState(224);
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

				setState(228);
				match(SEMI);
				}
				break;
			case PRINT:
				_localctx = new CommandPrintContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(229);
				match(PRINT);
				setState(230);
				expression(0);
				setState(231);
				match(SEMI);
				}
				break;
			case CLOSE:
				_localctx = new CommandCloseContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(233);
				match(CLOSE);
				setState(234);
				match(ID);
				setState(239);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(235);
					match(COMMA);
					setState(236);
					match(ID);
					}
					}
					setState(241);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(242);
				match(SEMI);
				}
				break;
			case MOVE:
				_localctx = new CommandMoveContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(243);
				match(MOVE);
				setState(244);
				identifier();
				setState(249);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(245);
					match(COMMA);
					setState(246);
					identifier();
					}
					}
					setState(251);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(252);
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
				setState(253);
				expression(0);
				setState(254);
				match(SEMI);
				}
				break;
			case ROTATE:
				_localctx = new CommandRotateContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(256);
				match(ROTATE);
				setState(257);
				identifier();
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(258);
					match(COMMA);
					setState(259);
					identifier();
					}
					}
					setState(264);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(265);
				match(BY);
				setState(266);
				expression(0);
				setState(267);
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
			setState(271);
			match(MOUSE);
			setState(272);
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
			setState(274);
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
			setState(276);
			match(FOR);
			setState(277);
			match(ID);
			setState(278);
			match(IN);
			setState(279);
			number_range();
			setState(280);
			match(DO);
			setState(281);
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
			setState(283);
			expression(0);
			setState(284);
			match(TWODOTS);
			setState(285);
			expression(0);
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TWODOTS) {
				{
				setState(286);
				match(TWODOTS);
				setState(287);
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
			setState(290);
			match(WHILE);
			setState(291);
			expression(0);
			setState(292);
			match(DO);
			setState(293);
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
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
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
			setState(295);
			match(REPEAT);
			setState(296);
			stat();
			setState(297);
			match(UNTIL);
			setState(298);
			expression(0);
			setState(299);
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
			setState(301);
			match(WITH);
			setState(302);
			identifier();
			setState(303);
			match(DO);
			setState(304);
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
			setState(306);
			match(PLAY);
			setState(307);
			match(ID);
			setState(308);
			match(WITH);
			setState(309);
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
	public static class ModelStatContext extends ParserRuleContext {
		public Boolean isAction;
		public ModelStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modelStat; }
	 
		public ModelStatContext() { }
		public void copyFrom(ModelStatContext ctx) {
			super.copyFrom(ctx);
			this.isAction = ctx.isAction;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModelStatBlockStatementContext extends ModelStatContext {
		public BlockStatementContext blockStatement() {
			return getRuleContext(BlockStatementContext.class,0);
		}
		public ModelStatBlockStatementContext(ModelStatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterModelStatBlockStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitModelStatBlockStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitModelStatBlockStatement(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModelStatLongAssignmentContext extends ModelStatContext {
		public LongAssignmentContext longAssignment() {
			return getRuleContext(LongAssignmentContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(AGLParser.SEMI, 0); }
		public ModelStatLongAssignmentContext(ModelStatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterModelStatLongAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitModelStatLongAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitModelStatLongAssignment(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModelStatInstantiationContext extends ModelStatContext {
		public InstantiationContext instantiation() {
			return getRuleContext(InstantiationContext.class,0);
		}
		public ModelStatInstantiationContext(ModelStatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterModelStatInstantiation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitModelStatInstantiation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitModelStatInstantiation(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModelStatActionContext extends ModelStatContext {
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public ModelStatActionContext(ModelStatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).enterModelStatAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AGLParserListener ) ((AGLParserListener)listener).exitModelStatAction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof AGLParserVisitor ) return ((AGLParserVisitor<? extends T>)visitor).visitModelStatAction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ModelStatContext modelStat() throws RecognitionException {
		ModelStatContext _localctx = new ModelStatContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_modelStat);
		try {
			setState(317);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				_localctx = new ModelStatInstantiationContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(311);
				instantiation();
				}
				break;
			case 2:
				_localctx = new ModelStatBlockStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(312);
				blockStatement();
				}
				break;
			case 3:
				_localctx = new ModelStatLongAssignmentContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(313);
				longAssignment();
				setState(314);
				match(SEMI);
				}
				break;
			case 4:
				_localctx = new ModelStatActionContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(316);
				action();
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
	public static class ModelInstantiationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode DOUBLECOLON() { return getToken(AGLParser.DOUBLECOLON, 0); }
		public TerminalNode Model() { return getToken(AGLParser.Model, 0); }
		public TerminalNode LBRACE() { return getToken(AGLParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(AGLParser.RBRACE, 0); }
		public List<ModelStatContext> modelStat() {
			return getRuleContexts(ModelStatContext.class);
		}
		public ModelStatContext modelStat(int i) {
			return getRuleContext(ModelStatContext.class,i);
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
		enterRule(_localctx, 42, RULE_modelInstantiation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			match(ID);
			setState(320);
			match(DOUBLECOLON);
			setState(321);
			match(Model);
			setState(322);
			match(LBRACE);
			setState(324); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(323);
				modelStat();
				}
				}
				setState(326); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 257698021376L) != 0) || _la==ACTION || _la==ID );
			setState(328);
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
		enterRule(_localctx, 44, RULE_action);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(330);
			match(ACTION);
			setState(331);
			match(ON);
			setState(332);
			identifier();
			setState(333);
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
		enterRule(_localctx, 46, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			match(IF);
			setState(336);
			expression(0);
			setState(337);
			match(DO);
			setState(338);
			stat();
			setState(342);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(339);
				match(ELSE);
				setState(340);
				match(DO);
				setState(341);
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
		public TypeIDContext typeID;
		public Token ID;
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
		public TerminalNode ARRAY() { return getToken(AGLParser.ARRAY, 0); }
		public TerminalNode LT() { return getToken(AGLParser.LT, 0); }
		public TypeIDContext typeID() {
			return getRuleContext(TypeIDContext.class,0);
		}
		public TerminalNode GT() { return getToken(AGLParser.GT, 0); }
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
		enterRule(_localctx, 48, RULE_typeID);
		try {
			setState(396);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(344);
				match(INTEGER);
				((TypeIDContext)_localctx).res =  new IntegerType();
				}
				break;
			case STRING_:
				enterOuterAlt(_localctx, 2);
				{
				setState(346);
				match(STRING_);
				((TypeIDContext)_localctx).res =  new StringType();
				}
				break;
			case POINT:
				enterOuterAlt(_localctx, 3);
				{
				setState(348);
				match(POINT);
				((TypeIDContext)_localctx).res =  new PointType();
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 4);
				{
				setState(350);
				match(NUMBER);
				((TypeIDContext)_localctx).res =  new NumberType();
				}
				break;
			case VECTOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(352);
				match(VECTOR);
				((TypeIDContext)_localctx).res =  new VectorType();
				}
				break;
			case TIME:
				enterOuterAlt(_localctx, 6);
				{
				setState(354);
				match(TIME);
				((TypeIDContext)_localctx).res =  new TimeType();
				}
				break;
			case BOOLEAN_:
				enterOuterAlt(_localctx, 7);
				{
				setState(356);
				match(BOOLEAN_);
				((TypeIDContext)_localctx).res =  new BooleanType();
				}
				break;
			case VIEW:
				enterOuterAlt(_localctx, 8);
				{
				setState(358);
				match(VIEW);
				((TypeIDContext)_localctx).res =  new ObjectType("View");
				}
				break;
			case LINE:
				enterOuterAlt(_localctx, 9);
				{
				setState(360);
				match(LINE);
				((TypeIDContext)_localctx).res =  new ObjectType("Line");
				}
				break;
			case RECTANGLE:
				enterOuterAlt(_localctx, 10);
				{
				setState(362);
				match(RECTANGLE);
				((TypeIDContext)_localctx).res =  new ObjectType("Rectangle");
				}
				break;
			case ELLIPSE:
				enterOuterAlt(_localctx, 11);
				{
				setState(364);
				match(ELLIPSE);
				((TypeIDContext)_localctx).res =  new ObjectType("Ellipse");
				}
				break;
			case ARC:
				enterOuterAlt(_localctx, 12);
				{
				setState(366);
				match(ARC);
				((TypeIDContext)_localctx).res =  new ObjectType("Arc");
				}
				break;
			case ARCHORD:
				enterOuterAlt(_localctx, 13);
				{
				setState(368);
				match(ARCHORD);
				((TypeIDContext)_localctx).res =  new ObjectType("ArcChord");
				}
				break;
			case PIESLICE:
				enterOuterAlt(_localctx, 14);
				{
				setState(370);
				match(PIESLICE);
				((TypeIDContext)_localctx).res =  new ObjectType("PieSlice");
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 15);
				{
				setState(372);
				match(TEXT);
				((TypeIDContext)_localctx).res =  new ObjectType("Text");
				}
				break;
			case DOTTYPE:
				enterOuterAlt(_localctx, 16);
				{
				setState(374);
				match(DOTTYPE);
				((TypeIDContext)_localctx).res =  new ObjectType("Dot");
				}
				break;
			case POLYLINE:
				enterOuterAlt(_localctx, 17);
				{
				setState(376);
				match(POLYLINE);
				((TypeIDContext)_localctx).res =  new ObjectType("PolyLine");
				}
				break;
			case SPLINE:
				enterOuterAlt(_localctx, 18);
				{
				setState(378);
				match(SPLINE);
				((TypeIDContext)_localctx).res =  new ObjectType("Spline");
				}
				break;
			case POLYGON:
				enterOuterAlt(_localctx, 19);
				{
				setState(380);
				match(POLYGON);
				((TypeIDContext)_localctx).res =  new ObjectType("Polygon");
				}
				break;
			case BLOB:
				enterOuterAlt(_localctx, 20);
				{
				setState(382);
				match(BLOB);
				((TypeIDContext)_localctx).res =  new ObjectType("Blob");
				}
				break;
			case SCRIPT:
				enterOuterAlt(_localctx, 21);
				{
				setState(384);
				match(SCRIPT);
				((TypeIDContext)_localctx).res =  new ObjectType("Script");
				}
				break;
			case Enum:
				enterOuterAlt(_localctx, 22);
				{
				setState(386);
				match(Enum);
				((TypeIDContext)_localctx).res =  new EnumType();
				}
				break;
			case ARRAY:
				enterOuterAlt(_localctx, 23);
				{
				setState(388);
				match(ARRAY);
				setState(389);
				match(LT);
				setState(390);
				((TypeIDContext)_localctx).typeID = typeID();
				setState(391);
				match(GT);
				((TypeIDContext)_localctx).res =  new ArrayType("Array<" + (((TypeIDContext)_localctx).typeID!=null?_input.getText(((TypeIDContext)_localctx).typeID.start,((TypeIDContext)_localctx).typeID.stop):null) + ">");
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 24);
				{
				setState(394);
				((TypeIDContext)_localctx).ID = match(ID);
				((TypeIDContext)_localctx).res =  new ModelType((((TypeIDContext)_localctx).ID!=null?((TypeIDContext)_localctx).ID.getText():null));
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
		public TerminalNode ID() { return getToken(AGLParser.ID, 0); }
		public TerminalNode DOT() { return getToken(AGLParser.DOT, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public List<TerminalNode> LBRACK() { return getTokens(AGLParser.LBRACK); }
		public TerminalNode LBRACK(int i) {
			return getToken(AGLParser.LBRACK, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> RBRACK() { return getTokens(AGLParser.RBRACK); }
		public TerminalNode RBRACK(int i) {
			return getToken(AGLParser.RBRACK, i);
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
		enterRule(_localctx, 50, RULE_identifier);
		try {
			int _alt;
			setState(415);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(398);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(399);
				match(ID);
				setState(400);
				match(DOT);
				setState(401);
				identifier();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(402);
				match(ID);
				setState(407); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(403);
						match(LBRACK);
						setState(404);
						expression(0);
						setState(405);
						match(RBRACK);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(409); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(413);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
				case 1:
					{
					setState(411);
					match(DOT);
					setState(412);
					identifier();
					}
					break;
				}
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
			return precpred(_ctx, 16);
		case 1:
			return precpred(_ctx, 15);
		case 2:
			return precpred(_ctx, 14);
		case 3:
			return precpred(_ctx, 13);
		case 4:
			return precpred(_ctx, 12);
		case 5:
			return precpred(_ctx, 11);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001Y\u01a2\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0001\u0000\u0005\u00006\b\u0000\n\u0000\f\u0000"+
		"9\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0004\u0001J\b\u0001"+
		"\u000b\u0001\f\u0001K\u0001\u0001\u0001\u0001\u0003\u0001P\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002U\b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003[\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004a\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004h\b\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005m\b\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005"+
		"\u0006v\b\u0006\n\u0006\f\u0006y\t\u0006\u0001\u0006\u0003\u0006|\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0005\t\u008b\b\t\n"+
		"\t\f\t\u008e\t\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0005\n\u00a9\b\n\n\n\f\n\u00ac\t\n\u0001\n\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0003\n\u00bd\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u00d1\b\n\n\n\f\n\u00d4\t\n"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00da\b\u000b"+
		"\n\u000b\f\u000b\u00dd\t\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u00e3\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005"+
		"\u000b\u00ee\b\u000b\n\u000b\f\u000b\u00f1\t\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u00f8\b\u000b\n\u000b"+
		"\f\u000b\u00fb\t\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u0105\b\u000b"+
		"\n\u000b\f\u000b\u0108\t\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u010e\b\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0003\u000f\u0121\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014"+
		"\u013e\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0004\u0015\u0145\b\u0015\u000b\u0015\f\u0015\u0146\u0001\u0015\u0001"+
		"\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0003\u0017\u0157\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0003\u0018\u018d\b\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0004"+
		"\u0019\u0198\b\u0019\u000b\u0019\f\u0019\u0199\u0001\u0019\u0001\u0019"+
		"\u0003\u0019\u019e\b\u0019\u0003\u0019\u01a0\b\u0019\u0001\u0019\u0000"+
		"\u0001\u0014\u001a\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02\u0000\t\u0002\u0000CDOO\u0001"+
		"\u0000ST\u0001\u0000/0\u0001\u0000EF\u0001\u0000CD\u0001\u0000GJ\u0001"+
		"\u0000KL\u0001\u0000;<\u0001\u0000?@\u01d8\u00007\u0001\u0000\u0000\u0000"+
		"\u0002O\u0001\u0000\u0000\u0000\u0004T\u0001\u0000\u0000\u0000\u0006V"+
		"\u0001\u0000\u0000\u0000\bg\u0001\u0000\u0000\u0000\ni\u0001\u0000\u0000"+
		"\u0000\fq\u0001\u0000\u0000\u0000\u000e\u007f\u0001\u0000\u0000\u0000"+
		"\u0010\u0082\u0001\u0000\u0000\u0000\u0012\u0085\u0001\u0000\u0000\u0000"+
		"\u0014\u00bc\u0001\u0000\u0000\u0000\u0016\u010d\u0001\u0000\u0000\u0000"+
		"\u0018\u010f\u0001\u0000\u0000\u0000\u001a\u0112\u0001\u0000\u0000\u0000"+
		"\u001c\u0114\u0001\u0000\u0000\u0000\u001e\u011b\u0001\u0000\u0000\u0000"+
		" \u0122\u0001\u0000\u0000\u0000\"\u0127\u0001\u0000\u0000\u0000$\u012d"+
		"\u0001\u0000\u0000\u0000&\u0132\u0001\u0000\u0000\u0000(\u013d\u0001\u0000"+
		"\u0000\u0000*\u013f\u0001\u0000\u0000\u0000,\u014a\u0001\u0000\u0000\u0000"+
		".\u014f\u0001\u0000\u0000\u00000\u018c\u0001\u0000\u0000\u00002\u019f"+
		"\u0001\u0000\u0000\u000046\u0003\u0002\u0001\u000054\u0001\u0000\u0000"+
		"\u000069\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000"+
		"\u0000\u00008:\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000:;\u0005"+
		"\u0000\u0000\u0001;\u0001\u0001\u0000\u0000\u0000<P\u0003\u0006\u0003"+
		"\u0000=P\u0003*\u0015\u0000>P\u0003\n\u0005\u0000?@\u0003\u000e\u0007"+
		"\u0000@A\u0005\t\u0000\u0000AP\u0001\u0000\u0000\u0000BP\u0003$\u0012"+
		"\u0000CP\u0003&\u0013\u0000DP\u0003\u0004\u0002\u0000EP\u0003.\u0017\u0000"+
		"FP\u0003\u0016\u000b\u0000GI\u0005\u0003\u0000\u0000HJ\u0003\u0002\u0001"+
		"\u0000IH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KI\u0001\u0000"+
		"\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MN\u0005"+
		"\u0004\u0000\u0000NP\u0001\u0000\u0000\u0000O<\u0001\u0000\u0000\u0000"+
		"O=\u0001\u0000\u0000\u0000O>\u0001\u0000\u0000\u0000O?\u0001\u0000\u0000"+
		"\u0000OB\u0001\u0000\u0000\u0000OC\u0001\u0000\u0000\u0000OD\u0001\u0000"+
		"\u0000\u0000OE\u0001\u0000\u0000\u0000OF\u0001\u0000\u0000\u0000OG\u0001"+
		"\u0000\u0000\u0000P\u0003\u0001\u0000\u0000\u0000QU\u0003\u001c\u000e"+
		"\u0000RU\u0003 \u0010\u0000SU\u0003\"\u0011\u0000TQ\u0001\u0000\u0000"+
		"\u0000TR\u0001\u0000\u0000\u0000TS\u0001\u0000\u0000\u0000U\u0005\u0001"+
		"\u0000\u0000\u0000VW\u0005Q\u0000\u0000WZ\u0005\u0007\u0000\u0000X[\u0003"+
		"\b\u0004\u0000Y[\u0003\n\u0005\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001"+
		"\u0000\u0000\u0000[\u0007\u0001\u0000\u0000\u0000\\`\u00030\u0018\u0000"+
		"]^\u0005\'\u0000\u0000^a\u0003\u0014\n\u0000_a\u0003\u0010\b\u0000`]\u0001"+
		"\u0000\u0000\u0000`_\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000"+
		"ab\u0001\u0000\u0000\u0000bc\u0005\t\u0000\u0000ch\u0001\u0000\u0000\u0000"+
		"de\u00030\u0018\u0000ef\u0003\u0012\t\u0000fh\u0001\u0000\u0000\u0000"+
		"g\\\u0001\u0000\u0000\u0000gd\u0001\u0000\u0000\u0000h\t\u0001\u0000\u0000"+
		"\u0000il\u00030\u0018\u0000jk\u0005\'\u0000\u0000km\u0003\u0014\n\u0000"+
		"lj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000"+
		"\u0000no\u0005&\u0000\u0000op\u0003\f\u0006\u0000p\u000b\u0001\u0000\u0000"+
		"\u0000qr\u0005\u0003\u0000\u0000rw\u0003\u000e\u0007\u0000st\u0005\t\u0000"+
		"\u0000tv\u0003\u000e\u0007\u0000us\u0001\u0000\u0000\u0000vy\u0001\u0000"+
		"\u0000\u0000wu\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000x{\u0001"+
		"\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000z|\u0005\t\u0000\u0000{z\u0001"+
		"\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000"+
		"}~\u0005\u0004\u0000\u0000~\r\u0001\u0000\u0000\u0000\u007f\u0080\u0003"+
		"2\u0019\u0000\u0080\u0081\u0003\u0010\b\u0000\u0081\u000f\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0005\b\u0000\u0000\u0083\u0084\u0003\u0014\n"+
		"\u0000\u0084\u0011\u0001\u0000\u0000\u0000\u0085\u0086\u00058\u0000\u0000"+
		"\u0086\u0087\u0005\u0003\u0000\u0000\u0087\u008c\u0005Q\u0000\u0000\u0088"+
		"\u0089\u0005\n\u0000\u0000\u0089\u008b\u0005Q\u0000\u0000\u008a\u0088"+
		"\u0001\u0000\u0000\u0000\u008b\u008e\u0001\u0000\u0000\u0000\u008c\u008a"+
		"\u0001\u0000\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000\u008d\u008f"+
		"\u0001\u0000\u0000\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008f\u0090"+
		"\u0005\u0004\u0000\u0000\u0090\u0013\u0001\u0000\u0000\u0000\u0091\u0092"+
		"\u0006\n\uffff\uffff\u0000\u0092\u0093\u0007\u0000\u0000\u0000\u0093\u00bd"+
		"\u0003\u0014\n\u0012\u0094\u0095\u0005\u0001\u0000\u0000\u0095\u0096\u0003"+
		"\u0014\n\u0000\u0096\u0097\u0005\u0002\u0000\u0000\u0097\u00bd\u0001\u0000"+
		"\u0000\u0000\u0098\u0099\u0005\u0001\u0000\u0000\u0099\u009a\u0003\u0014"+
		"\n\u0000\u009a\u009b\u0005\n\u0000\u0000\u009b\u009c\u0003\u0014\n\u0000"+
		"\u009c\u009d\u0005\u0002\u0000\u0000\u009d\u00bd\u0001\u0000\u0000\u0000"+
		"\u009e\u009f\u0005\u0001\u0000\u0000\u009f\u00a0\u0003\u0014\n\u0000\u00a0"+
		"\u00a1\u0005\u0007\u0000\u0000\u00a1\u00a2\u0003\u0014\n\u0000\u00a2\u00a3"+
		"\u0005\u0002\u0000\u0000\u00a3\u00bd\u0001\u0000\u0000\u0000\u00a4\u00a5"+
		"\u0005\u0005\u0000\u0000\u00a5\u00aa\u0003\u0014\n\u0000\u00a6\u00a7\u0005"+
		"\n\u0000\u0000\u00a7\u00a9\u0003\u0014\n\u0000\u00a8\u00a6\u0001\u0000"+
		"\u0000\u0000\u00a9\u00ac\u0001\u0000\u0000\u0000\u00aa\u00a8\u0001\u0000"+
		"\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u00ad\u0001\u0000"+
		"\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005\u0006"+
		"\u0000\u0000\u00ae\u00bd\u0001\u0000\u0000\u0000\u00af\u00bd\u0007\u0001"+
		"\u0000\u0000\u00b0\u00bd\u0005P\u0000\u0000\u00b1\u00bd\u0005U\u0000\u0000"+
		"\u00b2\u00bd\u00032\u0019\u0000\u00b3\u00b4\u0005-\u0000\u0000\u00b4\u00bd"+
		"\u0003\u0018\f\u0000\u00b5\u00b6\u0005.\u0000\u0000\u00b6\u00b7\u0003"+
		"2\u0019\u0000\u00b7\u00b8\u0005@\u0000\u0000\u00b8\u00b9\u0003\u0014\n"+
		"\u0002\u00b9\u00bd\u0001\u0000\u0000\u0000\u00ba\u00bb\u0007\u0002\u0000"+
		"\u0000\u00bb\u00bd\u0005U\u0000\u0000\u00bc\u0091\u0001\u0000\u0000\u0000"+
		"\u00bc\u0094\u0001\u0000\u0000\u0000\u00bc\u0098\u0001\u0000\u0000\u0000"+
		"\u00bc\u009e\u0001\u0000\u0000\u0000\u00bc\u00a4\u0001\u0000\u0000\u0000"+
		"\u00bc\u00af\u0001\u0000\u0000\u0000\u00bc\u00b0\u0001\u0000\u0000\u0000"+
		"\u00bc\u00b1\u0001\u0000\u0000\u0000\u00bc\u00b2\u0001\u0000\u0000\u0000"+
		"\u00bc\u00b3\u0001\u0000\u0000\u0000\u00bc\u00b5\u0001\u0000\u0000\u0000"+
		"\u00bc\u00ba\u0001\u0000\u0000\u0000\u00bd\u00d2\u0001\u0000\u0000\u0000"+
		"\u00be\u00bf\n\u0010\u0000\u0000\u00bf\u00c0\u0007\u0003\u0000\u0000\u00c0"+
		"\u00d1\u0003\u0014\n\u0011\u00c1\u00c2\n\u000f\u0000\u0000\u00c2\u00c3"+
		"\u0007\u0004\u0000\u0000\u00c3\u00d1\u0003\u0014\n\u0010\u00c4\u00c5\n"+
		"\u000e\u0000\u0000\u00c5\u00c6\u0007\u0005\u0000\u0000\u00c6\u00d1\u0003"+
		"\u0014\n\u000f\u00c7\u00c8\n\r\u0000\u0000\u00c8\u00c9\u0007\u0006\u0000"+
		"\u0000\u00c9\u00d1\u0003\u0014\n\u000e\u00ca\u00cb\n\f\u0000\u0000\u00cb"+
		"\u00cc\u0005M\u0000\u0000\u00cc\u00d1\u0003\u0014\n\r\u00cd\u00ce\n\u000b"+
		"\u0000\u0000\u00ce\u00cf\u0005N\u0000\u0000\u00cf\u00d1\u0003\u0014\n"+
		"\f\u00d0\u00be\u0001\u0000\u0000\u0000\u00d0\u00c1\u0001\u0000\u0000\u0000"+
		"\u00d0\u00c4\u0001\u0000\u0000\u0000\u00d0\u00c7\u0001\u0000\u0000\u0000"+
		"\u00d0\u00ca\u0001\u0000\u0000\u0000\u00d0\u00cd\u0001\u0000\u0000\u0000"+
		"\u00d1\u00d4\u0001\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000"+
		"\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d3\u0015\u0001\u0000\u0000\u0000"+
		"\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d5\u00d6\u0005)\u0000\u0000\u00d6"+
		"\u00db\u0005Q\u0000\u0000\u00d7\u00d8\u0005\n\u0000\u0000\u00d8\u00da"+
		"\u0005Q\u0000\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00da\u00dd\u0001"+
		"\u0000\u0000\u0000\u00db\u00d9\u0001\u0000\u0000\u0000\u00db\u00dc\u0001"+
		"\u0000\u0000\u0000\u00dc\u00e2\u0001\u0000\u0000\u0000\u00dd\u00db\u0001"+
		"\u0000\u0000\u0000\u00de\u00df\u0005:\u0000\u0000\u00df\u00e0\u0003\u0014"+
		"\n\u0000\u00e0\u00e1\u0007\u0007\u0000\u0000\u00e1\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e2\u00de\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e3\u00e4\u0001\u0000\u0000\u0000\u00e4\u010e\u0005\t\u0000\u0000"+
		"\u00e5\u00e6\u0005(\u0000\u0000\u00e6\u00e7\u0003\u0014\n\u0000\u00e7"+
		"\u00e8\u0005\t\u0000\u0000\u00e8\u010e\u0001\u0000\u0000\u0000\u00e9\u00ea"+
		"\u0005*\u0000\u0000\u00ea\u00ef\u0005Q\u0000\u0000\u00eb\u00ec\u0005\n"+
		"\u0000\u0000\u00ec\u00ee\u0005Q\u0000\u0000\u00ed\u00eb\u0001\u0000\u0000"+
		"\u0000\u00ee\u00f1\u0001\u0000\u0000\u0000\u00ef\u00ed\u0001\u0000\u0000"+
		"\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00f2\u0001\u0000\u0000"+
		"\u0000\u00f1\u00ef\u0001\u0000\u0000\u0000\u00f2\u010e\u0005\t\u0000\u0000"+
		"\u00f3\u00f4\u0005=\u0000\u0000\u00f4\u00f9\u00032\u0019\u0000\u00f5\u00f6"+
		"\u0005\n\u0000\u0000\u00f6\u00f8\u00032\u0019\u0000\u00f7\u00f5\u0001"+
		"\u0000\u0000\u0000\u00f8\u00fb\u0001\u0000\u0000\u0000\u00f9\u00f7\u0001"+
		"\u0000\u0000\u0000\u00f9\u00fa\u0001\u0000\u0000\u0000\u00fa\u00fc\u0001"+
		"\u0000\u0000\u0000\u00fb\u00f9\u0001\u0000\u0000\u0000\u00fc\u00fd\u0007"+
		"\b\u0000\u0000\u00fd\u00fe\u0003\u0014\n\u0000\u00fe\u00ff\u0005\t\u0000"+
		"\u0000\u00ff\u010e\u0001\u0000\u0000\u0000\u0100\u0101\u0005>\u0000\u0000"+
		"\u0101\u0106\u00032\u0019\u0000\u0102\u0103\u0005\n\u0000\u0000\u0103"+
		"\u0105\u00032\u0019\u0000\u0104\u0102\u0001\u0000\u0000\u0000\u0105\u0108"+
		"\u0001\u0000\u0000\u0000\u0106\u0104\u0001\u0000\u0000\u0000\u0106\u0107"+
		"\u0001\u0000\u0000\u0000\u0107\u0109\u0001\u0000\u0000\u0000\u0108\u0106"+
		"\u0001\u0000\u0000\u0000\u0109\u010a\u0005?\u0000\u0000\u010a\u010b\u0003"+
		"\u0014\n\u0000\u010b\u010c\u0005\t\u0000\u0000\u010c\u010e\u0001\u0000"+
		"\u0000\u0000\u010d\u00d5\u0001\u0000\u0000\u0000\u010d\u00e5\u0001\u0000"+
		"\u0000\u0000\u010d\u00e9\u0001\u0000\u0000\u0000\u010d\u00f3\u0001\u0000"+
		"\u0000\u0000\u010d\u0100\u0001\u0000\u0000\u0000\u010e\u0017\u0001\u0000"+
		"\u0000\u0000\u010f\u0110\u0005+\u0000\u0000\u0110\u0111\u0003\u001a\r"+
		"\u0000\u0111\u0019\u0001\u0000\u0000\u0000\u0112\u0113\u0005,\u0000\u0000"+
		"\u0113\u001b\u0001\u0000\u0000\u0000\u0114\u0115\u00052\u0000\u0000\u0115"+
		"\u0116\u0005Q\u0000\u0000\u0116\u0117\u00058\u0000\u0000\u0117\u0118\u0003"+
		"\u001e\u000f\u0000\u0118\u0119\u00059\u0000\u0000\u0119\u011a\u0003\u0002"+
		"\u0001\u0000\u011a\u001d\u0001\u0000\u0000\u0000\u011b\u011c\u0003\u0014"+
		"\n\u0000\u011c\u011d\u0005\u000b\u0000\u0000\u011d\u0120\u0003\u0014\n"+
		"\u0000\u011e\u011f\u0005\u000b\u0000\u0000\u011f\u0121\u0003\u0014\n\u0000"+
		"\u0120\u011e\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000\u0000"+
		"\u0121\u001f\u0001\u0000\u0000\u0000\u0122\u0123\u00053\u0000\u0000\u0123"+
		"\u0124\u0003\u0014\n\u0000\u0124\u0125\u00059\u0000\u0000\u0125\u0126"+
		"\u0003\u0002\u0001\u0000\u0126!\u0001\u0000\u0000\u0000\u0127\u0128\u0005"+
		"4\u0000\u0000\u0128\u0129\u0003\u0002\u0001\u0000\u0129\u012a\u00055\u0000"+
		"\u0000\u012a\u012b\u0003\u0014\n\u0000\u012b\u012c\u0005\t\u0000\u0000"+
		"\u012c#\u0001\u0000\u0000\u0000\u012d\u012e\u0005&\u0000\u0000\u012e\u012f"+
		"\u00032\u0019\u0000\u012f\u0130\u00059\u0000\u0000\u0130\u0131\u0003\f"+
		"\u0006\u0000\u0131%\u0001\u0000\u0000\u0000\u0132\u0133\u00051\u0000\u0000"+
		"\u0133\u0134\u0005Q\u0000\u0000\u0134\u0135\u0005&\u0000\u0000\u0135\u0136"+
		"\u0003\f\u0006\u0000\u0136\'\u0001\u0000\u0000\u0000\u0137\u013e\u0003"+
		"\u0006\u0003\u0000\u0138\u013e\u0003\n\u0005\u0000\u0139\u013a\u0003\u000e"+
		"\u0007\u0000\u013a\u013b\u0005\t\u0000\u0000\u013b\u013e\u0001\u0000\u0000"+
		"\u0000\u013c\u013e\u0003,\u0016\u0000\u013d\u0137\u0001\u0000\u0000\u0000"+
		"\u013d\u0138\u0001\u0000\u0000\u0000\u013d\u0139\u0001\u0000\u0000\u0000"+
		"\u013d\u013c\u0001\u0000\u0000\u0000\u013e)\u0001\u0000\u0000\u0000\u013f"+
		"\u0140\u0005Q\u0000\u0000\u0140\u0141\u0005\r\u0000\u0000\u0141\u0142"+
		"\u0005\"\u0000\u0000\u0142\u0144\u0005\u0003\u0000\u0000\u0143\u0145\u0003"+
		"(\u0014\u0000\u0144\u0143\u0001\u0000\u0000\u0000\u0145\u0146\u0001\u0000"+
		"\u0000\u0000\u0146\u0144\u0001\u0000\u0000\u0000\u0146\u0147\u0001\u0000"+
		"\u0000\u0000\u0147\u0148\u0001\u0000\u0000\u0000\u0148\u0149\u0005\u0004"+
		"\u0000\u0000\u0149+\u0001\u0000\u0000\u0000\u014a\u014b\u0005A\u0000\u0000"+
		"\u014b\u014c\u0005B\u0000\u0000\u014c\u014d\u00032\u0019\u0000\u014d\u014e"+
		"\u0003\u0002\u0001\u0000\u014e-\u0001\u0000\u0000\u0000\u014f\u0150\u0005"+
		"6\u0000\u0000\u0150\u0151\u0003\u0014\n\u0000\u0151\u0152\u00059\u0000"+
		"\u0000\u0152\u0156\u0003\u0002\u0001\u0000\u0153\u0154\u00057\u0000\u0000"+
		"\u0154\u0155\u00059\u0000\u0000\u0155\u0157\u0003\u0002\u0001\u0000\u0156"+
		"\u0153\u0001\u0000\u0000\u0000\u0156\u0157\u0001\u0000\u0000\u0000\u0157"+
		"/\u0001\u0000\u0000\u0000\u0158\u0159\u0005\u000e\u0000\u0000\u0159\u018d"+
		"\u0006\u0018\uffff\uffff\u0000\u015a\u015b\u0005\u0010\u0000\u0000\u015b"+
		"\u018d\u0006\u0018\uffff\uffff\u0000\u015c\u015d\u0005\u0011\u0000\u0000"+
		"\u015d\u018d\u0006\u0018\uffff\uffff\u0000\u015e\u015f\u0005\u000f\u0000"+
		"\u0000\u015f\u018d\u0006\u0018\uffff\uffff\u0000\u0160\u0161\u0005\u0012"+
		"\u0000\u0000\u0161\u018d\u0006\u0018\uffff\uffff\u0000\u0162\u0163\u0005"+
		"\u0013\u0000\u0000\u0163\u018d\u0006\u0018\uffff\uffff\u0000\u0164\u0165"+
		"\u0005\u0014\u0000\u0000\u0165\u018d\u0006\u0018\uffff\uffff\u0000\u0166"+
		"\u0167\u0005\u0015\u0000\u0000\u0167\u018d\u0006\u0018\uffff\uffff\u0000"+
		"\u0168\u0169\u0005\u0016\u0000\u0000\u0169\u018d\u0006\u0018\uffff\uffff"+
		"\u0000\u016a\u016b\u0005\u0017\u0000\u0000\u016b\u018d\u0006\u0018\uffff"+
		"\uffff\u0000\u016c\u016d\u0005\u0018\u0000\u0000\u016d\u018d\u0006\u0018"+
		"\uffff\uffff\u0000\u016e\u016f\u0005\u0019\u0000\u0000\u016f\u018d\u0006"+
		"\u0018\uffff\uffff\u0000\u0170\u0171\u0005\u001a\u0000\u0000\u0171\u018d"+
		"\u0006\u0018\uffff\uffff\u0000\u0172\u0173\u0005\u001b\u0000\u0000\u0173"+
		"\u018d\u0006\u0018\uffff\uffff\u0000\u0174\u0175\u0005\u001c\u0000\u0000"+
		"\u0175\u018d\u0006\u0018\uffff\uffff\u0000\u0176\u0177\u0005\u001d\u0000"+
		"\u0000\u0177\u018d\u0006\u0018\uffff\uffff\u0000\u0178\u0179\u0005\u001e"+
		"\u0000\u0000\u0179\u018d\u0006\u0018\uffff\uffff\u0000\u017a\u017b\u0005"+
		"\u001f\u0000\u0000\u017b\u018d\u0006\u0018\uffff\uffff\u0000\u017c\u017d"+
		"\u0005 \u0000\u0000\u017d\u018d\u0006\u0018\uffff\uffff\u0000\u017e\u017f"+
		"\u0005!\u0000\u0000\u017f\u018d\u0006\u0018\uffff\uffff\u0000\u0180\u0181"+
		"\u0005%\u0000\u0000\u0181\u018d\u0006\u0018\uffff\uffff\u0000\u0182\u0183"+
		"\u0005#\u0000\u0000\u0183\u018d\u0006\u0018\uffff\uffff\u0000\u0184\u0185"+
		"\u0005$\u0000\u0000\u0185\u0186\u0005H\u0000\u0000\u0186\u0187\u00030"+
		"\u0018\u0000\u0187\u0188\u0005G\u0000\u0000\u0188\u0189\u0006\u0018\uffff"+
		"\uffff\u0000\u0189\u018d\u0001\u0000\u0000\u0000\u018a\u018b\u0005Q\u0000"+
		"\u0000\u018b\u018d\u0006\u0018\uffff\uffff\u0000\u018c\u0158\u0001\u0000"+
		"\u0000\u0000\u018c\u015a\u0001\u0000\u0000\u0000\u018c\u015c\u0001\u0000"+
		"\u0000\u0000\u018c\u015e\u0001\u0000\u0000\u0000\u018c\u0160\u0001\u0000"+
		"\u0000\u0000\u018c\u0162\u0001\u0000\u0000\u0000\u018c\u0164\u0001\u0000"+
		"\u0000\u0000\u018c\u0166\u0001\u0000\u0000\u0000\u018c\u0168\u0001\u0000"+
		"\u0000\u0000\u018c\u016a\u0001\u0000\u0000\u0000\u018c\u016c\u0001\u0000"+
		"\u0000\u0000\u018c\u016e\u0001\u0000\u0000\u0000\u018c\u0170\u0001\u0000"+
		"\u0000\u0000\u018c\u0172\u0001\u0000\u0000\u0000\u018c\u0174\u0001\u0000"+
		"\u0000\u0000\u018c\u0176\u0001\u0000\u0000\u0000\u018c\u0178\u0001\u0000"+
		"\u0000\u0000\u018c\u017a\u0001\u0000\u0000\u0000\u018c\u017c\u0001\u0000"+
		"\u0000\u0000\u018c\u017e\u0001\u0000\u0000\u0000\u018c\u0180\u0001\u0000"+
		"\u0000\u0000\u018c\u0182\u0001\u0000\u0000\u0000\u018c\u0184\u0001\u0000"+
		"\u0000\u0000\u018c\u018a\u0001\u0000\u0000\u0000\u018d1\u0001\u0000\u0000"+
		"\u0000\u018e\u01a0\u0005Q\u0000\u0000\u018f\u0190\u0005Q\u0000\u0000\u0190"+
		"\u0191\u0005\f\u0000\u0000\u0191\u01a0\u00032\u0019\u0000\u0192\u0197"+
		"\u0005Q\u0000\u0000\u0193\u0194\u0005\u0005\u0000\u0000\u0194\u0195\u0003"+
		"\u0014\n\u0000\u0195\u0196\u0005\u0006\u0000\u0000\u0196\u0198\u0001\u0000"+
		"\u0000\u0000\u0197\u0193\u0001\u0000\u0000\u0000\u0198\u0199\u0001\u0000"+
		"\u0000\u0000\u0199\u0197\u0001\u0000\u0000\u0000\u0199\u019a\u0001\u0000"+
		"\u0000\u0000\u019a\u019d\u0001\u0000\u0000\u0000\u019b\u019c\u0005\f\u0000"+
		"\u0000\u019c\u019e\u00032\u0019\u0000\u019d\u019b\u0001\u0000\u0000\u0000"+
		"\u019d\u019e\u0001\u0000\u0000\u0000\u019e\u01a0\u0001\u0000\u0000\u0000"+
		"\u019f\u018e\u0001\u0000\u0000\u0000\u019f\u018f\u0001\u0000\u0000\u0000"+
		"\u019f\u0192\u0001\u0000\u0000\u0000\u01a03\u0001\u0000\u0000\u0000\u001d"+
		"7KOTZ`glw{\u008c\u00aa\u00bc\u00d0\u00d2\u00db\u00e2\u00ef\u00f9\u0106"+
		"\u010d\u0120\u013d\u0146\u0156\u018c\u0199\u019d\u019f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}