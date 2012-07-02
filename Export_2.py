# -*- coding: utf-8 -*-
# ----------------------
# export.py
# written by Robert Reed
# ----------------------

# -------
# imports
# -------

from xml.etree.ElementTree import Element, SubElement
from Models import Crisis, Organization, Person

# ---------
# buildTree
# ---------

def buildTree(crisisList, orgList, personList):
	"""
This method takes in three lists of models, and returns the data stored
in them into an ElementTree object that represents a well-formed xml 
document that validates according to the xml schema stored in WC1.xsd.
crisisList is a list of Crisis model objects
orgList is a list of Organizations model objects
personList is a list of People model objects
return the root element of the data tree containing all the data 
"""
	root = Element("data")
	SubElement(root, "crises")
	SubElement(root, "organizations")
	SubElement(root, "people")	
	buildPagesofType(root[0], "crisis", crisisList, buildCrisisPage)
	buildPagesofType(root[1], "organization", orgList, buildOrgPage)
	buildPagesofType(root[2], "person", personList, buildPersonPage)
	return root

# ----------
# buildPages
# ----------

def buildPagesofType(root, pageType, pageList, pageTypeBuildFunction) :
	"""
Given a root, build all the subElements of a given page type (using the 
given function: pageTypeBuildFunction) and make them subElements of the
root.
root is an ElementTree Element object
pageType is a string that is the tag to be used for each child element
pageList is a list of GAE models, all compatible with the function argumetn
pageTypeBuildFunction is a function that builds up the structure underneath
a page Element object using the data from the model.
"""
	for x in range(len(pageList)) :
		SubElement(root, pageType)
		elements = pageTypeBuildFunction(root[x], pageList[x])		

		# add sub elements		
		for element in elements :
			root[x].append(element)	

# ---------------
# buildCrisisPage
# ---------------

def buildCrisisPage(crisisElement, crisisModel) :
	"""
Build a crisis page using the data from the model. Note: this method just
generates the sub-elements
crisisElement is a Element that represents a crisis page
crisisModel is a model object that represents a crisis model
returns a list of sub-elements to be added in correct order
"""
#append shared data first
	crisisElement.attrib("id", crisisModel.ID)
	
	# create elements
	 elements = []
	 elements.append(Element("name", crisisModel.name))
	 elements.append(Element("kind", crisisModel.kind))
	if crisisModel.location == "":
		if crisisModel.city != "":
			 elements.append( Element("city", crisisModel.city) )
		if crisisModel.state != "":
			 elements.append( Element("state", crisisModel.state) )
		if crisisModel.country != "":
			 elements.append( Element("country", crisisModel.country) )
	else:
		 elements.append(Element("unspecific", crisisModel.location))
	for image in crisisModel.images:
		 elements.append(Element("image", crisisModel.image))
	for video in crisisModel.videos:
		 elements.append(Element("video", crisisModel.video))
	for network in crisisModel.networks:
		 elements.append(Element("network", crisisModel.network))
	for link in crisisModel.links:
		 elements.append(Element("link", crisisModel.link))

	
	if crisisModel.date == "" :
		if crisisModel.startDate != "":
			elements.append(Element("start", crisisModel.startDate))
		if crisisModel.endDate != "":
			elements.append(Element("end", crisisModel.startDate))
		if crisisMode.additional != "":
			elements.append(Element("additional", crisisModel.additional))
	else :
		elements.append(Element("otherDiscription", crisisModel.date)) 
	elements.append(Element("humanImpact", crisisModel.humanImpact))
	elements.append(Element("economicImpact", crisisModel.ecoImpact))
	elements.append(Element("resourcesNeeded", crisisModel.resources))
	wth = Element("waysToHelp", orgModel.contactInfoText[0])
	i = 0
	while i < len(waysToHelpLinks) :
		subElement(wth, "link", crisisModel.waysToHelpLinks[i], tail=crisisModel.waysToHelpText[i + 1])
		++i
	for id in crisisModel.orgs:
		elements.append(Element("organizationId", crisisModel.orgs[id]))
	for id in crisisModel.people:
		elements.append(Element("personId", crisisModel.people[id]))
	return elements

