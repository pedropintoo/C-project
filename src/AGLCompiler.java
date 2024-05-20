/*
   File: AGL Generator to Python
   */

import org.stringtemplate.v4.*;

import .antlr.AGLParser;

import org.antlr.v4.runtime.ParserRuleContext;

@SuppressWarnings("CheckReturnValue")
public class AGLCompiler extends AGLParserBaseVisitor<ST> {
   

   private STGroup templates = new STGroupFile("AGL_python.stg");

   private int varCounter = 0;

   private String newVarName() {
      return "v" + varCounter++;
   }

   private ST binaryExpression(String e1Stats, String e2Stats, String var, String e1Var, String op, String e2Var) {
      ST res = templates.getInstanceOf("binaryExpression");
      res.add("stat", e1Stats);
      res.add("stat", e2Stats);
      res.add("var", var);
      res.add("e1", (op=="," ? "(" : "")+e1Var);
      res.add("op", op);
      res.add("e2", e2Var+(op=="," ? ")" : ""));
      return res;
   }


/*
   Compiler visitor methods
   */

//% program
   @Override public ST visitProgram(AGLParser.ProgramContext ctx) {
      ST res = templates.getInstanceOf("module");
      
      // iterate all stat*
      for (AGLParser.StatContext stat : ctx.stat()){
         ST statRes = visit(stat);
         res.add("stat", statRes).render(); // render the return value!
      }

      return res;
   }


//% stat
   @Override public ST visitStatInstantiation(AGLParser.StatInstantiationContext ctx) {
      return visit(ctx.instantiation());
   }

   @Override public ST visitStatBlockStatement(AGLParser.StatBlockStatementContext ctx) {
      return visit(ctx.blockStatement());
   }

   @Override public ST visitStatLongAssignment(AGLParser.StatLongAssignmentContext ctx) {
      return visit(ctx.longAssignment());
   }

   @Override public ST visitStatCommand(AGLParser.StatCommandContext ctx) {
      return visit(ctx.command());
   }

   @Override public ST visitStatForLoop(AGLParser.StatForLoopContext ctx) {
      return null; // TODO: TO_BE_IMPLEMENTED
   }

   @Override public ST visitStatWithStatement(AGLParser.StatWithStatementContext ctx) {
      return null; // TODO: TO_BE_IMPLEMENTED
   }


//% instantiation
   @Override public ST visitInstantiation(AGLParser.InstantiationContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      String id = ctx.ID().getText();

      ST stat = null;
      String value;
      if (ctx.simpleStatement() != null) {
         stat = visit(ctx.simpleStatement());
         value = ctx.simpleStatement().varName;
      } else {
         stat = visit(ctx.blockStatement());
         value = ctx.blockStatement().varName;
      }

      res.add("stat", stat.render()); // render the return value!
      res.add("var", id);
      if (value != null) {
         res.add("value", value); // blockStatement can be uninitialized
      }
      

      return res;
   }


//* simpleStatement
   @Override public ST visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      String value;
      if (ctx.assignment() != null) {
         res.add("stat", visit(ctx.assignment()).render()); // render the return value!
         value = ctx.assignment().varName;
      } else { 
         value = "DEFAULT_VALUE";  // TODO: TO_BE_IMPLEMENTED
      } 

      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);
      res.add("value", value);   // assign the value to current variable

      return res;
   }

   
//* blockStatement
   @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      ST res = templates.getInstanceOf("canvas");
      
      // TODO: generalize this ( for now, we only have View )

      ST view_title = templates.getInstanceOf("view_title");
      ST view_properties = templates.getInstanceOf("view_properties");
      for (AGLParser.LongAssignmentContext longAssign: ctx.propertiesAssignment().longAssignment()) {
         ST assign = templates.getInstanceOf("assign");
         assign.add("stat", visit(longAssign.assignment()).render()); // render the return value!
         
         String id = newVarName();

         assign.add("var", id);
         assign.add("value", longAssign.assignment().varName);
         
         res.add("stat", assign.render()); // render the return value!

         if (longAssign.ID(0).getText().equals("title")) {
            view_title.add("title", id);
         } else {
            String field = longAssign.ID(0).getText();
            if (field.equals("background")) {
               field = "bg";
            }
            view_properties.add("field", field + "=" + id);
         }
      }

      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);
      res.add("view_title", view_title.render());
      res.add("view_properties", view_properties.render());

      return res;

   }

