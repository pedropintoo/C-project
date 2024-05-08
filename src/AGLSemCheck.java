@SuppressWarnings("CheckReturnValue")
public class AGLSemCheck extends AGLParserBaseVisitor<Boolean> {

   @Override public Boolean visitProgram(AGLParser.ProgramContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      //return res;
   }

   @Override public Boolean visitNumber(AGLParser.NumberContext ctx) {
      Boolean res = null;
      if (ctx.NUMBER() == null) {
         System.out.println("Error: Number expected at line " + ctx.start.getLine() + " column " + ctx.start.getCharPositionInLine());
         res = false;
      } else if (ctx.NUMBER().getText().contains(".")) {
         System.out.println("Error: Integer expected at line " + ctx.start.getLine() + " column " + ctx.start.getCharPositionInLine());
         res = false;
      }
      // return visitChildren(ctx);
      return res;
   }

   @Override public Boolean visitPoint(AGLParser.PointContext ctx) {
      Boolean res = null;
      return visitChildren(ctx);
      //return res;
   }
}
