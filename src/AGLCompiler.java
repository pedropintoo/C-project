import org.stringtemplate.v4.*;

import .antlr.AGLParser;

import .antlr.AGLParser;


@SuppressWarnings("CheckReturnValue")
public class AGLCompiler extends AGLParserBaseVisitor<ST> {
   // AGL Compiler assuming previous semantic validation

   private STGroup templates = new STGroupFile("AGL_python.stg");

   @Override public ST visitProgram(AGLParser.ProgramContext ctx) {
      ST res = templates.getInstanceOf("module");
      
      for (AGLParser.StatContext stat : ctx.stat()){
         ST statRes = visit(stat);
         if (statRes != null) {
            res.add("stat", statRes).render();
         }
      }

      return res;
   }

   @Override public ST visitStatInstantiation(AGLParser.StatInstantiationContext ctx) {
      return visit(ctx.instantiantion());
   }

   @Override public ST visitInstantiation(AGLParser.InstantiationContext ctx) {
      String id = ctx.ID().getText();
      
      return visit(ctx.statement);
   }

   @Override public ST visitStatBlockStatement(AGLParser.StatBlockStatementContext ctx) {
      // ST res = templates.getInstanceOf("stat");
      
      // res.add("output", "adasda");
      return visit(ctx.blockStatement());
   }

   @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitStatCommand(AGLParser.StatCommandContext ctx) {
      return visit(ctx.command());
   }

   @Override public ST visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitPropertiy(AGLParser.PropertiyContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
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

   @Override public ST visitTypeID(AGLParser.TypeIDContext ctx) {
      ST res = templates.getInstanceOf("typeID");
      if (ctx.ID != null) {
         res.add("type", ctx.ID());
      } else {
         res.add("type", visit(ctx.primitiveType()));
      }
      return res;
   }

   @Override public ST visitPrimitiveType(AGLParser.PrimitiveTypeContext ctx) {
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
