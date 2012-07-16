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
This method takes in three lists of World Crisis Page models, and returns the data stored
in them into an ElementTree object that represents a well-formed xml 
document that validates according to the xml schema stored in WC2.xsd.
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
		opage = Element(tag='organization')
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
Build a crisis page using the data from the Crisismodel,
including all referred to models of other types.
crisisElement is a Element that represents a crisis page
crisisModel is a model object that represents a crisis model
	"""
	buildInitInfo(crisisElement, crisisModel);
	buildCrisisInfo(crisisElement, crisisModel.crisisinfo)
	buildExternalRefs(crisisElement, crisisModel.reflink)
	temp = SubElement(crisisElement, tag="misc")
	temp.text = crisisModel.misc
	buildPageRefs(crisisElement, crisisModel.orgref)
	buildPageRefs(crisisElement, crisisModel.personref)


# ------------
# buildOrgPage
# ------------

def buildOrgPage(orgElement, orgModel) :
	"""
Build a organization page using the data from the organization model,
including all referred to models of other types.
orgElement is a Element that represents a organization page
orgModel is a model object that represents a organization model
	"""
	buildInitInfo(orgElement, orgModel);
	buildOrgInfo(orgElement, orgModel.orginfo)
	buildExternalRefs(orgElement, orgModel.reflink)
	temp = SubElement(orgElement, tag="misc")
	temp.text = orgModel.misc
	buildPageRefs(orgElement, orgModel.crisisref)
	buildPageRefs(orgElement, orgModel.personref)


# ---------------
# buildPersonPage
# ---------------

def buildPersonPage(personElement, personModel) :
	"""
Build a person page using the data from the personmodel,
including all referred to models of other types.
personElement is a Element that represents a person page
personModel is a model object that represents a person model
	"""
	buildInitInfo(personElement, personModel)
	buildPersonInfo(personElement, personModel.personinfo)
	buildExternalRefs(personElement, personModel.reflink)
	temp = SubElement(personElement, tag="misc")
	temp.text = personModel.misc
	buildPageRefs(personElement, personModel.crisisref)
	buildPageRefs(personElement, personModel.orgref)


# -------------
# buildInitInfo
# -------------

def buildInitInfo(element, model):	
	"""
Add common data to the elelment from the model provided.
element is a Element that represents a person page
model is a model object that represents a person model
	"""
	element.attrib["id"] =  model.ID
	temp = SubElement(element, tag="name")
	temp.text = model.name


# ---------------
# buildCrisisInfo
# ---------------

def buildCrisisInfo(crisisElement, crisisInfoModel):
	"""
Build a crisisinfo element tree using the data from the crisismodel,
including all referred to models of other types.
crisisElement is a Element that represents a crisis
crisisModel is a model object that represents a crsis model
	"""
	info = Element(tag="info")
	temp = SubElement(info, tag="history")
	temp.text = crisisInfoModel.history
	temp = SubElement(info, tag="help")
	temp.text = crisisInfoModel.helps
	temp = SubElement(info, tag="resources")
	temp.text = crisisInfoModel.resources
	temp = SubElement(info, tag="type")
	temp.text = crisisInfoModel.ctype
	buildDate(info, crisisInfoModel.date, 'time')
	buildLocation(info, crisisInfoModel.location)
	buildImpact(info, crisisInfoModel.impact)
	crisisElement.append(info)


# ---------------
# buildDate
# ---------------

def buildDate(parentElem, dateModel, title):
	"""
Build a dateelement tree using the data from the dateModell,
title is a string, containing the tag name of the outer element
to be created.
parentElement is a Element 
dateModel is a model object that represents a date
	"""
	time = Element(tag=title)
	temp = SubElement(time, tag="time")
	temp.text = dateModel.time
	temp = SubElement(time, tag="day")
	temp.text = str(dateModel.day)
	temp = SubElement(time, tag="month")
	temp.text = str(dateModel.month)
	temp = SubElement(time, tag="year")
	temp.text = str(dateModel.year)
	temp = SubElement(time, tag="misc")
	temp.text = str(dateModel.time_misc)
	parentElem.append(time)


# ---------------
# buildLocation
# ---------------

def buildLocation(parentElem, locationModel):
	"""
Build a location element tree using the data from the locationModel,
parentElement is a Element 
ocation Model is a model object that represents a location
	"""
	loc = Element(tag="loc")
	temp = SubElement(loc, tag="city")
	temp.text = locationModel.city
	temp = SubElement(loc, tag="region")
	temp.text = locationModel.region
	temp = SubElement(loc, tag="country")
	temp.text = locationModel.country
	parentElem.append(loc)
	
	
# ---------------
# buildImpact
# ---------------

def buildImpact(parentElem, impactModel):
	"""
Build an impact element tree using the data from the impactModel,
including all of the information in the child models
parentElement is a Element 
impactModel is a model object that represents an impact
	"""
	impact = Element(tag="impact")
	buildHumanImpact(impact, impactModel.human_impact)
	buildEconomicImpact(impact, impactModel.eco_impact)
	parentElem.append(impact)


# ---------------
# buildHumanImpact
# ---------------

def buildHumanImpact(parentElem, hImpactModel):
	"""
