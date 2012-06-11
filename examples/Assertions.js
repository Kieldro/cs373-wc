// -------------
// Assertions.js
// -------------

function assert (b) {
    if (!b) {
        throw "Assertion Error";}}

function cycle_length (n) {
    assert(n > 0);
    c = 0;
    while (n > 1) {
        if ((n % 2) == 0)
            n = n / 2;
        else
            n = (3 * n) + 1;
        ++c;}
    assert(c > 0);
    return c;}

print("Assertions.js\n");

assert(cycle_length(1) == 1);
assert(cycle_length(5) == 6);

print("Done.\n");

/*
Assertions.js
script error in file Assertions.js : sun.org.mozilla.javascript.internal.JavaScriptException: Assertion Error (Assertions.js#7) in Assertions.js at line number 7
*/
