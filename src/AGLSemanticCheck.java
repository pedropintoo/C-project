import org.antlr.v4.runtime.ParserRuleContext;

@SuppressWarnings("CheckReturnValue")
public class AGLSemanticCheck extends AGLParserBaseVisitor<Boolean> {

   private final IntegerType integerType = new IntegerType();
   private final StringType stringType = new StringType();
   private final NumberType numberType = new NumberType();
   private final PointType pointType = new PointType();
   private final VectorType vectorType = new VectorType();
   private final BooleanType booleanType = new BooleanType();
   // private final ObjectType objectType;

   @Override
   public Boolean visitProgram(AGLParser.ProgramContext ctx) {
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
      Boolean res = true;
      String ID = ctx.ID().getText();

      if (AGLParser.symbolTable.containsKey(ID)) {
         ErrorHandling.printError("Variable \"" + ID + "\" already declared!");
         return false;
      }
      if (ctx.simpleStatement() != null) {
         res = visit(ctx.simpleStatement());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement instantiation");
            return false;
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

   // @Override
   // public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
   //    // simpleStatement: typeID (assignment)? and simpleStatement returns [String varName] and typeID returns[Type res]
   //    // assignment = expression    and   expression returns [Type eType, String varName]
   //    String type = ctx.typeID().getText();
   //    Type typeObject = ctx.typeID().res;

   //    if (ctx.assignment() != null) {
   //       Boolean res = visit(ctx.assignment().expression());
   //       if (!res) {
   //          ErrorHandling.printError("Error: invalid simple statement");
   //          return false;
   //       }

   //       if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
   //          ErrorHandling.printError("Expression type does not conform to variable type!");
   //          return false;
   //       }
   //    }

   //    return true;
   // }


   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      // simpleStatement: typeID ('at' expression)? ((assignment)? ';' | in_assignment)
      // assignment = expression    and   expression returns [Type eType, String varName]
      // in_assignment: 'in' '{' ID (',' ID)* '}'

      System.out.println("Check simple statement");

      String type = ctx.typeID().getText();
      Type typeObject = ctx.typeID().res;

      // check if we have an expression and if we have typeObject must be a ObjectType()
      if (ctx.expression() != null) {
         Boolean res = visit(ctx.expression());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }

         // expression must be a PointType
         Type pointType = new PointType();
         if (!ctx.expression().eType.conformsTo(pointType)) {
            ErrorHandling.printError("Error: invalid expression type in simple statement (must be point!)");
            return false;
         }

         // typeObject must be a instanceof ObjectType
         Type t = new ObjectType(type);
         
         if (!t.conformsTo(typeObject)) {
            ErrorHandling.printError("Error: invalid type in simple statement (must be an object type!)");
            return false;
         }

      }

  
      // check if we have an assignment or a in_assignment and if it conforms to the type
      if (ctx.assignment() != null) {
         Boolean res = visit(ctx.assignment());
         System.out.println("Check assignment");
         System.out.println("Type: " + ctx.assignment().eType.name());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }

         if (!ctx.assignment().eType.conformsTo(typeObject)) {
            ErrorHandling.printError("Expression type does not conform to variable type!");
            return false;
         }
      } else if (ctx.in_assignment() != null) {
         
         Boolean res = visit(ctx.in_assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }

         return true; // TO DO
      }

