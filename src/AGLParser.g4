parser grammar AGLParser;

@parser::header {
import java.util.Map;
import java.util.HashMap;
}

@parser::members {
static protected Map<String, Symbol> symbolTable = new HashMap<>();
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
    : typeID ('at' expression | assignment)? ';'
    | typeID in_assignment
    ;

blockStatement returns [String varName]
    : typeID ('at' expression)? 'with' propertiesAssignment 
    ;

propertiesAssignment returns [String idToAssign]
    : '{' longAssignment ( ';' longAssignment)* ';'? '}'
    ;

longAssignment
    : identifier assignment
    ;

assignment returns [Type eType, String varName]
    : '=' expression
    ;

in_assignment returns [Type eType, String varName]
    : 'in' '{' ID (',' ID)* '}'
    ;    

expression returns [Type eType, String varName]
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
    | op=('input'|'load') STRING                            #ExprScript
    ;

command
    : 'refresh' ID (',' ID)* ('after' expression suffix=('ms'|'s'))? ';'   #CommandRefresh
    | 'print' expression ';'                                               #CommandPrint
    | 'close' ID (',' ID)* ';'                                             #CommandClose
    | 'move' identifier (',' identifier)* type=('by'|'to') expression ';'  #CommandMove
    | 'rotate' identifier (',' identifier)* 'by' expression ';'            #CommandRotate
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

playStatement
    : 'play' ID 'with' propertiesAssignment
    ;  

modelStat returns [Boolean isAction]
    : instantiation                             #ModelStatInstantiation
    | blockStatement                            #ModelStatBlockStatement
    | longAssignment ';'                        #ModelStatLongAssignment
    | action                                    #ModelStatAction
    ;   


modelInstantiation
    : ID '::' 'Model' '{' (modelStat)+ '}'
    ;

action
    : 'action' 'on' identifier stat
    ;

ifStatement
    : 'if' expression 'do' stat ('else' 'do' stat)?
    ;

 

typeID returns[Type res]
    : 'Integer'                 {$res = new IntegerType();}
    | 'String'                  {$res = new StringType();}
    | 'Point'                   {$res = new PointType();}
    | 'Number'                  {$res = new NumberType();}
    | 'Vector'                  {$res = new VectorType();}
    | 'Time'                    {$res = new TimeType();}
    | 'Boolean'                 {$res = new BooleanType();}
    | 'View'                    {$res = new ObjectType("View");}
    | 'Line'                    {$res = new ObjectType("Line");} 
    | 'Rectangle'               {$res = new ObjectType("Rectangle");}
    | 'Ellipse'                 {$res = new ObjectType("Ellipse");}
    | 'Arc'                     {$res = new ObjectType("Arc");}
    | 'ArcChord'                {$res = new ObjectType("ArcChord");}
    | 'PieSlice'                {$res = new ObjectType("PieSlice");}
    | 'Text'                    {$res = new ObjectType("Text");}
    | 'Dot'                     {$res = new ObjectType("Dot");}
    | 'Polyline'                {$res = new ObjectType("PolyLine");}
    | 'Spline'                  {$res = new ObjectType("Spline");}   
    | 'Polygon'                 {$res = new ObjectType("Polygon");}
    | 'Blob'                    {$res = new ObjectType("Blob");}
    | 'Script'                  {$res = new ObjectType("Script");}
    | 'Enum'                    {$res = new EnumType();}   
    | 'Array' '<' typeID '>'    {$res = new ArrayType("Array<" + $typeID.text + ">");}
    | ID                        {$res = new ModelType($ID.text);}
    ;

identifier
    : ID
    | ID '.' identifier
    | ID ('[' expression ']')+ ('.' identifier)?
    ;
