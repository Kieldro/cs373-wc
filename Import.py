# -*- coding: utf-8 -*-
"""This module builds the models from the constructed tree."""
from Models import *
from google.appengine.ext.db import delete, get
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

	cList = generateList(cTreeList, Crisis.all(), createCrisis, mergeCrisis, root)
	oList = generateList(org_list, Organization.all(), createOrganization, mergeOrganization, root)
	pList= generateList(per_list, Person.all(), createPerson, mergePerson, root)

	buildReferences(Crisis.all(), Organization.all(), Person.all())
	#mergeRefs(cList, oList, pList)

	return cList, oList, pList

# ------------------
# generateList
# ------------------

def generateList(treeList, dataList, createModel, mergeModels, treeRoot):
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
# createReferences
# ------------------

def createSingleReference(itype, ref) :
	"""
	Create a single Reference model, of a given itype and put it in 
	it in the datastore.
	itype a string representing of the thing a reference to
	elem an ElementTree ElementTree
	return a key to the reference in the datastore.
	"""
	d = {}
	d['sref'] = ref.attrib['idref']
	d['rType'] = itype
	r = Reference(**d)
	r.put()

	return r
		
	
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
	dest.name = source.findtext('name')

	orginfo = source.find('info')

	dest.orginfo.otype = orginfo.findtext('type')

	history = orginfo.findtext('history')
	estring = unicode(dest.orginfo.history)
	if history not in estring:
		dest.orginfo.history = dest.orginfo.history + " " + history

	ncontact = orginfo.find('contact')
	dest.orginfo.contacts.phone = ncontact.findtext('phone')
	dest.orginfo.contacts.email = ncontact.findtext('email')

	nmail = ncontact.find('mail')
	dest.orginfo.contacts.address.address = nmail.findtext('address')
	dest.orginfo.contacts.address.city = nmail.findtext('city')
	dest.orginfo.contacts.address.state = nmail.findtext('state')
	dest.orginfo.contacts.address.country = nmail.findtext('country')
	dest.orginfo.contacts.address.zipcode = nmail.findtext('zip')

	dest.orginfo.contacts.address.put()
	dest.orginfo.contacts.put()

	nloc = orginfo.find('loc')
	dest.orginfo.location.city = nloc.findtext('city')
	dest.orginfo.location.region = nloc.findtext('region')
	dest.orginfo.location.country = nloc.findtext('country')

	dest.orginfo.location.put()
	dest.orginfo.put()

	misc = source.findtext('misc')
	estring = unicode(dest.misc)
	if misc not in estring:
		dest.misc = dest.misc + " " + misc


	mergeIDREFS(source, dest, "crisis", dest.crisisref)
	mergeIDREFS(source, dest, "person", dest.personref)
	mergeLinks(source, dest)
	dest.put()

def mergePerson(source, dest) :
	dest.name = source.findtext('name')

	perinfo = source.find('info')

	dest.personinfo.ptype = perinfo.findtext('type')
	dest.personinfo.nationality = perinfo.findtext('nationality')
	dest.personinfo.biography = perinfo.findtext('biography')

	bday = perinfo.find('birthdate')
	dest.personinfo.birthdate.time = bday.findtext('time')
	dest.personinfo.birthdate.day = bday.findtext('day')
	dest.personinfo.birthdate.month = bday.findtext('month')
	dest.personinfo.birthdate.year = bday.findtext('year')
	dest.personinfo.birthdate.time_misc = bday.findtext('misc')
	dest.personinfo.birthdate.put()

	dest.personinfo.put()

	misc = source.findtext('misc')
	estring = unicode(dest.misc)
	if misc not in estring:
		dest.misc = dest.misc + " " + misc


	mergeIDREFS(source, dest, "crisis", dest.crisisref)
	mergeIDREFS(source, dest, "org", dest.orgref)
	mergeLinks(source, dest)
	dest.put()

def mergeCrisis(source, dest) :
	dest.name = source.findtext('name')

	criinfo = source.find('info')

	history = criinfo.findtext('history')
	estring = unicode(dest.crisisinfo.history)
	if history not in estring:
		dest.crisisinfo.history = dest.crisisinfo.history + " " + history

	dest.crisisinfo.helps = criinfo.findtext('help')
	dest.crisisinfo.resources = criinfo.findtext('resources')
	dest.crisisinfo.ctype = criinfo.findtext('type')

	nloc = criinfo.find('loc')
	dest.crisisinfo.location.city = nloc.findtext('city')
	dest.crisisinfo.location.region = nloc.findtext('region')
	dest.crisisinfo.location.country = nloc.findtext('country')
	dest.crisisinfo.location.put()

	impact = criinfo.find('impact')
	himpact = impact.find('human')
	dest.crisisinfo.impact.human_impact.deaths = himpact.findtext('deaths')
	dest.crisisinfo.impact.human_impact.displaced = himpact.findtext('displaced')
	dest.crisisinfo.impact.human_impact.injured = himpact.findtext('injured')
	dest.crisisinfo.impact.human_impact.missing = himpact.findtext('missing')
	dest.crisisinfo.impact.human_impact.himpact_misc = himpact.findtext('misc')
	dest.crisisinfo.impact.human_impact.put()

	eimpact = impact.find('economic')
	dest.crisisinfo.impact.eco_impact.amount = eimpact.findtext('amount')
	dest.crisisinfo.impact.eco_impact.currency =  eimpact.findtext('currency')
	dest.crisisinfo.impact.eco_impact.eimpact_misc = eimpact.findtext('misc')
	dest.crisisinfo.impact.eco_impact.put()
	dest.crisisinfo.impact.put()

	time = criinfo.find('time')
	dest.crisisinfo.date.time = time.findtext('time')
	dest.crisisinfo.date.day = time.findtext('day')
	dest.crisisinfo.date.month = time.findtext('month')
	dest.crisisinfo.date.year = time.findtext('year')
	dest.crisisinfo.date.time_misc = time.findtext('misc')
	dest.crisisinfo.date.put()

	dest.crisisinfo.put()



	misc = source.findtext('misc')
	estring = unicode(dest.misc)
	if misc not in estring:
		dest.misc = dest.misc + " " + misc


	mergeIDREFS(source, dest, "person", dest.personref)
	mergeIDREFS(source, dest, "org", dest.orgref)
	mergeLinks(source, dest)
	dest.put()

def mergeLinks(source, dest) :
	refs = source.find('ref')
	primaryImage = refs.find('primaryImage')
	epi = dest.reflink.primaryImage
	epi.site = primaryImage.findtext('site')
	epi.title = primaryImage.findtext('title')
	epi.url = primaryImage.findtext('url').strip()
	epi.description = primaryImage.findtext('description')
	dest.reflink.primaryImage.put()
	
	mergeRefs(refs.findall('image'), dest.reflink.image, 'image')
	mergeRefs(refs.findall('video'), dest.reflink.video, 'video')
	mergeRefs(refs.findall('social'), dest.reflink.social, 'social')
	mergeRefs(refs.findall('ext'), dest.reflink.ext, 'ext')
	dest.reflink.put()

def mergeRefs(nList, eList, eType) :
	if len(nList) >= len(eList) :
		eList = []
		for elem in nList :
			eList.append(createLink(eType, elem).key())

def mergeIDREFS(source, dest, eType, refObject) :
	idList = source.findall(eType)

	for i in idList :
		for j in refObject:
			elem = get(j)
			if i.attrib['idref'] == elem.sref :
				break
		else :
			#add i to dest
			refObject.append(createSingleReference(eType, i).key())