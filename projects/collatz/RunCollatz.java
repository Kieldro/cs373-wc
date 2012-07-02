// --------------------------------
// projects/collatz/RunCollatz.java
// Copyright (C) 2011
// Glenn P. Downing
// --------------------------------

/*
To run the program:
    % javac -Xlint RunCollatz.java
    % java  -ea    RunCollatz < RunCollatz.in > RunCollatz.out

To document the program:
    % javadoc -d html -private Collatz.java
*/

// -------
// imports
// -------

import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

import java.util.Scanner;

// ----------
// RunCollatz
// ----------

final class RunCollatz {
    public static void main (String[] args) throws IOException {
        final Scanner r = new Scanner(System.in);
        final Writer  w = new PrintWriter(System.out);
        Collatz.solve(r, w);}}
