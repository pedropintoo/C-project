public class PointType extends Type {
    public PointType() {
        super("Point");
    }

    @Override
    public boolean isNumeric() {
        return false;
    }
}
