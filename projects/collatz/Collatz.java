// -----------------------------
// projects/collatz/Collatz.java
// Copyright (C) 2011
// Glenn P. Downing
// -----------------------------

import java.io.IOException;
import java.io.Writer;

import java.util.Scanner;

public final class Collatz {
    // ----
    // read
    // ----

    /**
     * reads two ints into a[0] and a[1]
     * @param r a  java.util.Scanner
     * @param a an array of int
     * @return true if that succeeds, false otherwise
     */
    public static boolean read (Scanner r, int[] a) {
        if (!r.hasNextInt())
            return false;
        a[0] = r.nextInt();
        a[1] = r.nextInt();
        assert a[0] > 0;
        assert a[1] > 0;
        return true;}

    // ----
    // eval
    // ----

    /**
     * @param i the beginning of the range, inclusive
     * @param j the end       of the range, inclusive
     * @return the max cycle length in the range [i, j]
     */
    public static int eval (int i, int j) {
        assert i > 0;
        assert j > 0;
        // <your code>
        int v = 1;
        assert v > 0;
        return v;}

    // -----
    // print
    // -----

    /**
     * prints the values of i, j, and v
     * @param w a java.io.Writer
     * @param i the beginning of the range, inclusive
     * @param j the end       of the range, inclusive
     * @param v the max cycle length
     */
    public static void print (Writer w, int i, int j, int v) throws IOException {
        assert i > 0;
        assert j > 0;
        assert v > 0;
        w.write(i + " " + j + " " + v + "\n");
        w.flush();}

    // -----
    // solve
    // -----

    /**
     * @param r a java.util.Scanner
     * @param w a java.io.Writer
     */
    public static void solve (Scanner r, Writer w) throws IOException {
        final int[] a = {0, 0};
        while (Collatz.read(r, a)) {
            final int v = Collatz.eval(a[0], a[1]);
            Collatz.print(w, a[0], a[1], v);}}}
