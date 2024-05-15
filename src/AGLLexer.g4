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
PRIMITIVE_TYPE: INTEGER | NUMBER | STRING_ | POINT | VECTOR;
INTEGER : 'Integer';    
NUMBER  : 'Number';
STRING_  : 'String';
POINT   : 'Point';
VECTOR  : 'Vector';


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

// Operators
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';


// Identifier names
ID      : LETTER (LETTER | DIGIT)*;

// Numbers        
INT     : DIGIT+;
FLOAT: DIGIT* [.] DIGIT+ ([eE][+-]?DIGIT+)? | DIGIT+ [.] DIGIT* ([eE][+-]?DIGIT+)?;

// For loop
NUMBER_RANGE : DIGIT+ '..' DIGIT+;

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