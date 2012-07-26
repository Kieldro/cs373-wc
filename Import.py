# -*- coding: utf-8 -*-
"""This module builds the models from the constructed tree."""
from Models import *
from google.appengine.ext.db import delete
from xml.etree.ElementTree import Element, SubElement

# ------------------
# buildModels
# ------------------

def buildModels(tree) :
	"""
	Take in an element tree object that contains an xml file
	create and store the models in the data store and returns 
	lists of the page opjects
	tree is an ElementTree object
	return 3 lists of WorldCrisisPage objects.
	"""
	root = tree.getroot()
	cTreeList = root.findall('crisis')
	org_list = root.findall('organization')
	per_list = root.findall('person')

	cList = generateList(cTreeList, Crisis.all(), createCrisis, mergeCrisis)
	oList = generateList(org_list, Organization.all(), createOrganization, mergeOrganization)
	pList= generateList(per_list, Person.all(), createPerson, mergePerson)

	buildReferences(cList, oList, pList)
	#mergeRefs(cList, oList, pList)

	return cList, oList, pList

# ------------------
# generateList
# ------------------

def generateList(treeList, dataList, createModel, mergeModels):
	"""Return list of built models."""
	modelList = []
	
	for tree in treeList :
		for existing in dataList :
			if existing.ID == tree.attrib['id'] :
				mergeModels(tree, existing)
				break
		else :
			modelList.append(createModel(tree))
	
	return modelList

# ------------------
# createCrisis
# ------------------

def createCrisis(elem):
	"""
	Create a crisis model, including references to all child models, 
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Crisis in the datastore.
	"""
	d = {}
	d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['misc'] = elem.findtext('misc')
	d['crisisinfo'] = createCrisisInfo(elem.find('info'))
	d['reflink'] = createRefLinks(elem.find('ref'))

	personrefs = createReferences('person', elem)
	d['personref'] = personrefs
	orgrefs = createReferences('org', elem)
	d['orgref'] = orgrefs
	
	c = Crisis(**d)
	c.put()
	return c
	
	
# ------------------
# createOrganization
# ------------------

def createOrganization(elem):
	"""
	Create a organization model, including references to all child models, 
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the organization in the datastore.
	"""
	d = {}
	d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['misc'] = elem.findtext('misc')
	d['orginfo'] = createOrgInfo(elem.find('info'))
	d['reflink'] = createRefLinks(elem.find('ref'))

	crisisrefs = createReferences('crisis', elem)
	d['crisisref'] = crisisrefs
	personrefs = createReferences('person', elem)
	d['personref'] = personrefs
	
	o = Organization(**d)
	o.put()
	return o
		
	
# ------------------
# createPerson
# ------------------

def createPerson(elem):
	"""
	Create a person model, including references to all child models, 
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the person in the datastore.
	"""
	d = {}
	d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['misc'] = elem.findtext('misc')
	d['personinfo'] = createPersonInfo(elem.find('info'))
	d['reflink'] = createRefLinks(elem.find('ref'))

	crisisrefs = createReferences('crisis', elem)
	d['crisisref'] = crisisrefs
	orgrefs = createReferences('org', elem)
	d['orgref'] = orgrefs
	
	p = Person(**d)
	p.put()
	return p
		
	
# ------------------
# createDate
# ------------------

def createDate(elem) :
	"""
	Create a Date model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Date in the datastore.
	"""
	d = {}
	d['time'] = elem.findtext('time')
	d['day'] = elem.findtext('day')
	d['month'] = elem.findtext('month')
	d['year'] = elem.findtext('year')
	d['time_misc'] = elem.findtext('misc')
	
	de = Date(**d)
	de.put()
	return de
		
	
# ------------------
# createCrisisInfo
# ------------------

def createCrisisInfo(elem):
	"""
	Create a CrisisInfo model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the CrisisInfo in the datastore.
	"""
	d = {}
	d['history'] = elem.findtext('history')
	d['helps'] = elem.findtext('help')
	d['resources'] = elem.findtext('resources')
	d['ctype'] = elem.findtext('type')
	
	d['location'] = createLocationInfo(elem.find('loc'))
	d['impact'] = createImpact(elem.find('impact'))
	d['date'] = createDate(elem.find('time'))
	
	ci = CrisisInfo(**d)
	ci.put()
	return ci
		
	
# ------------------
# createOrgInfo
# ------------------
	"""
	Create a OrgInfo model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the OrgInfo in the datastore.
	"""
