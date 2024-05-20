// import java.util.Iterator;

// @SuppressWarnings("CheckReturnValue")
// public class AGLSemCheck extends AGLParserBaseVisitor<Boolean> {

//     @Override
//     public Boolean visitProgram(AGLParser.ProgramContext ctx) {
//         Boolean res = null;
//         Iterator<AGLParser.StatContext> iterator = ctx.stat().iterator();

//         while (iterator.hasNext()) {
//             res = visit(iterator.next());
//             if (res == null || !res) {
//                 return false;
//             }
//         }

//         return true;
//     }

//     @Override
//     public Boolean visitStat(AGLParser.StatContext ctx) {
//         Boolean res = null;

//         if (ctx.expr() != null) {
//             res = visit(ctx.expr());
//         } else if (ctx.ID() != null) {
//             String id = ctx.ID().getText();
//             if (AGLParser.symbolTable.get(id) == null) {
//                 System.err.println("Error: variable " + id + " not declared");
//                 return false;
//             }
//         }

//         return true;
//     }

// }
