from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring
from Export import buildTree
from Models import Crisis, Organization, Person

import sys, operator

def runExport():
	crisisList = []
	orgList = []
	personList = []


	crises = Crisis.all()
	for c in crises:
		crisisList.append(c)

	organizations = Organization.all()
	for o in organizations:
		orgList.append(o)

	people = Person.all()
	for p in people:
		personList.append(p)

	ans = buildTree(crisisList, orgList, personList)
	tree = ElementTree(ans)
	outfile = tostring(ans)
	return outfile