def createOrgInfo(elem):
	d = {}
	d['otype'] = elem.findtext('type')
	d['history'] = elem.findtext('history')	
	
	d['location'] = createLocationInfo(elem.find('loc'))
	d['contacts'] = createContacts(elem.find('contact'))
	
	oi = OrgInfo(**d)
	oi.put()
	return oi
		
	
# ------------------
# createPersonInfo
# ------------------

def createPersonInfo(elem):
	"""
	Create a PersonInfo model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the PersonInfo in the datastore.
	"""
	d = {}
	d['biography'] = elem.findtext('biography')
	d['nationality'] = elem.findtext('nationality')
	d['ptype'] = elem.findtext('type')

	d['birthdate'] = createDate(elem.find('birthdate'))
	
	pi = PersonInfo(**d)
	pi.put()
	return pi
	
# ------------------
# createRefLinks
# ------------------

def createRefLinks(elem) :
	"""
	Create all the reference models for a single info instance, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the  in the datastore.
	"""
	d = {}
	d['primaryImage'] = createLink('primaryImage', elem.find('primaryImage'))
	images = elem.findall('image')
	image_list = []
	for image in images :
		image_list.append(createLink('image', image).key())
	d['image'] = image_list
	
	videos = elem.findall('video')
	video_list = []
	for video in videos :
		video_list.append(createLink('video', video).key())
	d['video'] = video_list
	
	socials = elem.findall('social')
	social_list = []
	for social in socials :
		social_list.append(createLink('social', social).key())
	d['social'] = social_list
	
	exts = elem.findall('ext')
	ext_list = []
	for ext in exts :
		ext_list.append(createLink('ext', ext).key())
	d['ext'] = ext_list
	
	rl = ReferenceLinks(**d)
	rl.put()
	return rl
		
	
# ------------------
# createLink
# ------------------

def createLink(etype, elem) :
	"""
	Create a Link model, and put it in the datastore.
	etype is a string representation of the type of the link
	elem an ElementTree ElementTree
	return a key to the Link in the datastore.
	"""
	d = {}
	d['site'] = elem.findtext('site')
	d['title'] = elem.findtext('title')
	s = elem.findtext('url')
	d['url'] = s.strip()
	desc = elem.findtext('description')
	if(desc) :
		d['description'] = desc
	d['link_type'] = etype
	
	l = Link(**d)
	l.put()
	return l
	
	
# ------------------
# createReferences
# ------------------

def createReferences(itype, elem) :
	"""
	Create Reference models, of a given itype and put them in 
	it in the datastore.
	itype a string representing of the thing a reference to
	elem an ElementTree ElementTree
	return a key to the EconomicImpact in the datastore.
	"""
	d = {}
	refs = elem.findall(itype)
	ref_list = []
	for ref in refs :
		d = {}
		d['sref'] = ref.attrib['idref']
		d['rType'] = itype
		r = Reference(**d)
		r.put()
		ref_list.append(r.key())

	return ref_list
		
	
# ------------------
# createLocationInfo
# ------------------

def createLocationInfo(elem) :
	"""
	Create a Location model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Location in the datastore.
	"""
	d = {}
	d['city'] = elem.findtext('city')
	d['region'] = elem.findtext('region')
	d['country'] = elem.findtext('country')
	
	l = Location(**d)
	l.put()
	return l
		
	
# ------------------
# createHumanImpact
# ------------------

def createHumanImpact(elem) :
	"""
	Create a HumanImpact model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the HumanImpact in the datastore.
	"""
	d = {}
	d['deaths'] = elem.findtext('deaths')
	d['displaced'] = elem.findtext('displaced')
	d['injured'] = elem.findtext('injured')
	d['missing'] = elem.findtext('missing')
	d['himpact_misc'] = elem.findtext('misc')
	
	hi = HumanImpact(**d)
	hi.put()
	return hi
		
	
# ------------------
# createEconomicImpact
# ------------------

def createEconomicImpact(elem) :
	"""
	Create a EconomicImpact model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the EconomicImpact in the datastore.
	"""
	d = {}
	d['amount'] = elem.findtext('amount')
	d['currency'] = elem.findtext('currency')
	d['eimpact_misc'] = elem.findtext('misc')
	
	ei = EconomicImpact(**d)
	ei.put()
	return ei
		
	
# ------------------
# createImpact
# ------------------

def createImpact(elem) :
	"""
	Create a Impact model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Impact in the datastore.
	"""
	d = {}
	d['human_impact'] = createHumanImpact(elem.find('human'))
	d['eco_impact'] = createEconomicImpact(elem.find('economic'))
	
	i = Impact(**d)
	i.put()
	return i
		
	
