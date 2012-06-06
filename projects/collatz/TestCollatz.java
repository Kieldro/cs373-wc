// ---------------------------------
// projects/collatz/TestCollatz.java
// Copyright (C) 2011
// Glenn P. Downing
// ---------------------------------

/*
To test the program:
    % locate junit4-4.8
    /usr/share/java/junit4-4.8.1.jar
    % setenv CLASSPATH .:/usr/share/java/junit4-4.8.1.jar
    % javac -Xlint TestCollatz.java
    % java  -ea    TestCollatz > TestCollatz.java.out
*/

// -------
// imports
// -------

import java.io.IOException;
import java.io.StringWriter;
import java.io.Writer;

import java.util.Scanner;

import junit.framework.Assert;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

// -----------
// TestCollatz
// -----------

public final class TestCollatz extends TestCase {
    // ----
    // read
    // ----

    public void testRead () {
        final Scanner r   = new Scanner("1 10\n");
        final int     a[] = {0, 0};
        final boolean b   = Collatz.read(r, a);
    	Assert.assertTrue(b    == true);
    	Assert.assertTrue(a[0] ==    1);
    	Assert.assertTrue(a[1] ==   10);}

    // ----
    // eval
    // ----

    public void testEval1 () {
        final int v = Collatz.eval(1, 10);
    	Assert.assertTrue(v == 20);}

    public void testEval2 () {
        final int v = Collatz.eval(100, 200);
    	Assert.assertTrue(v == 125);}

    public void testEval3 () {
        final int v = Collatz.eval(201, 210);
    	Assert.assertTrue(v == 89);}

    public void testEval4 () {
        final int v = Collatz.eval(900, 1000);
    	Assert.assertTrue(v == 174);}

    // -----
    // print
    // -----

    public void testPrint () throws IOException {
        final Writer w = new StringWriter();
        Collatz.print(w, 1, 10, 20);
    	Assert.assertTrue(w.toString().equals("1 10 20\n"));}

    // -----
    // solve
    // -----

    public void testSolve () throws IOException {
        final Scanner r = new Scanner("1 10\n100 200\n201 210\n900 1000\n");
        final Writer  w = new StringWriter();
        Collatz.solve(r, w);
    	Assert.assertTrue(w.toString().equals("1 10 20\n100 200 125\n201 210 89\n900 1000 174\n"));}

    // ----
    // main
    // ----

    public static void main (String[] args) {
        System.out.println("TestCollatz.java");
        TestRunner.run(new TestSuite(TestCollatz.class));
        System.out.println("Done.");}}
