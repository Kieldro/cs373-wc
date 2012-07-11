# file variables
source="WC.py"


#echo RUNNING UNIT TESTS...

dev_appserver.py .

<<MULTICOMMENT
# multicomment cannot have leading spaces
echo RUNNING PYDOC...;	pydoc -w ./$source

echo GENERATING COMMIT LOG...;	git log > WC2.log

echo ZIPPING FILES...
zip WC2 README.txt *.html *.py app.yaml WC2.log TestWC2.out test/TestWC2.py \
		WC2.pdf UML.svg WC2.xml

turnin --submit hychyc07 cs373pj4 WC2.zip
turnin --list	hychyc07 cs373pj4 WC2.zip
turnin --verify hychyc07 cs373pj4 WC2.zip
MULTICOMMENT