# ------------
# buildOrgPage
# ------------

def buildOrgPage(orgElement, orgModel) :
	"""
Build an organization page using the data from the model. Note: this 
method just generates the sub-elements
orgElement is a Element that represents a org page
orgModel is a model object that represents a org model
returns a list of sub-elements to be added in correct order
"""
	#create and append shared data first
	orgElement.attrib("id", orgModel.ID)
	
	# create elements
	 elements = []
	 elements.append(Element("name", orgModel.name))
	 elements.append(Element("kind", orgModel.kind))
	if orgModel.location == "":
		if orgModel.city != "":
			 elements.append( Element("city", orgModel.city) )
		if orgModel.state != "":
			 elements.append( Element("state", orgModel.state) )
		if orgModel.country != "":
			 elements.append( Element("country", orgModel.country) )
	else:
		 elements.append(Element("unspecific", orgModel.location))
	for image in orgModel.images:
		 elements.append(Element("image", orgModel.image))
	for video in orgModel.videos:
		 elements.append(Element("video", orgModel.video))
	for network in orgModel.networks:
		 elements.append(Element("network", orgModel.network))
	for link in orgModel.links:
		 elements.append(Element("link", orgModel.link))

	
	elements.append( Element("history", orgModel.history))
	cie = Element("contactInfo", orgModel.contactInfoText[0])
	i = 0
	while i < len(contactInfoLinks) :
		subElement(cie, "link", orgModel.contactInfoLink[i], tail=orgMode.contactInfoText[i + 1])
		++i
	for id in orgModel.crises:
		elements.append(Element("crisisId", orgModel.crises[id]))
	for id in orgModel.people:
		elements.append(Element("personId", orgModel.people[id]))
	return elements

# ---------------
# buildPersonPage
# ---------------

def buildPersonPage(personElement, personModel) :
	"""
Build a person page using the data from the model. Note: this method just
generates the sub-elements
personElement is a Element that represents a person page
personModel is a model object that represents a person model
returns a list of sub-elements to be added in correct order
"""
	#append shared data first
        
	personElement.attrib("id", personModel.ID)
	
	# create elements
	 elements = []
	 elements.append(Element("name", personModel.name))
	 elements.append(Element("kind", personModel.kind))
	if personModel.location == "":
		if personModel.city != "":
			 elements.append( Element("city", personModel.city) )
		if personModel.state != "":
			 elements.append( Element("state", personModel.state) )
		if personModel.country != "":
			 elements.append( Element("country", personModel.country) )
	else:
		 elements.append(Element("unspecific", personModel.location))
	for image in personModel.images:
		 elements.append(Element("image", personModel.image))
	for video in personModel.videos:
		 elements.append(Element("video", personModel.video))
	for network in personModel.networks:
		 elements.append(Element("network", personModel.network))
	for link in personModel.links:
		 elements.append(Element("link", personModel.link))

	
	for id in personModel.crises:
		elements.append(Element("crisisId", personModel.crises[id]))
	for id in personModel.orgs:
		elements.append(Element("personId", orgModel.people[id]))
	return elements

# ---------------
# buildCommonData
# ---------------
"""
def buildCommonData(element, model):
	""
All pages have a certain amount of data incommon, represented in children
elements with the same tags. This is where these common elements are 
added to the page element from the model.
element is a Element that represents a page of any of the three types
model is a model that represents the same type as the element
""
	# add id attribute
	element.attrib("id", model.ID)
	
	# create elements
	 elements = []
	 elements.append(Element("name", model.name))
	 elements.append(Element("kind", model.kind))
	if model.location == "":
		if model.city != "":
			 elements.append( Element("city", model.city) )
		if model.state != "":
			 elements.append( Element("state", model.state) )
		if model.country != "":
			 elements.append( Element("country", model.country) )
	else:
		 elements.append(Element("unspecific", model.location))
	for image in model.images:
		 elements.append(Element("image", model.image))
	for video in model.videos:
		 elements.append(Element("video", model.video))
	for network in model.networks:
		 elements.append(Element("network", model.network))
	for link in model.links:
		 elements.append(Element("link", model.link))

	# append elements
	for elem in  elements:
		element.append(elem)

"""