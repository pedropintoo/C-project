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
      res.add("e1", e1Var);
      res.add("op", op);
      res.add("e2", e2Var);
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

   @Override public ST visitStatCommand(AGLParser.StatCommandContext ctx) {
      return visit(ctx.command());
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
      
      String id = newVarName();
      ctx.varName = id;

      String value;
      if (ctx.assignment() != null) {
         res.add("stat", visit(ctx.assignment()).render()); // render the return value!
         value = ctx.assignment().varName;
      } else { 
         value = "DEFAULT_VALUE";  // TODO: TO_BE_IMPLEMENTED
      }

      res.add("var", id);
      res.add("value", value);   // assign the value to current variable

      return res;
   }

   
//* blockStatement
   @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      ST res = templates.getInstanceOf("assign");
      String type = visit(ctx.typeID()).render();

      if (type.equals("View")) {
         res = templates.getInstanceOf("canvas");
         res.add("view", type);
      }

      return null;
   }

   
//* propertiesAssignment
   @Override public ST visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
      return null;
   }

//* property
   @Override public ST visitProperty(AGLParser.PropertyContext ctx) {
      return null;
   }

   @Override public ST visitAssignment(AGLParser.AssignmentContext ctx) {
      ST res = templates.getInstanceOf("assign");
      
      String id = newVarName();
      ctx.varName = id;

      // TODO: 'at' expression

      res.add("stat", visit(ctx.expression()).render()); // render the return value!
      res.add("var", id);
      res.add("value", ctx.expression().varName); // assign the value to current variable

      return res;
   }


//* expression  
   @Override public ST visitExprUnary(AGLParser.ExprUnaryContext ctx) {
      ST res = templates.getInstanceOf("unaryExpression");

      String id = newVarName();
      ctx.varName = id;

      res.add("stat", visit(ctx.expression()).render()); // render the return value!
      
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
      ST res = templates.getInstanceOf("binaryExpression");
      ctx.varName = newVarName();
      return binaryExpression(visit(ctx.expression(0)).render(), visit(ctx.expression(1)).render(), newVarName(), ctx.expression(0).varName, ctx.op.getText(), ctx.expression(1).varName);
   }

   @Override public ST visitExprPoint(AGLParser.ExprPointContext ctx) {
      ST res = templates.getInstanceOf("binaryExpression");
      ctx.varName = newVarName();
      return binaryExpression(visit(ctx.x).render(), visit(ctx.y).render(), newVarName(), ctx.x.varName, ",", ctx.y.varName);
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
      return null;
   }


//* command   
   @Override public ST visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
      return null;
   }

   @Override public ST visitCommandPrint(AGLParser.CommandPrintContext ctx) {
      return null;
   }

   @Override public ST visitCommandClose(AGLParser.CommandCloseContext ctx) {
      return null;
   }


//* eventTrigger
   @Override public ST visitEventTrigger(AGLParser.EventTriggerContext ctx) {
      return null;
   }


//* mouseTrigger   
   @Override public ST visitMouseTrigger(AGLParser.MouseTriggerContext ctx) {
      return null;
   }

}
