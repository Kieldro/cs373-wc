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
	for x in crisisList :
		cpage = Element(tag='crisis')
		buildCrisisPage(cpage, x)
		root.append(cpage)
	for x in orgList :
		opage = Element(tag='org')
		buildOrgPage(opage, x)
		root.append(opage)
	for x in personList :
		ppage = Element(tag='person')
		buildPersonPage(ppage, x)
		root.append(ppage)

	return root

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
	SubElement(crisisElement, tag="misc", Text=crisisModel.misc)
	buildPageRefs(crisisElement, crisisModel.orgref)
	buildPageRefs(crisisElement, crisisModel.personref)

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
	buildPageRefs(orgElement, orgModel.crisisref)
	buildPageRefs(orgElement, orgModel.personref)

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
	buildPageRefs(personElement, personModel.crisisref)
	buildPageRefs(personElement, personModel.orgref)

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
	SubElement(time, tag="day", text=str(dateModel.day))
	SubElement(time, tag="month", text=str(dateModel.month))
	SubElement(time, tag="year", text=str(dateModel.year))
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
	SubElement(human, tag="deaths", text=str(hImpactModel.deaths))
	SubElement(human, tag="displaced", text=str(hImpactModel.displaced))
	SubElement(human, tag="injured", text=str(hImpactModel.injured))
	SubElement(human, tag="missing", text=str(hImpactModel.missing))
	SubElement(human, tag="misc", test=hImpactModel.himpact_misc)
	parentElem.append(human)

def buildEconomicImpact(parentElem, eImpactModel):
	eco = Element(tag="economic")
	SubElement(eco, tag="amount", text=str(eImpactModel.amount))
	SubElement(eco, tag="currency", text=eImpactModel.currency)
	SubElement(eco, tag="misc", text=eImpactModel.eimpact_misc)
	parentElem.append(eco)
	
# ---------------
# buildOrgInfo
# ---------------

def buildOrgInfo(orgElement, orgInfoModel):
	info = Element(tag="info")
	SubElement(info, tag="type", text=orgInfoModel.otype)
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
	SubElement(info, tag="type", text=personModel.ptype)	
	buildDate(info, personModel.birthdate, 'birthdate')
	SubElement(info, tag="nationality", text=personModel.nationality)
	SubElement(info, tag="biography", text=personModel.biography)
	personElement.append(info)

def buildRefs(elem, refs):
	for ref in refs:
		ref = db.get(ref)
		temp = Element(tag=ref.link_type)
		buildLink(temp, ref.site, ref.title, ref.url, ref.description)
		elem.append(temp)

def buildExternalRefs(element, model):
	ref = Element(tag="ref")
	buildRefs(ref, [model.primary_image.key(),])
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

def buildPageRefs(element, refs):
	for ref in refs:
		ref = db.get(ref)
		temp = Element(tag=ref.rType)
		temp.attrib["idref"] = ref.sref
		element.append(temp)
