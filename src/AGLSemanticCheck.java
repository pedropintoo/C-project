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
   
   // ------ Start visit stat ------

   @Override
   public Boolean visitStatInstantiation(AGLParser.StatInstantiationContext ctx) {
      // stat: instantiation;
      Boolean res = true;
      System.out.println("visitStatInstantiation");
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
      System.out.println("visitStatBlockStatement");
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
      System.out.println("visitStatLongAssignment");
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
      System.out.println("visitStatCommand");
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
      System.out.println("visitStatForLoop");
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
      System.out.println("visitStatWithStatement");
      res = visit(ctx.withStatement());
      if (!res) {
         ErrorHandling.printError(ctx, "Error: invalid with statement");
      }
      return res;
   }

   // ------ End visit stat ------

   @Override
   public Boolean visitInstantiation(AGLParser.InstantiationContext ctx) {
      // instantiation: ID ':' (simpleStatement | blockStatement);
      Boolean res = true;
      String ID = ctx.ID().getText();
      System.out.println("visitInstantiation: " + ID);

      if (AGLParser.symbolTable.containsKey(ID)) {
         ErrorHandling.printError(ctx, "Variable \"" + ID + "\" already declared!");
         System.out.println("Variable \"" + ID + "\" already declared!");
         res = false;
      } else {
         System.out.println("Variable \"" + ID + "\" not declared yet!");
         if (ctx.simpleStatement() != null) {
            System.out.println("-- visitInstantiation: simpleStatement");
            res = visit(ctx.simpleStatement());
            if (res) {
               AGLParser.symbolTable.put(ID, new VariableSymbol(ID, ctx.simpleStatement().typeID().res));
               System.out.println("Added " + ID + " to symbol table with type " + ctx.simpleStatement().typeID().res.name());
            } else {
               ErrorHandling.printError(ctx, "Error: invalid instantiation");
            }

         } else if (ctx.blockStatement() != null) {
            System.out.println("-- visitInstantiation: blockStatement");
            res = visit(ctx.blockStatement());
            if (res) {
               AGLParser.symbolTable.put(ID, new VariableSymbol(ID, ctx.blockStatement().typeID().res));
               System.out.println("Added " + ID + " to symbol table with type " + ctx.blockStatement().typeID().res.name());
            } else {
               ErrorHandling.printError("Error: invalid block statement instantiation");
            }
         } else {
            ErrorHandling.printError(ctx, "Error: invalid instantiation");
            res = false;
         }
      }

      return res;
   }

   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      // simpleStatement: typeID (assignment)?     and      simpleStatement returns [String varName]      and typeID returns[Type res]
      String type = ctx.typeID().getText();
      Type typeObject = ctx.typeID().res;

      System.out.println("visitSimpleStatement: " + type);

      if (ctx.assignment() != null) {
         Boolean res = visit(ctx.assignment().expression());
         if (!res) {
            System.out.println("Error: invalid simple statement");
            return false;
         }
         if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
            System.out.println("Expression type does not conform to variable type!");
            return false;
         }
      }



      // if (ctx.assignment() != null) {
      // if (!ctx.assignment().expression().eType.conformsTo(typeObject)) {
      // ErrorHandling.printError(ctx, "Expression type does not conform to
      // variable \""+id+"\" type!");
      // res = false;
      // } else {
      // System.out.println("sym.setValueDefined()"); // TODO: ??
      // }
      // }

      return true;
   }

   @Override
   public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      Boolean res = true;
      System.out.println("visitBlockStatement");

      String ID = ctx.typeID().getText();
      System.out.println("visitBlockStatement: " + ID);

      // Verificar se o tipo é válido
      if (!ID.equals("Line") && !ID.equals("Rectangle") && !ID.equals("Ellipse") &&
            !ID.equals("Arc") && !ID.equals("ArcChord") && !ID.equals("PiesSlice") &&
            !ID.equals("Text") && !ID.equals("Dot")) {
         // ErrorHandling.printError(ctx, "Error: invalid block statement");
         System.out.println("Error: invalid block statement");
         return false;
      }

      System.out.println("visitBlockStatement: " + ctx.expression().getText());

      // if (ctx.expression() != null) {
      //    res = visit(ctx.expression());
      //    if (!res) {
      //       System.out.println("Error: invalid block statement");
      //       return false;
      //    }
      // }

      res = visit(ctx.propertiesAssignment());
      if (!res) {
         System.out.println("Error: invalid properties assignment in block statement");
      }

      System.out.println("visitBlockStatement: Success");

      return res;
   }

   @Override
   public Boolean
   visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
   System.out.println("visitPropertiesAssignment");
   Boolean res = null;
   return visitChildren(ctx);
   // return res;
   }

   @Override
   public Boolean visitLongAssignment(AGLParser.LongAssignmentContext ctx) {
      
      System.out.println("--- visitLongAssignment");

      // Consultar primeiro ID
      String id1 = ctx.ID(0).getText();
      System.out.println("visitLongAssignment: " + id1);

      // Se houver um segundo ID
      String id2 = null;
      if (ctx.ID(1) != null) {
         id2 = ctx.ID(1).getText();
         System.out.println("visitLongAssignment: second ID " + id2);
      }

      Boolean res = visit(ctx.assignment());
      
      if (res) {
         if (!AGLParser.symbolTable.containsKey(id1)) {
               System.out.println("Variable \"" + id1 + "\" does not exist!");
               return false;
         }
         Symbol sym = AGLParser.symbolTable.get(id1);
         if (!ctx.assignment().expression().eType.conformsTo(sym.type())) {
               System.out.println("Expression type does not conform to variable type!");
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
      System.out.println("visitAssignment");
    
      Boolean res = visit(ctx.expression());
  
      if (res) {
         String exprText = ctx.expression().getText();
         System.out.println("visitAssignment: Expression = " + exprText);
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
      System.out.println("-- visitExprUnary: " + signal);

      if (!signal) {
         ErrorHandling.printError(ctx, "Invalid unary operator!");
         return false;
      }

      Boolean res = visit(ctx.e);
      if (res && ctx.e.eType != null && checkNumericType(ctx, ctx.e.eType)) {
         ctx.eType = ctx.e.eType;
         System.out.println("visitExprUnary: " + ctx.eType.name());
      } else {
         System.out.println("Error: invalid unary expression or undefined type!");
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
      // expression: number=(INT | FLOAT)     and     expression returns[Type eType]
      System.out.println("-- visitExprNumber " + ctx.getText() );
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
      // expression: ID     and     expression returns[Type eType]
      Boolean res = true;
      String id = ctx.ID().getText();
      System.out.println("visitExprID: " + id);
      if (!AGLParser.symbolTable.containsKey(id)) {
         ErrorHandling.printError(ctx, "Variable \""+id+"\" does not exists!");
         res = false;
      } else {
         Symbol sym = AGLParser.symbolTable.get(id);
         System.out.println("Type: " + sym.type().name()); // está a imprimir correto: "Integer"
         System.out.println("sym.valueDefined() -> " + sym.valueDefined()); // está a imprimir incorreto: "false"
         if (!sym.valueDefined()) {
            ErrorHandling.printError(ctx, "Variable \""+id+"\" not defined!");
            res = false;
         } else
            System.out.println("sym.type() -> " + sym.type().name());
            ctx.eType = sym.type();
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
