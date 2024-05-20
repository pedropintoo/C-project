import org.stringtemplate.v4.*;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.antlr.v4.runtime.ParserRuleContext;

public class test {
    public static void main(String[] args) {
        STGroup stg =  new STGroupFile("tkinter.stg");

        ST module = stg.getInstanceOf("module");
        ST stat = stg.getInstanceOf("stats");
        ST canvas = stg.getInstanceOf("canvas");
        ST property = stg.getInstanceOf("property");
        ST assign = stg.getInstanceOf("assign");
        ST assign2 = stg.getInstanceOf("assign");
        assign.add("var", "height");
        assign.add("value", "600");
        property.add("field", assign.render());
        assign2.add("var", "width");
        assign2.add("value", "500");
        property.add("field", assign2.render());
        canvas.add("title", "no title");
        canvas.add("view", "view");
        canvas.add("property", property.render());
        stat.add("stat", canvas.render());
        module.add("stat", stat.render());
        System.out.println(module.render());
    }
}