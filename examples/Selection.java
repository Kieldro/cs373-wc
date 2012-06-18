// --------------
// Selection.java
// --------------

final class Selection {
    private static int f (int n) {
        final int m;
        if (n < 0)
            m = -1;
        else if (n > 0)
            m = 1;
        else
            m = 0;
        return m;}

    private static int g (int n) {
        return (n < 0) ? -1 : (n > 0) ? 1 : 0;}

    private static int h (int n) {
        final int m;
        switch (n) {
            case -2:
                m = -1;
                break;
            case 3:
                m = 1;
                break;
            default:
                m = 0;
                break;}
        return m;}

    public static void main (String[] args) {
        System.out.println("Selection.java");

        assert f(-2) == -1;
        assert f( 0) ==  0;
        assert f( 3) ==  1;

        assert g(-2) == -1;
        assert g( 0) ==  0;
        assert g( 3) ==  1;

        assert h(-2) == -1;
        assert h( 0) ==  0;
        assert h( 3) ==  1;

        System.out.println("Done.");}}
