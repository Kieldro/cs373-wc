import sys
from elementtree import ElementTree


def readFile(filename) :
	tree = parse(filename)
	return tree
	
def importData(filename) :
	tree = readFile(filename) 
	
	root = tree.getRoot()
	
	crisesRoot = tree.find("crises")
	organizationsRoot = tree.find("organizations")
	peopleRoot = tree.find("people")
	
	crisesList = crisesRoot.findall("crisis")
	for crisis in crisesList :
		print crisis.get("id") ,
		
		
if __name__ == "__main__" :
	importData(sys.stdin)
