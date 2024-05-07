parser grammar AGLParser;

options {
    tokenVocab = AGLLexer; // join lexer
}

program: stat* EOF;

stat: instantiation
    | '{' stat '}';

number: INT | FLOAT;

point: '(' x=number ',' y=number ')';

position: point | ID;

instantiation: ID ':' expression;    // line 42 ex01.agl
assignment: ID '=' value ';';

value: number | point | STRING;

expression: TYPE ( (('=' value)? ';') | ( ('at' position)? 'with' '{' assignment '}' ) );  // line 9 and line 19 ex01.

p,a,d : Point

refresh a; refresh a;