import java.util.List;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.antlr.v4.runtime.ParserRuleContext;


@SuppressWarnings("CheckReturnValue")
public class AGLSemanticCheck extends AGLParserBaseVisitor<Boolean> {

   private final IntegerType integerType = new IntegerType();
   private final StringType stringType = new StringType();
   private final NumberType numberType = new NumberType();
   private final PointType pointType = new PointType();
   private final VectorType vectorType = new VectorType();
   private final BooleanType booleanType = new BooleanType();
   private final ObjectType scriptType = new ObjectType("Script");
   private final EnumType enumType = new EnumType();

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

         Symbol sym = new VariableSymbol(ID, ctx.simpleStatement().typeID().res);
         sym.setValueDefined();
         AGLParser.symbolTable.put(ID, sym);

      } else if (ctx.blockStatement() != null) {
         res = visit(ctx.blockStatement());
         if (!res) {
            ErrorHandling.printError(ctx, "Error: invalid block statement instantiation");
            return false;
         }
         Symbol sym = new VariableSymbol(ID, ctx.blockStatement().typeID().res);
         sym.setValueDefined();
         AGLParser.symbolTable.put(ID, sym);
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

      // Type type = getConcreteTypeID(ctx, typeID);
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

      // TODO:

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
         
         // System.out.println("««««««");
         // System.out.println("Type: " + type.name());
         // System.out.println("Assignment type: " + ctx.assignment().eType.name());
         // System.out.println("««««««");


         if (type == null) {
            type=ctx.typeID().res;
         }

         if (!ctx.assignment().eType.conformsTo(type)) {
            // If eType is number may be integer or number      
            if (!(ctx.assignment().eType instanceof IntegerType && type instanceof NumberType)) {
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
         // System.out.println(longAssign.getText());
         // System.out.println(longAssign.identifier().getText());
         // System.out.println("ola" + longAssign.assignment().expression().getText());

         if (!identifierIsValid(longAssign.identifier().getText(), longAssign.assignment().expression().getText())) {
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
      Boolean res = true;

      for (AGLParser.LongAssignmentContext longAssign : ctx.longAssignment()) {
         res = visit(longAssign);
         if (!res) {
            ErrorHandling.printError("Error: invalid properties assignment");
            return false;
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


      // TODO: 
      // quero saber o tipo da variavel do lado esquerdo -> usando a função getConcreteID
      // os visitores da expressao vão me dar os tipos do lado direito -> ctx.assignment().eType

      Type type = getConcreteIDType(ctx.identifier());   
      if (type == null) {
         ErrorHandling.printError("Variable does not exist");
         return false;
      }  

      System.out.println("«««««« Type: " + type.name() + " »»»»»»");

      
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

               System.out.println("«««««« Assignment Type: " + ctx.assignment().eType.name() + " »»»»»»");
            
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
            
            System.out.println("«««««« Assignment Type: " + ctx.assignment().eType.name() + " »»»»»»");

            if (ctx.identifier().identifier() != null) {
               String attributeName = ctx.identifier().identifier().getText();
               if (type instanceof ObjectType) {
                  ObjectType objectType = new ObjectType(type.name());
                  if (!objectType.checkAttributes(attributeName, ctx.assignment().eType)) {
                     ErrorHandling.printError("--------------------- Expression type does not conform to attribute type");
                     return false;
                  }
               } else {
                  ErrorHandling.printError(ctx, "----------------   Type is not an ObjectType!");
                  return false;
               }
            }
            else if (!ctx.assignment().eType.conformsTo(type)) {
               ErrorHandling.printError(ctx, "----------------   Expression type does not conform to variable type!");
               return false;
            }

            // TODO: sym.setValueDefined();

            // define variable symbol
            Symbol sym = new VariableSymbol(id, ctx.assignment().eType);
            AGLParser.symbolTable.put(id, sym);
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
      System.out.println("AAA " + exprText);
   
      if (res == null) {
         ErrorHandling.printError("ERROR: Expression is null");
         return false;
      }
      // If expression have more than one index then we have to check the last index
      // E.g. a[1] is a Array<Array<Point>> but a[1][2] is a Array<Point>
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

      EnumType enumType = new EnumType();
      String ID = ctx.varName;

      // store id's in list of enums
      for (int i = 0; i < ctx.ID().size(); i++) {
         String id = ctx.ID(i).getText();
         EnumValueType enumValue = new EnumValueType(id);

         Symbol sym = new VariableSymbol(id, enumValue);
         sym.setValueDefined();
         AGLParser.symbolTable.put(id, sym);

         enumType.addEnum(enumValue); // add enumValue to a list of enums in EnumType
      }

      Symbol sym = new VariableSymbol(ID, enumType);
      sym.setValueDefined();
      AGLParser.symbolTable.put(ID, sym);

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
         if (res && ctx.e.eType != null && checkNumericType(ctx.e.eType)) {
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
   public Boolean visitExprAddSubMultDivAndOr(AGLParser.ExprAddSubMultDivAndOrContext ctx) {
      // expression: e1=expression op=('*'|'/'|'and') e2=expression | e1=expression op=('+'|'-'|'or') e2=expression
      // expression returns [Type eType, String varName]

      Boolean res = true;

      // if op is 'and' or 'or' then both expressions must be boolean
      if (ctx.op.getText().equals("and") || ctx.op.getText().equals("or")) {
         res = visit(ctx.e1) && visit(ctx.e2);
         if (res) {
            if (!ctx.e1.eType.conformsTo(booleanType) || !ctx.e2.eType.conformsTo(booleanType)) {
               ErrorHandling.printError(ctx, "The operator " + ctx.op.getText() + " requires boolean operands!");
               res = false;
            } else {
               ctx.eType = booleanType;
            }
         }
         return res;
      }

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
      // expression: e1=expression RELATIONAL_OPERATOR e2=expression and expression returns [Type eType, String varName]
      Boolean res = true;

      res = visit(ctx.e1) && visit(ctx.e2);

      if (res) {
         // if e1 is a EnumType then e2 must be in enums list
         if (ctx.e1.eType instanceof EnumType && !(ctx.e2.eType instanceof EnumType)) {
            if (!(ctx.e2.eType instanceof EnumValueType)) {
               ErrorHandling.printError(ctx, "Error: it must be an enum type or enum value type!");
               return false;
            }

            Symbol s1 = AGLParser.symbolTable.get(ctx.e1.getText());
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

         if (ctx.e1.eType instanceof BooleanType) {
            ErrorHandling.printError(ctx, "Error: invalid relational expression (boolean type)");
            return false;
         }

         if (ctx.e1.eType instanceof PointType || ctx.e1.eType instanceof VectorType) {
            ErrorHandling.printError(ctx, "Error: invalid relational expression (point or vector type)");
            return false;
         }

         // TODO: 2.0 == 2

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
         // Caso inesperado, pode ser necessário tratar isso adequadamente
         ErrorHandling.printError("Unexpected number type");
         return false;
      }
      return true;
   }

   @Override
   public Boolean visitExprString(AGLParser.ExprStringContext ctx) {
      ctx.eType = stringType;
      if (ctx.STRING() == null) {
         // Caso inesperado, pode ser necessário tratar isso adequadamente
         ErrorHandling.printError("Unexpected string type");
         return false;
      }
      return true;
   }

   @Override
   public Boolean visitExprID(AGLParser.ExprIDContext ctx) {
      // expression: identifier and expression returns [Type eType, String varName]
      // identifier : ID | ID '.' identifier | ID '[' expression ']' ('.' identifier)? ;

      Boolean res = true;
      String id = ctx.identifier().getText();

      Type type = getConcreteIDType(ctx.identifier());

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
         Type type = getConcreteIDType(ctx.identifier());
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
      ctx.eType = pointType;
      return true;
   }

   // --------- End Visit Expression ---------

   @Override
   public Boolean visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
      // 'refresh' ID (',' ID)* ('after' expression suffix=('ms'|'s'))? ';' and Expression returns [Type eType, String varName]
      Boolean res = true;
      String id = ctx.ID(0).getText();

      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
         res = false;
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

         if (!ctx.expression().eType.conformsTo(numberType) && !ctx.expression().eType.conformsTo(integerType)) {
            ErrorHandling.printError(ctx, "Error: invalid expression type in refresh command (must be integer!)");
            return false;
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
      String id = ctx.ID(0).getText();

      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
         res = false;
      }

      return res;
   }

   @Override
   public Boolean visitCommandMove(AGLParser.CommandMoveContext ctx) {
      // command: 'move' identifier (',' identifier)* type=('by'|'to') expression ';'
      Boolean res = true;
      String id = ctx.identifier(0).getText();

      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
         res = false;
      }

      res = visit(ctx.expression());
      if (!res) {
         ErrorHandling.printError("Error: invalid expression in move command");
         return false;
      }

      // if type is 'by' then the expression can be a point or a vector
      // if type is 'to' then the expression must be a point
      if (ctx.type.getText().equals("by")) {
         if (!ctx.expression().eType.conformsTo(pointType) && !ctx.expression().eType.conformsTo(vectorType)) {
            ErrorHandling.printError("Error: invalid expression type in move command (must be a point or a vector!)");
            return false;
         }
      } else if (ctx.type.getText().equals("to")) {
         if (!ctx.expression().eType.conformsTo(pointType)) {
            ErrorHandling.printError("Error: invalid expression type in move command (must be a point!)");
            return false;
         }
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
      }

      // second expression can not be less than the first expression
      if (Integer.parseInt(ctx.number_range().expression(0).getText()) > Integer.parseInt(ctx.number_range().expression(1).getText())) {
         ErrorHandling.printError("Error: second expression must be greater than the first expression in for statement");
         return false;
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

      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError("Error: identifier \"" + id + "\" is not defined");
         return false;
      }

      Symbol symbol = AGLParser.symbolTable.get(id);
      if (symbol == null) {
         ErrorHandling.printError("Error: Symbol for identifier " + id + " is null");
         return false;
      }

      if (!(symbol.type() instanceof ObjectType)) {
         ErrorHandling.printError("Error: identifier \"" + id + "\" is not an object type");
         return false;
      }

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
      Symbol sym = new VariableSymbol(ID, modelType);
      AGLParser.symbolTable.put(ID, sym);

      for (AGLParser.ModelStatContext modelStat : ctx.modelStat()) {
         if (!visit(modelStat)) {
            return false;
         }
      }

      return true;

   }

   @Override
   public Boolean visitAction(AGLParser.ActionContext ctx) {
      // action: 'action' 'on' identifier stat
      // identifier : ID | ID '.' identifier | ID '[' expression ']' ('.' identifier)? ;
      Boolean res = true;
      String id = ctx.identifier().getText();

      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError("Error: identifier \"" + id + "\" is not defined");
         return false;
      }

      Type idType = AGLParser.symbolTable.get(id).type();

      // id type must be an EnumType 
      if (!idType.conformsTo(enumType)) {
         ErrorHandling.printError("Error: identifier \"" + id + "\" is not an enum type");
         return false;
      }

      res = visit(ctx.stat());
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

      res = visit(ctx.stat(0));

      if (!res) {
         ErrorHandling.printError("Error: invalid statement in if statement");
         return false;
      }

      if (ctx.stat(1) != null) {
         res = visit(ctx.stat(1));
         if (!res) {
            ErrorHandling.printError("Error: invalid statement in else statement");
            return false;
         }
      }

      return res;
   }

   // -- Correct --
   private Boolean checkNumericType(Type t) {
      Boolean res = true;

      if (!t.isNumeric()) {
         ErrorHandling.printError("Numeric operator applied to a non-numeric operand!");
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
      }

      return res;
   }

   private boolean isValidType(String typeID) {
      // typeID: 'Integer' | 'String' | 'Point' | 'Number' | 'Vector' | 'Time' | ... |
      // 'Array' | ID

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
         case "PolyLine":
         case "Spline":
         case "Polygon":
         case "Blob":
         case "Script":
         case "Enum":
         case "Array":
            return true;
      }
      ;

      // typeID can be a Array of a an array of a valid type. 
      // E.g: Array<Number>
      // E.g: Array<Array<Point>>
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


   // TODO: 
   // identifier : ID | ID '.' identifier | ID ('[' expression ']')+ ('.' identifier)? ;
   // returns the type of the expression
   private Type getConcreteIDType(AGLParser.IdentifierContext ctx) {  
      
      String id = ctx.ID().getText();
      Type type = null;

      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
         return null;
      }   

      if (ctx.expression(0) != null) { // ID '[' expression ']' ('.' identifier)?
         Boolean res = visit(ctx.expression(0));
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
         }

         // expression must be a IntegerType
         if (!ctx.expression(0).eType.conformsTo(integerType)) {
            ErrorHandling.printError("Error: invalid expression type in simple statement (must be integer!)");
         }

         System.out.println(ctx.expression(0).eType.name());
         System.out.println("ID: " + id);

         Type elemType = AGLParser.symbolTable.get(id).type();

         if (!(elemType instanceof ArrayType)) {
            ErrorHandling.printError("Error: \"" + id + "\" is not an array!");
            return null;
         }
         
         // return casted to ArrayType
         return new ArrayType(((ArrayType)elemType).getElementType().name());
      } 
      
      if (ctx.identifier() != null) { // ID '.' identifier
         System.out.println("Attribute type");
         type = AGLParser.symbolTable.get(id).type();
         if (!(type instanceof ObjectType)) {
            ErrorHandling.printError("Variable \"" + id + " is not of object type");
            return null;
         }

         ObjectType objectType = (ObjectType) type;
         String attributeName = ctx.identifier().ID().getText();
         List<Type> allowedTypes = objectType.getAttributes().get(attributeName);
         if (allowedTypes == null || allowedTypes.isEmpty()) {
            type = null;
         }
         type = allowedTypes.get(0);
         System.out.println(attributeName);
         System.out.println(type);

         if (type == null) {
            ErrorHandling.printError("Attribute " + attributeName + " does not exist in type " + id);
            return null;
         }
         if (ctx.identifier().identifier() != null) {
            return getConcreteIDType(ctx.identifier());
         }
      }

      // ID
      Symbol sym = AGLParser.symbolTable.get(id);
      if (!sym.valueDefined()) {
         ErrorHandling.printError(ctx, "Variable \"" + id + "\" not defined!"); // type will be null
         return null;
      } else {
         type = sym.type(); 
      }

      return type;
   }

   private boolean identifierIsValid(String id, String value) {
      // System.out.println("identifierIsValid: " + id);
      switch (id) {
         case "fill":
         case "length":
         case "origin":
         case "state":
         case "start":
         case "extent":
         case "outline":
         case "points":
         case "text":
         case "width":
         case "height":
         case "title":
         case "Ox":
         case "Oy":
         case "background":
            return true;
      }
      
      for (String key : AGLParser.symbolTable.keySet()) {
         // System.out.println("Key: " + key);
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

}
