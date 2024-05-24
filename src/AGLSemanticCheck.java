import org.antlr.v4.runtime.ParserRuleContext;

@SuppressWarnings("CheckReturnValue")
public class AGLSemanticCheck extends AGLParserBaseVisitor<Boolean> {

   private final IntegerType integerType = new IntegerType();
   private final StringType stringType = new StringType();
   private final NumberType numberType = new NumberType();
   private final PointType pointType = new PointType();
   private final VectorType vectorType = new VectorType();
   
   // @Override
   // public Boolean visitProgram(AGLParser.ProgramContext ctx) {
   // Boolean res = true;

   // for (AGLParser.StatContext stat : ctx.stat()) {
   // res = visit(stat);
   // if (!res || res == null) {
   // return false;
   // }
   // }
   // return true;
   // }

   @Override
   public Boolean visitStatInstantiation(AGLParser.StatInstantiationContext ctx) {
      Boolean res = true;
      System.out.println("visitStatInstantiation");

      res = visit(ctx.instantiation());
      if (res == false) {
         // HandlingError.printError(ctx, "Error: invalid instantiation");
         System.out.println("Error: invalid instantiation");
      }

      return res;
   }

   @Override
   public Boolean visitStatBlockStatement(AGLParser.StatBlockStatementContext ctx) {
      Boolean res = true;
      System.out.println("visitStatBlockStatement");

      res = visit(ctx.blockStatement());
      if (res == false) {
         // HandlingError.printError(ctx, "Error: invalid block statement");
         System.out.println("Error: invalid block statement");
      }

      return res;
   }

