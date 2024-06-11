public class TimeType extends Type {
    public TimeType() {
        super("Time");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
