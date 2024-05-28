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
    : sign=('+'|'-') e=expression                 #ExprUnary
    | '(' e=expression ')'                        #ExprParenthesis
    | e1=expression op=('*' | '/') e2=expression      #ExprAddSubMultDiv
    | e1=expression op=('+' | '-') e2=expression      #ExprAddSubMultDiv
    | '(' x=expression ',' y=expression ')'     #ExprPoint
    | number=(INT | FLOAT)                      #ExprNumber                  
    | STRING                                    #ExprString                              
    | ID                                        #ExprID
    | 'wait' eventTrigger                       #ExprWait
    | '[' expression (',' expression)* ']'      #ExprArray
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
    : 'for' ID 'in' number_range 'do' '{' stat+ '}' 
    ;

withStatement
    : 'with' ID 'do' '{' propertiesAssignment '}' 
    ;

typeID returns[Type res]:
    'Integer'
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
