public class ArrayType extends Type {

    private Type elementType;
    private int length;

    public ArrayType(String elementTypeName) {
        super(elementTypeName);
        
        String firstChild = elementTypeName.split("<")[0];

        // check subtypes
        if (!firstChild.equals(elementTypeName)) {
            int start = elementTypeName.indexOf('<') + 1;
            int end = elementTypeName.lastIndexOf('>');
            String innerType = elementTypeName.substring(start, end).trim();
            this.elementType = new ArrayType(innerType);
            return;
        }

        switch (firstChild) {
            case "Integer":
                this.elementType = new IntegerType();
                break;
            
            case "String":
                this.elementType = new StringType();
                break;

            case "Point":
                this.elementType = new PointType();
                break;
        }
    }

    @Override
    public String name() {
        
        if (elementType instanceof ArrayType) {
            return "Array<" + elementType.name() + ">";
        }
        return name;
    }

    public Type getElementType() {
        return elementType;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public int getLength() {
        return length;
    }
}
