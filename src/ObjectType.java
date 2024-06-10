import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ObjectType extends Type {
    private Map<String, List<Type>> attributes;
    private List<ObjectType> subTypes;
    public Map<String, Symbol> symbolModelTable;

    protected ObjectType(String name) {
        super(name);
        this.attributes = new HashMap<String, List<Type>>();
        this.subTypes = new ArrayList<ObjectType>();
        switch (name) {
            case "Line":
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addFill();
                break;
            case "Polyline":
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                break;
            case "Spline":
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                break;
            case "Polygon":
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                this.addOutline();
                break;
            case "Blob":
                this.addState();
                this.addOrigin();
                this.addPoints();
                this.addFill();
                this.addOutline();
                break;
            case "Rectangle":
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addFill();
                break;
            case "Ellipse":
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addFill();
                break;
            case "Arc":
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addStart();
                this.addExtent();
                this.addOutline();
                break;
            case "ArcChord":
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addStart();
                this.addExtent();
                this.addFill();
                this.addOutline();
                break;
            case "PieSlice":
                this.addState();
                this.addOrigin();
                this.addLength();
                this.addStart();
                this.addExtent();
                this.addFill();
                break;
            case "Text":
                this.addState();
                this.addOrigin();
                this.addText();
                this.addFill();
                break;
            case "Dot":
                this.addState();
                this.addOrigin();
                this.addFill();
                break;
            case "Model":
                this.addState();
                this.addOrigin();
                this.addSubTypes();
                break;
            case "Script":
                break;
            case "View":
                this.addWidth();
                this.addHeight();
                this.addTitle();
                this.addOx();
                this.addOy();
                this.addBackground();
                break;
            default:
                // check if exists a modelType with the same name
                Symbol model = AGLParser.symbolTable.get(name);

                if (model == null || !(model.type instanceof ModelType)) {
                    ErrorHandling.printError("Error: Invalid type!");
                    break;
                }

                this.addState();
                this.addOrigin();
                
                // This object should have the same symbolModelTable as the modelType    
                ModelType modelType = (ModelType) model.type;
                this.symbolModelTable = modelType.symbolModelTable;
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

    public boolean checkSubType(ObjectType subType) {
        if (!subTypes.contains(subType)) {
            ErrorHandling.printError("That subtype is not allowed");
            return false;
        }
        return true;
    }

    public Map<String, List<Type>> getAttributes() {
        return attributes;
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
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new ArrayType("Point")));
        this.attributes.put("points", typesAllowed);
    }

    private void addText() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("text", typesAllowed);
    }

    private void addWidth() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new IntegerType()));
        this.attributes.put("width", typesAllowed);
    }

    private void addHeight() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new IntegerType()));
        this.attributes.put("height", typesAllowed); 
    }

    private void addTitle() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("title", typesAllowed);
    }

    private void addBackground() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new StringType()));
        this.attributes.put("background", typesAllowed);
    }

    private void addOx() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new IntegerType()));
        this.attributes.put("Ox", typesAllowed);
    }

    private void addOy() {
        ArrayList<Type> typesAllowed = new ArrayList<>(List.of(new IntegerType()));
        this.attributes.put("Oy", typesAllowed);
    }
    
    private void addSubTypes() {
        this.subTypes.add(new ObjectType("Line"));
        this.subTypes.add(new ObjectType("Polyline"));
        this.subTypes.add(new ObjectType("Spline"));
        this.subTypes.add(new ObjectType("Polygon"));
        this.subTypes.add(new ObjectType("Blob"));
        this.subTypes.add(new ObjectType("Rectangle"));
        this.subTypes.add(new ObjectType("Ellipse"));
        this.subTypes.add(new ObjectType("Arc"));
        this.subTypes.add(new ObjectType("ArcChord"));
        this.subTypes.add(new ObjectType("PieSlice"));
        this.subTypes.add(new ObjectType("Text"));
        this.subTypes.add(new ObjectType("Dot"));
    }

    public Map<String, Symbol> getSymbolModelTable() {
        return symbolModelTable;
    }

  
}              