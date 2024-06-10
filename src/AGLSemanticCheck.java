import java.util.List;
import java.lang.reflect.Array;
import java.sql.Time;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import org.antlr.v4.runtime.tree.TerminalNode;

import org.antlr.v4.runtime.ParserRuleContext;

@SuppressWarnings("CheckReturnValue")
public class AGLSemanticCheck extends AGLParserBaseVisitor<Boolean> {

   private final IntegerType integerType = new IntegerType();
   private final StringType stringType = new StringType();
   private final NumberType numberType = new NumberType();
   private final PointType pointType = new PointType();
   private final VectorType vectorType = new VectorType();
   private final BooleanType booleanType = new BooleanType();
   private final TimeType timeType = new TimeType();
   private final ObjectType scriptType = new ObjectType("Script");
   private final ObjectType viewType = new ObjectType("View");
   private final ObjectType modelObjectType = new ObjectType("Model");
   private ObjectType prevObjectType = null;

   private ModelType currentModel = null;

   private boolean inAction = false;

   @Override
   public Boolean visitProgram(AGLParser.ProgramContext ctx) {
      // program: stat* EOF;
      Boolean res = true;
      
      for (AGLParser.StatContext stat : ctx.stat()) {
         res = visit(stat);
         if (!res || res == null) {
            return false;
         }
      }
      return true;
   }

   // ------ Start visit stat ------

