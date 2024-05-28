import org.antlr.v4.runtime.ParserRuleContext;


@SuppressWarnings("CheckReturnValue")
public class AGLSemanticCheck extends AGLParserBaseVisitor<Boolean> {

   private final IntegerType integerType = new IntegerType();
   private final StringType stringType = new StringType();
   private final NumberType numberType = new NumberType();
   private final PointType pointType = new PointType();
   private final VectorType vectorType = new VectorType();

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
   public Boolean visitStatForLoop(AGLParser.StatForLoopContext ctx) {
      // stat: for_loop;
      Boolean res = true;
      res = visit(ctx.for_loop());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid for loop");
      }
      return res;
   }

   @Override
   public Boolean visitStatWithStatement(AGLParser.StatWithStatementContext ctx)
   {
      // stat: withStatement;
      Boolean res = true;
      res = visit(ctx.withStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid with statement");
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

   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      // simpleStatement: typeID (assignment)?     and      simpleStatement returns [String varName]      and typeID returns[Type res]
      String type = ctx.typeID().getText();
      Type typeObject = ctx.typeID().res;

      if (ctx.assignment() != null) {
         Boolean res = visit(ctx.assignment().expression());
         if (!res) {
            ErrorHandling.printError("Error: invalid simple statement");
            return false;
         }

         if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
            ErrorHandling.printError("Expression type does not conform to variable type!");
            return false;
         } 
      }

      return true;
   }

   @Override
   public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
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

      String id1 = ctx.ID(0).getText();

      if (!AGLParser.symbolTable.containsKey(id1)) {
         ErrorHandling.printError("Variable \"" + id1 + "\" does not exist!");
         return false;
      }

      // if attribute exists
      String atr = null;
      if (ctx.ID(1) != null) {
         atr = ctx.ID(1).getText();
      }

      Boolean res = visit(ctx.assignment());
      if (res) {
         Symbol sym = AGLParser.symbolTable.get(id1); // TODO: with attribute!!!
         if (!ctx.assignment().eType.conformsTo(sym.type())) {
            ErrorHandling.printError("Expression type does not conform to variable type!");
            return false;
         } else {
            sym.setValueDefined();
         }
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
      // expression: sign=('+'|'-') e=expression     and     expression returns[Type eType]
      Boolean signal = ctx.sign.getText().equals("+") || ctx.sign.getText().equals("-");

      if (!signal) {
         ErrorHandling.printError(ctx, "Invalid unary operator!");
         return false;
      }

      Boolean res = visit(ctx.e);
      if (res && ctx.e.eType != null && checkNumericType(ctx, ctx.e.eType)) {
         ctx.eType = ctx.e.eType;
      } else {
         ErrorHandling.printError("Error: invalid unary expression or undefined type!");
         res = false;
      }
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
            ErrorHandling.printError(ctx, "The integer operator "+ctx.op.getText()+"requires integer operands!");
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
         ErrorHandling.printError(ctx, "Point creation requires numeric operands!");
      }
      return res;
   }


   @Override
   public Boolean visitExprNumber(AGLParser.ExprNumberContext ctx) {
      // expression: number=(INT | FLOAT)     and     expression returns[Type eType]
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
      // expression: ID     and     expression returns[Type eType]
      Boolean res = true;
      String id = ctx.ID().getText();
      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
         res = false;
      } else {
         Symbol sym = AGLParser.symbolTable.get(id);
         if (!sym.valueDefined()) {
            ErrorHandling.printError(ctx, "Variable \""+id+"\" not defined!");
            res = false;
         } else {
            ctx.eType = sym.type();
         }
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
