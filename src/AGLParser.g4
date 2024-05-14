parser grammar AGLParser;

@parser::header {
import java.util.Map;
import java.util.HashMap;
}

@parser::members {
static protected Map<String,Number> symbolTable = new HashMap<>();
}

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
    : ID ':' (simpleStatement | blockStatement)
    ;

simpleStatement returns [String varName]
    : typeID (assignment)? ';'
    ;

blockStatement returns [String varName]
    : typeID ('at' expression)? 'with' '{' propertiesAssignment '}'
    | (typeID '.' propertie ';')+ // to change a single property, the dot (.) may be used instead of the 'with' construction
    | (command)+
    ;

propertiesAssignment
    : property ( ';' property)* ';'?
    ;

property
    : ID assignment
    ;

assignment returns [String varName]
    : '=' expression
    ;

expression returns [String varName]
    : sign=('+'|'-') expression                 #ExprUnary
    | '(' expression ')'                        #ExprParenthesis
    | expression op=('*' | '/') expression      #ExprAddSubMultDiv
    | expression op=('+' | '-') expression      #ExprAddSubMultDiv
    | '(' x=expression ',' y=expression ')'     #ExprPoint
    | number=(INT | FLOAT)                      #ExprNumber                  
    | STRING                                    #ExprString                              
    | ID                                        #ExprID
    | 'wait' eventTrigger                       #ExprWait
    ;

command
    : 'refresh' ID ('after' number 'ms')? ';'   #CommandRefresh
    | 'print' expression ';'                    #CommandPrint
    | 'close' ID ';'                            #CommandClose
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

typeID
    : type=(PRIMITIVE_TYPE | ID)
    ;





// RAW

//expression: TYPE ( (('=' value)? ';') | ( ('at' position)? 'with' '{' assignment '}' ) );  // line 9 and line 19 ex01.

// p,a,d : Point

// refresh a; refresh a;

//instantiation: ID ':' expression;    // line 42 ex01.agl
//assignment: ID '=' value ';';

