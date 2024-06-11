// /*
//    File: AGL Generator to Python
//    */

import org.stringtemplate.v4.*;

import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;
import java.util.Iterator;
import java.util.Scanner;

@SuppressWarnings("CheckReturnValue")
public class AGLCompiler extends AGLParserBaseVisitor<ST> {
    
    private STGroup templates = new STGroupFile("AGL_python.stg");

    private int varCounter = 0;

    private String newVarName() {
        return "v" + varCounter++;
    }

    private ST binaryExpression(String e1Stats, String e2Stats, String var, String e1Var, String op, String e2Var) {
        ST res = templates.getInstanceOf("binaryExpression");
        if (!op.equals(",") && !op.equals("or") && !op.equals("and")) {
            e1Var = "np.array("+e1Var+")"; e2Var = "np.array("+e2Var+")";
            if (op.equals("*")) {
                e1Var = "np.dot(" + e1Var;
                e2Var = e2Var + ")";
            }
        }
        res.add("stat", e1Stats);
        res.add("stat", e2Stats);
        res.add("var", var);
        res.add("e1", (op.equals(",") ? "(" : "")+e1Var);
        res.add("op", !op.equals("*")? op : ",");
        res.add("e2", e2Var+(op.equals(",") ? ")" : ""));
        return res;
    }

    private String getConcreteId(AGLParser.IdentifierContext ctx, ST res){  
        String id = ctx.ID().getText();
        if (!isReserved(id)) {
            id = "var__agl__" + id;
        }

        if (ctx.expression() != null) {
            for (AGLParser.ExpressionContext expression : ctx.expression()) {
                res.add("stat", visit(expression).render()); // render the return value!
                id += "[" + expression.varName + "]";
            }
        } 

        if (ctx.identifier() != null) {
            id += '.' + getConcreteId(ctx.identifier(), res);
        }
        
        return id;
    }

    public boolean isReserved(String id) {
        boolean isReserved = true;
        switch (id) {
            case "fill":
            case "length":
            case "origin":
            case "state":
            case "start":
            case "extent":
            case "outline":
            case "points":
            case "text":
            case "width":
            case "height":
            case "title":
            case "Ox":
            case "Oy":
            case "background":
            break;
            default:
                isReserved = false;
        }
        return isReserved;
    }


// /*
//    Compiler visitor methods
//    */

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

    @Override public ST visitStatModelInstantiation(AGLParser.StatModelInstantiationContext ctx) {
        return visit(ctx.modelInstantiation());
    }

    @Override public ST visitStatBlockStatement(AGLParser.StatBlockStatementContext ctx) {
        return visit(ctx.blockStatement());
    }

    @Override public ST visitStatLongAssignment(AGLParser.StatLongAssignmentContext ctx) {
        return visit(ctx.longAssignment());
    }

    @Override public ST visitStatWithStatement(AGLParser.StatWithStatementContext ctx) {
       return visit(ctx.withStatement());
    }

    @Override public ST visitStatPlayStatement(AGLParser.StatPlayStatementContext ctx) {
        return visit(ctx.playStatement());
    }

    @Override public ST visitStatRepetitiveStatement(AGLParser.StatRepetitiveStatementContext ctx) {
        return visit(ctx.repetitiveStatement());
    }

    @Override public ST visitStatIfStatement(AGLParser.StatIfStatementContext ctx) {
        return visit(ctx.ifStatement());
    }
    
    @Override public ST visitStatCommand(AGLParser.StatCommandContext ctx) {
        return visit(ctx.command());
    }

