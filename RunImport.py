from xml.etree.ElementTree import Element, SubElement, parse
from Import import buildModels
from Models import Crisis, Organization, Person
import StringIO

import sys, operator

def runImport(filestring):
	xmlstring = StringIO.StringIO(filestring)
	tree = parse(xmlstring)
	buildModels(tree)
