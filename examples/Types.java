// ----------
// Types.java
// ----------

interface I<T> {
    void f ();}

class A<T> implements I<T> {
    private int    i;
    private double d;
    private T      x;

    public void f () {}}

class B<T> extends A<T>
    {}

enum Color {red, green, blue}

final class Types {
    public static void main (String[] args) {
        System.out.println("Types.java");

        boolean b = false;                                 // 1 bit
        char    c = 'a';                                   // 2 bytes

        byte bt = 2;                                       // 1 byte
        assert Byte.MIN_VALUE == -128;
        assert Byte.MAX_VALUE ==  127;

        short s = 2;                                       // 2 bytes
        assert Short.MIN_VALUE == -32768;
        assert Short.MAX_VALUE ==  32767;

        int i = 2;                                         // 4 bytes
        assert Integer.MIN_VALUE == -2147483648;
        assert Integer.MAX_VALUE ==  2147483647;

        long j = 2L;                                       // 8 bytes
        assert Long.MIN_VALUE == -9223372036854775808L;
        assert Long.MAX_VALUE ==  9223372036854775807L;

        float f = 2.3F;                                    // 4 bytes
        assert Float.MAX_VALUE == 3.4028235E38F;
        assert Float.MIN_VALUE == 1.4E-45F;

        double d = 2.3;                                    // 8 bytes
        assert Double.MAX_VALUE == 1.7976931348623157E308;
        assert Double.MIN_VALUE == 4.9E-324;

        String st = "abc";

        int[] a = {2, 3, 4};

        I<Integer> x = new A<Integer>();
        assert x instanceof A;
        assert x instanceof I;
        assert x instanceof Object;

        I<Double> y = new B<Double>();
        assert y instanceof B;
        assert y instanceof A;
        assert y instanceof I;
        assert y instanceof Object;

        assert I.class.isInterface();
        assert I.class.getInterfaces().length == 0;
        assert I.class.getSuperclass()        == null;

        assert !A.class.isInterface();
        assert A.class.getInterfaces().length == 1;
        assert A.class.getInterfaces()[0]     == I.class;
        assert A.class.getSuperclass()        == Object.class;

        Color c1 = Color.red;
        Color c2 = Color.green;
        Color c3 = Color.blue;

        System.out.println("Done.");}}
