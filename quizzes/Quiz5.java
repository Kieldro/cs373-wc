/*
CS373: Quiz #5 (9 pts)
*/

/* -----------------------------------------------------------------------
1. What is the output of the following program?
   (9 pts)

m1 f1 f2 m2 m4 m5
m1 f1 m3 m4 m5
*/

class Quiz5 {
    static void f (boolean b) {
        System.out.print("f1 ");
        if (b)
            throw new RuntimeException("abc");
        System.out.print("f2 ");}

    public static void main (String[] args) {
        try {
            System.out.print("m1 ");
            f(false);
            System.out.print("m2 ");}
        catch (RuntimeException e) {
            System.out.print("m3 ");}
        finally {
            System.out.print("m4 ");}
        System.out.print("m5 ");
        System.out.println();

        try {
            System.out.print("m1 ");
            f(true);
            System.out.print("m2 ");}
        catch (RuntimeException e) {
            System.out.print("m3 ");}
        finally {
            System.out.print("m4 ");}
        System.out.print("m5 ");
        System.out.println();}}
