public class ArrayType extends Type {

    private Type elementType;

    public ArrayType(String elementTypeName) {
        super("Array");
        
        String firstChild = elementTypeName.split("<")[0];

        switch (firstChild) {
            
            case "Point":
                this.elementType = new PointType();
                break;

            case "Array":
                int start = elementTypeName.indexOf('<') + 1;
                int end = elementTypeName.lastIndexOf('>');
                System.out.println(elementTypeName);
                System.out.println("start: " + start + " end: " + end);
                String innerType = elementTypeName.substring(start, end).trim();
                System.out.println("---- " + innerType);
                this.elementType = new ArrayType(innerType);
                break;
        }
    }

    @Override
    public boolean isNumeric() {
        return false;
    }

    public Type getElementType() {
        return elementType;
    }
}
