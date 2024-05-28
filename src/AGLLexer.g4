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
DOUBLECOLON : '::';


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
Model   : 'Model';
Enum    : 'Enum';
SCRIPT  : 'Script';


// Keywords
WITH    : 'with';
AT      : 'at';
PRINT   : 'print';
REFRESH : 'refresh';
CLOSE   : 'close';
MOUSE   : 'mouse';
CLICK   : 'click';
WAIT    : 'wait';
INPUT   : 'input';
LOAD    : 'load';
PLAY    : 'play';
FOR     : 'for';
IF      : 'if';
ELSE    : 'else';
IN      : 'in';
DO      : 'do';
AFTER   : 'after';
MS      : 'ms';
S       : 's';
MOVE    : 'move';
BY      : 'by';
TO      : 'to';
ACTION  : 'action';
ON      : 'on';

// Operators
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
RELATIONAL_OPERATOR
    : '<' 
    | '<='
    | '>'
    | '>='
    | '=='
    | '!='
    ;
AND     : '&&';
OR      : '||';
NOT     : '!';

// Identifier names
ID      : LETTER (LETTER | DIGIT)*;
NAME    : ID;

// Boolean
BOOLEAN : 'True' | 'False';

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