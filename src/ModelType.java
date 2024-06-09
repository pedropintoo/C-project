import java.util.HashSet;
import java.util.Set;

public class ModelType extends Type {
    private Set<ObjectType> modelStructure = new HashSet<>();
    
    public ModelType(String name) {
        super(name);
    }

    @Override
    public boolean isNumeric() {
        return true;
    }
}
