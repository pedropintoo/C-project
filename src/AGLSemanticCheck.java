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

      if (ctx.simpleStatement() != null) {
         // Add the variable to the symbol table AgLParser.symbolTable static protected Map<String, Type> symbolTable = new HashMap<>();
         AGLParser.symbolTable.put(ID, new VariableSymbol(ID, Type.getType(ctx.simpleStatement().typeID().getText()) ));

   
         res = visit(ctx.simpleStatement());
      } else if (ctx.blockStatement() != null) {
         res = visit(ctx.blockStatement());
      } else {
         // HandlingError.printError(ctx, "Error: invalid instantiation");
         System.out.println("Error: invalid instantiation");
         res = false;
      }

      return res;
   }


   // 

   // public Boolean visitDeclaration(CalcParser.DeclarationContext ctx) {
   //    Boolean res = true;
   //    //visit(ctx.type());
   //    for(TerminalNode t: ctx.idList().ID())
   //    {
   //       String id = t.getText();
   //       //out.println(t.getText());

   //       if (CalcParser.symbolTable.containsKey(id))
   //       {
   //          ErrorHandling.printError(ctx, "Variable \""+id+"\" already declared!");
   //          res = false;
   //       }
   //       else
   //          CalcParser.symbolTable.put(id, new VariableSymbol(id, ctx.type().res));
   //    }
   //    return res;

   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      Boolean res = true;
      String type = ctx.typeID().getText();
      System.out.println("olá! " + type);

      if (type == null) {
         // HandlingError.printError(ctx, "Error: invalid type");
         System.out.println("Error: invalid type");
         res = false;
      } else {

         // Call Type.java method getType(String name) to check if String is a valid type
         // and return the corresponding Type object
         Type typeObject = Type.getType(type);

         if (typeObject == null) {
            System.out.println("Error: invalid type");
            res = false;
         } else {
            // Check if the type is a valid type
            if (typeObject instanceof StringType) {
               System.out.println("String");
            } else if (typeObject instanceof IntegerType) {
               System.out.println("Integer");
            } else if (typeObject instanceof NumberType) {
               System.out.println("Number");
            } else if (typeObject instanceof PointType) {
               System.out.println("Point");
            } else if (typeObject instanceof VectorType) {
               System.out.println("Vector");
            } else {
               System.out.println("Error: invalid type");
               res = false;
            }
         }

         if (ctx.assignment() != null) {
            res = visit(ctx.assignment());
            System.out.println("visit assignment");
         }
      }

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
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   // @Override
   // public Boolean visitExprPoint(AGLParser.ExprPointContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

   @Override
   public Boolean visitExprUnary(AGLParser.ExprUnaryContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitExprNumber(AGLParser.ExprNumberContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   // @Override
   // public Boolean visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
   // Boolean res = null;
   // return visitChildren(ctx);
   // // return res;
   // }

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

   @Override
   public Boolean visitFor_loop(AGLParser.For_loopContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitWithStatement(AGLParser.WithStatementContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitTypeID(AGLParser.TypeIDContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }
}
