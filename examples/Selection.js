// ------------
// Selection.js
// ------------

function assert (b) {
    if (!b) {
        throw "Assertion Error"}}

function f (n) {
    if (n < 0)
        m = -1;
    else if (n > 0)
        m = 1;
    else
        m = 0;
    return m;}

function g (n) {
    return (n < 0) ? -1 : (n > 0) ? 1 : 0;}

function h (n) {
    switch (n) {
        case -2:
            m = -1;
            break;
        case 3:
            m = 1;
            break;
        default:
            m = 0;
            break;}
    return m;}

print("Selection.js\n");

assert(f(-2) == -1);
assert(f( 0) ==  0);
assert(f( 3) ==  1);

assert(g(-2) == -1);
assert(g( 0) ==  0);
assert(g( 3) ==  1);

assert(h(-2) == -1);
assert(h( 0) ==  0);
assert(h( 3) ==  1);

print("Done.\n");
