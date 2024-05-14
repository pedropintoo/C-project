/*
   File: AGL Generator to Python
 */

import org.stringtemplate.v4.*;

@SuppressWarnings("CheckReturnValue")
public class AGLCompiler extends AGLParserBaseVisitor<ST> {
   

   private STGroup templates = new STGroupFile("AGL_python.stg");

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
      ST value = null;

      if (ctx.simpleStatement() != null) {
         value = visit(ctx.simpleStatement());
      } else {
         value = visit(ctx.blockStatement());
      }

      res.add("var", id);
      res.add("value", value.render()); // render the return value!

      return res;
   }


//* simpleStatement
   @Override public ST visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      ST res = templates.getInstanceOf("value");
      
      if (ctx.assignment() == null) {
         // default value
         res.add("value", "TO_BE_IMPLEMENTED");
      } else {
         res.add("value", visit(ctx.assignment()).render()); // render the return value!
      } 

      return res;
   }

   
//* blockStatement
   @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      ST res = null;
      String type = visit(ctx.typeID()).render();

      if (type.equals("View")) {
         res = templates.getInstanceOf("canvas");
         res.add("view", type);
         res.add("title", ctx.titl)
      }

      return null;
   }

   
//* propertiesAssignment
   @Override public ST visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
      return null;
   }

//* property
   @Override public ST visitPropertiy(AGLParser.PropertiyContext ctx) {
      return null;
   }

   @Override public ST visitAssignment(AGLParser.AssignmentContext ctx) {
      ST res = templates.getInstanceOf("value");
      
      res.add("value", visit(ctx.expression()).render()); // render the return value!
      
      return res;
   }


//* expression  
   @Override public ST visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      return null;
   }

   @Override public ST visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
      return null;
   }

   @Override public ST visitExprPoint(AGLParser.ExprPointContext ctx) {
      return null;
   }

   @Override public ST visitExprNumber(AGLParser.ExprNumberContext ctx) {
      ST res = templates.getInstanceOf("value");

      res.add("value", visit(ctx.number()).render()); // render the return value!

      return res;
   }

   @Override public ST visitExprString(AGLParser.ExprStringContext ctx) {
      ST res = templates.getInstanceOf("value");
      
      res.add("value", ctx.STRING()); // Terminal node

      return res;
   }

   @Override public ST visitExprID(AGLParser.ExprIDContext ctx) {
      return null;
   }

   @Override public ST visitExprWaitFor(AGLParser.ExprWaitForContext ctx) {
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

   @Override public ST visitWaitFor(AGLParser.WaitForContext ctx) {
      return null;
   }

   @Override public ST visitEventTrigger(AGLParser.EventTriggerContext ctx) {
      return null;
   }

   @Override public ST visitMouseTrigger(AGLParser.MouseTriggerContext ctx) {
      return null;
   }

   @Override public ST visitNumber(AGLParser.NumberContext ctx) {
      ST res = templates.getInstanceOf("value");

      res.add("value", ctx.INT() == null ? ctx.FLOAT() : ctx.INT()); // Terminal node

      return res;
   }

   @Override public ST visitPoint(AGLParser.PointContext ctx) {
      return null;
   }

   @Override public ST visitOperator(AGLParser.OperatorContext ctx) {
      return null;
   }

   @Override public ST visitSign(AGLParser.SignContext ctx) {
      return null;
   }
}
