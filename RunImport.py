from xml.etree.ElementTree import Element, SubElement
from Import import parse, buildModels
from Models import Crisis, Organization, Person
import StringIO

import sys, operator

def runImport(filestring):
	stuff = StringIO.StringIO(filestring)
	tree = parse(stuff)
	crises, organizations, people = buildModels(tree)

	for c in crises:
		c.put()


	for o in organizations:
		o.put()

	for p in people:
		p.put()
