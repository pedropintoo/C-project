public abstract class Type {
    protected final String name;

    protected Type(String name) {
        assert name != null;
        this.name = name;
    }

    public String name() {
        return name;
    }

    public boolean conformsTo(Type other) {
        return name().equals(other.name());
    }

    public boolean isNumeric() {
        return false;
    }

    @Override
    public String toString() {
        return name;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Type other = (Type) obj;
        if (name == null) {
            if (other.name != null)
                return false;
        } else if (!name.equals(other.name))
            return false;
        return true;
    }

}
