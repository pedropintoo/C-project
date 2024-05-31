public class ModelType extends Type {
    public ModelType(String name) {
        super(name);
    }

    @Override
    public boolean isNumeric() {
        return true;
    }
}
