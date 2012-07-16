# file variables
source="WC.py"

#dev_appserver.py .


# multicomment cannot have leading spaces

export PYTHONPATH=~/cs373/WCAppspot/google_appengine/:	\
					~/cs373/WCAppspot/google_appengine/lib/webob_1_1_1/
echo RUNNING PYDOC...;	pydoc -w ./
mv *.html pydoc/
<<MULTICOMMENT
echo GENERATING COMMIT LOG...;	git log > WC2.log

echo ZIPPING FILES...
zip WC2 README.txt pydoc/ *.py app.yaml WC2.log TestWC2.out test/TestWC2.py \
		WC2.pdf UML.svg WC2.xml

turnin --submit hychyc07 cs373pj4 WC2.zip
turnin --list	hychyc07 cs373pj4 WC2.zip
turnin --verify hychyc07 cs373pj4 WC2.zip
MULTICOMMENT
