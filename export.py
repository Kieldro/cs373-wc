# ----------------------
# export.py
# written by Robert Reed
# ----------------------

from xml.etree.ElementTree import Element, SubElement

def buildTree(crisisList, orgList, personList):
	root = buildRoot()
	SubElement(root, "crises")
	SubElement(root, "organizations")
	SubElement(root, "people")	
	buildPagesofType(root[0], "crisis", crisisList, buildCrisisPage)
	buildPagesofType(root[1], "organization", orgList, buildOrgPage)
	buildPagesofType(root[2], "person", personList, buildPersonPage)
	return root

def buildPagesOfType(root, pageType, pageList, pageTypeBuildFunction) :
	for x in range(len(pageList)) :
		SubElement(root, pageType)
		pageTypeBuildFunction(root[x], pageList[x])

def buildCrisisPage(crisisElement, crisisModel) :
	#append shared data first
        buildCommonData(crisisElement, crisisModel)

	#append type specific data next
	elements = []
	elements.append( Element("humanImpact", crisisModel.humanImpact) )
	elements.append( Element("economicImpact", crisisModel.ecoImpact) )
	elements.append( resources = Element("resourcesNeeded", crisisModel.resources) )
# These need to be updated in the model to match the schema, or visa-versa
	elements.append( Element("waysToHelp", crisisModel.waysToHelp) )
	elements.append( date = Element("date", crisisModel.date) )
# Need to be updated in the model to have integer values.
# Possibly changed here
	elements.append( org = Element("organizationId", crisisModel.orgs) )
	elements.append( people = Element("personId", crisisModel.people) )
	
	# add sub elements		
	for element in elements :
		crisisElement.append(element)

def buildOrgPage(orgElement, orgModel) :
	#create and append shared data first
        buildCommonData(orgElement, orgModel)

	#create type specific data
	elements = []
	elements.append( Element("history", orgModel.history) )
#May need to alter schema/model
	elements.append( Element("contactInfo", orgModel.contactInfo) )
	elements.append( Element("crisisId", orgModel.crises) )
	elements.append( Element("personId", orgModel.people) )

	# append subElements
	for element in elements:
		orgElement.append(element)

def buildPersonPage(personElement, personModel) :
	#append shared data first
        buildCommonData(personElement, personModel) 

	#create type specific data
	elements = []
       	elements.append( Element("organizationId", personModel.crises) )
	elements.append( Element("personId", crisisModel.people) )
#need to update model
	
	# append subElements
	for element in elements :
		personElement.append(element)

def buildCommonData(element, model) :
	# add id attribute
	element.attrib("id", modelId)
	
	# create elements
	subElems = []
	subElems.append( Element("name", model.name) )
	subElems.append( Element("kind", model.kind) )
#need to update models
	if model.hasSpecLoc:
		if model.city != "":
			subElems.append( Element("city", model.city) )
		if model.state != "":
			subElems.append( Element("state", model.state) )
		if model.country != "":
			subElems.append( Element("country", model.country) )
	else:
		subElems.append( Element("unspecific", model.locString) )
	for image in model.images:
		subElems.append( Element("image", image) )
	for video in model.videos:
		subElems.append( Element("video", video) )
	for network in model.networks:
		subElems.append( Element("network", network) )
	for link in model.links:
		subElems.append( Element("link", link) )

	# append elements
	for elem in subElems:
		element.append(elem)

