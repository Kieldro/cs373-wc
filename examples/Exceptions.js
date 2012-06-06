// -------------
// Exceptions.js
// -------------

function assert (b) {
    if (!b) {
        throw "Assertion Error"}}

function f (b) {
    if (b) {
        throw "Error"}
    return 0;}

print("Exceptions.js\n");

try {
    assert(f(false) == 0);}
catch (e) {
    assert(false);}

try {
    assert(f(true) == 0);}
catch (e) {
    assert(e == "Error");}

print("Done.\n");
