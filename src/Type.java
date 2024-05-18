public abstract class Type {
    protected final String name;

    protected Type(String name) {
        assert name != null;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public boolean comformsTo(Type other) {
        return name.equals(other.getName());
    }

    public boolean isNumeric() {
        return false;
    }

    @Override
    public String toString() {
        return name;
    }
}
