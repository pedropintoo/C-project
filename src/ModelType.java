import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ModelType extends Type {
    // symbol table
    public Map<String, Symbol> symbolModelTable = new HashMap<String, Symbol>();
    
    public ModelType(String name) {
        super(name);
    }

    @Override
    public boolean isNumeric() {
        return true;
    }
}