    @Override public ST visitStatBlock(AGLParser.StatBlockContext ctx) {
        ST res = templates.getInstanceOf("stats");
  
        for (AGLParser.StatContext stat : ctx.stat()){
           ST statRes = visit(stat);
           res.add("stat", statRes).render(); // render the return value!
        }
        
        return res;
     }
    

//% repetitiveStatement    
   @Override
    public ST visitRepForStatement(AGLParser.RepForStatementContext ctx) {
        return visit(ctx.forStatement());
    }
    @Override
    public ST visitRepWhileStatement(AGLParser.RepWhileStatementContext ctx) {
        return visit(ctx.whileStatement());
    }
    @Override
    public ST visitRepRepeatStatement(AGLParser.RepRepeatStatementContext ctx) {
        return visit(ctx.repeatStatement());
    }


//% instantiation
    @Override public ST visitInstantiation(AGLParser.InstantiationContext ctx) {
        ST res = templates.getInstanceOf("assign");
        
        String id = "var__agl__" + ctx.ID().getText();

        ST stat = null;
        String value;
        if (ctx.simpleStatement() != null) {
            stat = visit(ctx.simpleStatement());
            value = ctx.simpleStatement().varName;
        } else {
            stat = visit(ctx.blockStatement());
            value = ctx.blockStatement().varName;
        }

        res.add("stat", stat.render()); // render the return value!
        res.add("var", id);
        if (value != null) {
            res.add("value", value); // blockStatement can be uninitialized
        }

        res.add("varIfModel", id);
        

        return res;
    }


//* simpleStatement
    @Override public ST visitSimpleStatement(AGLParser.SimpleStatementContext ctx) {
        ST res = templates.getInstanceOf("assign");
        
        String value;
        if (ctx.in_assignment() != null) {
            // -> Enum
            value = ctx.in_assignment().ID(0).getText(); // first values is the default

            ST enum_temp = templates.getInstanceOf("enum");

            String enum_id = newVarName();
            enum_temp.add("var", enum_id);

            for (TerminalNode id : ctx.in_assignment().ID()) {
                enum_temp.add("id", "var__agl__" + id); 
            }

            value = newVarName();
            enum_temp.add("value", value);
            
            res.add("stat", enum_temp.render()); // render the return value!

        } else if (ctx.assignment() != null) {
            // -> Expression
            res.add("stat", visit(ctx.assignment()).render()); // render the return value!
            value = ctx.assignment().varName;

        } else { 

            if (ctx.typeID().ID() != null) {
                // -> Model (because have a ID() in typeID)
                ST model = templates.getInstanceOf("model");
            
                model.add("modelName", "var__agl__" + ctx.typeID().getText());
                value = newVarName();
                model.add("var", value);

                if (ctx.expression() != null) {
                    res.add("stat", visit(ctx.expression()).render()); // render the return value!
                    model.add("origin", ctx.expression().varName);
                }

                res.add("stat", model.render()); // render the return value!
            } else {
                value = "0"; // Integer
                // Normal default values
                switch (ctx.typeID().getText().split("<")[0]) {
                    case "Number":
                        value = "0";
                        break;
                    case "String":
                        value = "\"\"";
                        break;
                    case "Point":
                        value = "(0, 0)";
                        break;
                    case "Vector":
                        value = "(0.0, 0.0)";
                        break;
                    case "Boolean":
                        value = "False";
                        break;
                    case "Array":
                        int numberOfChains = ctx.typeID().getText().split("<").length - 1;
                        if (numberOfChains > 0) {
                            value = "";
                            for (int i = 0; i < numberOfChains; i++) {
                                value += "[";
                            }
                            for (int i = 0; i < numberOfChains; i++) {
                                value += "]";
                            }
                        } else {
                            value = "[]";
                        }
                        break;
                    case "Time":
                        value = "0";
                        break;
                }
            }
        } 

        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("value", value);   // assign the value to current variable

        return res;
    }

   
//* blockStatement
    @Override public ST visitBlockStatement(AGLParser.BlockStatementContext ctx) {
        ST res = null;

        res = templates.getInstanceOf("object");
        res.add("type", ctx.typeID().getText());

        if (ctx.typeID().getText().equals("View")) {
            res.add("update_lastView", "True");
        }
        
        // (at expression)?
        if (ctx.expression() != null) {
            // define the origin
            res.add("stat", visit(ctx.expression()).render()); // render the return value!
            res.add("origin", ctx.expression().varName);
        }

        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        
        ctx.propertiesAssignment().idToAssign = id;
        res.add("properties", visit(ctx.propertiesAssignment()).render()); // render the return value!

        return res;

    }

//* propertiesAssignment    
    @Override
    public ST visitPropertiesAssignment(AGLParser.PropertiesAssignmentContext ctx) {
        ST res = templates.getInstanceOf("block_properties");
        String id = ctx.idToAssign;

        for (AGLParser.LongAssignmentContext longAssign: ctx.longAssignment()) {
            //////////////////////////////////////////////////////////////
            // assign the properties
            ST assign = templates.getInstanceOf("assign");
            assign.add("stat", visit(longAssign.assignment()).render()); // render the return value!
            String id2 = newVarName();
            assign.add("var", id2);
            assign.add("value", longAssign.assignment().varName);
            //////////////////////////////////////////////////////////////

            res.add("stat", assign.render()); // render the return value!
            res.add("field", id+"."+getConcreteId(longAssign.identifier(), res) + " = " + id2);
        }

        return res;
    }

//* longAssignment
    @Override public ST visitLongAssignment(AGLParser.LongAssignmentContext ctx) {      
        ST res = templates.getInstanceOf("assign");
        
        res.add("stat", visit(ctx.assignment()).render()); // render the return value!
        res.add("var", getConcreteId(ctx.identifier(), res));
        res.add("value", ctx.assignment().varName); // render the return value!

        return res;
    }

   
//* assignment   
    @Override public ST visitAssignment(AGLParser.AssignmentContext ctx) {
        ST res = templates.getInstanceOf("assign");

        res.add("stat", visit(ctx.expression()).render()); // render the return value!
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("value", ctx.expression().varName); // assign the value to current variable

        return res;
    }


//* expression  
    @Override public ST visitExprUnary(AGLParser.ExprUnaryContext ctx) {
        ST res = templates.getInstanceOf("unaryExpression");

        res.add("stat", visit(ctx.expression()).render()); // render the return value!
        String e1Var = ctx.expression().varName;
        String op = ctx.sign.getText();
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("op", op); // ('+' | '-' | 'not')
        
        if (!op.equals("not")) {
            e1Var = "np.array("+e1Var+")";
        }
        res.add("e1", e1Var);
        
        return res;
    }

