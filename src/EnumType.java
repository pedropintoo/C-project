public class EnumType extends Type {
    public EnumType() {
        super("Enum");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
