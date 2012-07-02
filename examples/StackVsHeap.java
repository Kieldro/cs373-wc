// ----------------
// StackVsHeap.java
// ----------------

final class StackVsHeap {
    private static int f (int n) {
        if (n == 0)
            return 0;
        return 1 + f(n - 1);}

    public static void main (String[] args) {
        System.out.println("StackVsHeap.java");

        try {
            assert f(1234) == 1234;}
        catch (StackOverflowError e) {
            assert false;}

        try {
            assert f(12345) == 12345;
            assert false;}
        catch (StackOverflowError e) {
            assert e.toString().equals("java.lang.StackOverflowError");}

        try {
            final int[] a = new int[12345678];}
        catch (OutOfMemoryError e) {
            assert false;}

        try {
            final int[] a = new int[123456789];
            assert false;}
        catch (OutOfMemoryError e) {
            assert e.toString().equals("java.lang.OutOfMemoryError: Java heap space");}

        System.out.println("Done.");}}
