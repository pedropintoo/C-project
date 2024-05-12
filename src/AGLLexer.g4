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
DOT     : '.';
WITH    : 'with';
AT      : 'at';

// Types
INTEGER : 'Integer';    
NUMBER  : 'Number';
STRING_  : 'String';
POINT   : 'Point';
VECTOR  : 'Vector';



// Identifier names
ID      : LETTER (LETTER | DIGIT)*;

// Numbers        
INT     : DIGIT+;
FLOAT: DIGIT* [.] DIGIT+ ([eE][+-]?DIGIT+)? | DIGIT+ [.] DIGIT* ([eE][+-]?DIGIT+)?;

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