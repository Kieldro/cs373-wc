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
	tempList = []
	crises = Crisis.all()
	sorted_crises = sorted(crises, key=lambda crisis : crisis.ID)
	for x in sorted_crises:
		crisisList.append(x)

	organizations = Organization.all()
	sorted_orgs = sorted(organizations, key=lambda crisis : crisis.ID)
	for x in sorted_orgs:
		orgList.append(x)

	people = Person.all()
	sorted_people = sorted(people, key=lambda crisis : crisis.ID)
	for x in sorted_people:
		personList.append(x)

	ans = buildTree(crisisList, orgList, personList)
	tree = ElementTree(ans)
	outstring = StringIO.StringIO()
	tree.write(outstring)
	return outstring.getvalue()

