import java.util.Map;
import java.util.HashMap;

public class ObjectType extends Type {
    private Map<String, Map<String, Type>> attributes = new HashMap<String, Map<String, Type>>();

    protected ObjectType(String name) {
        super(name);
        switch (name) {
            case "Line":
                addAttribute("Line", "state", new StringType());
                addAttribute("Line", "origin", new PointType());
                addAttribute("Line", "length", new PointType());
                addAttribute("Line", "fill", new StringType());
                break;
            case "PolyLine":
                addAttribute("PolyLine", "state", new StringType());
                addAttribute("PolyLine", "state", new PointType());
                addAttribute("PolyLine", "state", new PointType());  // in need to especify that I can put a list of points
                addAttribute("PolyLine", "state", new StringType());
            default:
                ErrorHandling.printError("Error: Invalid type");
                break;
        }
    }

    public void addAttribute(String typeName, String attributeName, Type type) {
        if (!attributes.containsKey(typeName)) {
            attributes.put(typeName, new HashMap<>());
        }
        attributes.get(typeName).put(attributeName, type);
    }

    public boolean checkAttributes(String typeName, String attributeName, Type type) {
        if (!attributes.containsKey(typeName)) {
            ErrorHandling.printError("Error: Type not defined");
            return false;
        }

        Map<String, Type> typeAttributes = attributes.get(typeName);
        if (!typeAttributes.containsKey(attributeName)) {
            ErrorHandling.printError("Error: Attribute not defined");
            return false;
        }
    
        Type expectedType = typeAttributes.get(attributeName);
        if (!expectedType.equals(type)) {
            ErrorHandling.printError("Error: Attribute type invalid");
            return false;
        }

        return false;
    }
    
}
