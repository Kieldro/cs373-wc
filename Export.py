# -*- coding: utf-8 -*-

# ----------------------
# export.py
# written by Robert Reed
# ----------------------

# -------
# imports
# -------
from xml.etree.ElementTree import Element, SubElement
from Models import *
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
	buildCrisisInfo(crisisElement, crisisModel.crisisinfo)
	buildExternalRefs(crisisElement, crisisModel.reflink)
	SubElement(crisisElement, tag="misc", text=crisisModel.misc)
	buildOrgRefs(crisisElement, crisisModel.orgref)
	buildPersonRefs(crisisElement, crisisModel.personref)

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
	buildOrgInfo(orgElement, orgModel.orginfo)
	buildExternalRefs(orgElement, orgModel.reflink)
	SubElement(orgElement, tag="misc", text=orgModel.misc)
	buildCrisisRefs(orgElement, orgModel.crisisref)
	buildPersonRefs(orgElement, orgModel.personref)

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
	buildPersonInfo(personElement, personModel.personinfo)
	buildExternalRefs(personElement, personModel.reflink)
	SubElement(personElement, tag="misc", text=personModel.misc)
	buildCrisisRefs(personElement, personModel.crisisref)
	buildOrgRefs(personElement, personModel.orgref)

# -------------
# buildInitInfo
# -------------

def buildInitInfo(element, model):	
	element.attrib["id"] =  model.ID
	SubElement(element, tag="name", text=model.name)

# ---------------
# buildCrisisInfo
# ---------------

def buildCrisisInfo(crisisElement, crisisInfoModel):
	info = Element(tag="info")
	SubElement(info, tag="histroy", text=crisisInfoModel.history)
	SubElement(info, tag="help", text=crisisInfoModel.helps)
	SubElement(info, tag="resources", text=crisisInfoModel.resources)
	SubElement(info, tag="type", text=crisisInfoModel.ctype)
	buildDate(info, crisisInfoModel.date, 'time')
	buildLocation(info, crisisInfoModel.location)
	buildImpact(info, crisisInfoModel.impact)
	crisisElement.append(info)

def buildDate(parentElem, dateModel, title):
	time = Element(tag=title)
	SubElement(time, tag="time", text=dateModel.time)
	SubElement(time, tag="day", text=dateModel.day)
	SubElement(time, tag="month", text=dateModel.month)
	SubElement(time, tag="year", text=dateModel.year)
	SubElement(time, tag="misc", test=dateModel.time_misc)
	parentElem.append(time)

def buildLocation(parentElem, locationModel):
	loc = Element(tag="loc")
	SubElement(loc, tag="city", text=locationModel.city)
	SubElement(loc, tag="region", text=locationModel.region)
	SubElement(loc, tag="country", text=locationModel.country)
	parentElem.append(loc)

def buildImpact(parentElem, impactModel):
	impact = Element(tag="impact")
	buildHumanImpact(impact, impactModel.human_impact)
	buildEconomicImpact(impact, impactModel.eco_impact)
	parentElem.append(impact)
	
def buildHumanImpact(parentElem, hImpactModel):
	human = Element(tag="human")
	SubElement(human, tag="deaths", text=hImpactModel.deaths)
	SubElement(human, tag="displaced", text=hImpactModel.displaced)
	SubElement(human, tag="injured", text=hImpactModel.injured)
	SubElement(human, tag="missing", text=hImpactModel.missing)
	SubElement(human, tag="misc", test=hImpactModel.himpact_misc)
	parentElem.append(human)

def buildEconomicImpact(parentElem, eImpactModel):
	eco = Element(tag="economic")
	SubElement(eco, tag="amount", text=eImpactModel.amount)
	SubElement(eco, tag="currency", text=eImpactModel.currency)
	SubElement(eco, tag="misc", text=eImpactModel.eimpact_misc)
	parentElem.append(eco)
	
# ---------------
# buildOrgInfo
# ---------------

def buildOrgInfo(orgElement, orgInfoModel):
	info = Element(tag="info")
	SubElement(info, tag="type", text=orgInfoModel.oType)
	SubElement(info, tag="history", text=orgInfoModel.history)
	buildContact(info, orgInfoModel.contacts)
	buildLocation(info, orgInfoModel.location)
	orgElement.append(info)

def buildContact(parentElem, contactModel):
	contact = Element(tag="contact")	
	SubElement(contact, tag="phone", text=contactModel.phone)
	SubElement(contact, tag="email", text=contactModel.email)
  	buildAddress(contact, contactModel.address)
	parentElem.append(contact)

def buildAddress(parentElem, addressModel):
	mail = Element(tag="mail")	
	SubElement(mail, tag="address", text=addressModel.address)
	SubElement(mail, tag="city", text=addressModel.city)
	SubElement(mail, tag="state", text=addressModel.state)
	SubElement(mail, tag="country", text=addressModel.country)
	SubElement(mail, tag="zip", text=addressModel.zipcode)
	parentElem.append(mail)
	
# ---------------
# buildPersonInfo
# ---------------

def buildPersonInfo(personElement, personModel):
	info = Element(tag="info")
	Subelement(info, tag="type", text=personModel.ptype)	
	buildDate(info, personModel.birthdate, 'birthdate')
	SubElement(info, tag="nationality", text=personModel.nationality)
	SubElement(info, tag="biography", text=personModel.biography)
	personElement.append(info)

def buildRefs(elem, refs):
	for ref in refs:
		temp = Element(tag=ref.link_type)
		buildLink(temp, ref.site, ref.title, ref.url, ref.description)
		elem.append(temp)

def buildExternalRefs(element, model):
	ref = Element(tag="ref")
	buildRefs(ref, [model.primary_image])
	buildRefs(ref, model.image)
	buildRefs(ref, model.video)
	buildRefs(ref, model.social)
	buildRefs(ref, model.ext)
	element.append(ref)

def buildLink(element, site, title, url, description):
	SubElement(element, tag="site", text=site)
	SubElement(element, tag="title", text=title)
	SubElement(element, tag="url", text=url)
	SubElement(element, tag="description", text=description)

def buildCrisisRefs(element, refs):
	for ref in refs:
		temp = Element(tag=ref.rType)
		temp.attrib["idref"] = ref.sref
		element.append(temp)