      return true;
   }

   @Override
   public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      // blockStatement: typeID ('at' expression)? 'with' '{' propertiesAssignment '}'
      Boolean res = true;

      String ID = ctx.typeID().getText();

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

      // we do not need PropertyAssignment visitor!
      for (AGLParser.LongAssignmentContext longAssign : ctx.propertiesAssignment().longAssignment()) {
         res = visit(longAssign.assignment());
         if (!res) {
            ErrorHandling.printError("Error: invalid properties assignment in block statement");
            return false;
         }
      }

      return res;
   }


   @Override
   public Boolean visitLongAssignment(AGLParser.LongAssignmentContext ctx) {
      // longAssignment : identifier assignment; 
      // identifier : ID | ID('.' ID)+;
      // assignment : '=' expression;
      Boolean res = true;
      String id = ctx.identifier().getText();

      System.out.println("Check long assignment");
      if (ctx.identifier().ID(1) == null) {
         if (!AGLParser.symbolTable.containsKey(id)) {
            ErrorHandling.printError(ctx, "Variable \"" + id + "\" does not exists!");
            res = false;
         }
         Boolean resExpr = visit(ctx.assignment());
         if (res) {
            Symbol sym = AGLParser.symbolTable.get(id);
            if (!ctx.assignment().eType.conformsTo(sym.type())) {
               ErrorHandling.printError(ctx, "Expression type does not conform to variable type!");
               res = false;
            } else {
               sym.setValueDefined();
            }
         }
      } else {
         ErrorHandling.printError("TO BE IMPLEMENTED ID ('.' ID)+ - attributes"); // TODO
      }

      return res;
   }


   @Override
   public Boolean visitAssignment(AGLParser.AssignmentContext ctx) {
      // assignment '=' expression

      Boolean res = visit(ctx.expression());

      if (res) {
         String exprText = ctx.expression().getText();
         ctx.eType = ctx.expression().eType;
      }

      return res;

   }

   // @Override
   // public Boolean visitPoint(AGLParser.PointContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

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
         if (res && ctx.e.eType != null && checkNumericType( ctx.e.eType)) {
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
      if (ctx.op.getText().equals("+") || ctx.op.getText().equals("-") || ctx.op.getText().equals("*") || ctx.op.getText().equals("/")) {
         
         
         res = visit(ctx.e1) && visit(ctx.e2);
         
         
         if (res) {

            // we can't sum or subtract a point with a point
            // we can't multiply or divide a point with a point
            // we can sum or subtract a point with a vector
            // we can divide a point or a vector with a scalar
            // we can multiply a point with a scalar or a vector with a scalar
            // we can multiply a scalar with a point or a scalar with a vector
            // we can sum, subtract, multiply or divide a scalar with a scalar
            
            
            // we can't divide by zero
            if (ctx.op.getText().equals("/") && ctx.e2.getText().equals("0")) {
               ErrorHandling.printError(ctx, "Error: division by zero!");
               return false;
            }

            System.out.println("e1: " + ctx.e1.eType.name());
            System.out.println("e2: " + ctx.e2.eType.name());
            // we can't divide a scalar with a point 
            if ( (ctx.e1.eType.conformsTo(integerType) || ctx.e1.eType.conformsTo(numberType) ) && ctx.e2.eType.conformsTo(pointType)) {
               ErrorHandling.printError(ctx, "Error: invalid expression type in arithmetic operation (cannot divide a scalar with a point!)");
               return false;
            }


             

            ctx.eType = fetchType(ctx.e1.eType, ctx.e2.eType);
         }
         return res;
      }

      return res;
   
   }

   @Override
   public Boolean visitExprPoint(AGLParser.ExprPointContext ctx) {
      // expression: '(' x=expression ',' y=expression ')'  and expression returns [Type eType, String varName]
      
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
      
      Boolean res = visit(ctx.deg) && checkNumericType(ctx.deg.eType) && visit(ctx.length) && checkNumericType(ctx.length.eType);

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
      // expression: expression RELATIONAL_OPERATOR expression and expression returns [Type eType, String varName]
      Boolean res = true;

      // Visit the left expression and check if it is IntegerType
      res = visit(ctx.expression(0));
      Type leftType = ctx.expression(0).eType;
      if (!leftType.conformsTo(integerType)) {
         ErrorHandling.printError("Error: The left expression should be an integer");
         return false;
      }
      
      // Visit the right expression and check if it is IntegerType
      res = visit(ctx.expression(0));
      Type rightType = ctx.expression(0).eType;
      if (!rightType.conformsTo(integerType)) {
         ErrorHandling.printError("Error: The right expression should be an integer");
         return false;
      }

      // Define the expression type as BooleanType: tx.eType = new BooleanType();
      ctx.eType = new BooleanType();

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
      // identifier : ID | ID('.' ID)+;
      Boolean res = true;
      String id = ctx.identifier().getText();
      if (ctx.identifier().ID(1) == null) {
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
         ErrorHandling.printError("TO BE IMPLEMENTED ID ('.' ID)+ - attributes"); // TODO
      }
      
      return res;
   }

   // --------- End Visit Expression ---------

   @Override
   public Boolean visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
      // 'refresh' ID ('after' expression suffix=('ms'|'s'))? ';'    and     Expression returns [Type eType, String varName]
      Boolean res = true;
      String id = ctx.ID().getText();
      
      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
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
      // 'close' ID ';' #CommandClose
      Boolean res = true;
      String id = ctx.ID().getText();
      
      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
         res = false;
      } 

      return res;
   }

   // @Override
   // public Boolean visitCommandMove(AGLParser.CommandMoveContext ctx) {
   //    // 'move' ID 'by' expression ';' #CommandMove
   //    Boolean res = true;
   //    String id = ctx.ID().getText();

   //    if (!AGLParser.symbolTable.containsKey(id)) {
   //       ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
   //       res = false;
   //    }

   //    res = visit(ctx.expression());
   //    if (!res) {
   //       ErrorHandling.printError("Error: invalid expression in move command");
   //       return false;
   //    }

   //    if (!ctx.expression().eType.conformsTo(pointType)) {
   //       ErrorHandling.printError("Error: invalid expression type in move command (must be a point!)");
   //       return false;
   //    }

   //    return res;
      
   // }
   
   @Override
   public Boolean visitCommandMove(AGLParser.CommandMoveContext ctx) {
      // 'move' identifier type=('by'|'to') expression ';' #CommandMove
      Boolean res = true;
      String id = ctx.identifier().getText();
      
      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
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

      // second expression can not be less than the first expression
      if ( ! (ctx.number_range().expression(0).eType instanceof IntegerType && ctx.number_range().expression(1).eType instanceof IntegerType ))  {
         ErrorHandling.printError("Error: invalid expression type in for statement (must be integer!)");
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
      System.out.println("Expression type: " + exprType.name());
      if (!(exprType instanceof BooleanType)) {
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
      System.out.println("Check repeat statement");

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

   // @Override
   // public Boolean visitWithStatement(AGLParser.WithStatementContext ctx) {
   //    Boolean res = true;
   //    String id = ctx.identifier().getText();
   //    System.out.println("Check with statement");

   //    if (!AGLParser.symbolTable.containsKey(id)) {
   //       ErrorHandling.printError("Error: identifier \"" + id + "\" is not defined");
   //       return false;
   //    }

   //    Type idType = ctx.identifier().eType;
   //    if (!(idType.conformsTo(ObjectType))) {
   //       ErrorHandling.printError("Error: identifier \"" + id + "\" is not an object type");
   //       return false;
   //    }

   //    res = visit(ctx.propertiesAssignment());
   //    if (!res) {
   //       ErrorHandling.printError("Error: invalid assignment in with statement");
   //       return false;
   //    }

   //    return res;
   // }

   // @Override
   // public Boolean visitTypeID(AGLParser.TypeIDContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // -- Correct --
   private Boolean checkNumericType(Type t) {
      Boolean res = true;

      if (!t.isNumeric()) {
         ErrorHandling.printError("Numeric operator applied to a non-numeric operand!");
         res = false;
      }
      return res;
   }

   private Type fetchType(Type t1, Type t2) {
      Type res = null;
      if (t1.isNumeric() && t2.isNumeric()) {
         if ("real".equals(t1.name()))
            res = t1;
         else if ("real".equals(t2.name()))
            res = t2;
         else
            res = t1;
      } else if ("boolean".equals(t1.name()) && "boolean".equals(t2.name()))
         res = t1;
      return res;
   }

   private boolean integerOperator(String op) {
      return "//".equals(op) || "\\\\".equals(op);
   }
}
