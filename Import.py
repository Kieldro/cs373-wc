import sys #remove this later
from xml.etree.ElementTree import Element, SubElement, parse

def buildModels(tree) :
	root = tree.getroot()
	crisesRoot = tree.find('crises')
	organizationsRoot = tree.find('organizations')
	peopleRoot = tree.find('people')
	
	crisesList = crisesRoot.getchildren()
	for crisis in crisesList :
		print crisis.attrib['id'] ,
		
	organizationsList = organizationsRoot.getchildren()
	for org in organizationsList :
		print org.attrib['id'] ,
	
	peopleList = peopleRoot.getchildren()
	for person in peopleList :
		print person.attrib['id'] ,
		
	#return cList, oList, pList
		
def createCrisis(rootElem) :
	d = {}
	c = Crisis(**d)

if __name__ == "__main__" :
	tree = parse(sys.stdin)
	buildModels(tree)
