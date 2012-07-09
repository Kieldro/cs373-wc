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
	root = Element("worldCrises")	
	buildPagesofType(root, "crisis", crisisList, buildCrisisPage)
	buildPagesofType(root, "organization", orgList, buildOrgPage)
	buildPagesofType(root, "person", personList, buildPersonPage)
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
		pageTypeBuildFunction(root[x], pageList[x])		

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
	buildInitInfo(crisisElement, crisisModel);
	buildCrisisInfo(crisisElement, crisisModel);
	buildExternalRefs(crisisElement, crisisModel); 
	buildOrgRefs(crisisElement, crisisModel);
	buildPersonRefs(crisisElement, crisisModel);

# ------------
# buildOrgPage
# ------------

def buildOrgPage(orgElement, orgModel) :
	"""
Build a org page using the data from the model. Note: this method just
generates the sub-elements
orgElement is a Element that represents a org page
orgModel is a model object that represents a org model
returns a list of sub-elements to be added in correct order
	"""
	buildInitInfo(orgElement, orgModel);
	buildOrgInfo(orgElement, orgModel);
	buildExternalRefs(orgElement, orgModel); 
	buildCrisisRefs(orgElement, orgModel);
	buildPersonRefs(orgElement, orgModel);

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
	buildInitInfo(personElement, personModel)
	buildPersonInfo(personElement, personModel)
	buildExternalRefs(personElement, personModel)
	buildCrisisRefs(personElement, personModel)
	buildOrgRefs(personElement, personModel)

# -------------
# buildInitInfo
# -------------

def buildInitInfo(element, model):	
	element.attrib["id"] =  model.ID
	SubElement(element, tag="name", text=Model.name)

# ---------------
# buildCrisisInfo
# ---------------

def buildCrisisInfo(crisisElement, crisisModel):
	info = Element(tag="info")
	SubElement(info, tag="histroy", text=crisisModel.history)
	SubElement(info, tag="help", text=crisisModel.helps)
	SubElement(info, tag="resources", text=crisisModel.resources)
	SubElement(info, tag="type", text=crisisModel.ctype)

	time = Element(tag="time")
	SubElement(time, tag="time", text=crisisModel.time)
	SubElement(time, tag="day", text=crisisModel.day)
	SubElement(time, tag="month", text=crisisModel.month)
	SubElement(time, tag="year", text=crisisModel.year)
	SubElement(time, tag="misc", test=crisisModel.time_misc)
	info.append(time)

	loc = Element(tag="loc")
	SubElement(loc, tag="city", text=crisisModel.city)
	SubElement(loc, tag="region", text=crisisModel.region)
	SubElement(loc, tag="country", text=crisisModel.country)
	info.append(loc)

	impact = Element(tag="impact")
	human = Element(tag="human")
	SubElement(human, tag="deaths", text=crisisModel.deaths)
	SubElement(human, tag="displaced", text=crisisModel.displaced)
	SubElement(human, tag="injured", text=crisisModel.injured)
	SubElement(human, tag="missing", text=crisisModel.missing)
	SubElement(human, tag="misc", test=crisisModel.himpact_misc)
	impact.append(human)

	eco = Element(tag="economic")
	SubElement(eco, tag="amount", text=crisisModel.amount)
	SubElement(eco, tag="currency", text=crisisModel.currency)
	SubElement(eco, tag="misc", text=crisisModel.eimpact_misc)
	impact.append(eco)
	info.append(impact)
	crisisElement.append(info)

# ---------------
# buildOrgInfo
# ---------------

def buildOrgInfo(orgElement, orgModel):
	info = Element(tag="info")
	SubElement(info, tag="type", text=orgModel.cType)
	SubElement(info, tag="history", text=orgModel.history)
	
	contact = Element(tag="contact")	
	SubElement(contact, tag="phone", text=orgModel.phone)
	SubElement(contact, tag="email", text=orgModel.email)

	mail = Element(tag="mail")	
	SubElement(mail, tag="address", text=orgModel.address)
	SubElement(mail, tag="city", text=orgModel.city)
	SubElement(mail, tag="state", text=orgModel.state)
	SubElement(mail, tag="country", text=orgModel.country)
	SubElement(mail, tag="zip", text=orgModel.zipcode)
	contact.append(mail)
	info.append(contact)
	
	loc = Element(tag="loc")
	SubElement(loc, tag="city", text=orgModel.city)
	SubElement(loc, tag="region", text=orgModel.region)
	SubElement(loc, tag="country", text=orgModel.country)
	info.append(loc)
	orgElement.append(info)

# ---------------
# buildPersonInfo
# ---------------

def buildPersonInfo(personElement, personModel):
	info = Element(tag="info")
	Subelement(info, tag="type", text=personModel.ptype)	

	bday = Element(tag="birthday")
	SubElement(bday, tag="time", text=personModel.birthtime)
	SubElement(bday, tag="day", text=personModel.birthday)
	SubElement(bday, tag="month", text=personModel.birthmonth)
	SubElement(bday, tag="year", text=personModel.birthyear)
	SubElement(bday, tag="misc", text=personModel.birthtime_misc)
	info.append(bday)
	
	SubElement(info, tag="nationality", text=personModel.nationality)
	SubElement(info, tag="biography", text=personModel.biography)
	personElement.append(info)


def buildExternalRefs(element, model):
	ref = Element(tag="ref")

	pi = Element(tag="primaryImage")
	buildLink(pi, model.pi_site, model.pi_title, model.pi_url, 
		model.pi_description)
	ref.append(pi)
	
	for x in range(len(image_sites)):
		image = Element(tag="image")
		buildLink(image, model.image_sites[x], model.image_titles[x],
			 model.image_urls[x], model.image_descriptions[x])
		ref.append(image)
			
	for x in range(len(video_sites)):
		video = Element(tag="video")
		buildLink(video, model.video_sites[x], model.video_titles[x],
			 model.video_urls[x], model.video_descriptions[x])
		ref.append(video)

	for x in range(len(social_sites)):
		social = Element(tag="social")
		buildLink(social, model.social_sites[x], model.social_titles[x],
			 model.social_urls[x], model.social_descriptions[x])
		ref.append(social)


	for x in range(len(ext_sites)):
		ext = Element(tag="ext")
		buildLink(ext, model.ext_sites[x], model.ext_titles[x],
			 model.ext_urls[x], model.ext_descriptions[x])
		ref.append(ext)

	
	element.append(ref)
	SubElement(element, tag="misc", text=model.misc)

def buildLink(element, site, title, url, description):
	SubElement(element, tag="site", text=site)
	SubElement(element, tag="title", text=title)
	SubElement(element, tag="url", text=url)
	SubElement(element, tag="description", text=description)

def buildCrisisRefs(element, model):
	for ref in model.crises:
		SubElement(element, tag="crisis", text=ref)

def buildOrgRefs(element, model):	
	for ref in modeul.crises:
		SubElement(element, tag="org", text=ref)

def buildPersonRefs(element, model):	
	for ref in model.crises:
		SubElement(element, tag="person", text=ref)
