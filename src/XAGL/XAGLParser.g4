parser grammar XAGLParser;

options {
    tokenVocab = XAGLLexer; // join lexer
}

program
    : stat* EOF
    ;

stat
    : instantiation                             
    | longAssignment[None] ';'                        
    | withStatement                             
    | forStatement                              
    | whileStatement                            
    | repeatStatement                            
    | ifStatement                               
    | command                                   
    | '{' stat+ '}'                             
    ;

instantiation
    : ID ':' simpleStatement
    ;

simpleStatement
    : typeID assignment? ';'
    ;

propertiesAssignment[varName]
    : '{' longAssignment[$varName] ( ';' longAssignment[$varName])* ';'? '}'
    ;

longAssignment[varName]
    : identifier assignment
    ;

assignment
    : '=' expression
    ;

expression
    : sign=('+'|'-'|'not') e=expression                     #ExprUnary
    | '(' e=expression ')'                                  #ExprParenthesis
    | e1=expression op=('*'|'/') e2=expression              #ExprAddSubMultDiv
    | e1=expression op=('+'|'-') e2=expression              #ExprAddSubMultDiv
    | e1=expression op=('>'|'<'|'>='|'<=') e2=expression    #ExprRelational
    | e1=expression op=('=='|'!=') e2=expression            #ExprRelational
    | e1=expression 'and' e2=expression                     #ExprAnd
    | e1=expression 'or' e2=expression                      #ExprOr
    | '(' x=expression ',' y=expression ')'                 #ExprPoint
    | '(' deg=expression ':' length=expression ')'          #ExprVector
    | '[' expression (',' expression)* ']'                  #ExprArray
    | number=(INT | FLOAT)                                  #ExprNumber
    | BOOLEAN                                               #ExprBoolean                   
    | STRING                                                #ExprString                              
    | identifier                                            #ExprID
    | 'wait' 'mouse' 'click'                                #ExprWait
    | 'input' STRING                                        #ExprInput
    ;

command
    : 'refresh' identifier ('after' expression suffix=('ms'|'s'))? ';'      #CommandRefresh
    | 'print' expression ';'                                                #CommandPrint
    | 'close' identifier ';'                                                #CommandClose
    | 'move' identifier (',' identifier)* type=('by'|'to') expression ';'   #CommandMove
    | 'rotate' identifier (',' identifier)* 'by' expression ';'             #CommandRotate
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
    : 'with' Id=identifier 'do' propertiesAssignment[$Id.text]
    ;

ifStatement
    : 'if' expression 'do' stat elseStatement?
    ;

elseStatement
    : 'else' ifStatement    #ElseIfStat
    | 'else' 'do' stat      #ElseStat
    ;

typeID
    : 'Integer'
    | 'String'
    | 'Point'
    | 'Number'
    | 'Vector'
    | 'Time'
    | 'Boolean'
    | 'Array' '<' typeID '>'
    ;

identifier
    : ID
    | ID '.' identifier
    | ID ('[' expression ']')+ ('.' identifier)?
    ;