Build a human impact element tree using the data from the hImpactMnodel,
parentElement is a Element 
hImpact Model is a model object that represents a human Imapct
	"""
	human = Element(tag="human")
	temp = SubElement(human, tag="deaths")
	temp.text = str(hImpactModel.deaths)
	temp = SubElement(human, tag="displaced")
	temp.text = str(hImpactModel.displaced)
	temp = SubElement(human, tag="injured")
	temp.text = str(hImpactModel.injured)
	temp = SubElement(human, tag="missing")
	temp.text = str(hImpactModel.missing)
	temp = SubElement(human, tag="misc")
	temp.text = hImpactModel.himpact_misc
	parentElem.append(human)


# ---------------
# buildEconomicImpact
# ---------------

def buildEconomicImpact(parentElem, eImpactModel):
	"""
Build an economic impact element tree using the data from the eImpactMnodel,
parentElement is a Element 
eImpact Model is a model object that represents the economic Imapct
	"""
	eco = Element(tag="economic")
	temp = SubElement(eco, tag="amount")
	temp.text = str(eImpactModel.amount)
	temp = SubElement(eco, tag="currency")
	temp.text = str(eImpactModel.currency)
	temp = SubElement(eco, tag="misc")
	temp.text = eImpactModel.eimpact_misc
	parentElem.append(eco)


# ---------------
# buildOrgInfo
# ---------------

def buildOrgInfo(orgElement, orgInfoModel):
	"""
Build a orginfo element tree using the data from the orgmodel,
including all referred to models of other types.
orgElement is a Element that represents a org
orginfoModel is a model object that represents a orginfo model
	"""
	info = Element(tag="info")
	temp = SubElement(info, tag="type")
	temp.text = orgInfoModel.otype
	temp = SubElement(info, tag="history")
	temp.text = orgInfoModel.history
	buildContact(info, orgInfoModel.contacts)
	buildLocation(info, orgInfoModel.location)
	orgElement.append(info)


# ---------------
# buildContact
# ---------------

def buildContact(parentElem, contactModel):
	"""
Build a contact element tree using the data from the ,
including all referred to models of other types.
parentElem is a Element
contactModel is a model object that represents a contact
	"""
	contact = Element(tag="contact")	
	temp = SubElement(contact, tag="phone")
	temp.text = contactModel.phone
	temp = SubElement(contact, tag="email")
	temp.text = contactModel.email
	buildAddress(contact, contactModel.address)
	parentElem.append(contact)


# ---------------
# buildAddress
# ---------------

def buildAddress(parentElem, addressModel):
	"""
Build a address element tree using the data from the addressModel,
parentElem is an Element 
addressModel is a model object that represents the address
	"""
	mail = Element(tag="mail")	
	temp = SubElement(mail, tag="address")
	temp.text = addressModel.address
	temp = SubElement(mail, tag="city")
	temp.text = addressModel.city
	temp = SubElement(mail, tag="state")
	temp.text = addressModel.state
	temp = SubElement(mail, tag="country")
	temp.text = addressModel.country
	temp = SubElement(mail, tag="zip")
	temp.text = addressModel.zipcode
	parentElem.append(mail)
	

# ---------------
# buildPersonInfo
# ---------------

def buildPersonInfo(personElement, personModel):
	"""
Build a personinfo element tree using the data from the personmodel,
including all referred to models of other types.
personElement is a Element that represents a person
personModel is a model object that represents a person model
	"""
	info = Element(tag="info")
	temp = SubElement(info, tag="type")	
	temp.text = personModel.ptype
	buildDate(info, personModel.birthdate, 'birthdate')
	temp = SubElement(info, tag="nationality")
	temp.text = personModel.nationality
	temp = SubElement(info, tag="biography")
	temp.text = personModel.biography
	personElement.append(info)


# ---------------
# buildRefs
# ---------------

def buildRefs(elem, refs):
	"""
Build a refs elements using the data from the refs
elem is an Element 
refs is a list of model objects that represents the external references
	"""
	for ref in refs:
		ref = db.get(ref)
		temp = Element(tag=ref.link_type)
		buildLink(temp, ref.site, ref.title, ref.url, ref.description)
		elem.append(temp)


# ---------------
# buildExternalRefs
# ---------------

def buildExternalRefs(element, model):
	"""
Build a personinfo element tree using the data from the personmodel,
including all referred to models of other types.
personElement is a Element that represents a person
personModel is a model object that represents a person model
	"""
	ref = Element(tag="ref")
	buildRefs(ref, [model.primaryImage.key()])
	buildRefs(ref, model.image)
	buildRefs(ref, model.video)
	buildRefs(ref, model.social)
	buildRefs(ref, model.ext)
	element.append(ref)


# ---------------
# buildLink
# ---------------

def buildLink(element, site, title, url, description):
	"""
Build a link element tree using the data provided,
element is a Element that represents the parent
site is a string
title is a string
url is a string
description is a string, can be null
	"""
	temp = SubElement(element, tag="site")
	temp.text = site
	temp = SubElement(element, tag="title")
	temp.text = title
	temp = SubElement(element, tag="url")
	temp.text = url
	if description != None:
		temp = SubElement(element, tag="description")
		temp.text = description


# ---------------
# buildPageRefs
# ---------------

def buildPageRefs(element, refs):
	"""
Build a refs elements using the data from the refs
element is an Element 
refs is a list of model objects that represents the internal references
	"""
	for ref in refs:
		ref = db.get(ref)
		temp = Element(tag=ref.rType)
		temp.attrib["idref"] = ref.sref
		element.append(temp)

