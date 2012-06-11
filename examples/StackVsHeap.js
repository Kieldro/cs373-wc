// --------------
// StackVsHeap.js
// --------------

function assert (b) {
    if (!b) {
        throw "Assertion Error";}}

function f (n) {
    if (n == 0)
        return 0;
    return 1 + f(n - 1);}

print("StackVsHeap2.js\n");

assert(f(123456) == 123456);

//assert(f(1234567) == 1234567);
//assert(false);

print("Done.\n");

/*
2012-06-11 08:48:49.241 jrunscript[1161:5f07] Unable to obtain JNIEnv for context:0
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at sun.org.mozilla.javascript.internal.Interpreter.initFrame(Interpreter.java:3768)
	at sun.org.mozilla.javascript.internal.Interpreter.interpretLoop(Interpreter.java:3029)
	at sun.org.mozilla.javascript.internal.Interpreter.interpret(Interpreter.java:2239)
	at sun.org.mozilla.javascript.internal.InterpretedFunction.call(InterpretedFunction.java:138)
	at sun.org.mozilla.javascript.internal.ContextFactory.doTopCall(ContextFactory.java:323)
	at com.sun.script.javascript.RhinoScriptEngine$1.superDoTopCall(RhinoScriptEngine.java:92)
	at com.sun.script.javascript.RhinoScriptEngine$1.doTopCall(RhinoScriptEngine.java:85)
	at sun.org.mozilla.javascript.internal.ScriptRuntime.doTopCall(ScriptRuntime.java:2747)
	at sun.org.mozilla.javascript.internal.InterpretedFunction.exec(InterpretedFunction.java:149)
	at sun.org.mozilla.javascript.internal.Context.evaluateReader(Context.java:1169)
	at com.sun.script.javascript.RhinoScriptEngine.eval(RhinoScriptEngine.java:149)
	at javax.script.AbstractScriptEngine.eval(AbstractScriptEngine.java:232)
	at com.sun.tools.script.shell.Main.evaluateReader(Main.java:314)
	at com.sun.tools.script.shell.Main.evaluateStream(Main.java:350)
	at com.sun.tools.script.shell.Main.processSource(Main.java:267)
	at com.sun.tools.script.shell.Main.access$100(Main.java:19)
	at com.sun.tools.script.shell.Main$2.run(Main.java:182)
	at com.sun.tools.script.shell.Main.main(Main.java:30)
*/