    @Override public ST visitExprParenthesis(AGLParser.ExprParenthesisContext ctx) {
        ST res = visit(ctx.expression());
        ctx.varName = ctx.expression().varName;
        return res;
    }

    @Override public ST visitExprAddSubMultDiv(AGLParser.ExprAddSubMultDivContext ctx) {
        ctx.varName = newVarName(); 
        return binaryExpression(visit(ctx.e1).render(), visit(ctx.e2).render(), ctx.varName, ctx.e1.varName, ctx.op.getText(), ctx.e2.varName);
    }

    @Override public ST visitExprRelational(AGLParser.ExprRelationalContext ctx) {
        ctx.varName = newVarName(); 
        return binaryExpression(visit(ctx.e1).render(), visit(ctx.e2).render(), ctx.varName, ctx.e1.varName, ctx.op.getText(), ctx.e2.varName);
    }

    @Override public ST visitExprAndOr(AGLParser.ExprAndOrContext ctx) {
        ctx.varName = newVarName(); 
        String op = ctx.OR() != null ? ctx.OR().getText() : ctx.AND().getText();
        return binaryExpression(visit(ctx.e1).render(), visit(ctx.e2).render(), ctx.varName, ctx.e1.varName, op, ctx.e2.varName);
    }

    @Override public ST visitExprPoint(AGLParser.ExprPointContext ctx) {
        ctx.varName = newVarName(); 
        return binaryExpression(visit(ctx.x).render(), visit(ctx.y).render(), ctx.varName, ctx.x.varName, ",", ctx.y.varName);
    }

