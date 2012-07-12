from xml.etree.ElementTree import Element, SubElement
from Models import Crisis, Organization, Person
from Export import buildTree	

def build_tester_tree():
	cmods = []
	omods = []
	pmods = []
	for x in range(5):
		cmods.append(Crisis(id = str(x),
	name = 'n',
	knd = 'k',
	location = 'l',
	state = 's',
	city = 'c',
	country = 'c',
	image = ['i1', '12'],
	video = ['v1', 'v2'],
	network = ['n1', 'n2'],
	link = ['l1', 'l2'],
	date ='d1',
	startDate = '2012-7-1',
	endDate = '2012-7-1',
	additional = 'a',
	humanImpact = 'hi',
	ecoImpact = 'ei',
	resources = 'r',
	waysToHelpText = ['wtht1','wtht2'],
	waysToHelpLinks = ['wthl1', 'wthl2'],
	orgs = ['o1', 'o2'],
	people = ['p1', 'p2']))
	
	for y in range(5):
		omods.append(Crisis(id = str(y),
	name = 'n',
	knd = 'k',
	location = 'l',
	state = 's',
	city = 'c',
	country = 'c',
	image = ['i1', '12'],
	video = ['v1', 'v2'],
	network = ['n1', 'n2'],
	link = ['l1', 'l2'],
	history = 'h',
	contactInfoText = ['cit1','cit2'],
	contactInfoLinks = ['cil1', 'cil2'],
	crises = ['c1', 'c2'],
	people = ['p1', 'p2']))
	  
	  
	for z in range(5):
		pmods.append(Crisis(id = str(z),
	name = 'n',
	knd = 'k',
	location = 'l',
	state = 's',
	city = 'c',
	country = 'c',
	image = ['i1', '12'],
	video = ['v1', 'v2'],
	network = ['n1', 'n2'],
	link = ['l1', 'l2'],
	orgs = ['o1', 'o2'],
	crises = ['c1', 'c2']))

	return [cmods, omods, pmods]
