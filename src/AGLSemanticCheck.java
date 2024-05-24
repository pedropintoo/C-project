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
      return visitChildren(ctx);
   }

   // @Override
   // public Boolean visitStatBlockStatement(AGLParser.StatBlockStatementContext
   // ctx) {
   // Boolean res = true;
   // System.out.println("visitStatBlockStatement");
   // return visitChildren(ctx);
   // // return res;
   // }

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
      
      if (res == false) {
         // HandlingError.printError(ctx, "Error: invalid simple statement");
         System.out.println("Error: invalid simple statement");
         return false;
      }

      // if (ctx.assignment() != null) {
      //    if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
      //       // ErrorHandling.printError(ctx, "Expression type does not conform to variable \""+id+"\" type!");
      //       System.out.println("Expression type does not conform to variable type!");
      //       res = false;
      //    } else {
      //       System.out.println("sym.setValueDefined()"); // TODO: ??
      //    }
      // }

      
      return res;
   }

   // @Override
   // public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

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

   // @Override
   // public Boolean visitExprWait(AGLParser.ExprWaitContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   @Override
   public Boolean visitExprString(AGLParser.ExprStringContext ctx) {
      ctx.eType = stringType;
      return true;
   }

   @Override
   public Boolean visitExprPoint(AGLParser.ExprPointContext ctx) {
      ctx.eType = pointType;
      return true;
   }

   @Override
   public Boolean visitExprUnary(AGLParser.ExprUnaryContext ctx) {
      Boolean res = visit(ctx.e) && checkNumericType(ctx, ctx.e.eType);
      if (res)
         ctx.eType = ctx.e.eType;
      return res;
   }

   @Override
   public Boolean visitExprNumber(AGLParser.ExprNumberContext ctx) {
      ctx.eType = numberType;
      return true;
   }

   @Override
   public Boolean visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      Boolean res = visit(ctx.e);
      if (res)
         ctx.eType = ctx.e.eType;
      return res;
   }

   // @Override
   // public Boolean visitExprID(AGLParser.ExprIDContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   // @Override
   // public Boolean visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx)
   // {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

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
   //    Boolean res = null;
   //    return visitChildren(ctx);
   //    // return res;
   // }

   // @Override
   // public Boolean visitWithStatement(AGLParser.WithStatementContext ctx) {
   //    Boolean res = null;
   //    return visitChildren(ctx);
   //    // return res;
   // }

   // @Override
   // public Boolean visitTypeID(AGLParser.TypeIDContext ctx) {
   //    Boolean res = null;
   //    return visitChildren(ctx);
   //    // return res;
   // }

   private Boolean checkNumericType(ParserRuleContext ctx, Type t)
   {
      Boolean res = true;
      if (!t.isNumeric())
      {
         // ErrorHandling.printError(ctx, "Numeric operator applied to a non-numeric operand!");
         System.out.println("Numeric operator applied to a non-numeric operand!");
         res = false;
      }
      return res;
   }
}
