# -*- coding: utf-8 -*-
# -------------
# TestExport.py
# -------------
  
# -------
# imports
# -------

from xml.etree.ElementTree import Element, SubElement
from Models.py import Crisis, Organization, Person
from Export.py

class TestExport (unittest.TestCase) :

global cmods, omods, pmods = [], [], [] 
cmods.append(new Crisis.


def test_build_tree() :
  for x in range(5):
        cmods.append(Crisis(ID = x,
	name = 'n',
	kind = 'k',
	location = 'l',
	state = 's',
	city = 'c',
	country = 'c',
	image = ['i1', '12'],
	video = ['v1', 'v2'],
	network = ['n1', 'n2'],
	link = ['l1', 'l2'],
	date =['d1', 'd2'],
	startDate = '2012-7-1',
	endDate = '2012-7-1',
	additional = 'a',
	humanImpact = 'hi',
	ecoImpact = 'ei',
	resources = 'r',
	waysToHelpText = ['wtht1','wtht2'],
	waysToHelpLinks = ['wthl1. wthl2'],
	orgs = [o1, o2],
	people = [p1, p2])
	
  for x in range(5):
        omods.append(Crisis(ID = x,
	name = 'n',
	kind = 'k',
	location = 'l',
	state = 's',
	city = 'c',
	country = 'c',
	image = ['i1', '12'],
	video = ['v1', 'v2'],
	network = ['n1', 'n2'],
	link = ['l1', 'l2'],
	history = 'h'
	contactInfoText = ['cit1','cit2'],
	contactInfoLinks = ['cil1. cil2'],
	crises = [o1, o2],
	people = [p1, p2])

  for x in range(5):
        pmods.append(Crisis(ID = x,
	  name = 'n',
	  kind = 'k',
	  location = 'l',
	  state = 's',
	  city = 'c',
	  country = 'c',
	  image = ['i1', '12'],
	  video = ['v1', 'v2'],
	  network = ['n1', 'n2'],
	  link = ['l1', 'l2'],
	  crises = [o1, o2],
	  orgs = [p1, p2])


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."