   @Override
   public Boolean visitStatInstantiation(AGLParser.StatInstantiationContext ctx) {
      // stat: instantiation;

      if (inAction) {
         ErrorHandling.printError("Error: instantiation is not allowed inside an action");
        return false;
      }
      Boolean res = true;
      res = visit(ctx.instantiation());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid instantiation");
      }
      return res;
   }

   @Override
   public Boolean visitStatModelInstantiation(AGLParser.StatModelInstantiationContext ctx) {
      // stat: modelInstantiation;
      if (inAction) {
         ErrorHandling.printError("Error: model instantiation is not allowed inside an action");
        return false;
      }
      Boolean res = true;
      res = visit(ctx.modelInstantiation());

      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid modelInstantiation");
      }
      return res;
   }

   @Override
   public Boolean visitStatBlockStatement(AGLParser.StatBlockStatementContext ctx) {
      // stat: blockStatement;
      Boolean res = true;
      res = visit(ctx.blockStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid block statement");
      }
      return res;
   }

   @Override
   public Boolean visitStatLongAssignment(AGLParser.StatLongAssignmentContext ctx) {
      // stat: longAssignment;
      Boolean res = true;
      res = visit(ctx.longAssignment());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid long assignment");
      }
      return res;
   }

   @Override
   public Boolean visitStatWithStatement(AGLParser.StatWithStatementContext ctx) {
      // stat: withStatement;
      Boolean res = true;
      res = visit(ctx.withStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid with statement");
      }
      return res;
   }

   @Override
   public Boolean visitStatPlayStatement(AGLParser.StatPlayStatementContext ctx) {
      // stat: playStatement;
      Boolean res = true;
      res = visit(ctx.playStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid with playStatement");
      }
      return res;
   }

   @Override
   public Boolean visitStatRepetitiveStatement(AGLParser.StatRepetitiveStatementContext ctx) {
      // stat: repetitiveStatement;
      Boolean res = true;
      res = visit(ctx.repetitiveStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid with repetitiveStatement");
      }
      return res;
   }

   @Override
   public Boolean visitStatIfStatement(AGLParser.StatIfStatementContext ctx) {
      // stat: ifStatement;
      Boolean res = true;
      res = visit(ctx.ifStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid with ifStatement");
      }
      return res;
   }

   @Override
   public Boolean visitStatCommand(AGLParser.StatCommandContext ctx) {
      // stat: command;
      Boolean res = true;
      res = visit(ctx.command());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid command");
      }
      return res;
   }

   @Override
   public Boolean visitStatBlock(AGLParser.StatBlockContext ctx) {
      // '{' stat+ '}'
      Boolean res = true;
      for (AGLParser.StatContext stat : ctx.stat()) {
         res = visit(stat);
         if (!res || res == null) {
            return false;
         }
      }
      return res;
   }

   // ------ End visit stat ------

   @Override
   public Boolean visitInstantiation(AGLParser.InstantiationContext ctx) {
      // instantiation: ID ':' (simpleStatement | blockStatement)
      Boolean res = true;
      String ID = ctx.ID().getText();
      List<String> reservedWords = Arrays.asList(RESERVED_WORDS);

      if (reservedWords.contains(ID)) {
         ErrorHandling.printError("Error: variable name \"" + ID + "\" is a reserved word!");
         return false;
      }

      if (AGLParser.symbolTable.containsKey(ID)) {
         ErrorHandling.printError("Variable \"" + ID + "\" already declared!");
         return false;
      }
      if (ctx.simpleStatement() != null) {
         ctx.simpleStatement().varName = ID;
         res = visit(ctx.simpleStatement());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement instantiation");
            return false;
         } else if (ctx.simpleStatement().in_assignment() != null) {
            return true; // enum is defined in children visit!
         }

         Symbol sym = null;
         if (ctx.simpleStatement().typeID().res instanceof ModelType) {
            ObjectType objectType = new ObjectType(ctx.simpleStatement().typeID().res.name());
            sym = new VariableSymbol(ID, objectType);
         } else {
            sym = new VariableSymbol(ID, ctx.simpleStatement().typeID().res);
         }
         sym.setValueDefined();  

         if( currentModel != null) {
            currentModel.symbolModelTable.put(ID, sym);
         } else {
            AGLParser.symbolTable.put(ID, sym);
         }

      } else if (ctx.blockStatement() != null) {
         res = visit(ctx.blockStatement());
         if (!res) {
            ErrorHandling.printError(ctx, "Error: invalid block statement instantiation");
            return false;
         }
         Symbol sym = new VariableSymbol(ID, ctx.blockStatement().typeID().res);
         sym.setValueDefined();

         if (currentModel != null) {
            currentModel.symbolModelTable.put(ID, sym);
         } else {
            AGLParser.symbolTable.put(ID, sym);
         }
      }

      return res;
   }

   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      // simpleStatement: typeID ('at' expression | assignment)? ';' | typeID in_assignment
      // assignment = expression and expression returns [Type eType, String varName]
      // in_assignment: 'in' '{' ID (',' ID)* '}'
      
      String typeID = ctx.typeID().getText();
      
      if (!isValidType(typeID)) { // check if type is valid
         ErrorHandling.printError("Error: invalid type in simple statement");
         return false;
      }

      Symbol s = AGLParser.symbolTable.get(typeID);

      Type type;

      if (s != null) {
         // ModelType
         type = new ModelType(typeID);
      } else {
         type = ctx.typeID().res;
         if (type == null) {
            type = AGLParser.symbolTable.get(typeID).type();
         }
      }

      // check if we have an expression 
      if (ctx.expression() != null) {
         Boolean res = visit(ctx.expression());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }

         // expression must be a PointType
         if (!ctx.expression().eType.conformsTo(pointType)) {
            ErrorHandling.printError("Error: invalid expression type in simple statement (must be point!)");
            return false;
         }

         if (s != null && type instanceof ModelType) {
            if (!(type instanceof ModelType)) {
               ErrorHandling.printError("Error: invalid type in simple statement (must be an model type!)");
               return false;
            }
         } else {
            if (!(type instanceof ObjectType)) {
               ErrorHandling.printError("Error: invalid type in simple statement (must be an object type!)");
               return false;
            }
         }
      }

      // check if we have an assignment or a in_assignment and if it conforms to the type
      if (ctx.assignment() != null) {
         Boolean res = visit(ctx.assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }

         if (type == null) {
            type=ctx.typeID().res;
         }

         if (!ctx.assignment().eType.conformsTo(type)) {
            if (type instanceof TimeType && (ctx.assignment().eType instanceof NumberType || ctx.assignment().eType instanceof IntegerType)){
               return true;
            }
            // If eType is number may be integer or number      
            if (!((ctx.assignment().eType instanceof IntegerType && type instanceof NumberType) || (ctx.assignment().eType instanceof PointType && type instanceof VectorType))) {
               ErrorHandling.printError("Expression type does not conform to variable type!");
               return false;
            }
         }

      } else if (ctx.in_assignment() != null) {
         ctx.in_assignment().varName = ctx.varName;
         Boolean res = visit(ctx.in_assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }
         return true;
      }

      return true;
   }

   @Override
   public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      // blockStatement: typeID ('at' expression)? 'with' propertiesAssignment
      Boolean res = true;

      String ID = ctx.typeID().getText();

      if (!isValidType(ID)) { // check if type is valid
         ErrorHandling.printError("Error: invalid type in block statement");
         return false;
      }

      if (ctx.expression() != null) {
         res = visit(ctx.expression());
         if (!res) {
            ErrorHandling.printError("Error: invalid block statement");
            return false;
         }
         Type type = new PointType();
         if (!ctx.expression().eType.conformsTo(type)) {
            ErrorHandling.printError("Error: invalid expression type in block statement (must be point origin!)");
            return false;
         }
      }

      Type type = ctx.typeID().res;
      if (type == null) {
         ErrorHandling.printError("Error: invalid type in block statement");
         return false;
      }
   
      // only object types can have properties, should give an error if not
      if (ctx.propertiesAssignment() != null && !(type instanceof ObjectType) ) {
         ErrorHandling.printError("Error: only object types can have properties");
         return false;
      }

      // we do not need PropertyAssignment visitor!
      for (AGLParser.LongAssignmentContext longAssign : ctx.propertiesAssignment().longAssignment()) {
         Type valueType = null;

         // visit(expression) to get type
         visit(longAssign.assignment());
         valueType = longAssign.assignment().eType;
         
         if (!identifierIsValid(longAssign.identifier().getText(), longAssign.assignment().expression().getText(), valueType ,ID)) {
            ErrorHandling.printError("Error: invalid properties assignment in block statement");
            return false;
         }

         res = visit(longAssign.assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid properties assignment in block statement");
            return false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
      // propertiesAssignment : '{' longAssignment ( ';' longAssignment)* ';'? '}'
      Boolean res = true;

      for (AGLParser.LongAssignmentContext longAssign : ctx.longAssignment()) {
         String id = longAssign.identifier().getText();

         // Visit the assignment to get its type
         res = visit(longAssign.assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid long assignment in properties assignment");
            return false;
         }

         // Get the type of the assignment's expression
         Type typeAttribute = longAssign.assignment().eType;
         if (typeAttribute == null) {
            ErrorHandling.printError("Error: type of assignment is null for identifier: " + id);
            return false;
         }

         // Check if the identifier is already in the symbol table
         if (!AGLParser.symbolTable.containsKey(id)) {
            // If not, create a new symbol and add it to the symbol table
            Symbol sym = new VariableSymbol(id, typeAttribute);
            sym.setValueDefined();
            AGLParser.symbolTable.put(id, sym);
         } else {
            // If the symbol already exists, ensure the types conform
            Symbol sym = AGLParser.symbolTable.get(id);
            if (!typeAttribute.conformsTo(sym.type())) {
                  ErrorHandling.printError("Error: type mismatch for identifier: " + id);
                  return false;
            }
            sym.setValueDefined();
         }
      }

      return res;
   }

   
   @Override
   public Boolean visitLongAssignment(AGLParser.LongAssignmentContext ctx) {
      // longAssignment : identifier assignment;
      // identifier : ID | ID '.' identifier | ID '[' expression ']' ('.' identifier)? ;
      // assignment : '=' expression; 
      Boolean res = true;
      String id = ctx.identifier().getText();

      // to konw the type of the variable on the left side we use the function getConcreteID
      // the visitors of the expression will give me the types on the right side -> ctx.assignment().eType
      Type type = getConcreteIDType(ctx.identifier(), null);   
      

      if (type == null) {
         ErrorHandling.printError("Variable does not exist");
         return false;
      }  
   
      if ( (ctx.identifier().expression() == null ) && (ctx.identifier().identifier() == null) ) { // therefore it is a simple identifier (not an attribute)
         if (!AGLParser.symbolTable.containsKey(id)) {
            ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
            return false;
         } else {
            Boolean resExpr = visit(ctx.assignment());
            if (resExpr) {
               Symbol sym = AGLParser.symbolTable.get(id);
               if (sym == null) {
                  ErrorHandling.printError(ctx, "Symbol for variable " + id + " is null");
                  return false;
               }
               if (ctx.assignment().eType == null) {
                  ErrorHandling.printError(ctx, "Assignment type is null");
                  return false;
               }
            
               if (!ctx.assignment().eType.conformsTo(sym.type())) {
                  ErrorHandling.printError(ctx, "Expression type does not conform to variable type!");
                  return false;
               } else {
                  sym.setValueDefined();
               }
            } else {
               return false;
            }
         }
      
      } else {
         Boolean resExpr = visit(ctx.assignment());
         if (resExpr) {
            if (ctx.assignment().eType == null) {
               ErrorHandling.printError(ctx, "Assignment type is null");
               return false;
            }       
            if (ctx.identifier().identifier() != null) {
               String attributeName = ctx.identifier().identifier().getText();

               // if contains '.' attribute name should be the last identifier. e.g: tower2.disks[0].state -> state
               if (attributeName.contains(".")) {
                  String[] parts = attributeName.split("\\.");
                  attributeName = parts[parts.length - 1];
               }

               if (type instanceof ObjectType) {
                  ObjectType objectType = new ObjectType(type.name());
                  if (!objectType.checkAttributes(attributeName, ctx.assignment().eType)) {
                     ErrorHandling.printError("Expression type does not conform to attribute type");
                     return false;
                  }
               } 
            }

            if (type instanceof EnumType && ((EnumType)type).getEnums().contains(ctx.assignment().eType)) {
               return true;
            }

            if (!ctx.assignment().eType.conformsTo(type)) {
               // If eType is number may be integer or number      
               if (!((ctx.assignment().eType instanceof IntegerType && type instanceof NumberType) || (ctx.assignment().eType instanceof PointType && type instanceof VectorType))) {
                  ErrorHandling.printError("Expression type does not conform to variable type!");
                  return false;
               }
            }

            // define variable symbol
            Symbol sym = new VariableSymbol(id, ctx.assignment().eType);

            if (currentModel != null) {
               currentModel.symbolModelTable.put(id, sym);
            } else {
               AGLParser.symbolTable.put(id, sym);
            }

            sym.setValueDefined();

         } else {
            return false;
         }
      }

      return true;
   }

   @Override
   public Boolean visitAssignment(AGLParser.AssignmentContext ctx) {
      // assignment '=' expression
      //  '[' expression (',' expression)* ']'   #ExprArray

      Boolean res = visit(ctx.expression());
      String exprText = ctx.expression().getText();
   
      if (res == null) {
         ErrorHandling.printError("ERROR: Expression is null");
         return false;
      }
      // If expression have more than one index then we have to check the last index: E.g. a[1] is a Array<Array<Point>> but a[1][2] is a Array<Point>
      if (res) {
         Type type = ctx.expression().eType;

         // if it's an access to an array element: exprText = varName[1]
         String varName = exprText.split("\\[")[0];

         // if it's an access to an array element: varName[1], varName belongs to symbol table
         if (ctx.expression().eType instanceof ArrayType && AGLParser.symbolTable.containsKey(varName)) {
            // check the number of indexes in exprText, by counting the number of '['
            int count = 0;
            for (int i = 0; i < exprText.length(); i++) {
               if (exprText.charAt(i) == '[') {
                  count++;
               }
            }
            // if count > 1 then we have to check the last index
            if (count > 1) {
               String typeStr = type.name();
               // remove from "typeStr" the first (count-1) "<Array>"
               for (int i = 0; i < count - 1; i++) {
                  int start = typeStr.indexOf('<') + 1;
                  int end = typeStr.lastIndexOf('>');
                  typeStr = typeStr.substring(start, end);
               }
               type = new ArrayType(typeStr);
            }
         }
         ctx.eType = type;
      }

      return res;
   }

   @Override
   public Boolean visitIn_assignment(AGLParser.In_assignmentContext ctx) {
      // in_assignment: 'in' '{' ID (',' ID)* '}'

      Boolean res = true;
      String ID = ctx.varName;
      EnumType enumType = new EnumType();

      // store id's in list of enums
      for (int i = 0; i < ctx.ID().size(); i++) {
         String id = ctx.ID(i).getText();
         EnumValueType enumValue = new EnumValueType(id);
         Symbol sym = new VariableSymbol(id, enumValue);
         sym.setValueDefined();

         // Both symbol tables
         if (currentModel != null) {
            currentModel.symbolModelTable.put(id, sym);
         } 
         AGLParser.symbolTable.put(id, sym);
      
         enumType.addEnum(enumValue); // add enumValue to a list of enums in EnumType
      }

      Symbol sym = new VariableSymbol(ID, enumType);
      sym.setValueDefined();

      if (currentModel != null) {
         currentModel.symbolModelTable.put(ID, sym);
      } else {
         AGLParser.symbolTable.put(ID, sym);
      }

      List<EnumValueType> enums = enumType.getEnums();
      ctx.eType = enumType;

      return res;
   }

   // ------ Visit Expression ------

   @Override
   public Boolean visitExprUnary(AGLParser.ExprUnaryContext ctx) {
      // expression: sign=('+'|'-'|'not') e=expression and expression returns [Type eType, String varName]
      Boolean signal = ctx.sign.getText().equals("+") || ctx.sign.getText().equals("-") || ctx.sign.getText().equals("not");

      if (!signal) {
         ErrorHandling.printError(ctx, "Invalid unary operator!");
         return false;
      }

      Boolean res = visit(ctx.e);

      // If signal is not 'not' then the expression must be numeric
      if (res && ctx.sign.getText().equals("not")) {
         if (!ctx.e.eType.conformsTo(booleanType)) {
            ErrorHandling.printError(ctx, "The 'not' operator requires a boolean operand!");
            res = false;
         } else {
            ctx.eType = booleanType;
         }
      } else {
         if (res && ctx.e.eType != null && checkUnaryType(ctx.e.eType)) {
            ctx.eType = ctx.e.eType;
         } else {
            ErrorHandling.printError("Error: invalid unary expression or undefined type!");
            res = false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      // expression: '(' e=expression ')' and expression returns [Type eType, String varName]
      Boolean res = visit(ctx.e);
      if (res)
         ctx.eType = ctx.e.eType;
      return res;
   }

   // @Override
   public Boolean visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
      // expression: e1=expression op=('*'|'/') e2=expression | e1=expression op=('+'|'-') e2=expression
      // expression returns [Type eType, String varName]
      Boolean res = true;

      // if op is '+','-','*','/' then both expressions must be numeric
      if (ctx.op.getText().equals("+") || ctx.op.getText().equals("-") || ctx.op.getText().equals("*")
            || ctx.op.getText().equals("/")) {

         res = visit(ctx.e1) && visit(ctx.e2);

         if (res) {

            // we can't divide by zero
            if (ctx.op.getText().equals("/") && ctx.e2.getText().equals("0")) {
               ErrorHandling.printError(ctx, "Error: division by zero!");
               return false;
            }

            // we cannot divide, sum or subtract a scalar with a point or vector
            if ((ctx.op.getText().equals("/") || ctx.op.getText().equals("+") || ctx.op.getText().equals("-"))
                  && (ctx.e1.eType.conformsTo(integerType) || ctx.e1.eType.conformsTo(numberType))
                  && (ctx.e2.eType.conformsTo(pointType) || ctx.e2.eType.conformsTo(vectorType))) {
               ErrorHandling.printError(ctx, "Error: cannot divide, sum or subtract a scalar with a point or vector!");
               return false;
            }

            // we cannot sum or subtract a point or vector with a scalar
            if ((ctx.op.getText().equals("+") || ctx.op.getText().equals("-"))
                  && (ctx.e1.eType.conformsTo(pointType) || ctx.e1.eType.conformsTo(vectorType))
                  && (ctx.e2.eType.conformsTo(integerType) || ctx.e2.eType.conformsTo(numberType))) {
               ErrorHandling.printError(ctx, "Error: cannot sum or subtract a point or vector with a scalar!");
               return false;
            }

            // we can't sum, subtract, multiply or divide a point with a point
            if (ctx.e1.eType.conformsTo(pointType) && ctx.e2.eType.conformsTo(pointType)) {
               ErrorHandling.printError(ctx, "Error: cannot sum, subtract, multiply or divide a point with a point!");
               return false;
            }

            // we can't divide a vector by a vector
            if (ctx.op.getText().equals("/")
                  && (ctx.e1.eType.conformsTo(vectorType) && ctx.e2.eType.conformsTo(vectorType))) {
               ErrorHandling.printError(ctx, "Error: cannot divide a vector by a vector!");
               return false;
            }

            ctx.eType = fetchType(ctx.e1.eType, ctx.e2.eType, ctx.op.getText());

            if (ctx.eType == null) {
               ErrorHandling.printError(ctx, "Error: invalid type in arithmetic operation!");
               return false;
            }

         }
         return res;
      }

      return res;

   }

   @Override
   public Boolean visitExprAndOr(AGLParser.ExprAndOrContext ctx) {
      // expression: e1=expression 'and' e2=expression | e1=expression 'or' e2=expression
      Boolean res = true;

      // if op is 'and' or 'or' then both expressions must be boolean
      res = visit(ctx.e1) && visit(ctx.e2);
      if (res) {
         if (!ctx.e1.eType.conformsTo(booleanType) || !ctx.e2.eType.conformsTo(booleanType)) {
            ErrorHandling.printError(ctx, "The operator and or or requires boolean operands!");
            res = false;
         } else {
            ctx.eType = booleanType;
         }
      }
      return res;
   }

   @Override
   public Boolean visitExprPoint(AGLParser.ExprPointContext ctx) {
      // expression: '(' x=expression ',' y=expression ')' and expression returns [Type eType, String varName]
      
      Boolean res = visit(ctx.x) && checkNumericType(ctx.x.eType) && visit(ctx.y) && checkNumericType(ctx.y.eType);

      // Define as PointType
      if (res) {
         ctx.eType = new PointType();
      } else {
         ErrorHandling.printError(ctx, "Point creation requires numeric operands!");
      }
      return res;
   }

   @Override
   public Boolean visitExprVector(AGLParser.ExprVectorContext ctx) {
      // '(' deg=expression ':' length=expression ')' and expression returns [Type eType, String varName]

      Boolean res = visit(ctx.deg) && checkNumericType(ctx.deg.eType) && visit(ctx.length)
            && checkNumericType(ctx.length.eType);

      // Define as VectorType
      if (res) {
         ctx.eType = new VectorType();
      } else {
         ErrorHandling.printError(ctx, "Vector creation requires numeric operands!");
      }
      return res;
   }

   @Override
   public Boolean visitExprRelational(AGLParser.ExprRelationalContext ctx) {
      // e1=expression op=('>'|'<'|'>='|'<=') e2=expression |  e1=expression op=('=='|'!=') e2=expression
      // expression returns [Type eType, String varName]
      Boolean res = true;
      res = visit(ctx.e1) && visit(ctx.e2);

      if (res) {
         // if e1 is a EnumType then e2 must be in enums list
         if (ctx.e1.eType instanceof EnumType && !(ctx.e2.eType instanceof EnumType)) {
            if (!(ctx.e2.eType instanceof EnumValueType)) {
               ErrorHandling.printError(ctx, "Error: it must be an enum type or enum value type!");
               return false;
            }

            Symbol s1 = null;
            if (currentModel != null) {
               s1 = currentModel.symbolModelTable.get(ctx.e1.getText());
            } else {
               s1 = AGLParser.symbolTable.get(ctx.e1.getText());
            }

            EnumType e1 = (EnumType) s1.type();

            List<EnumValueType> enums = e1.getEnums();

            Symbol s2 = AGLParser.symbolTable.get(ctx.e2.getText());
            EnumValueType e2 = (EnumValueType) s2.type();

            if (!enums.contains(e2)) {
               ErrorHandling.printError(ctx, "Error: invalid relational expression (enum type)");
               return false;
            }
            ctx.eType = booleanType;

            return true;
         }

         if (!ctx.e1.eType.conformsTo(ctx.e2.eType)) {
            // If eType is number may be integer or number
            if (!(ctx.e1.eType instanceof IntegerType && ctx.e2.eType instanceof NumberType)
            && !(ctx.e1.eType instanceof NumberType && ctx.e2.eType instanceof IntegerType)) {
               ErrorHandling.printError(ctx, "Error: must be the same type in relational expression!");
               return false;
            }
  
         }

         if (ctx.e1.eType instanceof PointType || ctx.e1.eType instanceof VectorType) {
            ErrorHandling.printError(ctx, "Error: invalid relational expression (point or vector type)");
            return false;
         }
         ctx.eType = booleanType;
      } else {
         ErrorHandling.printError(ctx, "Error: invalid relational expression");
      }

      return true;
   }

   @Override
   public Boolean visitExprNumber(AGLParser.ExprNumberContext ctx) {
      // expression: number=(INT | FLOAT) and expression returns[Type eType]
      if (ctx.INT() != null) {
         ctx.eType = integerType;
      } else if (ctx.FLOAT() != null) {
         ctx.eType = numberType;
      } else {
         ErrorHandling.printError("Unexpected number type");
         return false;
      }
      return true;
   }

   @Override
   public Boolean visitExprString(AGLParser.ExprStringContext ctx) {
      ctx.eType = stringType;
      if (ctx.STRING() == null) {
         ErrorHandling.printError("Unexpected string type");
         return false;
      }
      return true;
   }

   @Override
   public Boolean visitExprBoolean(AGLParser.ExprBooleanContext ctx) {
      // expression: 'True' | 'False' and expression returns [Type eType, String varName]
      ctx.eType = booleanType;
      return true;
   }

   @Override
   public Boolean visitExprID(AGLParser.ExprIDContext ctx) {
      // expression: identifier and expression returns [Type eType, String varName]
      // identifier : ID | ID '.' identifier | ID '[' expression ']' ('.' identifier)? ;
      Boolean res = true;
      String id = ctx.identifier().getText();

      Type type = getConcreteIDType(ctx.identifier(), null);

      if (type == null) {
         ErrorHandling.printError(ctx, "Error: invalid type in identifier");
         return false;
      } else {
         ctx.eType = type;
      }

      return res;
   }

   @Override
   public Boolean visitExprScript(AGLParser.ExprScriptContext ctx) {
      // expression: op=('input'|'load') STRING and expression returns [Type eType, String varName]
      ctx.eType = scriptType;
      return true;
   }

   @Override
   public Boolean visitExprDeepCopy(AGLParser.ExprDeepCopyContext ctx) {
      // expression: 'deepcopy' identifier 'to' expression and expression returns [Type eType, String varName]
      // identifier : ID | ID '.' identifier | ID '[' expression ']' ('.' identifier)? ;
      Boolean res = true;
      String id = ctx.identifier().getText();

      if ( (ctx.identifier().expression() == null ) && (ctx.identifier().identifier() == null) ) {
         if (!AGLParser.symbolTable.containsKey(id)) {
            ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
            res = false;
         } else {
            Symbol sym = AGLParser.symbolTable.get(id);
            if (!sym.valueDefined()) {
               ErrorHandling.printError(ctx, "Variable \"" + id + "\" not defined!");
               res = false;
            } else {
               ctx.eType = sym.type();
            }
         }
      } else {
         Type type = getConcreteIDType(ctx.identifier(), null);
         if (type == null) {
            ErrorHandling.printError("Error: invalid type in identifier");
            return false;
         } else {
            ctx.eType = type;
         }
      }
      res = visit(ctx.expression());
      
      if (!res) {
         ErrorHandling.printError("Error: invalid expression in deepcopy command");
         return false;
      }
      // check if expression is a point
      if (!ctx.expression().eType.conformsTo(pointType)) {
         ErrorHandling.printError("Error: invalid expression type in deepcopy command (must be point!)");
         return false;
      }
      return res;
   }

   @Override
   public Boolean visitExprArray(AGLParser.ExprArrayContext ctx) {
      // expression: '[' (expression (',' expression)*)? ']' and expression returns [Type eType, String varName]
      Boolean res = true;

      // the values of the array must be the same type
      Type elemType = null;
      for (AGLParser.ExpressionContext expr : ctx.expression()) {
         res = visit(expr);
         if (!res) {
            ErrorHandling.printError("Error: invalid expression in array expression");
            return false;
         }
         if (elemType == null) {
            elemType = expr.eType;
         }
         if (!expr.eType.conformsTo(elemType)) {
            ErrorHandling.printError("Error: invalid expression type in array expression");
            return false;
         }
      }
      if (res) {
         ctx.eType = new ArrayType("Array<" + elemType.name() + ">");
      }

      return res;
   }   

   @Override
   public Boolean visitExprWait(AGLParser.ExprWaitContext ctx) {
      // 'wait' eventTrigger #ExprWait
      // eventTrigger: 'mouse' mouseTrigger
      // mouseTrigger: 'click'
      ctx.eType = pointType;
      return true;
   }

   // --------- End Visit Expression ---------

   @Override
   public Boolean visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
      // 'refresh' ID (',' ID)* ('after' expression suffix=('ms'|'s'))? ';' and Expression returns [Type eType, String varName]
      Boolean res = true;
      
      String id;
      Type type;
      for (TerminalNode idCtx : ctx.ID()) {
         id = idCtx.getText();
         if (!AGLParser.symbolTable.containsKey(id)) {
            ErrorHandling.printError(ctx, "VariableBBB \"" + id + "\" does not exists!");
            res = false;
         }
         type = AGLParser.symbolTable.get(id).type();
         // must conforms to view type
         if (!type.conformsTo(viewType)) {
            ErrorHandling.printError(ctx, "Error: invalid type in refresh command (must be a view type!)");
            return false;
         }
      }

      if (ctx.expression() != null) {
         res = visit(ctx.expression());
         if (!res) {
            ErrorHandling.printError(ctx, "Error: invalid expression in refresh command");
            return false;
         }

         if (ctx.expression().getText().contains("-")) {
            ErrorHandling.printError(ctx, "Error: invalid expression in refresh command (cannot have '-' signal)");
            return false;
         }

         // expression must be a number, integer or variable of type Time
         if (!ctx.expression().eType.conformsTo(numberType) && !ctx.expression().eType.conformsTo(integerType) && !ctx.expression().eType.conformsTo(timeType) ) {
            ErrorHandling.printError(ctx, "Error: invalid expression type in refresh command (must be a number, integer or time type!)");
            return false;
         } else {
            // if expression().getText() is a number (integer ot float) check if it is positive
            if (ctx.expression().getText().matches("[0-9]+") || ctx.expression().getText().matches("[0-9]+.[0-9]+")) {
               Double value = Double.parseDouble(ctx.expression().getText());
               if (value < 0) {
                  ErrorHandling.printError(ctx, "Error: invalid expression value in refresh command (must be positive!)");
                  return false;
               }
               return true;
            } else {
               Symbol sym = AGLParser.symbolTable.get(ctx.expression().getText());
            }
         }
      }

      return res;
   }

   @Override
   public Boolean visitCommandPrint(AGLParser.CommandPrintContext ctx) {
      // command: 'print' expression ';' and expression returns [Type eType, String varName]
      Boolean res = true;
      res = visit(ctx.expression());

      if (!res) {
         ErrorHandling.printError("Error: invalid expression in print command");
         return false;
      }
      return res;
   }

   @Override
   public Boolean visitCommandClose(AGLParser.CommandCloseContext ctx) {
      // command: 'close' ID (',' ID)* ';'
      Boolean res = true;
      String id;
      Type type;

      for (TerminalNode idCtx : ctx.ID()) {
         id = idCtx.getText();
         if (!AGLParser.symbolTable.containsKey(id)) {
            ErrorHandling.printError(ctx, "VariableDDD \"" + id + "\" does not exists!");
            res = false;
         }
         type = AGLParser.symbolTable.get(id).type();
         // must conforms to view type
         if (!type.conformsTo(viewType)) {
            ErrorHandling.printError(ctx, "Error: invalid type in close command (must be a view type!)");
            return false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitCommandMove(AGLParser.CommandMoveContext ctx) {
      // command: 'move' identifier (',' identifier)* type=('by'|'to') expression ';'
      Boolean res = true;
      Type type;
  
      for (AGLParser.IdentifierContext ident : ctx.identifier()) {
         type = getConcreteIDType(ident, null);
         // must conforms to object type or model type or view type
         if ( !(type instanceof ObjectType) && !type.conformsTo(modelObjectType) && !type.conformsTo(viewType)) {
            ErrorHandling.printError(ctx, "Error: invalid type in move command (must be an object, model or view type!)");
            return false;
         }
      }

      res = visit(ctx.expression());
      if (!res) {
         ErrorHandling.printError("Error: invalid expression in move command");
         return false;
      }

      if (ctx.type.getText().equals("by")) { // if type is 'by' then the expression can be a point or a vector
         if (!ctx.expression().eType.conformsTo(pointType) && !ctx.expression().eType.conformsTo(vectorType)) {
            ErrorHandling.printError("Error: invalid expression type in move command (must be a point or a vector!)");
            return false;
         }
      } else if (ctx.type.getText().equals("to")) { // if type is 'to' then the expression must be a point
         if (!ctx.expression().eType.conformsTo(pointType)) {
            ErrorHandling.printError("Error: invalid expression type in move command (must be a point!)");
            return false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitCommandRotate(AGLParser.CommandRotateContext ctx) {
      // command : 'rotate' identifier (',' identifier)* 'by' expression ';'
      Boolean res = true;

      Type type;
      for (AGLParser.IdentifierContext ident : ctx.identifier()) {
         type = getConcreteIDType(ident, null);
         // must conforms to object type (except views because we cannot rotate views) or model type 
         if ( !(type instanceof ObjectType) && !type.conformsTo(modelObjectType) || (type.conformsTo(viewType)) ) {
            ErrorHandling.printError(ctx, "Error: invalid type in rotate command (must be an object or model type!)");
            return false;
         }
      }
   
      res = visit(ctx.expression());
      if (!res) {
         ErrorHandling.printError("Error: invalid expression in rotate command");
         return false;
      }

      // expression must be a number
      if (!ctx.expression().eType.conformsTo(numberType) && !ctx.expression().eType.conformsTo(integerType)) {
         ErrorHandling.printError("Error: invalid expression type in rotate command (must be a number!)");
         return false;
      }

      return res;
   }   

   @Override
   public Boolean visitForStatement(AGLParser.ForStatementContext ctx) {
      // forStatement : 'for' ID 'in' number_range 'do' stat;
      // number_range : expression '..' expression ('..' expression)?
      Boolean res = true;
      String id = ctx.ID().getText();

      if (AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError("Variable \"" + id + "\" already declared!");
         return false;
      }

      Symbol sym = new VariableSymbol(id, integerType);
      sym.setValueDefined();
      if (currentModel != null) {
         currentModel.symbolModelTable.put(id, sym);
      } else {
         AGLParser.symbolTable.put(id, sym);
      }

      // first expression
      res = visit(ctx.number_range().expression(0));
      if (!res) {
         ErrorHandling.printError("Error: invalid first expression in for statement");
         return false;
      }

      // second expression
      res = visit(ctx.number_range().expression(1));
      if (!res) {
         ErrorHandling.printError("Error: invalid second expression in for statement");
         return false;
      }

      // expressions must be integer
      if (!(ctx.number_range().expression(0).eType instanceof IntegerType
            && ctx.number_range().expression(1).eType instanceof IntegerType)) {
         ErrorHandling.printError("Error: invalid expression type in for statement (must be integer!)");
         return false;
      }

      // third expression
      if (ctx.number_range().expression().size() == 3) {
         res = visit(ctx.number_range().expression(2));
         if (!res) {
            ErrorHandling.printError("Error: invalid third expression in for statement");
            return false;
         }
         // expression must be integer
         if (!(ctx.number_range().expression(2).eType instanceof IntegerType)) {
            ErrorHandling.printError("Error: invalid expression type in for statement (must be integer!)");
            return false;
         }
      }

      res = visit(ctx.stat());

      if (!res) {
         ErrorHandling.printError("Error: invalid statement in for statement");
         return false;
      }

      if (currentModel != null) {
         currentModel.symbolModelTable.remove(id);
      } else {
         AGLParser.symbolTable.remove(id);
      }

      return res;
   }

   @Override
   public Boolean visitWhileStatement(AGLParser.WhileStatementContext ctx) {
      Boolean res = true;
      res = visit(ctx.expression());

      if (!res) {
         ErrorHandling.printError("Error: invalid expression in while statement");
         return false;
      }

      Type exprType = ctx.expression().eType;
      if (!(exprType.conformsTo(booleanType))) {
         ErrorHandling.printError("Error: the expression in the while statement has to be a boolean");
         return false;
      }

      res = visit(ctx.stat());
      if (!res) {
         ErrorHandling.printError("Error: invalid statement in while statement");
         return false;
      }

      return res;
   }

   @Override
   public Boolean visitRepeatStatement(AGLParser.RepeatStatementContext ctx) {
      // repeatStatement : 'repeat' stat 'until' expression;
      Boolean res = true;
      res = visit(ctx.stat());

      if (!res) {
         ErrorHandling.printError("Error: invalid statement in repeat statement");
         return false;
      }

      res = visit(ctx.expression());
      if (!res) {
         ErrorHandling.printError("Error: invalid expression in repeat statement");
         return false;
      }

      Type exprType = ctx.expression().eType;
      if (!(exprType.conformsTo(booleanType))) {
         ErrorHandling.printError("Error: the expression in the repeat statement has to be a boolean");
         return false;
      }
      return res;
   }

   @Override
   public Boolean visitWithStatement(AGLParser.WithStatementContext ctx) {
      Boolean res = true;
      String id = ctx.identifier().getText();
      Symbol symbol = null;
      Type type;
      if (currentModel != null) {
         symbol = currentModel.symbolModelTable.get(id);
         if (symbol == null) {
            ErrorHandling.printError("Error: Symbol for identifier " + id + " is null");
            return false;
         }
         type = symbol.type();
         if (!currentModel.symbolModelTable.containsKey(id)) {
            ErrorHandling.printError("Error: identifier \"" + id + "\" is not defined inside the model");
            return false;
         }
      } else {
         type = getConcreteIDType(ctx.identifier(), null);
      }

      if (!(type instanceof ObjectType)) {
         ErrorHandling.printError("Error: identifier \"" + id + "\" is not an object type");
         return false;
      }

      ObjectType objectType = (ObjectType) type;
      Map<String, Symbol> previousScope = new HashMap<>(AGLParser.symbolTable);
      try {
         res = visit(ctx.propertiesAssignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid assignment in with statement");
            return false;
         }
      } catch (Exception e) {
         e.printStackTrace();
         res = false;
      } finally {
         AGLParser.symbolTable.clear();
         AGLParser.symbolTable.putAll(previousScope);
      }

      return res;
   }

   @Override
   public Boolean visitPlayStatement(AGLParser.PlayStatementContext ctx) {
      // 'play' ID 'with' propertiesAssignment
      Boolean res = true;
      String ID = ctx.ID().getText();

      if (!AGLParser.symbolTable.containsKey(ID)) {
         ErrorHandling.printError("Error: identifier \"" + ID + "\" is not defined");
         return false;
      }

      Type idType = AGLParser.symbolTable.get(ID).type();

      // id type must be "Script" that is an ObjectType
      if (!idType.conformsTo(scriptType)) {
         ErrorHandling.printError("Error: identifier \"" + ID + "\" is not a script type");
         return false;
      }

      // we do not need PropertyAssignment visitor!
      for (AGLParser.LongAssignmentContext longAssign : ctx.propertiesAssignment().longAssignment()) {
         res = visit(longAssign.assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid properties assignment in play statement");
            return false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitModelStatInstantiation(AGLParser.ModelStatInstantiationContext ctx) {
      // modelStat : instantiation
      Boolean res = true;
      res = visit(ctx.instantiation());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid instantiation");
      }
      return res;
   }

   @Override
   public Boolean visitModelStatBlockStatement(AGLParser.ModelStatBlockStatementContext ctx) {
      // modelStat : blockStatement
      Boolean res = true;
      res = visit(ctx.blockStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid block statement");
      }
      return res;
   }

   @Override
   public Boolean visitModelStatLongAssignment(AGLParser.ModelStatLongAssignmentContext ctx) {
      // modelStat : longAssignment ';'
      Boolean res = true;
      res = visit(ctx.longAssignment());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid long assignment");
      }
      return res;
   }

   @Override
   public Boolean visitModelStatAction(AGLParser.ModelStatActionContext ctx) {
      // modelStat : action
      Boolean res = true;
      res = visit(ctx.action());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid action");
      }
      return res;
   }

   @Override
   public Boolean visitModelInstantiation(AGLParser.ModelInstantiationContext ctx) {
      // modelInstantiation : ID '::' 'Model' '{' (modelStat)+ '}';
      Boolean res = true;
      String ID = ctx.ID().getText();

      if (AGLParser.symbolTable.containsKey(ID)) {
         ErrorHandling.printError("Variable \"" + ID + "\" already declared!");
         return false;
      }

      ModelType modelType = new ModelType(ID);
      currentModel = modelType; // IMPORTANT: set currentModel to modelType
      Symbol sym = new VariableSymbol(ID, modelType);
      AGLParser.symbolTable.put(ID, sym);

      for (AGLParser.ModelStatContext modelStat : ctx.modelStat()) {
         // use currentModel to visit

         if (!visit(modelStat)) {
            return false;
         }
      }

      currentModel = null; // IMPORTANT: set currentModel to null

      return true;
   }

   @Override
   public Boolean visitAction(AGLParser.ActionContext ctx) {
      // action: 'action' 'on' identifier stat
      // identifier : ID | ID '.' identifier | ID '[' expression ']' ('.' identifier)? ;
      Boolean res = true;
      String id = ctx.identifier().ID().getText();

      Type idType = null;

      if (currentModel != null) {
         if (!currentModel.symbolModelTable.containsKey(id)) {
            ErrorHandling.printError("Error: identifier \"" + id + "\" is not defined in the model");
            return false;
         }
         idType = currentModel.symbolModelTable.get(id).type();
      } else {
         if (!AGLParser.symbolTable.containsKey(id)) {
            ErrorHandling.printError("Error: identifier \"" + id + "\" is not defined");
            return false;
         }
         idType = AGLParser.symbolTable.get(id).type();
      }

      // Check if the action is on a valid property

      Type type = getConcreteIDType(ctx.identifier(), null);
      if (type == null) {
         ErrorHandling.printError("Error: invalid type in identifier");
         return false;
      } 

      inAction = true;

      res = visit(ctx.stat());
      inAction = false;

      if (!res) {
         ErrorHandling.printError("Error: invalid statement in action");
         return false;
      }

      return res;
   }

   @Override
   public Boolean visitIfStatement(AGLParser.IfStatementContext ctx) {
      // ifStatement: 'if' expression 'do' stat ('else' 'do' stat)?
      Boolean res = true;
      res = visit(ctx.expression());
      if (!res) {
          ErrorHandling.printError("Error: invalid expression in if statement");
          return false;
      }

      Type exprType = ctx.expression().eType;
      if (!(exprType instanceof BooleanType)) {
         ErrorHandling.printError("Error: the expression in the if statement has to be a boolean");
         return false;
      }

      // stat -> loop through all statements
      res = visit(ctx.stat(0));
      if (!res) {
         ErrorHandling.printError("Error: invalid statement in if statement");
         return false;
      }
   
      if (ctx.stat().size() > 1) {
         res = visit(ctx.stat(1));
         if (!res) {
             ErrorHandling.printError("Error: invalid statement in else block of if statement");
             return false;
         }
      }
 
      return res;
   }

   // -- Correct --
   private Boolean checkNumericType(Type t) {
      Boolean res = true;

      if (!t.isNumeric()){
         ErrorHandling.printError("Numeric operator applied to a non-numeric operand!");
         res = false;
      }
      return res;
   }

   private Boolean checkUnaryType(Type t) {
      Boolean res = true;

      if (!t.isNumeric() && !t.name().equals("Point") && !t.name().equals("Vector") && !(t instanceof BooleanType)){
         ErrorHandling.printError("Not an unary type!");
         res = false;
      }
      return res;
   }

   private Type fetchType(Type t1, Type t2, String op) {
      Type res = null;
      if (t1.isNumeric() && t2.isNumeric()) {
         if ("Number".equals(t1.name())) {
            res = t1;
         } else if ("Number".equals(t2.name())) {
            res = t2;
         } else
            res = t1;
      } else if ("boolean".equals(t1.name()) && "boolean".equals(t2.name())) {
         res = t1;
      } else if ("Point".equals(t1.name()) && "Vector".equals(t2.name())) {
         res = t1;
      } else if ("Vector".equals(t1.name()) && "Point".equals(t2.name())) {
         res = t2;
      } else if ("Vector".equals(t1.name()) && t2.isNumeric()) {
         res = t1;
      } else if (t1.isNumeric() && "Vector".equals(t2.name())) {
         res = t2;
      } else if ("Point".equals(t1.name()) && t2.isNumeric()) {
         res = t1;
      } else if (t1.isNumeric() && "Point".equals(t2.name())) {
         res = t2;
      } else if ("Vector".equals(t1.name()) && "Vector".equals(t2.name())) {
         if ("*".equals(op)) {
            res = numberType;
         } else {
            res = t1;
         }
      } else if ("Time".equals(t1.name()) && "Time".equals(t2.name())) {
         res = t1;
      } else if ("Time".equals(t1.name()) && t2.isNumeric()) {
         res = numberType;
      }
      
      return res;
   }

   private boolean isValidType(String typeID) {
      // typeID: 'Integer' | 'String' | 'Point' | 'Number' | 'Vector' | 'Time' | ... | 'Array' | ID

      // Check if type is valid
      switch (typeID) {
         case "Integer":
         case "String":
         case "Point":
         case "Number":
         case "Vector":
         case "Time":
         case "Boolean":
         case "View":
         case "Line":
         case "Rectangle":
         case "Ellipse":
         case "Arc":
         case "ArcChord":
         case "PieSlice":
         case "Text":
         case "Dot":
         case "Polyline":
         case "Spline":
         case "Polygon":
         case "Blob":
         case "Script":
         case "Enum":
         case "Array":
            return true;
      }
      ;

      // typeID can be a Array of a an array of a valid type: E.g: Array<Number> or Array<Array<Point>>
      if (typeID.startsWith("Array<") && typeID.endsWith(">")) {
         String arrayType = typeID.substring(6, typeID.length() - 1);
         return isValidType(arrayType);
      }
   
      // typeID can be a ID
      if (!AGLParser.symbolTable.containsKey(typeID)) {
         ErrorHandling.printError("Error: type not exists: " + typeID);
         return false;
      }

      // must be a ModelType
      Symbol sym = AGLParser.symbolTable.get(typeID);
      if (!(sym.type() instanceof ModelType)) {
         ErrorHandling.printError("Error: invalid model type: " + typeID);
         return false;
      }

      return true;
   }

   private Type getConcreteIDType(AGLParser.IdentifierContext ctx, Type prevType) {

      String id = ctx.ID().getText();
      Type type = null;

      if (prevType == null) {
         if (currentModel == null) {
            if (!AGLParser.symbolTable.containsKey(id)) {
               ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
               return null;
            }
            type = AGLParser.symbolTable.get(id).type();
         } else {
            if (!currentModel.symbolModelTable.containsKey(id)) {
               ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists in model " + currentModel.name);
               return null;
            }
            type = currentModel.symbolModelTable.get(id).type();
         }
      } else {
         type = prevType;
      }
      

      for (AGLParser.ExpressionContext expr : ctx.expression()) {
         Boolean res = visit(expr);
         if (!res) {
            ErrorHandling.printError("Error: invalid expression in simple statement");
            return null;
         }

         // expression must be a IntegerType
         if (!expr.eType.conformsTo(integerType)) {
            ErrorHandling.printError("Error: invalid expression type in simple statement (must be integer!)");
            return null;
         }

         // can be an array or a point
         if (!(type instanceof ArrayType) && !(type instanceof PointType)) {
            ErrorHandling.printError("Error: invalid type in simple statement (must be an array or a point!)");
            return null;
         }

         if (type instanceof PointType) {
            type = numberType;
            continue;
         }

         // if type name don't have <Array> then it is a simple type
         if (((ArrayType)type).getElementType().name().indexOf("Array") == -1) {
            type = new ObjectType(((ArrayType)type).getElementType().name());
            continue;
         }

         // return casted to ArrayType
         type = new ArrayType(((ArrayType)type).getElementType().name());
      }

      if (!(type instanceof ObjectType)) {
         if (ctx.identifier() != null) {
            if (type instanceof ArrayType) {
               type = getConcreteIDType(ctx.identifier(), (ObjectType) ((ArrayType)type).getElementType());
            } else {
               ErrorHandling.printError("Error: invalid attribute in simple statement");
               return null;
            }
         }
         return type;
      } else {
         type = (ObjectType) type;
      }

      String attributeName;
      
      if (ctx.identifier() != null) {
         String nextId = ctx.identifier().ID().getText(); // next ID in the chain   
         
         if (type instanceof ObjectType) {
            ObjectType objectType = (ObjectType) type;
            if (objectType.symbolModelTable != null) {
               if (!objectType.symbolModelTable.containsKey(nextId)) {
                  List<Type> allowedTypes = objectType.getAttributes().get(nextId);
                  if (allowedTypes == null || allowedTypes.isEmpty()) {
                     ErrorHandling.printError("Error: invalid attribute in simple statement");
                     return null;
                  }
                  type = allowedTypes.get(0);
               } else {
                  type = objectType.symbolModelTable.get(nextId).type();
               }
               
            } else {
               List<Type> allowedTypes = objectType.getAttributes().get(nextId);
               if (allowedTypes == null || allowedTypes.isEmpty()) {
                  ErrorHandling.printError("Error: invalid attribute in simple statement");
                  return null;
               }
               type = allowedTypes.get(0);
            
            } 
         }
           
         type = getConcreteIDType(ctx.identifier(), type);

      }

      return type;


   }

   private boolean identifierIsValid(String id, String value, Type valueType, String ID) {
      List<String> colorsList = Arrays.asList(COLORS);
      List<String> statesList = Arrays.asList(STATES);

      if (id.equals("fill")) {
         String valueString = value.substring(1, value.length() - 1);
         if (!colorsList.contains(valueString)) {
            return false;
         }
      }

      if (id.equals("state")) {
         String valueString = value.substring(1, value.length() - 1);
         if (!statesList.contains(valueString)) {
            return false;
         }
      }

      if (id.equals("fill") || id.equals("length") || id.equals("origin") || id.equals("state") || id.equals("start") || id.equals("extent") || id.equals("outline") || id.equals("points") || id.equals("text") || id.equals("width") || id.equals("height") || id.equals("title") || id.equals("Ox") || id.equals("Oy") || id.equals("background")) {

         ObjectType objectType = new ObjectType(ID);

         if (objectType.checkAttributes(id, valueType)) {
            return true;
         } else {
            return false;
         }
      }
      
      if (isValidType(ID)) {
         return false;
      }

      for (String key : AGLParser.symbolTable.keySet()) {
         if (key.equals(value)) {
            return true;
         }
      }

      return false;
   }

   private boolean checkTypeConformance(Type lhsType, Type rhsType) {
      if (lhsType == null || rhsType == null) {
         return false;
      }

      if (lhsType.equals(rhsType)) {
         return true;
      }

      if (lhsType instanceof ArrayType && rhsType instanceof ArrayType) {
         return checkTypeConformance(((ArrayType) lhsType).getElementType(), ((ArrayType) rhsType).getElementType());
      }

      return false;
   }
   
      String[] COLORS = {
         "snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "white", "black", "wheat",
         "linen", "antique white", "papaya whip", "blanched almond", "bisque", "peach puff",
         "navajo white", "lemon chiffon", "mint cream", "azure", "alice blue", "lavender",
         "lavender blush", "misty rose", "dark slate gray", "dim gray", "slate gray",
         "light slate gray", "gray", "light grey", "midnight blue", "navy", "cornflower blue", "dark slate blue",
         "slate blue", "medium slate blue", "light slate blue", "medium blue", "royal blue",  "blue",
         "dodger blue", "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue",
         "light blue", "powder blue", "pale turquoise", "dark turquoise", "medium turquoise", "turquoise",
         "cyan", "light cyan", "cadet blue", "medium aquamarine", "aquamarine", "dark green", "dark olive green",
         "dark sea green", "sea green", "medium sea green", "light sea green", "pale green", "spring green",
         "lawn green", "medium spring green", "green yellow", "lime green", "yellow green",
         "forest green", "green", "olive drab", "dark khaki", "khaki", "pale goldenrod", "light goldenrod yellow",
         "light yellow", "yellow", "gold", "light goldenrod", "goldenrod", "dark goldenrod", "rosy brown",
         "indian red", "saddle brown", "sandy brown", "brown",
         "dark salmon", "salmon", "light salmon", "orange", "dark orange",
         "coral", "light coral", "tomato", "orange red", "red", "hot pink", "deep pink", "pink", "light pink",
         "pale violet red", "maroon", "medium violet red", "violet red",
         "medium orchid", "dark orchid", "dark violet", "blue violet", "purple", "medium purple",
         "thistle"
      };
  
     String[] STATES = {
        "normal", "hidden"
     };

     String[] RESERVED_WORDS = {
      "Integer", "String", "Point", "Number", "Vector", "Time", "Boolean", "View", "Line", "Rectangle", "Ellipse", "Arc", "ArcChord", "PieSlice", "Text", "Dot", "Polyline", "Spline", "Polygon", "Blob", "Script", "Enum", "Array", "length", "origin", "state", "start", "extent", "outline", "points", "text", "width", "height", "title", "Ox", "Oy", "background", "if", "for", "while", "repeat", "with", "play", "action"
      };

}