    @Override public ST visitExprVector(AGLParser.ExprVectorContext ctx) {
        ST res = templates.getInstanceOf("stats");

        ST assign = templates.getInstanceOf("assign");
        assign.add("stat", visit(ctx.deg).render()); // render the return value!
        String degree = newVarName();
        assign.add("var", degree);
        assign.add("value", ctx.deg.getText());

        ST assign2 = templates.getInstanceOf("assign");
        assign2.add("stat", visit(ctx.length).render()); // render the return value!
        String length = newVarName();
        assign2.add("var", length);
        assign2.add("value", ctx.length.getText());

        String x = length + "*math.cos(math.radians(" + degree + "))";
        String y = length + "*math.sin(math.radians(" + degree + "))";

        ctx.varName = newVarName();
        return binaryExpression(assign.render(), assign2.render(), ctx.varName, x, ",", y);
    }

     @Override public ST visitExprArray(AGLParser.ExprArrayContext ctx) {
        ST res = templates.getInstanceOf("array");
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);

        for (AGLParser.ExpressionContext expression : ctx.expression()) {
            res.add("stat", visit(expression).render());
            res.add("field", expression.varName);
        }

        return res;
    }

    

    @Override public ST visitExprNumber(AGLParser.ExprNumberContext ctx) {
        ST res = templates.getInstanceOf("assign");
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("value", ctx.number.getText()); // assign the value to current variable

        return res;
    }

    @Override public ST visitExprBoolean(AGLParser.ExprBooleanContext ctx) {
        ST res = templates.getInstanceOf("assign");
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("value", ctx.BOOLEAN().getText()); // assign the value to current variable

        return res;
    }

    @Override public ST visitExprString(AGLParser.ExprStringContext ctx) {
        ST res = templates.getInstanceOf("assign");
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("value", ctx.STRING().getText()); // assign the value to current variable

        return res;
    }

    @Override public ST visitExprID(AGLParser.ExprIDContext ctx) {
        ST res = templates.getInstanceOf("assign");
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);
        res.add("value", getConcreteId(ctx.identifier(), res)); // assign the value to current variable

        return res;
    }

    @Override public ST visitExprWait(AGLParser.ExprWaitContext ctx) {
        ST res = templates.getInstanceOf("waitMouseClick");
        
        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);

        return res;
    }

    @Override public ST visitExprDeepCopy(AGLParser.ExprDeepCopyContext ctx) {
        ST res = templates.getInstanceOf("deepcopy");
        // 'deepcopy' identifier 'to' expression ';'

        res.add("stat", visit(ctx.expression()).render());
        res.add("origin", ctx.expression().varName);

        res.add("object", getConcreteId(ctx.identifier(), res));

        String id = newVarName();
        ctx.varName = id;

        res.add("var", id);

        return res;
    }


    @Override public ST visitExprScript(AGLParser.ExprScriptContext ctx) {
        ST res;
        
        String id = newVarName();
        String str = ctx.STRING().getText();
        if (ctx.op.getText().equals("input")) {
            res = templates.getInstanceOf("input");
                    
            String message = str.substring(1, str.length()-1);

            res.add("message", message);
            res.add("var", id);
        } else {
            res = templates.getInstanceOf("assign");

            res.add("var", id);
            res.add("value", str); // the str is the file name (load operation)
        }
        
        ctx.varName = id;

        return res; 
    }



