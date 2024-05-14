parser grammar AGLParser;

options {
    tokenVocab = AGLLexer; // join lexer
}


program
    : stat* EOF
    ;

stat
    : instantiation                             #StatInstantiation
    | blockStatement                            #StatBlockStatement
    | command                                   #StatCommand
    | for_loop                                  #StatForLoop
    ;

instantiation
    : ID ':' statement=(simpleStatement | blockStatement)
    ;

simpleStatement
    : typeID (assignment)? ';'
    ;

blockStatement
    : typeID ('at' expression)? 'with' '{' propertiesAssignment '}'
    | (typeID '.' propertie ';')+ // to change a single property, the dot (.) may be used instead of the 'with' construction
    | (command)+
    ;

propertiesAssignment
    : propertie ( ';' propertie)* ';'?
    ;

propertie
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
    : 'refresh' ID ('after' number 'ms')? ';'   #CommandRefresh
    | 'print' expression ';'                    #CommandPrint
    | 'close' ID ';'                            #CommandClose
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

for_loop
    : 'for' ID 'in' NUMBER_RANGE // 'do' '{' blockStatement '}' 
    ;

number
    : INT 
    | FLOAT
    ;

point
    : '(' x=expression ',' y=expression ')'
    ;

typeID
    : PRIMITIVE_TYPE 
    | ID
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

