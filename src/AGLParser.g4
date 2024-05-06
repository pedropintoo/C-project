parser grammar AGLParser;

options {
    tokenVocab = AGLLexer; // join lexer
}

program: point* EOF;

number: INT | FLOAT;

point: '(' x=number ',' y=number ')';

//instantiation: ID ':' expression;
