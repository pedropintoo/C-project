public class AGLVector {
    private AGLPoint start;
    private AGLPoint end;

    public AGLVector() {
        this.start = new AGLPoint();
        this.end = new AGLPoint();
    }

    public AGLVector(AGLPoint start, AGLPoint end) {
        this.start = start;
        this.end = end;
    }

    public AGLPoint getStart() {
        return start;
    }

    public AGLPoint getEnd() {
        return end;
    }

    public void setStart(AGLPoint start) {
        this.start = start;
    }

    public void setEnd(AGLPoint end) {
        this.end = end;
    }

    public double getLength() {
        return Math.sqrt(Math.pow(end.getX() - start.getX(), 2) + Math.pow(end.getY() - start.getY(), 2));
    }

    public AGLPoint getDifference() {
        return new AGLPoint(end.getX() - start.getX(), end.getY() - start.getY());
    }
}