   // @Override
   // public Boolean visitStatLongAssignment(AGLParser.StatLongAssignmentContext
   // ctx) {
   // Boolean res = true;
   // System.out.println("visitStatLongAssignment");
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitStatCommand(AGLParser.StatCommandContext ctx) {
   // Boolean res = true;
   // System.out.println("visitStatCommand");
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitStatForLoop(AGLParser.StatForLoopContext ctx) {
   // Boolean res = true;
   // System.out.println("visitStatForLoop");
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitStatWithStatement(AGLParser.StatWithStatementContext ctx)
   // {
   // Boolean res = true;
   // System.out.println("visitStatWithStatement");
   // return visitChildren(ctx);
   // // return res;
   // }

   @Override
   public Boolean visitInstantiation(AGLParser.InstantiationContext ctx) {
      Boolean res = true;
      String ID = ctx.ID().getText();
      System.out.println("visitInstantiation: " + ID);

      if (AGLParser.symbolTable.containsKey(ID)) {
         // HandlingError.printError(ctx, "Variable \"" + ID + "\" already declared!");
         System.out.println("Variable \"" + ID + "\" already declared!");
         res = false;
      } else {
         if (ctx.simpleStatement() != null) {
            res = visit(ctx.simpleStatement());
            if (res == true) {
               AGLParser.symbolTable.put(ID, new VariableSymbol(ID, ctx.simpleStatement().typeID().res));
            } else {
               // HandlingError.printError(ctx, "Error: invalid instantiation");
               System.out.println("Error: invalid instantiation");
            }

         } else if (ctx.blockStatement() != null) {
            res = visit(ctx.blockStatement());
         } else {
            // HandlingError.printError(ctx, "Error: invalid instantiation");
            System.out.println("Error: invalid instantiation");
            res = false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      // simpleStatement: typeID (assignment)?;
      Boolean res = visit(ctx.assignment().expression());
      String type = ctx.typeID().getText();
      Type typeObject = ctx.typeID().res;

      System.out.println("visitSimpleStatement: " + type + " " + typeObject.name());

      if (res == false) {
         // HandlingError.printError(ctx, "Error: invalid simple statement");
         System.out.println("Error: invalid simple statement");
         return false;
      }

      // if (ctx.assignment() != null) {
      // if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
      // ErrorHandling.printError(ctx, "Expression type does not conform to
      // variable \""+id+"\" type!");
      // System.out.println("Expression type does not conform to variable type!");
      // res = false;
      // } else {
      // System.out.println("ola");
      // }
      // }

      System.out.println("ola" + ctx.assignment().getText());

      // if (ctx.assignment() != null) {
      // if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
      // // ErrorHandling.printError(ctx, "Expression type does not conform to
      // variable \""+id+"\" type!");
      // System.out.println("Expression type does not conform to variable type!");
      // res = false;
      // } else {
      // System.out.println("sym.setValueDefined()"); // TODO: ??
      // }
      // }

      return res;
   }

   @Override
   public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      Boolean res = true;
      System.out.println("visitBlockStatement");

      String ID = ctx.typeID().getText();
      System.out.println("visitBlockStatement: " + ID);

      // Quais são os tipos possíveis de statement? Fazer aqui condições para
      // verificar se o tipo é válido

      if (ID == null) {
         // HandlingError.printError(ctx, "Error: invalid block statement");
         System.out.println("Error: invalid block statement");
         return false;
      }

      return res;
   }

   // @Override
   // public Boolean
   // visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitLongAssignment(AGLParser.LongAssignmentContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitAssignment(AGLParser.AssignmentContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitPoint(AGLParser.PointContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // ------ Visit Expression ------

   @Override
   public Boolean visitExprUnary(AGLParser.ExprUnaryContext ctx) {
      Boolean signal = ctx.sign.getText().equals("+") || ctx.sign.getText().equals("-");
      System.out.println("visitExprUnary: " + signal);

      if (!signal) {
         // ErrorHandling.printError(ctx, "Invalid unary operator!");
         System.out.println("Invalid unary operator!");
         return false;
      }

      Boolean res = visit(ctx.e) && checkNumericType(ctx, ctx.e.eType);
      if (res)
         ctx.eType = ctx.e.eType;
      System.out.println("visitExprUnary: " + ctx.eType.name());
      return res;
   }

   @Override
   public Boolean visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      Boolean res = visit(ctx.e);
      if (res)
         ctx.eType = ctx.e.eType;
      return res;
   }

   // @Override
   public Boolean visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
      Boolean res = visit(ctx.e1) && checkNumericType(ctx, ctx.e1.eType) &&
            visit(ctx.e2) && checkNumericType(ctx, ctx.e2.eType);
      if (res) {
         ctx.eType = fetchType(ctx.e1.eType, ctx.e2.eType);
         if (integerOperator(ctx.op.getText()) && !"integer".equals(ctx.eType.name())) {
            // ErrorHandling.printError(ctx, "The integer operator "+ctx.op.getText()+"
            // requires integer operands!");
            System.out.println("The integer operator " + ctx.op.getText() + " requires integer operands!");
            res = false;
         }
      }
      return res;
   }

   @Override
   public Boolean visitExprPoint(AGLParser.ExprPointContext ctx) {
      Boolean res = visit(ctx.x) && checkNumericType(ctx, ctx.x.eType) &&
            visit(ctx.y) && checkNumericType(ctx, ctx.y.eType);
      if (res) {
         ctx.eType = new PointType(); // Definindo o tipo da expressão como Point
      } else {
         // ErrorHandling.printError(ctx, "Point creation requires numeric operands!");
         System.out.println("Point creation requires numeric operands!");
      }
      return res;
   }

   /////////////////////////////// não deveria haver uma expressão de vetor??????

   // @Override
   // public Boolean visitExprVector(AGLParser.ExprVectorContext ctx) {
   // Boolean res = visit(ctx.x) && checkNumericType(ctx, ctx.x.eType) &&
   // visit(ctx.y) && checkNumericType(ctx, ctx.y.eType);
   // if (res) {
   // ctx.eType = new VectorType(); // Definindo o tipo da expressão como Vector
   // } else {
   // // ErrorHandling.printError(ctx, "Vector creation requires numeric
   // operands!");
   // System.out.println("Vector creation requires numeric operands!");
   // }
   // return res;
   // }

   ///////////////////////////////

   @Override
   public Boolean visitExprNumber(AGLParser.ExprNumberContext ctx) {
      if (ctx.INT() != null) {
         ctx.eType = integerType;
      } else if (ctx.FLOAT() != null) {
         ctx.eType = numberType;
      } else {
         // Caso inesperado, pode ser necessário tratar isso adequadamente
         System.out.println("Unexpected number type");
         return false;
      }
      return true;
   }

   @Override
   public Boolean visitExprString(AGLParser.ExprStringContext ctx) {
      ctx.eType = stringType;
      if (ctx.STRING() == null) {
         // Caso inesperado, pode ser necessário tratar isso adequadamente
         System.out.println("Unexpected string type");
         return false;
      }
      return true;
   }

   @Override
   public Boolean visitExprID(AGLParser.ExprIDContext ctx) {
      Boolean res = true;
      String id = ctx.ID().getText();
      if (!AGLParser.symbolTable.containsKey(id)) {
         // ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
         System.out.println("Variable \"" + id + "\" does not exists!");
         res = false;
      } else {
         Symbol sym = AGLParser.symbolTable.get(id);
         if (!sym.valueDefined()) {
            // ErrorHandling.printError(ctx, "Variable \""+id+"\" not defined!");
            System.out.println("Variable \"" + id + "\" not defined!");
            res = false;
         } else
            ctx.eType = sym.type();
      }
      return res;
   }

   @Override
   public Boolean visitExprWait(AGLParser.ExprWaitContext ctx) {
      Boolean res = visit(ctx.eventTrigger());
      if (res) {
         ctx.eType = stringType; // TODO: ????
      }
      return res;

   }

   // --------- End Visit Expression ---------

   // @Override
   // public Boolean visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitCommandPrint(AGLParser.CommandPrintContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitCommandClose(AGLParser.CommandCloseContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitCommandMove(AGLParser.CommandMoveContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitEventTrigger(AGLParser.EventTriggerContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitMouseTrigger(AGLParser.MouseTriggerContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitFor_loop(AGLParser.For_loopContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitWithStatement(AGLParser.WithStatementContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitTypeID(AGLParser.TypeIDContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // -- Correct --
   private Boolean checkNumericType(ParserRuleContext ctx, Type t) {
      Boolean res = true;
      if (!t.isNumeric()) {
         // ErrorHandling.printError(ctx, "Numeric operator applied to a non-numeric
         // operand!");
         System.out.println("Numeric operator applied to a non-numeric operand!");
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
