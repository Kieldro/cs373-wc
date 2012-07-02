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
from google.appengine.ext.db import Property

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
        elements = buildCommonData(crisisElement, crisisModel)
	#append type specific data next
	if crisisModel.date == "" :
		if crisisModel.startDate != "":
			elements.append(Element("start", text=crisisModel.startDate))
		if crisisModel.endDate != "":
			elements.append(Element("end", text=crisisModel.startDate))
		if crisisModel.additional != "":
			elements.append(Element("additional", text=crisisModel.additional))
	else :
		elements.append(Element("otherDiscription", text=crisisModel.date)) 
	elements.append(Element("humanImpact", text=crisisModel.humanImpact))
	elements.append(Element("economicImpact", text=crisisModel.ecoImpact))
	elements.append(Element("resourcesNeeded", text=crisisModel.resources))
	wth = Element("waysToHelp", text=crisisModel.waysToHelpText[0])
	i = 0
	while i < len(crisisModel.waysToHelpLinks) :
		SubElement(wth, "link", text=crisisModel.waysToHelpLinks[i], tail=crisisModel.waysToHelpText[i + 1])
		i += 1
	for id in crisisModel.orgs:
		elements.append(Element("organizationId", text=str(id)))
	for id in crisisModel.people:
		elements.append(Element("personId", text=str(id)))
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
        elements = buildCommonData(orgElement, orgModel)
	#create type specific data
	elements.append( Element("history", text=orgModel.history))
	cie = Element("contactInfo", text=orgModel.contactInfoText[0])
	i = 0

	while i < len(orgModel.contactInfoLinks) :
		SubElement(cie, "link", text=orgModel.contactInfoLinks[i], tail=orgModel.contactInfoText[i + 1])
		i += 1
	for id in orgModel.crises:
		elements.append(Element("crisisId", text=str(id)))
	for id in orgModel.people:
		elements.append(Element("personId", text=str(id)))
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
        elements = buildCommonData(personElement, personModel) 
        
		#create type specific data
	for id in personModel.crises:
		elements.append(Element("crisisId", text=str(id)))
	for id in personModel.orgs:
		elements.append(Element("personId", text=str(id)))
	return elements

# ---------------
# buildCommonData
# ---------------

def buildCommonData(element, model):
	"""
All pages have a certain amount of data incommon, represented in children
elements with the same tags. This is where these common elements are 
added to the page element from the model.
element is a Element that represents a page of any of the three types
model is a model that represents the same type as the element
"""
	# add id attribute
	element.attrib["id"] =  model.ID
	
	# create elements
	elements = []
	elements.append(Element("name", text=model.name))
	elements.append(Element("knd", text=model.knd))
	if model.location == "":
		if model.city != "":
			elements.append( Element("city", text=model.city) )
		if model.state != "":
			elements.append( Element("state", text=model.state) )
		if model.country != "":
			elements.append( Element("country", text=model.country) )
	else:
		elements.append(Element("unspecific", text=model.location))
	for x in model.image:
		elements.append(Element("image", text=x))
	for x in model.video:
		elements.append(Element("video", text=x))
	for x in model.network:
		elements.append(Element("network", text=x))
	for x in model.link:
		elements.append(Element("link", text=x))
	return elements
