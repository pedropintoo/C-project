import java.util.*;

@SuppressWarnings("CheckReturnValue")
public class AGLCompiler extends AGLParserBaseVisitor<ST> {

   private STGroup templates = new STGroupFile("python.stg");

   @Override public ST visitProgram(AGLParser.ProgramContext ctx) {
      ST res = templates.getInstanceOf("module");

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
}
