public class NumberType extends Type {
    public NumberType() {
        super("Number");
    }

    @Override
    public boolean isNumeric() {
        return true;
    }
}
