# file variables
python=true

source="PFD.py"
unit="TestPFD.py"
inFile="RunPFD.in"
outFile="RunPFD.out"
noError=false


echo RUNNING UNIT TESTS...
python $unit #&> $unit.out

if ([ $? == 0 ]); then
	echo RUNNING SOURCE...
	python $source < $inFile #> $outFile

<<MULTICOMMENT
	echo CHECKING OUTPUT...
	diff -lc RunPFD.out RunPFD.in

	echo GENERATING COMMIT LOG...
	git log > PFD.log

	echo UPDATING SPHERE FILE...
	cp $source Sphere$source

	echo RUNNING PYDOC...
	pydoc -w ./$source

	#echo ZIPPING FILE...
	
	
# multicomment cannot have leading spaces
MULTICOMMENT

fi
