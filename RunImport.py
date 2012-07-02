from xml.etree.ElementTree import Element, SubElement
from Import import parse, buildModels

import sys, operator, Models

def runImport(filestring):
	tree = parse(filestring)
	crises, organizations, people = buildModels(tree)

	for c in crises:
		Crisis(c).put()

	for o in organizations:
		Organization(o).put()

	for p in people:
		Person(p).put()
