parser grammar AGLParser;

@parser::header {
import java.util.Map;
import java.util.HashMap;
}

@parser::members {
static protected Map<String, Number> symbolTable = new HashMap<>();
}

options {
    tokenVocab = AGLLexer; // join lexer
}


program
    : stat* EOF
    ;

stat
    : instantiation                             #StatInstantiation
    | modelInstantiation                        #StatModelInstantiation
    | blockStatement                            #StatBlockStatement
    | longAssignment ';'                        #StatLongAssignment
    | withStatement                             #StatWithStatement
    | playStatement                             #StatPlayStatement
    | repetitiveStatement                       #StatRepetitiveStatement
    | ifStatement                               #StatIfStatement
    | command                                   #StatCommand
    | '{' stat+ '}'                             #StatBlock
    ;

repetitiveStatement
    : forStatement                              #RepForStatement
    | whileStatement                            #RepWhileStatement
    | repeatStatement                           #RepRepeatStatement  
    ;

instantiation
    : ID ':' (simpleStatement | blockStatement)
    ;

simpleStatement returns [String varName]
    : typeID ('at' expression)? ((assignment)? ';' | in_assignment)
    ;

blockStatement returns [String varName]
    : typeID ('at' expression)? 'with' propertiesAssignment 
    ;

propertiesAssignment
    : '{' longAssignment ( ';' longAssignment)* ';'? '}'
    ;

longAssignment
    : identifier assignment
    ;

assignment returns [Type eType, String varName]
    : '=' expression
    ;

in_assignment
    : 'in' '{' ID (',' ID)* '}'
    ;    

expression returns [String varName]
    : sign=('+'|'-'|'!') e=expression               #ExprUnary
    | '(' e=expression ')'                          #ExprParenthesis
    | e1=expression op=('*'|'/'|'&&') e2=expression #ExprAddSubMultDivAndOr
    | e1=expression op=('+'|'-'|'||') e2=expression #ExprAddSubMultDivAndOr
    | '(' x=expression ',' y=expression ')'         #ExprPoint
    | '[' expression (',' expression)* ']'          #ExprArray
    | expression RELATIONAL_OPERATOR expression     #ExprRelational
    | number=(INT | FLOAT)                          #ExprNumber
    | BOOLEAN                                       #ExprBoolean                   
    | STRING                                        #ExprString                              
    | identifier                                    #ExprID
    | 'wait' eventTrigger                           #ExprWait
    | op=('input'|'load') STRING                    #ExprScript
    ;

command
    : 'refresh' ID ('after' expression suffix=('ms'|'s'))? ';'   #CommandRefresh
    | 'print' expression ';'                    #CommandPrint
    | 'close' ID ';'                            #CommandClose
    | 'move' identifier type=('by'|'to') expression ';'             #CommandMove
    ;

eventTrigger
    : 'mouse' mouseTrigger
    ;

mouseTrigger
    : 'click'
    ;    

forStatement
    : 'for' ID 'in' number_range 'do' stat 
    ;

number_range
    : expression '..' expression ('..' expression)?
    ;    

whileStatement
    : 'while' expression 'do' stat
    ;    

repeatStatement
    : 'repeat' stat 'until' expression
    ;    

withStatement
    : 'with' identifier 'do' propertiesAssignment 
    ;

playStatement
    : 'play' ID 'with' propertiesAssignment
    ;   

modelInstantiation
    : ID '::' 'Model' '{' (instantiation|blockStatement|action|longAssignment ';')+ '}'
    ;

action
    : 'action' 'on' identifier stat
    ;

ifStatement
    : 'if' expression 'do' stat ('else' 'do' stat)?
    ;

 

typeID returns[Type res]
    : 'Integer'
    | 'String'
    | 'Point'
    | 'Number'
    | 'Vector'
    | 'Time'
    | 'Boolean'
    | 'View'
    | 'Line'
    | 'Rectangle'
    | 'Ellipse'
    | 'Arc'
    | 'ArcChord'
    | 'PieSlice'
    | 'Text'
    | 'Dot'
    | 'PolyLine'
    | 'Spline'
    | 'Polygon'
    | 'Blob'
    | 'Script'
    | 'Enum'
    | ID
    ;

identifier
    : ID
    | ID ('.' ID)+
    ;


