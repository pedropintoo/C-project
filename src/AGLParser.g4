parser grammar AGLParser;

options {
    tokenVocab = AGLLexer; // join lexer
}

program
    : stat* EOF;

stat
    : instantiation
    | expression
    ;

instantiation
    : ID ':' (simpleStatement | expression)
    ;

simpleStatement
    : type (assignment)? ';'
    ;

expression
    : type ('at' position)? 'with' '{' propertiesAssignment '}'
    ;

propertiesAssignment
    : ID assignment ( ';' ID assignment)* ';'?
    ;

assignment
    : '=' value
    ;

type
    : 'Integer' 
    | 'Number' 
    | 'String'
    | 'Point'
    | 'Vector'
    ;


value: number | point | STRING | ID;

number: INT | FLOAT;

point: '(' x=number ',' y=number ')';

position: point | ID;




//expression: TYPE ( (('=' value)? ';') | ( ('at' position)? 'with' '{' assignment '}' ) );  // line 9 and line 19 ex01.

// p,a,d : Point

// refresh a; refresh a;

//instantiation: ID ':' expression;    // line 42 ex01.agl
//assignment: ID '=' value ';';