//* command   
    @Override public ST visitCommandRefresh(AGLParser.CommandRefreshContext ctx) {
        ST res = templates.getInstanceOf("refresh");

        Iterator<TerminalNode> it = ctx.ID().iterator();
        TerminalNode current;
        boolean isFirst = true;
        while(it.hasNext()) {
            current = it.next();
            
            res.add("view", "var__agl__"+current.getText());

            if (isFirst && ctx.expression() != null) {
                res.add("stat", visit(ctx.expression()).render()); // render the return value!
                res.add("delay", ctx.expression().varName + (ctx.suffix.getText().equals("ms")? "/1000": ""));
            }

            isFirst = false;
            
            if (it.hasNext()) {
                String prev_refresh = res.render();
                res = templates.getInstanceOf("refresh");
                res.add("stat", prev_refresh);
            }
        }

        

        return res;
    }

    @Override public ST visitCommandPrint(AGLParser.CommandPrintContext ctx) {
        ST res = templates.getInstanceOf("print");
        
        res.add("stat", visit(ctx.expression()).render()); // render the return value!
        res.add("output", ctx.expression().varName);
        
        return res;
    }

    @Override public ST visitCommandClose(AGLParser.CommandCloseContext ctx) {
        ST res = templates.getInstanceOf("close");

        Iterator<TerminalNode> it = ctx.ID().iterator();
        TerminalNode current;
        while(it.hasNext()) {
            current = it.next();
            
            res.add("view", "var__agl__" + current.getText());

            if (it.hasNext()) {
                String prev_close = res.render();
                res = templates.getInstanceOf("close");
                res.add("stat", prev_close);
            }
        }
        
        return res;
    }

    @Override public ST visitCommandMove(AGLParser.CommandMoveContext ctx) {
        ST res = templates.getInstanceOf("move");

        Iterator<AGLParser.IdentifierContext> it = ctx.identifier().iterator();
        AGLParser.IdentifierContext current;
        String id; 
        while (it.hasNext()) {
            current = it.next();

            id = getConcreteId(current, res);
    
            res.add("var", id);
            res.add("stat", visit(ctx.expression()).render()); // render the return value!
            res.add("destination", ctx.expression().varName);
    
            if (ctx.type.getText().equals("by")) {
                res.add("relative", "True"); 
            } 

            if (it.hasNext()) {
                String prev_close = res.render();
                res = templates.getInstanceOf("move");
                res.add("stat", prev_close);
            }

        }        

        return res;
    }

    @Override public ST visitCommandRotate(AGLParser.CommandRotateContext ctx) {
        ST res = templates.getInstanceOf("rotate");

        Iterator<AGLParser.IdentifierContext> it = ctx.identifier().iterator();
        AGLParser.IdentifierContext current;
        String id; 
        while (it.hasNext()) {
            current = it.next();

            id = getConcreteId(current, res);
    
            res.add("var", id);
            res.add("stat", visit(ctx.expression()).render()); // render the return value!
            res.add("degree", ctx.expression().varName);

            if (it.hasNext()) {
                String prev_close = res.render();
                res = templates.getInstanceOf("rotate");
                res.add("stat", prev_close);
            }

        }        

        return res;
    }

//* forStatement   
    @Override public ST visitForStatement(AGLParser.ForStatementContext ctx) {
        ST res = templates.getInstanceOf("for");  
        
        res.add("var", "var__agl__" + ctx.ID().getText());

        AGLParser.Number_rangeContext number_range = ctx.number_range();

        res.add("stat", visit(number_range.expression(0)).render()); // render the return value!
        String var1 = number_range.expression(0).varName;

        res.add("stat", visit(number_range.expression(1)).render()); // render the return value!
        String var2 = number_range.expression(1).varName;
        
        String step = "1";
        if (number_range.expression(2) != null) {
            res.add("stat", visit(number_range.expression(2)).render()); // render the return value!
            step = number_range.expression(2).varName;
        }


        ST range = templates.getInstanceOf("range");
        range.add("start", var1);
        range.add("end", var2);
        range.add("step", step);

        res.add("range", range.render());

        res.add("instructions", visit(ctx.stat()).render()); // render the return value!

        return res;
    }

//* whileStatement   
@Override public ST visitWhileStatement(AGLParser.WhileStatementContext ctx) {
    ST res = templates.getInstanceOf("while");

    res.add("stat", visit(ctx.expression()).render()); // render the return value!
    res.add("condition", ctx.expression().varName);
    res.add("instructions", visit(ctx.stat()).render()); // render the return value!

    return res;
}  

