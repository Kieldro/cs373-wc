# file variables
source="WC.py"

dev_appserver.py .


# multicomment cannot have leading spaces
<<MULTICOMMENT
export PYTHONPATH=~/cs373/WCAppspot/google_appengine/:	~/cs373/WCAppspot/google_appengine/lib/webob_1_1_1/
echo RUNNING PYDOC...;	pydoc -w ./
mv *.html pydoc/
echo GENERATING COMMIT LOG...;	git log > WC3.log

echo ZIPPING FILES...
zip WC3 README.txt pydoc/*.html *.py app.yaml TestWC3.out test/TestWC3.py WC3.log WC3Presentation.pdf WC3Report.pdf WC3.xml

turnin --submit hychyc07 cs373pj5 WC3.zip
turnin --list	hychyc07 cs373pj5 WC3.zip
turnin --verify hychyc07 cs373pj5 WC3.zip
MULTICOMMENT


