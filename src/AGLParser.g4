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
    | blockStatement                            #StatBlockStatement
    | longAssignment ';'                        #StatLongAssignment
    | command                                   #StatCommand
    | for_loop                                  #StatForLoop
    | withStatement                             #StatWithStatement
    | modelInstantiation                        #StatModelInstantiation
    | ifStatement                               #StatIfStatement
    | '{' stat+ '}'
    ;

instantiation
    : ID ':' (simpleStatement | blockStatement)
    ;

simpleStatement returns [String varName]
    : typeID (assignment)? ';'
    ;

blockStatement returns [String varName]
    : typeID ('at' expression)? 'with' '{' propertiesAssignment '}'
    ;

propertiesAssignment
    : longAssignment ( ';' longAssignment)* ';'?
    ;

longAssignment
    : ID ('.' ID)? assignment
    ;

assignment returns [Type eType, String varName]
    : '=' expression
    ;

expression returns [String varName]
    : sign=('+'|'-'|NOT) e=expression               #ExprUnary
    | '(' e=expression ')'                          #ExprParenthesis
    | e1=expression op=('*'|'/'|AND) e2=expression  #ExprAddSubMultDivAndOr
    | e1=expression op=('+'|'-'|OR) e2=expression   #ExprAddSubMultDivAndOr
    | '(' x=expression ',' y=expression ')'         #ExprPoint
    | 'wait' eventTrigger                           #ExprWait
    | '[' expression (',' expression)* ']'          #ExprArray
    | expression RELATIONAL_OPERATOR expression     #ExprRelational
    | number=(INT | FLOAT)                          #ExprNumber
    | BOOLEAN                                       #ExprBoolean                   
    | STRING                                        #ExprString                              
    | ID                                            #ExprID
    ;

command
    : 'refresh' ID ('after' expression suffix=('ms'|'s'))? ';'   #CommandRefresh
    | 'print' expression ';'                    #CommandPrint
    | 'close' ID ';'                            #CommandClose
    | 'move' ID type=('by'|'to') expression ';'             #CommandMove
    ;

eventTrigger
    : 'mouse' mouseTrigger
    ;

mouseTrigger
    : 'click'
    ;    

for_loop
    : 'for' ID 'in' number_range 'do' stat 
    ;

withStatement
    : 'with' ID 'do' '{' propertiesAssignment '}' 
    ;


modelInstantiation
    : ID '::' typeID '{' (instantiation|action|longAssignment)+ '}'
    ;

action
    : 'action' 'on' ID '{' stat+ '}'
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
    ;

number_range
    : expression '..' expression ('..' expression)?
    ;
