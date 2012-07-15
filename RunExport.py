# -*- coding: utf-8 -*-
from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring, dump
from Export import buildTree
from Models import *

import sys, operator, StringIO

def runExport():
	"""
	gets everything that has been added to the datastore and 
	exports it in the form of a valid xml instance
	return a string containing the xml instance
	"""
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
	outstring = StringIO.StringIO()
	tree.write(outstring)
	return outstring.getvalue()

