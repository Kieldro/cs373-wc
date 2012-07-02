# -*- coding: utf-8 -*-

# -------------
# TestExport.py
# -------------

# -------
# imports
# -------

from xml.etree.ElementTree import Element, SubElement
from Models import Crisis, Organization, Person
from Export import buildTree

class TestExport (unittest.TestCase) :
	
	
  
	def build_tester_tree():
		cmods = []
		omods = []
		pmods = []
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
		waysToHelpLinks = ['wthl1', 'wthl2'],
		orgs = [o1, o2],
		people = [p1, p2]))
		
		for y in range(5):
			omods.append(Crisis(ID = y,
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
		history = 'h',
		contactInfoText = ['cit1','cit2'],
		contactInfoLinks = ['cil1', 'cil2'],
		crises = [o1, o2],
		people = [p1, p2]))
		  
		  
		for z in range(5):
			pmods.append(Crisis(ID = z,
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
		orgs = [p1, p2]))

		return [cmods, omods, pmods]

	# ----
	# test build tree
	# ----
	def test_build_tree1():
		try:
			cmods = []
			omods = []
			pmods = []
			cmods.append(Crisis(ID = 1))
			assert False
		except Exception:
			assert True

	def test_build_tree2():
		try:
			cmods, omods, pmods = build_tester_tree()
			root = buildTree(cmods, omods, pmods)
		except Exception:
			assert False

	def test_build_tree3():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)
		assert root[0].size() == 5
		assert root[1].size() == 5
		assert root[2].size() == 5
	  
	# ----
	# test build pages of type
	# ----
	def test_buildPagesofType1():
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[0]
		root2 = buildTree(cmods, omods, pmods)[0]
		buildPagesofType(root1, "crisis", cmods, buildCrisisPage)

		for x in range(len(cmods)) :
			SubElement(root2, "crisis")
			elements = buildCrisisPage(root2[x], cmods[x])		

			# add sub elements		
			for element in elements :
				root2[x].append(element)	

		assert root1 == root2

	def test_buildPagesofType2():
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[0]
		root2 = buildTree(cmods, omods, pmods)[0]
		buildPagesofType(root1, "crisis", cmods, buildCrisisPage)

		assert root1 != root2

	def test_buildPagesofType3():
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[1]
		root2 = buildTree(cmods, omods, pmods)[1]
		buildPagesofType(root1, "organization", omods, buildOrganizationPage)

		for x in range(len(omods)) :
			SubElement(root2, "organization")
			elements = buildOrganizationPage(root2[x], omods[x])		

			# add sub elements		
			for element in elements :
				root2[x].append(element)	

		assert root1 == root2

	def test_buildPagesofType4():
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[2]
		root2 = buildTree(cmods, omods, pmods)[2]
		buildPagesofType(root1, "person", pmods, buildPersonPage)

		for x in range(len(pmods)) :
			SubElement(root2, "person")
			elements = buildPersonPage(root2[x], pmods[x])		

			# add sub elements		
			for element in elements :
				root2[x].append(element)	

		assert root1 == root2

	def test_buildCrisisPage1():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCrisisPage(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0].size() == 20

	def test_buildCrisisPage2():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCrisisPage(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0][0] = 'n'

	def test_buildCrisisPage3():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCrisisPage(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0][root[0].size()-1][0] = p1

	def test_buildOrganizationPage1():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'Organization')
		elements = buildOrgPage(root[0], omods[0])
		for element in elements:
			root[0].append(element)

		assert root[0].size() == 16

	def test_buildOrganizationPage2():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'Organization')
		elements = buildOrgPage(root[0], omods[0])
		for element in elements:
			root[0].append(element)

		assert root[0][0] = 'n'

	def test_buildOrganizationPage3():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'Organization')
		elements = buildOrgPage(root[0], omods[0])
		for element in elements:
			root[0].append(element)

		assert root[0][root[0].size()-1][0] = p1

	def test_buildPersonPage1():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'Person')
		elements = buildPersonPage(root[0], pmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0].size() == 13

	def test_buildPersonPage2():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'Person')
		elements = buildPersonPage(root[0], pmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0][0] = 'n'

	def test_buildPersonPage3():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'Person')
		elements = buildPersonPage(root[0], pmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0][root[0].size()-1][0] = p1

	def test_buildCommonData():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCommonData(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0].size() == 11
		assert root[0][0] = 'n'

	def test_buildCommonData():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'crisis')
		elements = buildCommonData(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0].size() == 11
		assert root[0][0] = 'n'

	def test_buildCommonData():
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'crisis')
		elements = buildCommonData(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		assert root[0].size() == 11
		assert root[0][0] = 'n'


# ----
# main
# ----

print "TestWC.py"
unittest.main()
print "Done."