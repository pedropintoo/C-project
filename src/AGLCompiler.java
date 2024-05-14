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
      
      for (AGLParser.StatContext stat : ctx.stat()){
         ST statRes = visit(stat);
         if (statRes != null) {
            res.add("stat", statRes).render(); // write the response
         }
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

      res.add("var", id);
      res.add("value", 777);

      return res;
   }


//* simpleStatement
   @Override public ST visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      return null;
   }

   
//* blockStatement
   @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      return null;
   }

   
//* propertiesAssignment
   @Override public ST visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
      return null;
   }

//* property
   @Override public ST visitPropertiy(AGLParser.PropertiyContext ctx) {
      ST res = null;
      return visitChildren(ctx);
   }

   @Override public ST visitAssignment(AGLParser.AssignmentContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprString(AGLParser.ExprStringContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprWaitFor(AGLParser.ExprWaitForContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprPoint(AGLParser.ExprPointContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprNumber(AGLParser.ExprNumberContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprID(AGLParser.ExprIDContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
      return null;
   }

   @Override public ST visitCommandPrint(AGLParser.CommandPrintContext ctx) {
      ST res = null;
      return visitChildren(ctx);
   }

   @Override public ST visitCommandClose(AGLParser.CommandCloseContext ctx) {
      ST res = null;
      return visitChildren(ctx);
   }

   @Override public ST visitWaitFor(AGLParser.WaitForContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitEventTrigger(AGLParser.EventTriggerContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitMouseTrigger(AGLParser.MouseTriggerContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitNumber(AGLParser.NumberContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitPoint(AGLParser.PointContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitOperator(AGLParser.OperatorContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitSign(AGLParser.SignContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }
}
