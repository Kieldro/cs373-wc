// -------------
// Assertions.js
// -------------

function assert (b) {
    if (!b) {
        throw "Assertion Error"}}

function inc (v) {
    return v + 1;}

print("Assertions.js\n");

assert(inc(2) == 3);
assert(inc(2) == 4);

print("Done.\n");

/*
Assertions.js
script error in file Assertions.js : sun.org.mozilla.javascript.internal.JavaScriptException: Assertion Error (Assertions.js#7) in Assertions.js at line number 7
*/
