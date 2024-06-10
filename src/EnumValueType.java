
public class EnumValueType extends Type {
    private String enumValue;

    public EnumValueType(String enumValue) {
        super("EnumValueType");
        this.enumValue = enumValue;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((enumValue == null) ? 0 : enumValue.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        EnumValueType other = (EnumValueType) obj;
        if (enumValue == null) {
            if (other.enumValue != null)
                return false;
        } else if (!enumValue.equals(other.enumValue))
            return false;
        return true;
    }

    @Override
    public boolean isNumeric() {
        return false;
    }

    public String getEnumValue() {
        return enumValue;
    }



}