# ------------------
# createFullAddress
# ------------------

def createFullAddress(elem) :
	"""
	Create a FullAddress model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the FullAddress in the datastore.
	"""
	d = {}
	d['address'] = elem.findtext('address')
	d['city'] = elem.findtext('city')
	d['state'] = elem.findtext('state')
	d['country'] = elem.findtext('country')
	d['zipcode'] = elem.findtext('zip')
	
	fa = FullAddress(**d)
	fa.put()
	return fa
		
	
# ------------------
# createContacts
# ------------------

def createContacts(elem) :
	"""
	Create a contact model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the contact in the datastore.
	"""
	d = {}
	d['phone'] = elem.findtext('phone')
	d['email'] = elem.findtext('email')
	d['address'] = createFullAddress(elem.find('mail'))
	
	c = Contacts(**d)
	c.put()
	return c
	
	
# ------------------
# buildReferences
# ------------------

def buildReferences(cList, oList, pList) :
	"""
	Build references to each object using the keys provided by the 
	datastore.
	cList a list of crisis objects
	oList a list of org objects
	pList a list of person objects
	"""
	for crisis in cList:
		orefs= crisis.orgref
		for oref in orefs:
			oref_elem = db.get(oref)
			target = oref_elem.sref
			for org in oList:
				if org.ID == target:
					oref_elem.ref = org
					oref_elem.put()
					break
		prefs = crisis.personref
		for pref in prefs:
			pref_elem = db.get(pref)
			target = pref_elem.sref
			for person in pList:
				if person.ID == target:
					pref_elem.ref = person
					pref_elem.put()
					break
	
	for orgs in oList:
		crefs = orgs.crisisref
		for cref in crefs:
			cref_elem = db.get(cref)
			target = cref_elem.sref
			for crisis in cList:
				if crisis.ID == target:
					cref_elem.ref = crisis
					cref_elem.put()
					break
		prefs = orgs.personref
		for pref in prefs:
			pref_elem = db.get(pref)
			target = pref_elem.sref
			for person in pList:
				if person.ID == target:
					pref_elem.ref = person
					pref_elem.put()
					break

	for person in pList:
		crefs = person.crisisref
		for cref in crefs:
			cref_elem = db.get(cref)
			target = cref_elem.sref
			for crisis in cList:
				if crisis.ID == target:
					cref_elem.ref = crisis	
					cref_elem.put()
					break
		orefs= person.orgref
		for oref in orefs:
			oref_elem = db.get(oref)
			target = oref_elem.sref
			for org in oList:
				if org.ID == target:
					oref_elem.ref = org
					oref_elem.put()
					break



def mergeOrganization(source, dest) :
	"""dest is the object in the datastore
	   source is the element in the ElementTree
	   """

	orginfo = source.find('info')
	history = orginfo.findtext('history')
	estring = str(dest.orginfo.history)
	if history not in estring:
		dest.orginfo.history = dest.orginfo.history + " " + history

	mergeRefs(source, dest)

def mergePerson(source, dest) :
	pass

def mergeCrisis(source, dest) :
	pass

def mergeRefs(source, dest) :
	refs = source.find('ref')
	primaryImage = refs.find('primaryImage')
	epi = dest.reflink.primaryImage
	epi.site = primaryImage.findtext('site')
	epi.title = primaryImage.findtext('title')
	epi.url = primaryImage.findtext('url').strip()
	epi.description = primaryImage.findtext('description')

	image_list = refs.findall('image')
	eimagelist = dest.reflink.image
	if len(image_list) > len(eimagelist) :
		delete(eimagelist)
		for image in image_list :
			eimagelist.append(createLink("image", image))


"""def mergeRefs(cList, oList, pList) :
	cridata = Crisis.all()
	orgdata = Organization.all()
	perdata = Person.all()


	for crisis in cList :
		for ecri in cridata :
			if crisis.key() == ecri.key() :
				continue
			if compareCrises(crisis, ecri) :
				crisis.refer = ecri

	for person in pList :
		for eper in perdata :
			if person.key() == eper.key() :
				continue
			if comparePerson(person, eper) :
				person.refer = eper

	for org in oList :
		for eorg in orgdata :
			if org.key() == eorg.key() :
				continue
			if compareOrganization(org, eorg) :
				org.refer = eorg


	for crisis in cList :
		if crisis.refer == None :
			continue
		#update idrefs to crisis to refer's idref.
		mergeCrisis(crisis, crisis.refer)
		#delete
		deleteCrisis(crisis)"""