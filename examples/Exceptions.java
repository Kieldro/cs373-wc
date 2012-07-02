// ---------------
// Exceptions.java
// ---------------

final class Exceptions {
    private static int f (boolean b) throws IllegalAccessException {
        if (b)
            throw new IllegalAccessException("abc");
        return 0;}

    public static void main (String[] args) {
        System.out.println("Exceptions.java");

        try {
            assert f(false) == 0;
            }
        catch (IllegalAccessException e) {
            assert false;}

        try {
            assert f(true) == 1;
            assert false;
            }
        catch (IllegalAccessException e) {
//          assert e                == "java.lang.IllegalAccessException: abc";   // incomparable types: java.lang.IllegalAccessException and java.lang.String
            assert e.toString()     != "java.lang.IllegalAccessException: abc";
            assert e.toString().equals("java.lang.IllegalAccessException: abc");}

        assert IllegalAccessException.class.getSuperclass() == Exception.class;
        assert              Exception.class.getSuperclass() == Throwable.class;
        assert              Throwable.class.getSuperclass() ==    Object.class;
        assert              Object.class.getSuperclass()    ==    null;

        Exception p = new IllegalAccessException();
        Throwable q = new Exception();
        Object    r = new Throwable();

        System.out.println("Done.");}}
