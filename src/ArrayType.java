public class ArrayType extends Type {
    public ArrayType() {
        super("Array");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
