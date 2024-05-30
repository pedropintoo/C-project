import java.util.ArrayList;
import java.util.List;

public class EnumType extends Type {
    private List<EnumValueType> enums;

    public EnumType() {
        super("Enum");
        this.enums = new ArrayList<>();
    }

    @Override
    public boolean isNumeric() {
        return false;
    }

    public void addEnum(EnumValueType enumValue) {
        this.enums.add(enumValue);
    }

    public List<EnumValueType> getEnums() {
        return enums;
    }
}
