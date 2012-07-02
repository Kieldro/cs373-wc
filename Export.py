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
	DateElem = Element("date")
	tempElem = Element("")
	if crisisModel.date == "" :
		if crisisModel.startDate != "":
			tempElem = Element("start")
			tempElem.text = crisisModel.startDate
			DateElem.append(tempElem)
		if crisisModel.endDate != "":
			tempElem = Element("end")
			tempElem.text = crisisModel.startDate
			DateElem.append(tempElem)
		if crisisModel.additional != "":
			tempElem = Element("additional")
			tempElem.text = crisisModel.additional
			DateElem.append(tempElem)
	else :
		tempElem = Element("otherDiscription")
		tempElem.text = crisisModel.date
		DateElem.append(tempElem) 

	elements.append(DateElem)

	tempElem = Element("humanImpact")
	tempElem.text = crisisModel.humanImpact
	elements.append(tempElem)
	tempElem = Element("economicImpact")
	tempElem.text = crisisModel.ecoImpact
	elements.append(tempElem)
	tempElem = Element("resourcesNeeded")
	tempElem.text = crisisModel.resources
	elements.append(tempElem)

	wth = Element("waysToHelp")
	wth.text = crisisModel.waysToHelpText[0]
	i = 0
	while i < len(crisisModel.waysToHelpLinks) :
		tempElem = Element("link")
		tempElem.text = crisisModel.waysToHelpLinks[i]
		if crisisModel.waysToHelpText[i + 1] != "":
			tempElem.tail = crisisModel.waysToHelpText[i + 1]
		wth.append(tempElem)
		i += 1
	elements.append(wth)
	for id in crisisModel.orgs:
		tempElem = Element("organizationId")
		tempElem.text = str(id)
		elements.append(tempElem)
	for id in crisisModel.people:
		tempElem = Element("personId")
		tempElem.text = str(id)
		elements.append(tempElem)
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
	tempElem = Element("history")
	tempElem.text = orgModel.history
	elements.append(tempElem)
	cie = Element("contactInfo")
	cie.text = orgModel.contactInfoText[0]
	i = 0

	while i < len(orgModel.contactInfoLinks) :
		tempElem = Element("link")
		tempElem.text = orgModel.contactInfoLinks[i]
		if orgModel.contactInfoText[i + 1] != "None" :
			tempElem.tail = orgModel.contactInfoText[i + 1]
		cie.append(tempElem)
		i += 1
	for id in orgModel.crises:
		tempElem = Element("crisisId")
		tempElem.text = str(id)
		elements.append(tempElem)
	for id in orgModel.people:
		tempElem = Element("personId")
		tempElem.text = str(id)
		elements.append(tempElem)
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
	tempElem = Element("")
	for id in personModel.crises:
		tempElem = Element("crisisId")
		tempElem.text = str(id)
		elements.append(tempElem)
	for id in personModel.orgs:
		tempElem = Element("organizationId")
		tempElem.text = str(id)
		elements.append(tempElem)
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
	nameElem = Element("name")
	nameElem.text = model.name
	elements.append(nameElem)
	tempElem = Element("kind")
	tempElem.text = model.knd
	elements.append(tempElem)

	LocElem = Element("location")
	if model.location == "":
		if model.city != "":
			tempElem = Element("city")
			tempElem.text = model.city
			LocElem.append( tempElem )
		if model.state != "":
			tempElem = Element("state")
			tempElem.text = model.state
			LocElem.append( tempElem )
		if model.country != "":
			tempElem = Element("country")
			tempElem.text = model.country
			LocElem.append( tempElem )
	else:
		tempElem = Element("unspecific")
		tempElem.text = model.location
		LocElem.append(tempElem)
	elements.append(LocElem)
	for x in model.image:
		tempElem = Element("image")
		tempElem.text = x
		elements.append(tempElem)
	for x in model.video:
		tempElem = Element("video")
		tempElem.text = x
		elements.append(tempElem)
	for x in model.network:
		tempElem = Element("network")
		tempElem.text = x
		elements.append(tempElem)
	for x in model.link:
		tempElem = Element("link")
		tempElem.text = x
		elements.append(tempElem)
	return elements
