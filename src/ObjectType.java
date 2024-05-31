import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class ObjectType extends Type {
    private Map<String, List<Type>> attributes;

    protected ObjectType(String name) {
        super(name);
        this.attributes = new HashMap<String, List<Type>>();
        switch (name) {
            case "Line":
                System.out.println("Arrived in Line");
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addFill();
                break;
            case "PolyLine":
                System.out.println("Arrived in PolyLine");
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                break;
            case "Spline":
                System.out.println("Arrived in Spline");
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                break;
            case "Polygon":
                System.out.println("Arrived in Polygon");
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                this.addOutline();
                break;
            case "Blob":
                System.out.println("Arrived in Blob");
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                this.addOutline();
                break;
            case "Rectangle":
                System.out.println("Arrived in Rectangle");
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addFill();
                break;
            case "Ellipse":
                System.out.println("Arrived in Ellipse");
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addFill();
                break;
            case "Arc":
                System.out.println("Arrived in Arc");
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addStart();
                this.addExtent();
                this.addOutline();
                break;
            case "ArcChord":
                System.out.println("Arrived in ArcChord");
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addStart();
                this.addExtent();
                this.addFill();
                break;
            case "PieSlice":
                System.out.println("Arrived in PieSlice");
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addStart();
                this.addExtent();
                this.addFill();
                break;
            case "Text":
                System.out.println("Arrived in Text");
                this.addState();
                this.addOrigin();
                this.addText();
                this.addFill();
                break;
            case "Dot":
                System.out.println("Arrived in Dot");
                this.addState();
                this.addOrigin();
                this.addFill();
                break;
            case "Model":
                // TODO: To be implemented
            default:
                ErrorHandling.printError("Error: Invalid type");
                break;
        }
    }

    public boolean checkAttributes(String attributeName, Type type) {
        if (!attributes.containsKey(attributeName)) {
            ErrorHandling.printError("Error: Attribute not defined");
            return false;
        }
        
        List<Type> allowedTypes = attributes.get(attributeName);
        if (allowedTypes == null || !allowedTypes.contains(type)) {
            ErrorHandling.printError("Error: Invalid type for the attribute");
            return false;
        }
        
        return true;
    }
    
    ////////////////////////////////////////////////////////////////////

    private void addState() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("state", typesAllowed);
    }

    private void addOrigin() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new PointType()));
        this.attributes.put("origin", typesAllowed);
    }

    private void addLength() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new PointType()));
        this.attributes.put("length", typesAllowed);
    }

    private void addFill() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("fill", typesAllowed);
    }

    private void addStart() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new IntegerType()));
        this.attributes.put("start", typesAllowed);
    }

    private void addExtent() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new IntegerType()));
        this.attributes.put("extent", typesAllowed);
    }

    private void addOutline() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("outline", typesAllowed);
    }

    private void addPoints() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new PointType()));
        this.attributes.put("points", typesAllowed);
    }

    private void addText() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("text", typesAllowed);
    }

}
