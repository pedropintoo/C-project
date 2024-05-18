public class IntegerType extends Type {
    public IntegerType() {
        super("Integer");
    }

    @Override
    public boolean isNumeric() {
        return true;
    }
}
