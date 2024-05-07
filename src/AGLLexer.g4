lexer grammar AGLLexer;

/*
    In AGL (animated graphics language) we need primitive data types (with default values).
    - Integer [0] - integer number
    - Number [0.0] - integer or real number
    - String [""] - sequence of characters
    - Point [(0.0,0.0)] - a point in canvas coordinates
    - Vector [(0.0,0.0)] - the difference between two points
    - Vector [(0:1)] - a vector may also be defined using polar coordinates (angle:length).
 */


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

WS: [ \t\n\r]+ -> skip;
LINE_COMMENT: '#' .*? '\n' -> skip;
COMMENT: '#(' .*? ')#' -> skip;


// Separators

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI   : ';';
COMMA  : ',';
DOT    : '.';
WITH   : 'with';
AT     : 'at';

TYPE: 'int' | 'float' | 'point';

// ensure no lexical errors
ERROR: .;