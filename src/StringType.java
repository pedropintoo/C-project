public class StringType extends Type {
    public StringType() {
        super("String");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
