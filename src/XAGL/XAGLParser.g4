parser grammar XAGLParser;

options {
    tokenVocab = XAGLLexer; // join lexer
}

program
    : stat* EOF
    ;

stat
    : instantiation                             #StatInstantiation
    | longAssignment ';'                        #StatLongAssignment
    | withStatement                             #StatWithStatement
    | forStatement                              #RepForStatement
    | whileStatement                            #RepWhileStatement
    | repeatStatement                           #RepRepeatStatement 
    | ifStatement                               #StatIfStatement
    | command                                   #StatCommand
    | '{' stat+ '}'                             #StatBlock
    ;

instantiation
    : ID ':' simpleStatement
    ;

simpleStatement
    : typeID assignment? ';'
    | typeID in_assignment
    ;

propertiesAssignment
    : '{' longAssignment ( ';' longAssignment)* ';'? '}'
    ;

longAssignment
    : identifier assignment
    ;

assignment
    : '=' expression
    ;

in_assignment
    : 'in' '{' ID (',' ID)* '}'
    ;

expression
    : sign=('+'|'-'|'not') e=expression                     #ExprUnary
    | '(' e=expression ')'                                  #ExprParenthesis
    | e1=expression op=('*'|'/') e2=expression              #ExprAddSubMultDiv
    | e1=expression op=('+'|'-') e2=expression              #ExprAddSubMultDiv
    | e1=expression op=('>'|'<'|'>='|'<=') e2=expression    #ExprRelational
    | e1=expression op=('=='|'!=') e2=expression            #ExprRelational
    | e1=expression 'and' e2=expression                     #ExprAndOr
    | e1=expression 'or' e2=expression                      #ExprAndOr
    | '(' x=expression ',' y=expression ')'                 #ExprPoint
    | '(' deg=expression ':' length=expression ')'          #ExprVector
    | '[' expression (',' expression)* ']'                  #ExprArray
    | number=(INT | FLOAT)                                  #ExprNumber
    | BOOLEAN                                               #ExprBoolean                   
    | STRING                                                #ExprString                              
    | identifier                                            #ExprID
    | 'wait' eventTrigger                                   #ExprWait
    | 'deepcopy' identifier 'to' expression                 #ExprDeepCopy
    ;

command
    : 'refresh' identifier ('after' expression suffix=('ms'|'s'))? ';'      #CommandRefresh
    | 'print' expression ';'                                                #CommandPrint
    | 'close' identifier ';'                                                #CommandClose
    | 'move' identifier (',' identifier)* type=('by'|'to') expression ';'   #CommandMove
    | 'rotate' identifier (',' identifier)* 'by' expression ';'             #CommandRotate
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
    : 'repeat' stat 'until' expression ';'
    ;    

withStatement
    : 'with' identifier 'do' propertiesAssignment 
    ;

ifStatement
    : 'if' expression 'do' stat ('else' 'do' stat)?
    ;

typeID
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
    | 'Array'
    | ID
    ;

identifier
    : ID
    | ID '.' identifier
    | identifier '[' expression ']'
    ;