//* repeatStatement   
    @Override public ST visitRepeatStatement(AGLParser.RepeatStatementContext ctx) {
        ST res = templates.getInstanceOf("repeat");

        res.add("stat", visit(ctx.expression()).render()); // render the return value!
        res.add("condition", ctx.expression().varName);
        res.add("instructions", visit(ctx.stat()).render()); // render the return value!
    
        return res;
    }  
 
//* withStatement   
    @Override public ST visitWithStatement(AGLParser.WithStatementContext ctx) {
        ST res = templates.getInstanceOf("stats");

        // define the id used in propertiesAssignment (hierarchy attribute)
        ctx.propertiesAssignment().idToAssign = getConcreteId(ctx.identifier(), res);
        res.add("stat", visit(ctx.propertiesAssignment()).render()); // render the return value!

        return res;
    }      

//* modelStatement   
    @Override public ST visitPlayStatement(AGLParser.PlayStatementContext ctx) {
        ST res = templates.getInstanceOf("play");

        res.add("file", "var__agl__" + ctx.ID().getText());

        for (AGLParser.LongAssignmentContext longAssign : ctx.propertiesAssignment().longAssignment()){
            // define the id used in propertiesAssignment (hierarchy attribute)
            String toAssign = getConcreteId(longAssign.identifier(), res);
            
            ST prop = templates.getInstanceOf("assign");
            String id = newVarName();
            
            prop.add("stat", visit(longAssign.assignment()).render()); // render the return value!
            prop.add("value", longAssign.assignment().varName);
            prop.add("var", id);
            
            res.add("stat", prop.render()); // render the return value!
            res.add("field", "\"" + toAssign.replace("var__agl__", "") + "\":" + id);
        }

        return res;
    }

//* modelStat
    @Override public ST visitModelStatInstantiation(AGLParser.ModelStatInstantiationContext ctx) {
        ctx.isAction = false;
        return visit(ctx.instantiation());
    }

    @Override public ST visitModelStatBlockStatement(AGLParser.ModelStatBlockStatementContext ctx) {
        ctx.isAction = false;
        return visit(ctx.blockStatement());
    }

    @Override public ST visitModelStatLongAssignment(AGLParser.ModelStatLongAssignmentContext ctx) {
        ctx.isAction = false;
        return visit(ctx.longAssignment());
    }

    @Override public ST visitModelStatAction(AGLParser.ModelStatActionContext ctx) {
        ctx.isAction = true;
        return visit(ctx.action());
    }

//* modelStatement   
    @Override public ST visitModelInstantiation(AGLParser.ModelInstantiationContext ctx) {
        ST res = templates.getInstanceOf("model_creation");

        res.add("modelName", "var__agl__" + ctx.ID().getText());
        
        for (AGLParser.ModelStatContext stat : ctx.modelStat()){
            
            ST statRes = visit(stat);
            if (stat.isAction) {
                res.add("action", statRes.render()); // render the return value!
            } else {
                res.add("modelStat", statRes.render()); // render the return value!
            }
        }

        return res;
    }

//* action
    @Override public ST visitAction(AGLParser.ActionContext ctx) {
        ST res = templates.getInstanceOf("action");

        res.add("var", getConcreteId(ctx.identifier(), res));

        res.add("actionStat", visit(ctx.stat()).render()); // render the return value!
        
        return  res; 
    }

//* ifStatement
    @Override public ST visitIfStatement(AGLParser.IfStatementContext ctx) {
        ST res = templates.getInstanceOf("if_else"); // if_else(stat, condition, if_instructions, else_instructions)

        res.add("stat", visit(ctx.expression()).render()); // render the return value!

        res.add("condition", ctx.expression().varName);

        res.add("if_instructions", visit(ctx.stat(0)).render()); // render the return value!

        if (ctx.stat(1) != null) {
            res.add("else_instructions", visit(ctx.stat(1)).render()); // render the return value!
        }
        
        return res;
    }   

}
