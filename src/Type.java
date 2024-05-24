import java.util.List;

public abstract class Type {
    protected final String name;
    // private static final List<Type> types = List.of(new StringType(), new PointType(), new NumberType(),
    //         new VectorType(), new IntegerType());

    protected Type(String name) {
        assert name != null;
        this.name = name;
    }

    public String name() {
        return name;
    }

    public boolean comformsTo(Type other) {
        return name.equals(other.name());
    }

    public boolean isNumeric() {
        return false;
    }

    @Override
    public String toString() {
        return name;
    }

    // Check if String is a valid type and return the corresponding Type object
    // public static Type getType(String name) {
    //     for (Type type : types) {
    //         if (type.getName().equals(name)) {
    //             return type;
    //         }
    //     }
    //     return null;
    // }
}