//* longAssignment
   @Override public ST visitLongAssignment(AGLParser.LongAssignmentContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      // TODO: generalizate to attributes!
      res.add("stat", visit(ctx.assignment()).render()); // render the return value!
      
      res.add("var", ctx.ID(0));
      res.add("value", ctx.assignment().varName); // render the return value!

      return res;
   }

   
//* assignment   
   @Override public ST visitAssignment(AGLParser.AssignmentContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      res.add("stat", visit(ctx.expression()).render()); // render the return value!
      
      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);
      res.add("value", ctx.expression().varName); // assign the value to current variable

      return res;
   }


//* expression  
   @Override public ST visitExprUnary(AGLParser.ExprUnaryContext ctx) {
      ST res = templates.getInstanceOf("unaryExpression");

      res.add("stat", visit(ctx.expression()).render()); // render the return value!
      
      String id = newVarName();
      ctx.varName = id;
      // id = op=('+' | '-') e1
      res.add("var", id);
      res.add("op", ctx.sign.getText()); // ('+' | '-')
      res.add("e1", ctx.expression().varName); // render the return value!
      
      return res;
   }

   @Override public ST visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      ST res = visit(ctx.expression());
      ctx.varName = ctx.expression().varName;
      return res;
   }

   @Override public ST visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
      ctx.varName = newVarName();
      return binaryExpression(visit(ctx.expression(0)).render(), visit(ctx.expression(1)).render(), ctx.varName, ctx.expression(0).varName, ctx.op.getText(), ctx.expression(1).varName);
   }

   @Override public ST visitExprPoint(AGLParser.ExprPointContext ctx) {
      ctx.varName = newVarName();
      return binaryExpression(visit(ctx.x).render(), visit(ctx.y).render(), ctx.varName, ctx.x.varName, ",", ctx.y.varName);
   }

   @Override public ST visitExprNumber(AGLParser.ExprNumberContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);
      res.add("value", ctx.number.getText()); // assign the value to current variable

      return res;
   }

   @Override public ST visitExprString(AGLParser.ExprStringContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);
      res.add("value", ctx.STRING().getText()); // assign the value to current variable

      return res;
   }

   @Override public ST visitExprID(AGLParser.ExprIDContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);
      res.add("value", ctx.ID().getText()); // assign the value to current variable

      return res;
   }

   @Override public ST visitExprWait(AGLParser.ExprWaitContext ctx) {
      ST res = templates.getInstanceOf("waitMouseClick");
      
      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);

      return res;
   }


//* command   
   @Override public ST visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
      ST res = templates.getInstanceOf("refresh");

      res.add("view", ctx.ID().getText());

      if (ctx.expression() != null) {
         res.add("stat", visit(ctx.expression()).render()); // render the return value!
         res.add("delay", ctx.expression().varName + (ctx.suffix.getText().equals("ms")? "/1000": ""));
      }

      return res;
   }

   @Override public ST visitCommandPrint(AGLParser.CommandPrintContext ctx) {
      ST res = templates.getInstanceOf("print");
      
      res.add("stat", visit(ctx.expression()).render()); // render the return value!
      res.add("output", ctx.expression().varName);
      
      return res;
   }

   @Override public ST visitCommandClose(AGLParser.CommandCloseContext ctx) {
      return null; // TODO: why ?
   }

   @Override public ST visitCommandMove(AGLParser.CommandMoveContext ctx) {
      return null; // TODO: TO_BE_IMPLEMENTED
   }


//* for_loop   
   @Override public ST visitFor_loop(AGLParser.For_loopContext ctx) {
         return null;
      }

 
//* withStatement   
   @Override public ST visitWithStatement(AGLParser.WithStatementContext ctx) {
      return null; // TODO: TO_BE_IMPLEMENTED
   }      

}
