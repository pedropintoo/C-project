/*
   File: AGL Generator to Python
   */

import org.stringtemplate.v4.*;


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
      return visit(ctx.for_loop());
   }

   @Override public ST visitStatWithStatement(AGLParser.StatWithStatementContext ctx) {
      return visit(ctx.withStatement());
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
      ST res = null;

      res = templates.getInstanceOf("model");
      res.add("type", ctx.typeID().getText());
      // (at expression)?
      if (ctx.expression() != null) {
         // define the origin
         res.add("stat", visit(ctx.expression()).render()); // render the return value!
         res.add("origin", ctx.expression().varName);
      }

      String id = newVarName();
      ctx.varName = id;

      res.add("var", id);

      //ST properties = templates.getInstanceOf("properties");
      
      for (AGLParser.LongAssignmentContext longAssign: ctx.propertiesAssignment().longAssignment()) {
         ST properties2 = templates.getInstanceOf("properties2");
         //////////////////////////////////////////////////////////////
         // assign the properties
         ST assign = templates.getInstanceOf("assign");
         assign.add("stat", visit(longAssign.assignment()).render()); // render the return value!
         id = newVarName();
         assign.add("var", id);
         assign.add("value", longAssign.assignment().varName);
         //////////////////////////////////////////////////////////////
         
         res.add("stat", assign.render()); // render the return value!
         res.add("field", ctx.varName+"."+longAssign.ID(0).getText() + " = " + id);
         //res.add("properties2", properties2.render());
      }
       // render the return value!

      
      
      return res;

   }

//* longAssignment
   @Override public ST visitLongAssignment(AGLParser.LongAssignmentContext ctx) {      
      ST res = templates.getInstanceOf("assign");
      
      res.add("stat", visit(ctx.assignment()).render()); // render the return value!
      
      // TODO: how to handle this?
      if (ctx.ID(1) != null) {
         res.add("attribute", ctx.ID(1).getText());
         
      }

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
      ST res = templates.getInstanceOf("move");

      res.add("var", ctx.ID().getText());
      res.add("stat", visit(ctx.expression()).render()); // render the return value!
      res.add("destination", ctx.expression().varName);

      return res;
   }


//* for_loop   
   @Override public ST visitFor_loop(AGLParser.For_loopContext ctx) {
      ST res = templates.getInstanceOf("for");  
      
      res.add("var", ctx.ID().getText());

      AGLParser.Number_rangeContext number_range = ctx.number_range();

      res.add("stat", visit(number_range.expression(0)).render()); // render the return value!
      String var1 = number_range.expression(0).varName;

      res.add("stat", visit(number_range.expression(1)).render()); // render the return value!
      String var2 = number_range.expression(1).varName;
      
      String step = "1";
      if (number_range.expression(2) != null) {
         res.add("stat", visit(number_range.expression(2)).render()); // render the return value!
         step = number_range.expression(2).varName;
      }


      ST range = templates.getInstanceOf("range");
      range.add("start", var1);
      range.add("end", var2);
      range.add("step", step);

      res.add("range", range.render());

      for (AGLParser.StatContext stat : ctx.stat()){
         ST statRes = visit(stat);
         res.add("instruction", statRes).render(); // render the return value!
      }

      return res;
   }

 
//* withStatement   
   @Override public ST visitWithStatement(AGLParser.WithStatementContext ctx) {
      ST res = templates.getInstanceOf("with");
      
      ST properties = templates.getInstanceOf("properties");
      for (AGLParser.LongAssignmentContext longAssign: ctx.propertiesAssignment().longAssignment()) {
         //////////////////////////////////////////////////////////////
         // assign the properties
         ST assign = templates.getInstanceOf("assign");
         assign.add("stat", visit(longAssign.assignment()).render()); // render the return value!
         String id = newVarName();
         assign.add("var", id);
         assign.add("value", longAssign.assignment().varName);
         //////////////////////////////////////////////////////////////
         
         res.add("stat", assign.render()); // render the return value!
         properties.add("field", longAssign.ID(0).getText() + " = " + id);
      }

      res.add("var", ctx.ID().getText());
      res.add("properties", properties.render()); // render the return value!

      return res;
   }      

}
