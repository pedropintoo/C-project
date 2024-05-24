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

assignment returns [String varName]
    : '=' expression
    ;

expression returns [Type eType, String varName]
    : sign=('+'|'-') expression                 #ExprUnary
    | '(' e=expression ')'                        #ExprParenthesis
    | expression op=('*' | '/') expression      #ExprAddSubMultDiv
    | expression op=('+' | '-') expression      #ExprAddSubMultDiv
    | '(' x=expression ',' y=expression ')'     #ExprPoint
    | number=(INT | FLOAT)                      #ExprNumber                  
    | STRING                                    #ExprString                              
    | ID                                        #ExprID
    | 'wait' eventTrigger                       #ExprWait
    ;

command
    : 'refresh' ID ('after' expression suffix=('ms'|'s'))? ';'   #CommandRefresh
    | 'print' expression ';'                    #CommandPrint
    | 'close' ID ';'                            #CommandClose
    | 'move' ID 'by' expression ';'             #CommandMove
    ;

eventTrigger
    : 'mouse' mouseTrigger
    ;

mouseTrigger
    : 'click'
    ;    

for_loop
    : 'for' ID 'in' NUMBER_RANGE 'do' '{' stat* '}' 
    ;

withStatement
    : 'with' ID 'do' '{' propertiesAssignment '}' 
    ;

typeID returns[Type res]:
    'Integer'       {$res = new IntegerType();}
    | 'String'      {$res = new StringType();}
    | 'Point'       {$res = new PointType();}
    | 'Number'      {$res = new NumberType();}
    | 'Vector'      {$res = new VectorType();}
    | 'View'        {$res = new ObjectType("View");}
    | 'Line'        {$res = new ObjectType("Line");} 
    | 'Rectangle'   {$res = new ObjectType("Rectangle");}
    | 'Ellipse'     {$res = new ObjectType("Ellipse");}
    | 'Arc'         {$res = new ObjectType("Arc");}
    | 'ArcChord'    {$res = new ObjectType("ArcChord");}
    | 'PieSlice'    {$res = new ObjectType("PieSlice");}
    | 'Text'        {$res = new ObjectType("Text");}
    | 'Dot'         {$res = new ObjectType("Dot");}

    ;
// : type=(PRIMITIVE_TYPE | ID)
// ;

// private static final List<Type> types = List.of(new StringType(), new PointType(), new NumberType(),
    //         new VectorType(), new IntegerType());


// blockStatement returns [String varName]
//     : typeID ('at' expression)? 'with' '{' propertiesAssignment '}'
//     | (typeID '.' longAssignment ';')+ // to change a single property, the dot (.) may be used instead of the 'with' construction
//     | (command)+
//     ;




// RAW

//expression: TYPE ( (('=' value)? ';') | ( ('at' position)? 'with' '{' assignment '}' ) );  // line 9 and line 19 ex01.

// p,a,d : Point

// refresh a; refresh a;

//instantiation: ID ':' expression;    // line 42 ex01.agl
//assignment: ID '=' value ';';