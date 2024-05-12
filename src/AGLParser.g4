parser grammar AGLParser;

options {
    tokenVocab = AGLLexer; // join lexer
}

program
    : stat* EOF
    ;

stat
    : instantiation
    | blockStatement
    | command
    ;

instantiation
    : ID ':' (simpleStatement | blockStatement)
    ;

simpleStatement
    : typeID (assignment)? ';'
    ;

blockStatement
    : typeID ('at' expression)? 'with' '{' propertiesAssignment '}'
    ;

propertiesAssignment
    : propertiy ( ';' propertiy)* ';'?
    ;

propertiy
    : ID assignment
    ;

assignment
    : '=' expression
    ;

expression
    : sign? '(' expression ')'                  #ExprParenthesis
    | expression op=('*' | '/') expression      #ExprAddSubMultDiv
    | expression op=('+' | '-') expression      #ExprAddSubMultDiv
    | sign? point                               #ExprPoint
    | sign? number                              #ExprNumber                  
    | STRING                                    #ExprString                              
    | sign? ID                                  #ExprID
    | waitFor                                   #ExprWaitFor
    ;

command
    : 'refresh' ID ';'
    | 'print' expression ';'
    | 'close' ID ';'
    ;

waitFor
    : 'wait' eventTrigger
    ;    

eventTrigger
    : 'mouse' mouseTrigger
    ;

mouseTrigger
    : 'click'
    ;    

number
    : INT 
    | FLOAT
    ;

point
    : '(' x=expression ',' y=expression ')'
    ;

typeID
    : ID 
    | primitiveType
    ;

primitiveType
    : 'Integer'
    | 'Number'
    | 'String'
    | 'Point'
    | 'Vector'
    ;

operator
    : '+' 
    | '-' 
    | '*' 
    | '/'
    ;

sign
    : '+' 
    | '-'
    ;




// RAW

//expression: TYPE ( (('=' value)? ';') | ( ('at' position)? 'with' '{' assignment '}' ) );  // line 9 and line 19 ex01.

// p,a,d : Point

// refresh a; refresh a;

//instantiation: ID ':' expression;    // line 42 ex01.agl
//assignment: ID '=' value ';';