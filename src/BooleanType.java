public class BooleanType extends Type {
    public BooleanType() {
        super("Boolean");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
