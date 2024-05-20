public class VectorType extends Type {
    public VectorType() {
        super("Vector");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
