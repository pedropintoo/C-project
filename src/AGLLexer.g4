lexer grammar AGLLexer;

// Separators

LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACK  : '[';
RBRACK  : ']';
COLON   : ':';
EQUAL   : '=';
SEMI    : ';';
COMMA   : ',';
TWODOTS : '..';
DOT     : '.';


// Types
INTEGER : 'Integer';    
NUMBER  : 'Number';
STRING_  : 'String';
POINT   : 'Point';
VECTOR  : 'Vector';
VIEW    : 'View';
LINE    : 'Line';
RECTANGLE: 'Rectangle';
ELLIPSE : 'Ellipse';
ARC     : 'Arc';
ARCHORD : 'ArcChord';
PIESLICE : 'PieSlice';
TEXT    : 'Text';
DOTTYPE : 'Dot';
POLYLINE: 'PolyLine';
SPLINE  : 'Spline';
POLYGON : 'Polygon';
BLOB    : 'Blob';


// Keywords
WITH    : 'with';
AT      : 'at';
PRINT   : 'print';
REFRESH : 'refresh';
CLOSE   : 'close';
MOUSE   : 'mouse';
CLICK   : 'click';
WAIT    : 'wait';
FOR     : 'for';
IN      : 'in';
DO      : 'do';
AFTER   : 'after';
MS      : 'ms';
S       : 's';
MOVE    : 'move';
BY      : 'by';

// Operators
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';


// Identifier names
ID      : LETTER (LETTER | DIGIT)*;

// Numbers        
INT     : DIGIT+;
FLOAT: DIGIT+ [.] DIGIT+ ([eE][+-]?DIGIT+)?;

// Characters
STRING  : '"' (ESC | .)*? '"';

fragment LETTER: [a-zA-Z_\u00C0-\u00FF];
fragment DIGIT: [0-9];
fragment ESC: '\\"' | '\\\\';

LINE_COMMENT: '#' .*? '\n' -> skip;
COMMENT: '#(' (COMMENT | .)*? '#)' -> skip; // alow nested comments
WS: [ \t\n\r]+ -> skip;

// ensure no lexical errors
ERROR: .;