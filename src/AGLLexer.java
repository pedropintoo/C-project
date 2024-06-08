// Generated from AGLLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class AGLLexer extends Lexer {
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
		ID=80, NAME=81, BOOLEAN=82, INT=83, FLOAT=84, STRING=85, LINE_COMMENT=86, 
		COMMENT=87, WS=88, ERROR=89;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COLON", 
			"EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "DOUBLECOLON", "INTEGER", 
			"NUMBER", "STRING_", "POINT", "VECTOR", "TIME", "BOOLEAN_", "VIEW", "LINE", 
			"RECTANGLE", "ELLIPSE", "ARC", "ARCHORD", "PIESLICE", "TEXT", "DOTTYPE", 
			"POLYLINE", "SPLINE", "POLYGON", "BLOB", "Model", "Enum", "ARRAY", "SCRIPT", 
			"WITH", "AT", "PRINT", "REFRESH", "CLOSE", "MOUSE", "CLICK", "WAIT", 
			"DEEPCOPY", "INPUT", "LOAD", "PLAY", "FOR", "WHILE", "REPEAT", "UNTIL", 
			"IF", "ELSE", "IN", "DO", "AFTER", "MS", "S", "MOVE", "ROTATE", "BY", 
			"TO", "ACTION", "ON", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "GTE", 
			"LTE", "EQ", "NEQ", "AND", "OR", "NOT", "ID", "NAME", "BOOLEAN", "INT", 
			"FLOAT", "STRING", "LETTER", "DIGIT", "ESC", "LINE_COMMENT", "COMMENT", 
			"WS", "ERROR"
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
			"LTE", "EQ", "NEQ", "AND", "OR", "NOT", "ID", "NAME", "BOOLEAN", "INT", 
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


	public AGLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "AGLLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000Y\u0291\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007"+
		":\u0002;\u0007;\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007"+
		"?\u0002@\u0007@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007"+
		"D\u0002E\u0007E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007"+
		"I\u0002J\u0007J\u0002K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007"+
		"N\u0002O\u0007O\u0002P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007"+
		"S\u0002T\u0007T\u0002U\u0007U\u0002V\u0007V\u0002W\u0007W\u0002X\u0007"+
		"X\u0002Y\u0007Y\u0002Z\u0007Z\u0002[\u0007[\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001 \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001!"+
		"\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001"+
		"#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001%\u0001%\u0001%\u0001%\u0001%\u0001&\u0001&\u0001&\u0001\'\u0001"+
		"\'\u0001\'\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0001(\u0001("+
		"\u0001(\u0001(\u0001(\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001+\u0001+\u0001+\u0001+\u0001"+
		"+\u0001+\u0001,\u0001,\u0001,\u0001,\u0001,\u0001-\u0001-\u0001-\u0001"+
		"-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001.\u0001.\u0001.\u0001.\u0001"+
		".\u0001.\u0001/\u0001/\u0001/\u0001/\u0001/\u00010\u00010\u00010\u0001"+
		"0\u00010\u00011\u00011\u00011\u00011\u00012\u00012\u00012\u00012\u0001"+
		"2\u00012\u00013\u00013\u00013\u00013\u00013\u00013\u00013\u00014\u0001"+
		"4\u00014\u00014\u00014\u00014\u00015\u00015\u00015\u00016\u00016\u0001"+
		"6\u00016\u00016\u00017\u00017\u00017\u00018\u00018\u00018\u00019\u0001"+
		"9\u00019\u00019\u00019\u00019\u0001:\u0001:\u0001:\u0001;\u0001;\u0001"+
		"<\u0001<\u0001<\u0001<\u0001<\u0001=\u0001=\u0001=\u0001=\u0001=\u0001"+
		"=\u0001=\u0001>\u0001>\u0001>\u0001?\u0001?\u0001?\u0001@\u0001@\u0001"+
		"@\u0001@\u0001@\u0001@\u0001@\u0001A\u0001A\u0001A\u0001B\u0001B\u0001"+
		"C\u0001C\u0001D\u0001D\u0001E\u0001E\u0001F\u0001F\u0001G\u0001G\u0001"+
		"H\u0001H\u0001H\u0001I\u0001I\u0001I\u0001J\u0001J\u0001J\u0001K\u0001"+
		"K\u0001K\u0001L\u0001L\u0001L\u0001L\u0001M\u0001M\u0001M\u0001N\u0001"+
		"N\u0001N\u0001N\u0001O\u0001O\u0001O\u0005O\u022e\bO\nO\fO\u0231\tO\u0001"+
		"P\u0001P\u0001Q\u0001Q\u0001Q\u0001Q\u0001Q\u0001Q\u0001Q\u0001Q\u0001"+
		"Q\u0003Q\u023e\bQ\u0001R\u0004R\u0241\bR\u000bR\fR\u0242\u0001S\u0004"+
		"S\u0246\bS\u000bS\fS\u0247\u0001S\u0001S\u0004S\u024c\bS\u000bS\fS\u024d"+
		"\u0001S\u0001S\u0003S\u0252\bS\u0001S\u0004S\u0255\bS\u000bS\fS\u0256"+
		"\u0003S\u0259\bS\u0001T\u0001T\u0001T\u0005T\u025e\bT\nT\fT\u0261\tT\u0001"+
		"T\u0001T\u0001U\u0001U\u0001V\u0001V\u0001W\u0001W\u0001W\u0001W\u0003"+
		"W\u026d\bW\u0001X\u0001X\u0005X\u0271\bX\nX\fX\u0274\tX\u0001X\u0001X"+
		"\u0001X\u0001X\u0001Y\u0001Y\u0001Y\u0001Y\u0001Y\u0005Y\u027f\bY\nY\f"+
		"Y\u0282\tY\u0001Y\u0001Y\u0001Y\u0001Y\u0001Y\u0001Z\u0004Z\u028a\bZ\u000b"+
		"Z\fZ\u028b\u0001Z\u0001Z\u0001[\u0001[\u0003\u025f\u0272\u0280\u0000\\"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017"+
		"/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f? A!C\"E#G$I%"+
		"K&M\'O(Q)S*U+W,Y-[.]/_0a1c2e3g4i5k6m7o8q9s:u;w<y={>}?\u007f@\u0081A\u0083"+
		"B\u0085C\u0087D\u0089E\u008bF\u008dG\u008fH\u0091I\u0093J\u0095K\u0097"+
		"L\u0099M\u009bN\u009dO\u009fP\u00a1Q\u00a3R\u00a5S\u00a7T\u00a9U\u00ab"+
		"\u0000\u00ad\u0000\u00af\u0000\u00b1V\u00b3W\u00b5X\u00b7Y\u0001\u0000"+
		"\u0006\u0001\u0000..\u0002\u0000EEee\u0002\u0000++--\u0004\u0000AZ__a"+
		"z\u00c0\u00ff\u0001\u000009\u0003\u0000\t\n\r\r  \u029d\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000"+
		"\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'"+
		"\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000"+
		"\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000"+
		"\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005"+
		"\u0001\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000"+
		"\u0000\u0000\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000"+
		"\u0000?\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000C"+
		"\u0001\u0000\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0000G\u0001\u0000"+
		"\u0000\u0000\u0000I\u0001\u0000\u0000\u0000\u0000K\u0001\u0000\u0000\u0000"+
		"\u0000M\u0001\u0000\u0000\u0000\u0000O\u0001\u0000\u0000\u0000\u0000Q"+
		"\u0001\u0000\u0000\u0000\u0000S\u0001\u0000\u0000\u0000\u0000U\u0001\u0000"+
		"\u0000\u0000\u0000W\u0001\u0000\u0000\u0000\u0000Y\u0001\u0000\u0000\u0000"+
		"\u0000[\u0001\u0000\u0000\u0000\u0000]\u0001\u0000\u0000\u0000\u0000_"+
		"\u0001\u0000\u0000\u0000\u0000a\u0001\u0000\u0000\u0000\u0000c\u0001\u0000"+
		"\u0000\u0000\u0000e\u0001\u0000\u0000\u0000\u0000g\u0001\u0000\u0000\u0000"+
		"\u0000i\u0001\u0000\u0000\u0000\u0000k\u0001\u0000\u0000\u0000\u0000m"+
		"\u0001\u0000\u0000\u0000\u0000o\u0001\u0000\u0000\u0000\u0000q\u0001\u0000"+
		"\u0000\u0000\u0000s\u0001\u0000\u0000\u0000\u0000u\u0001\u0000\u0000\u0000"+
		"\u0000w\u0001\u0000\u0000\u0000\u0000y\u0001\u0000\u0000\u0000\u0000{"+
		"\u0001\u0000\u0000\u0000\u0000}\u0001\u0000\u0000\u0000\u0000\u007f\u0001"+
		"\u0000\u0000\u0000\u0000\u0081\u0001\u0000\u0000\u0000\u0000\u0083\u0001"+
		"\u0000\u0000\u0000\u0000\u0085\u0001\u0000\u0000\u0000\u0000\u0087\u0001"+
		"\u0000\u0000\u0000\u0000\u0089\u0001\u0000\u0000\u0000\u0000\u008b\u0001"+
		"\u0000\u0000\u0000\u0000\u008d\u0001\u0000\u0000\u0000\u0000\u008f\u0001"+
		"\u0000\u0000\u0000\u0000\u0091\u0001\u0000\u0000\u0000\u0000\u0093\u0001"+
		"\u0000\u0000\u0000\u0000\u0095\u0001\u0000\u0000\u0000\u0000\u0097\u0001"+
		"\u0000\u0000\u0000\u0000\u0099\u0001\u0000\u0000\u0000\u0000\u009b\u0001"+
		"\u0000\u0000\u0000\u0000\u009d\u0001\u0000\u0000\u0000\u0000\u009f\u0001"+
		"\u0000\u0000\u0000\u0000\u00a1\u0001\u0000\u0000\u0000\u0000\u00a3\u0001"+
		"\u0000\u0000\u0000\u0000\u00a5\u0001\u0000\u0000\u0000\u0000\u00a7\u0001"+
		"\u0000\u0000\u0000\u0000\u00a9\u0001\u0000\u0000\u0000\u0000\u00b1\u0001"+
		"\u0000\u0000\u0000\u0000\u00b3\u0001\u0000\u0000\u0000\u0000\u00b5\u0001"+
		"\u0000\u0000\u0000\u0000\u00b7\u0001\u0000\u0000\u0000\u0001\u00b9\u0001"+
		"\u0000\u0000\u0000\u0003\u00bb\u0001\u0000\u0000\u0000\u0005\u00bd\u0001"+
		"\u0000\u0000\u0000\u0007\u00bf\u0001\u0000\u0000\u0000\t\u00c1\u0001\u0000"+
		"\u0000\u0000\u000b\u00c3\u0001\u0000\u0000\u0000\r\u00c5\u0001\u0000\u0000"+
		"\u0000\u000f\u00c7\u0001\u0000\u0000\u0000\u0011\u00c9\u0001\u0000\u0000"+
		"\u0000\u0013\u00cb\u0001\u0000\u0000\u0000\u0015\u00cd\u0001\u0000\u0000"+
		"\u0000\u0017\u00d0\u0001\u0000\u0000\u0000\u0019\u00d2\u0001\u0000\u0000"+
		"\u0000\u001b\u00d5\u0001\u0000\u0000\u0000\u001d\u00dd\u0001\u0000\u0000"+
		"\u0000\u001f\u00e4\u0001\u0000\u0000\u0000!\u00eb\u0001\u0000\u0000\u0000"+
		"#\u00f1\u0001\u0000\u0000\u0000%\u00f8\u0001\u0000\u0000\u0000\'\u00fd"+
		"\u0001\u0000\u0000\u0000)\u0105\u0001\u0000\u0000\u0000+\u010a\u0001\u0000"+
		"\u0000\u0000-\u010f\u0001\u0000\u0000\u0000/\u0119\u0001\u0000\u0000\u0000"+
		"1\u0121\u0001\u0000\u0000\u00003\u0125\u0001\u0000\u0000\u00005\u012e"+
		"\u0001\u0000\u0000\u00007\u0137\u0001\u0000\u0000\u00009\u013c\u0001\u0000"+
		"\u0000\u0000;\u0140\u0001\u0000\u0000\u0000=\u0149\u0001\u0000\u0000\u0000"+
		"?\u0150\u0001\u0000\u0000\u0000A\u0158\u0001\u0000\u0000\u0000C\u015d"+
		"\u0001\u0000\u0000\u0000E\u0163\u0001\u0000\u0000\u0000G\u0168\u0001\u0000"+
		"\u0000\u0000I\u016e\u0001\u0000\u0000\u0000K\u0175\u0001\u0000\u0000\u0000"+
		"M\u017a\u0001\u0000\u0000\u0000O\u017d\u0001\u0000\u0000\u0000Q\u0183"+
		"\u0001\u0000\u0000\u0000S\u018b\u0001\u0000\u0000\u0000U\u0191\u0001\u0000"+
		"\u0000\u0000W\u0197\u0001\u0000\u0000\u0000Y\u019d\u0001\u0000\u0000\u0000"+
		"[\u01a2\u0001\u0000\u0000\u0000]\u01ab\u0001\u0000\u0000\u0000_\u01b1"+
		"\u0001\u0000\u0000\u0000a\u01b6\u0001\u0000\u0000\u0000c\u01bb\u0001\u0000"+
		"\u0000\u0000e\u01bf\u0001\u0000\u0000\u0000g\u01c5\u0001\u0000\u0000\u0000"+
		"i\u01cc\u0001\u0000\u0000\u0000k\u01d2\u0001\u0000\u0000\u0000m\u01d5"+
		"\u0001\u0000\u0000\u0000o\u01da\u0001\u0000\u0000\u0000q\u01dd\u0001\u0000"+
		"\u0000\u0000s\u01e0\u0001\u0000\u0000\u0000u\u01e6\u0001\u0000\u0000\u0000"+
		"w\u01e9\u0001\u0000\u0000\u0000y\u01eb\u0001\u0000\u0000\u0000{\u01f0"+
		"\u0001\u0000\u0000\u0000}\u01f7\u0001\u0000\u0000\u0000\u007f\u01fa\u0001"+
		"\u0000\u0000\u0000\u0081\u01fd\u0001\u0000\u0000\u0000\u0083\u0204\u0001"+
		"\u0000\u0000\u0000\u0085\u0207\u0001\u0000\u0000\u0000\u0087\u0209\u0001"+
		"\u0000\u0000\u0000\u0089\u020b\u0001\u0000\u0000\u0000\u008b\u020d\u0001"+
		"\u0000\u0000\u0000\u008d\u020f\u0001\u0000\u0000\u0000\u008f\u0211\u0001"+
		"\u0000\u0000\u0000\u0091\u0213\u0001\u0000\u0000\u0000\u0093\u0216\u0001"+
		"\u0000\u0000\u0000\u0095\u0219\u0001\u0000\u0000\u0000\u0097\u021c\u0001"+
		"\u0000\u0000\u0000\u0099\u021f\u0001\u0000\u0000\u0000\u009b\u0223\u0001"+
		"\u0000\u0000\u0000\u009d\u0226\u0001\u0000\u0000\u0000\u009f\u022a\u0001"+
		"\u0000\u0000\u0000\u00a1\u0232\u0001\u0000\u0000\u0000\u00a3\u023d\u0001"+
		"\u0000\u0000\u0000\u00a5\u0240\u0001\u0000\u0000\u0000\u00a7\u0245\u0001"+
		"\u0000\u0000\u0000\u00a9\u025a\u0001\u0000\u0000\u0000\u00ab\u0264\u0001"+
		"\u0000\u0000\u0000\u00ad\u0266\u0001\u0000\u0000\u0000\u00af\u026c\u0001"+
		"\u0000\u0000\u0000\u00b1\u026e\u0001\u0000\u0000\u0000\u00b3\u0279\u0001"+
		"\u0000\u0000\u0000\u00b5\u0289\u0001\u0000\u0000\u0000\u00b7\u028f\u0001"+
		"\u0000\u0000\u0000\u00b9\u00ba\u0005(\u0000\u0000\u00ba\u0002\u0001\u0000"+
		"\u0000\u0000\u00bb\u00bc\u0005)\u0000\u0000\u00bc\u0004\u0001\u0000\u0000"+
		"\u0000\u00bd\u00be\u0005{\u0000\u0000\u00be\u0006\u0001\u0000\u0000\u0000"+
		"\u00bf\u00c0\u0005}\u0000\u0000\u00c0\b\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c2\u0005[\u0000\u0000\u00c2\n\u0001\u0000\u0000\u0000\u00c3\u00c4"+
		"\u0005]\u0000\u0000\u00c4\f\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005"+
		":\u0000\u0000\u00c6\u000e\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005=\u0000"+
		"\u0000\u00c8\u0010\u0001\u0000\u0000\u0000\u00c9\u00ca\u0005;\u0000\u0000"+
		"\u00ca\u0012\u0001\u0000\u0000\u0000\u00cb\u00cc\u0005,\u0000\u0000\u00cc"+
		"\u0014\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005.\u0000\u0000\u00ce\u00cf"+
		"\u0005.\u0000\u0000\u00cf\u0016\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005"+
		".\u0000\u0000\u00d1\u0018\u0001\u0000\u0000\u0000\u00d2\u00d3\u0005:\u0000"+
		"\u0000\u00d3\u00d4\u0005:\u0000\u0000\u00d4\u001a\u0001\u0000\u0000\u0000"+
		"\u00d5\u00d6\u0005I\u0000\u0000\u00d6\u00d7\u0005n\u0000\u0000\u00d7\u00d8"+
		"\u0005t\u0000\u0000\u00d8\u00d9\u0005e\u0000\u0000\u00d9\u00da\u0005g"+
		"\u0000\u0000\u00da\u00db\u0005e\u0000\u0000\u00db\u00dc\u0005r\u0000\u0000"+
		"\u00dc\u001c\u0001\u0000\u0000\u0000\u00dd\u00de\u0005N\u0000\u0000\u00de"+
		"\u00df\u0005u\u0000\u0000\u00df\u00e0\u0005m\u0000\u0000\u00e0\u00e1\u0005"+
		"b\u0000\u0000\u00e1\u00e2\u0005e\u0000\u0000\u00e2\u00e3\u0005r\u0000"+
		"\u0000\u00e3\u001e\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005S\u0000\u0000"+
		"\u00e5\u00e6\u0005t\u0000\u0000\u00e6\u00e7\u0005r\u0000\u0000\u00e7\u00e8"+
		"\u0005i\u0000\u0000\u00e8\u00e9\u0005n\u0000\u0000\u00e9\u00ea\u0005g"+
		"\u0000\u0000\u00ea \u0001\u0000\u0000\u0000\u00eb\u00ec\u0005P\u0000\u0000"+
		"\u00ec\u00ed\u0005o\u0000\u0000\u00ed\u00ee\u0005i\u0000\u0000\u00ee\u00ef"+
		"\u0005n\u0000\u0000\u00ef\u00f0\u0005t\u0000\u0000\u00f0\"\u0001\u0000"+
		"\u0000\u0000\u00f1\u00f2\u0005V\u0000\u0000\u00f2\u00f3\u0005e\u0000\u0000"+
		"\u00f3\u00f4\u0005c\u0000\u0000\u00f4\u00f5\u0005t\u0000\u0000\u00f5\u00f6"+
		"\u0005o\u0000\u0000\u00f6\u00f7\u0005r\u0000\u0000\u00f7$\u0001\u0000"+
		"\u0000\u0000\u00f8\u00f9\u0005T\u0000\u0000\u00f9\u00fa\u0005i\u0000\u0000"+
		"\u00fa\u00fb\u0005m\u0000\u0000\u00fb\u00fc\u0005e\u0000\u0000\u00fc&"+
		"\u0001\u0000\u0000\u0000\u00fd\u00fe\u0005B\u0000\u0000\u00fe\u00ff\u0005"+
		"o\u0000\u0000\u00ff\u0100\u0005o\u0000\u0000\u0100\u0101\u0005l\u0000"+
		"\u0000\u0101\u0102\u0005e\u0000\u0000\u0102\u0103\u0005a\u0000\u0000\u0103"+
		"\u0104\u0005n\u0000\u0000\u0104(\u0001\u0000\u0000\u0000\u0105\u0106\u0005"+
		"V\u0000\u0000\u0106\u0107\u0005i\u0000\u0000\u0107\u0108\u0005e\u0000"+
		"\u0000\u0108\u0109\u0005w\u0000\u0000\u0109*\u0001\u0000\u0000\u0000\u010a"+
		"\u010b\u0005L\u0000\u0000\u010b\u010c\u0005i\u0000\u0000\u010c\u010d\u0005"+
		"n\u0000\u0000\u010d\u010e\u0005e\u0000\u0000\u010e,\u0001\u0000\u0000"+
		"\u0000\u010f\u0110\u0005R\u0000\u0000\u0110\u0111\u0005e\u0000\u0000\u0111"+
		"\u0112\u0005c\u0000\u0000\u0112\u0113\u0005t\u0000\u0000\u0113\u0114\u0005"+
		"a\u0000\u0000\u0114\u0115\u0005n\u0000\u0000\u0115\u0116\u0005g\u0000"+
		"\u0000\u0116\u0117\u0005l\u0000\u0000\u0117\u0118\u0005e\u0000\u0000\u0118"+
		".\u0001\u0000\u0000\u0000\u0119\u011a\u0005E\u0000\u0000\u011a\u011b\u0005"+
		"l\u0000\u0000\u011b\u011c\u0005l\u0000\u0000\u011c\u011d\u0005i\u0000"+
		"\u0000\u011d\u011e\u0005p\u0000\u0000\u011e\u011f\u0005s\u0000\u0000\u011f"+
		"\u0120\u0005e\u0000\u0000\u01200\u0001\u0000\u0000\u0000\u0121\u0122\u0005"+
		"A\u0000\u0000\u0122\u0123\u0005r\u0000\u0000\u0123\u0124\u0005c\u0000"+
		"\u0000\u01242\u0001\u0000\u0000\u0000\u0125\u0126\u0005A\u0000\u0000\u0126"+
		"\u0127\u0005r\u0000\u0000\u0127\u0128\u0005c\u0000\u0000\u0128\u0129\u0005"+
		"C\u0000\u0000\u0129\u012a\u0005h\u0000\u0000\u012a\u012b\u0005o\u0000"+
		"\u0000\u012b\u012c\u0005r\u0000\u0000\u012c\u012d\u0005d\u0000\u0000\u012d"+
		"4\u0001\u0000\u0000\u0000\u012e\u012f\u0005P\u0000\u0000\u012f\u0130\u0005"+
		"i\u0000\u0000\u0130\u0131\u0005e\u0000\u0000\u0131\u0132\u0005S\u0000"+
		"\u0000\u0132\u0133\u0005l\u0000\u0000\u0133\u0134\u0005i\u0000\u0000\u0134"+
		"\u0135\u0005c\u0000\u0000\u0135\u0136\u0005e\u0000\u0000\u01366\u0001"+
		"\u0000\u0000\u0000\u0137\u0138\u0005T\u0000\u0000\u0138\u0139\u0005e\u0000"+
		"\u0000\u0139\u013a\u0005x\u0000\u0000\u013a\u013b\u0005t\u0000\u0000\u013b"+
		"8\u0001\u0000\u0000\u0000\u013c\u013d\u0005D\u0000\u0000\u013d\u013e\u0005"+
		"o\u0000\u0000\u013e\u013f\u0005t\u0000\u0000\u013f:\u0001\u0000\u0000"+
		"\u0000\u0140\u0141\u0005P\u0000\u0000\u0141\u0142\u0005o\u0000\u0000\u0142"+
		"\u0143\u0005l\u0000\u0000\u0143\u0144\u0005y\u0000\u0000\u0144\u0145\u0005"+
		"L\u0000\u0000\u0145\u0146\u0005i\u0000\u0000\u0146\u0147\u0005n\u0000"+
		"\u0000\u0147\u0148\u0005e\u0000\u0000\u0148<\u0001\u0000\u0000\u0000\u0149"+
		"\u014a\u0005S\u0000\u0000\u014a\u014b\u0005p\u0000\u0000\u014b\u014c\u0005"+
		"l\u0000\u0000\u014c\u014d\u0005i\u0000\u0000\u014d\u014e\u0005n\u0000"+
		"\u0000\u014e\u014f\u0005e\u0000\u0000\u014f>\u0001\u0000\u0000\u0000\u0150"+
		"\u0151\u0005P\u0000\u0000\u0151\u0152\u0005o\u0000\u0000\u0152\u0153\u0005"+
		"l\u0000\u0000\u0153\u0154\u0005y\u0000\u0000\u0154\u0155\u0005g\u0000"+
		"\u0000\u0155\u0156\u0005o\u0000\u0000\u0156\u0157\u0005n\u0000\u0000\u0157"+
		"@\u0001\u0000\u0000\u0000\u0158\u0159\u0005B\u0000\u0000\u0159\u015a\u0005"+
		"l\u0000\u0000\u015a\u015b\u0005o\u0000\u0000\u015b\u015c\u0005b\u0000"+
		"\u0000\u015cB\u0001\u0000\u0000\u0000\u015d\u015e\u0005M\u0000\u0000\u015e"+
		"\u015f\u0005o\u0000\u0000\u015f\u0160\u0005d\u0000\u0000\u0160\u0161\u0005"+
		"e\u0000\u0000\u0161\u0162\u0005l\u0000\u0000\u0162D\u0001\u0000\u0000"+
		"\u0000\u0163\u0164\u0005E\u0000\u0000\u0164\u0165\u0005n\u0000\u0000\u0165"+
		"\u0166\u0005u\u0000\u0000\u0166\u0167\u0005m\u0000\u0000\u0167F\u0001"+
		"\u0000\u0000\u0000\u0168\u0169\u0005A\u0000\u0000\u0169\u016a\u0005r\u0000"+
		"\u0000\u016a\u016b\u0005r\u0000\u0000\u016b\u016c\u0005a\u0000\u0000\u016c"+
		"\u016d\u0005y\u0000\u0000\u016dH\u0001\u0000\u0000\u0000\u016e\u016f\u0005"+
		"S\u0000\u0000\u016f\u0170\u0005c\u0000\u0000\u0170\u0171\u0005r\u0000"+
		"\u0000\u0171\u0172\u0005i\u0000\u0000\u0172\u0173\u0005p\u0000\u0000\u0173"+
		"\u0174\u0005t\u0000\u0000\u0174J\u0001\u0000\u0000\u0000\u0175\u0176\u0005"+
		"w\u0000\u0000\u0176\u0177\u0005i\u0000\u0000\u0177\u0178\u0005t\u0000"+
		"\u0000\u0178\u0179\u0005h\u0000\u0000\u0179L\u0001\u0000\u0000\u0000\u017a"+
		"\u017b\u0005a\u0000\u0000\u017b\u017c\u0005t\u0000\u0000\u017cN\u0001"+
		"\u0000\u0000\u0000\u017d\u017e\u0005p\u0000\u0000\u017e\u017f\u0005r\u0000"+
		"\u0000\u017f\u0180\u0005i\u0000\u0000\u0180\u0181\u0005n\u0000\u0000\u0181"+
		"\u0182\u0005t\u0000\u0000\u0182P\u0001\u0000\u0000\u0000\u0183\u0184\u0005"+
		"r\u0000\u0000\u0184\u0185\u0005e\u0000\u0000\u0185\u0186\u0005f\u0000"+
		"\u0000\u0186\u0187\u0005r\u0000\u0000\u0187\u0188\u0005e\u0000\u0000\u0188"+
		"\u0189\u0005s\u0000\u0000\u0189\u018a\u0005h\u0000\u0000\u018aR\u0001"+
		"\u0000\u0000\u0000\u018b\u018c\u0005c\u0000\u0000\u018c\u018d\u0005l\u0000"+
		"\u0000\u018d\u018e\u0005o\u0000\u0000\u018e\u018f\u0005s\u0000\u0000\u018f"+
		"\u0190\u0005e\u0000\u0000\u0190T\u0001\u0000\u0000\u0000\u0191\u0192\u0005"+
		"m\u0000\u0000\u0192\u0193\u0005o\u0000\u0000\u0193\u0194\u0005u\u0000"+
		"\u0000\u0194\u0195\u0005s\u0000\u0000\u0195\u0196\u0005e\u0000\u0000\u0196"+
		"V\u0001\u0000\u0000\u0000\u0197\u0198\u0005c\u0000\u0000\u0198\u0199\u0005"+
		"l\u0000\u0000\u0199\u019a\u0005i\u0000\u0000\u019a\u019b\u0005c\u0000"+
		"\u0000\u019b\u019c\u0005k\u0000\u0000\u019cX\u0001\u0000\u0000\u0000\u019d"+
		"\u019e\u0005w\u0000\u0000\u019e\u019f\u0005a\u0000\u0000\u019f\u01a0\u0005"+
		"i\u0000\u0000\u01a0\u01a1\u0005t\u0000\u0000\u01a1Z\u0001\u0000\u0000"+
		"\u0000\u01a2\u01a3\u0005d\u0000\u0000\u01a3\u01a4\u0005e\u0000\u0000\u01a4"+
		"\u01a5\u0005e\u0000\u0000\u01a5\u01a6\u0005p\u0000\u0000\u01a6\u01a7\u0005"+
		"c\u0000\u0000\u01a7\u01a8\u0005o\u0000\u0000\u01a8\u01a9\u0005p\u0000"+
		"\u0000\u01a9\u01aa\u0005y\u0000\u0000\u01aa\\\u0001\u0000\u0000\u0000"+
		"\u01ab\u01ac\u0005i\u0000\u0000\u01ac\u01ad\u0005n\u0000\u0000\u01ad\u01ae"+
		"\u0005p\u0000\u0000\u01ae\u01af\u0005u\u0000\u0000\u01af\u01b0\u0005t"+
		"\u0000\u0000\u01b0^\u0001\u0000\u0000\u0000\u01b1\u01b2\u0005l\u0000\u0000"+
		"\u01b2\u01b3\u0005o\u0000\u0000\u01b3\u01b4\u0005a\u0000\u0000\u01b4\u01b5"+
		"\u0005d\u0000\u0000\u01b5`\u0001\u0000\u0000\u0000\u01b6\u01b7\u0005p"+
		"\u0000\u0000\u01b7\u01b8\u0005l\u0000\u0000\u01b8\u01b9\u0005a\u0000\u0000"+
		"\u01b9\u01ba\u0005y\u0000\u0000\u01bab\u0001\u0000\u0000\u0000\u01bb\u01bc"+
		"\u0005f\u0000\u0000\u01bc\u01bd\u0005o\u0000\u0000\u01bd\u01be\u0005r"+
		"\u0000\u0000\u01bed\u0001\u0000\u0000\u0000\u01bf\u01c0\u0005w\u0000\u0000"+
		"\u01c0\u01c1\u0005h\u0000\u0000\u01c1\u01c2\u0005i\u0000\u0000\u01c2\u01c3"+
		"\u0005l\u0000\u0000\u01c3\u01c4\u0005e\u0000\u0000\u01c4f\u0001\u0000"+
		"\u0000\u0000\u01c5\u01c6\u0005r\u0000\u0000\u01c6\u01c7\u0005e\u0000\u0000"+
		"\u01c7\u01c8\u0005p\u0000\u0000\u01c8\u01c9\u0005e\u0000\u0000\u01c9\u01ca"+
		"\u0005a\u0000\u0000\u01ca\u01cb\u0005t\u0000\u0000\u01cbh\u0001\u0000"+
		"\u0000\u0000\u01cc\u01cd\u0005u\u0000\u0000\u01cd\u01ce\u0005n\u0000\u0000"+
		"\u01ce\u01cf\u0005t\u0000\u0000\u01cf\u01d0\u0005i\u0000\u0000\u01d0\u01d1"+
		"\u0005l\u0000\u0000\u01d1j\u0001\u0000\u0000\u0000\u01d2\u01d3\u0005i"+
		"\u0000\u0000\u01d3\u01d4\u0005f\u0000\u0000\u01d4l\u0001\u0000\u0000\u0000"+
		"\u01d5\u01d6\u0005e\u0000\u0000\u01d6\u01d7\u0005l\u0000\u0000\u01d7\u01d8"+
		"\u0005s\u0000\u0000\u01d8\u01d9\u0005e\u0000\u0000\u01d9n\u0001\u0000"+
		"\u0000\u0000\u01da\u01db\u0005i\u0000\u0000\u01db\u01dc\u0005n\u0000\u0000"+
		"\u01dcp\u0001\u0000\u0000\u0000\u01dd\u01de\u0005d\u0000\u0000\u01de\u01df"+
		"\u0005o\u0000\u0000\u01dfr\u0001\u0000\u0000\u0000\u01e0\u01e1\u0005a"+
		"\u0000\u0000\u01e1\u01e2\u0005f\u0000\u0000\u01e2\u01e3\u0005t\u0000\u0000"+
		"\u01e3\u01e4\u0005e\u0000\u0000\u01e4\u01e5\u0005r\u0000\u0000\u01e5t"+
		"\u0001\u0000\u0000\u0000\u01e6\u01e7\u0005m\u0000\u0000\u01e7\u01e8\u0005"+
		"s\u0000\u0000\u01e8v\u0001\u0000\u0000\u0000\u01e9\u01ea\u0005s\u0000"+
		"\u0000\u01eax\u0001\u0000\u0000\u0000\u01eb\u01ec\u0005m\u0000\u0000\u01ec"+
		"\u01ed\u0005o\u0000\u0000\u01ed\u01ee\u0005v\u0000\u0000\u01ee\u01ef\u0005"+
		"e\u0000\u0000\u01efz\u0001\u0000\u0000\u0000\u01f0\u01f1\u0005r\u0000"+
		"\u0000\u01f1\u01f2\u0005o\u0000\u0000\u01f2\u01f3\u0005t\u0000\u0000\u01f3"+
		"\u01f4\u0005a\u0000\u0000\u01f4\u01f5\u0005t\u0000\u0000\u01f5\u01f6\u0005"+
		"e\u0000\u0000\u01f6|\u0001\u0000\u0000\u0000\u01f7\u01f8\u0005b\u0000"+
		"\u0000\u01f8\u01f9\u0005y\u0000\u0000\u01f9~\u0001\u0000\u0000\u0000\u01fa"+
		"\u01fb\u0005t\u0000\u0000\u01fb\u01fc\u0005o\u0000\u0000\u01fc\u0080\u0001"+
		"\u0000\u0000\u0000\u01fd\u01fe\u0005a\u0000\u0000\u01fe\u01ff\u0005c\u0000"+
		"\u0000\u01ff\u0200\u0005t\u0000\u0000\u0200\u0201\u0005i\u0000\u0000\u0201"+
		"\u0202\u0005o\u0000\u0000\u0202\u0203\u0005n\u0000\u0000\u0203\u0082\u0001"+
		"\u0000\u0000\u0000\u0204\u0205\u0005o\u0000\u0000\u0205\u0206\u0005n\u0000"+
		"\u0000\u0206\u0084\u0001\u0000\u0000\u0000\u0207\u0208\u0005+\u0000\u0000"+
		"\u0208\u0086\u0001\u0000\u0000\u0000\u0209\u020a\u0005-\u0000\u0000\u020a"+
		"\u0088\u0001\u0000\u0000\u0000\u020b\u020c\u0005*\u0000\u0000\u020c\u008a"+
		"\u0001\u0000\u0000\u0000\u020d\u020e\u0005/\u0000\u0000\u020e\u008c\u0001"+
		"\u0000\u0000\u0000\u020f\u0210\u0005>\u0000\u0000\u0210\u008e\u0001\u0000"+
		"\u0000\u0000\u0211\u0212\u0005<\u0000\u0000\u0212\u0090\u0001\u0000\u0000"+
		"\u0000\u0213\u0214\u0005>\u0000\u0000\u0214\u0215\u0005=\u0000\u0000\u0215"+
		"\u0092\u0001\u0000\u0000\u0000\u0216\u0217\u0005<\u0000\u0000\u0217\u0218"+
		"\u0005=\u0000\u0000\u0218\u0094\u0001\u0000\u0000\u0000\u0219\u021a\u0005"+
		"=\u0000\u0000\u021a\u021b\u0005=\u0000\u0000\u021b\u0096\u0001\u0000\u0000"+
		"\u0000\u021c\u021d\u0005!\u0000\u0000\u021d\u021e\u0005=\u0000\u0000\u021e"+
		"\u0098\u0001\u0000\u0000\u0000\u021f\u0220\u0005a\u0000\u0000\u0220\u0221"+
		"\u0005n\u0000\u0000\u0221\u0222\u0005d\u0000\u0000\u0222\u009a\u0001\u0000"+
		"\u0000\u0000\u0223\u0224\u0005o\u0000\u0000\u0224\u0225\u0005r\u0000\u0000"+
		"\u0225\u009c\u0001\u0000\u0000\u0000\u0226\u0227\u0005n\u0000\u0000\u0227"+
		"\u0228\u0005o\u0000\u0000\u0228\u0229\u0005t\u0000\u0000\u0229\u009e\u0001"+
		"\u0000\u0000\u0000\u022a\u022f\u0003\u00abU\u0000\u022b\u022e\u0003\u00ab"+
		"U\u0000\u022c\u022e\u0003\u00adV\u0000\u022d\u022b\u0001\u0000\u0000\u0000"+
		"\u022d\u022c\u0001\u0000\u0000\u0000\u022e\u0231\u0001\u0000\u0000\u0000"+
		"\u022f\u022d\u0001\u0000\u0000\u0000\u022f\u0230\u0001\u0000\u0000\u0000"+
		"\u0230\u00a0\u0001\u0000\u0000\u0000\u0231\u022f\u0001\u0000\u0000\u0000"+
		"\u0232\u0233\u0003\u009fO\u0000\u0233\u00a2\u0001\u0000\u0000\u0000\u0234"+
		"\u0235\u0005T\u0000\u0000\u0235\u0236\u0005r\u0000\u0000\u0236\u0237\u0005"+
		"u\u0000\u0000\u0237\u023e\u0005e\u0000\u0000\u0238\u0239\u0005F\u0000"+
		"\u0000\u0239\u023a\u0005a\u0000\u0000\u023a\u023b\u0005l\u0000\u0000\u023b"+
		"\u023c\u0005s\u0000\u0000\u023c\u023e\u0005e\u0000\u0000\u023d\u0234\u0001"+
		"\u0000\u0000\u0000\u023d\u0238\u0001\u0000\u0000\u0000\u023e\u00a4\u0001"+
		"\u0000\u0000\u0000\u023f\u0241\u0003\u00adV\u0000\u0240\u023f\u0001\u0000"+
		"\u0000\u0000\u0241\u0242\u0001\u0000\u0000\u0000\u0242\u0240\u0001\u0000"+
		"\u0000\u0000\u0242\u0243\u0001\u0000\u0000\u0000\u0243\u00a6\u0001\u0000"+
		"\u0000\u0000\u0244\u0246\u0003\u00adV\u0000\u0245\u0244\u0001\u0000\u0000"+
		"\u0000\u0246\u0247\u0001\u0000\u0000\u0000\u0247\u0245\u0001\u0000\u0000"+
		"\u0000\u0247\u0248\u0001\u0000\u0000\u0000\u0248\u0249\u0001\u0000\u0000"+
		"\u0000\u0249\u024b\u0007\u0000\u0000\u0000\u024a\u024c\u0003\u00adV\u0000"+
		"\u024b\u024a\u0001\u0000\u0000\u0000\u024c\u024d\u0001\u0000\u0000\u0000"+
		"\u024d\u024b\u0001\u0000\u0000\u0000\u024d\u024e\u0001\u0000\u0000\u0000"+
		"\u024e\u0258\u0001\u0000\u0000\u0000\u024f\u0251\u0007\u0001\u0000\u0000"+
		"\u0250\u0252\u0007\u0002\u0000\u0000\u0251\u0250\u0001\u0000\u0000\u0000"+
		"\u0251\u0252\u0001\u0000\u0000\u0000\u0252\u0254\u0001\u0000\u0000\u0000"+
		"\u0253\u0255\u0003\u00adV\u0000\u0254\u0253\u0001\u0000\u0000\u0000\u0255"+
		"\u0256\u0001\u0000\u0000\u0000\u0256\u0254\u0001\u0000\u0000\u0000\u0256"+
		"\u0257\u0001\u0000\u0000\u0000\u0257\u0259\u0001\u0000\u0000\u0000\u0258"+
		"\u024f\u0001\u0000\u0000\u0000\u0258\u0259\u0001\u0000\u0000\u0000\u0259"+
		"\u00a8\u0001\u0000\u0000\u0000\u025a\u025f\u0005\"\u0000\u0000\u025b\u025e"+
		"\u0003\u00afW\u0000\u025c\u025e\t\u0000\u0000\u0000\u025d\u025b\u0001"+
		"\u0000\u0000\u0000\u025d\u025c\u0001\u0000\u0000\u0000\u025e\u0261\u0001"+
		"\u0000\u0000\u0000\u025f\u0260\u0001\u0000\u0000\u0000\u025f\u025d\u0001"+
		"\u0000\u0000\u0000\u0260\u0262\u0001\u0000\u0000\u0000\u0261\u025f\u0001"+
		"\u0000\u0000\u0000\u0262\u0263\u0005\"\u0000\u0000\u0263\u00aa\u0001\u0000"+
		"\u0000\u0000\u0264\u0265\u0007\u0003\u0000\u0000\u0265\u00ac\u0001\u0000"+
		"\u0000\u0000\u0266\u0267\u0007\u0004\u0000\u0000\u0267\u00ae\u0001\u0000"+
		"\u0000\u0000\u0268\u0269\u0005\\\u0000\u0000\u0269\u026d\u0005\"\u0000"+
		"\u0000\u026a\u026b\u0005\\\u0000\u0000\u026b\u026d\u0005\\\u0000\u0000"+
		"\u026c\u0268\u0001\u0000\u0000\u0000\u026c\u026a\u0001\u0000\u0000\u0000"+
		"\u026d\u00b0\u0001\u0000\u0000\u0000\u026e\u0272\u0005#\u0000\u0000\u026f"+
		"\u0271\t\u0000\u0000\u0000\u0270\u026f\u0001\u0000\u0000\u0000\u0271\u0274"+
		"\u0001\u0000\u0000\u0000\u0272\u0273\u0001\u0000\u0000\u0000\u0272\u0270"+
		"\u0001\u0000\u0000\u0000\u0273\u0275\u0001\u0000\u0000\u0000\u0274\u0272"+
		"\u0001\u0000\u0000\u0000\u0275\u0276\u0005\n\u0000\u0000\u0276\u0277\u0001"+
		"\u0000\u0000\u0000\u0277\u0278\u0006X\u0000\u0000\u0278\u00b2\u0001\u0000"+
		"\u0000\u0000\u0279\u027a\u0005#\u0000\u0000\u027a\u027b\u0005(\u0000\u0000"+
		"\u027b\u0280\u0001\u0000\u0000\u0000\u027c\u027f\u0003\u00b3Y\u0000\u027d"+
		"\u027f\t\u0000\u0000\u0000\u027e\u027c\u0001\u0000\u0000\u0000\u027e\u027d"+
		"\u0001\u0000\u0000\u0000\u027f\u0282\u0001\u0000\u0000\u0000\u0280\u0281"+
		"\u0001\u0000\u0000\u0000\u0280\u027e\u0001\u0000\u0000\u0000\u0281\u0283"+
		"\u0001\u0000\u0000\u0000\u0282\u0280\u0001\u0000\u0000\u0000\u0283\u0284"+
		"\u0005#\u0000\u0000\u0284\u0285\u0005)\u0000\u0000\u0285\u0286\u0001\u0000"+
		"\u0000\u0000\u0286\u0287\u0006Y\u0000\u0000\u0287\u00b4\u0001\u0000\u0000"+
		"\u0000\u0288\u028a\u0007\u0005\u0000\u0000\u0289\u0288\u0001\u0000\u0000"+
		"\u0000\u028a\u028b\u0001\u0000\u0000\u0000\u028b\u0289\u0001\u0000\u0000"+
		"\u0000\u028b\u028c\u0001\u0000\u0000\u0000\u028c\u028d\u0001\u0000\u0000"+
		"\u0000\u028d\u028e\u0006Z\u0000\u0000\u028e\u00b6\u0001\u0000\u0000\u0000"+
		"\u028f\u0290\t\u0000\u0000\u0000\u0290\u00b8\u0001\u0000\u0000\u0000\u0011"+
		"\u0000\u022d\u022f\u023d\u0242\u0247\u024d\u0251\u0256\u0258\u025d\u025f"+
		"\u026c\u0272\u027e\u0280\u028b\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}