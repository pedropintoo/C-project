import java.io.InputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.stringtemplate.v4.*;


public class AGLMain {
   public static void main(String[] args) {
      try {
         InputStream file = new FileInputStream(args[0]);
         // create a CharStream that reads from standard input:
         CharStream input = CharStreams.fromStream(file);
         // create a lexer that feeds off of input CharStream:
         AGLLexer lexer = new AGLLexer(input);
         // create a buffer of tokens pulled from the lexer:
         CommonTokenStream tokens = new CommonTokenStream(lexer);
         // create a parser that feeds off the tokens buffer:
         AGLParser parser = new AGLParser(tokens);
         // replace error listener:
         //parser.removeErrorListeners(); // remove ConsoleErrorListener
         //parser.addErrorListener(new ErrorHandlingListener());
         // begin parsing at program rule:
         ParseTree tree = parser.program();
         if (parser.getNumberOfSyntaxErrors() == 0) {
            AGLCompiler compiler = new AGLCompiler();
            ST result = compiler.visit(tree);
            System.out.println(result.render());
         }
      }
      catch (FileNotFoundException e) {
         System.out.println("File not found: " + args[0]);
         System.exit(1);
      }
      catch(IOException e) {
         e.printStackTrace();
         System.exit(1);
      }
      catch(RecognitionException e) {
         e.printStackTrace();
         System.exit(1);
      }
   }
}