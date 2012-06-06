// ---------------
// Assertions.java
// ---------------

/*
Turn ON assertions at run time with -ea.
% javac -Xlint Assertions.java
% java  -ea    Assertions
*/

final class Assertions {
    public static int cycle_length (int n) {
        assert n > 0;
        int c = 0;
        while (n > 1) {
            if ((n % 2) == 0)
                n = n / 2;
            else
                n = (3 * n) + 1;
            ++c;}
        assert c > 0;
        return c;}

    public static void main (String[] args) {
        System.out.println("Assertions.java");

        assert cycle_length(1) == 1;
        assert cycle_length(5) == 6;

        System.out.println("Done.");}}

/*
Assertions.java
Exception in thread "main" java.lang.AssertionError
	at Assertions.cycle_length(Assertions.java:21)
	at Assertions.main(Assertions.java:27)
*/
