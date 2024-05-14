import org.stringtemplate.v4.*;


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

   @Override public ST visitStat(AGLParser.StatContext ctx) {
      ST res = templates.getInstanceOf("print");
      res.add("output", "adasda");
      return res;
   }

   @Override public ST visitInstantiation(AGLParser.InstantiationContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
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
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitCommandPrint(AGLParser.CommandPrintContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public ST visitCommandClose(AGLParser.CommandCloseContext ctx) {
      ST res = null;
      return visitChildren(ctx);
      //return res;
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
      ST res = null;
      return visitChildren(ctx);
      //return res;
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
