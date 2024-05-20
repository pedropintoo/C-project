import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

@SuppressWarnings("CheckReturnValue")
public class AGLSemAna extends AGLParserBaseVisitor<Boolean> {

   private Map<String, String> variables = new HashMap<>();

   @Override
   public Boolean visitProgram(AGLParser.ProgramContext ctx) {
      Boolean res = null;
      Iterator<AGLParser.StatContext> it = ctx.stat().iterator();
      while (it.hasNext()) {
         res = visit(it.next());
         if (res == null || !res) {
            System.out.println("Error: variable not declared");
            return false;
         }
      }
      return res;
   }

   @Override
   public Boolean visitStat(AGLParser.StatContext ctx) {
      Boolean res = null;

      if (ctx.instantiation() != null) {
         res = visit(ctx.instantiation());

      } else if (ctx.blockStatement() != null) {
         res = visit(ctx.blockStatement());

      } else if (ctx.command()) {
         res = visit(ctx.command());

      } else {
         System.out.println("Error: invalid statement");
         return false;
      }

      return res;
      // return res;
   }

   @Override
   public Boolean visitInstantiation(AGLParser.InstantiationContext ctx) {
      Boolean res = null;
      String ID = ctx.ID().getText();

      if (ctx.simpleStatement() != null) {
         res = visit(ctx.simpleStatement());

      } else if (ctx.blockStatement() != null) {
         res = visit(ctx.blockStatement());

      } else {
         System.out.println("Error: invalid instantiation");
         return false;
      }

      return res;
      // return res;
   }

   @Override
   public Boolean visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
      Boolean res = null;
      String type = ctx.typeID().getText();

      if (type == null) {
         System.out.println("Error: invalid type");
         return false;
      } else {
         if (ctx.assignment() != null) {
            res = visit(ctx.assignment());
         }
      }

      return true;
      // return res;
   }

   @Override
   public Boolean visitBlockStatement(AGLParser.BlockStatementContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitPropertiy(AGLParser.PropertiyContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitAssignment(AGLParser.AssignmentContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitExprString(AGLParser.ExprStringContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitExprWaitFor(AGLParser.ExprWaitForContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitExprPoint(AGLParser.ExprPointContext ctx) {
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

   @Override
   public Boolean visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitExprID(AGLParser.ExprIDContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitCommand(AGLParser.CommandContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitWaitFor(AGLParser.WaitForContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitEventTrigger(AGLParser.EventTriggerContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitMouseTrigger(AGLParser.MouseTriggerContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitNumber(AGLParser.NumberContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitPoint(AGLParser.PointContext ctx) {
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

   @Override
   public Boolean visitPrimitiveType(AGLParser.PrimitiveTypeContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitOperator(AGLParser.OperatorContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }

   @Override
   public Boolean visitSign(AGLParser.SignContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      // return res;
   }
}
