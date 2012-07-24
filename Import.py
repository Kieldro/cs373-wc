# -*- coding: utf-8 -*-
from Models import *
from xml.etree.ElementTree import Element, SubElement
	
	
# ------------------
# buildModels
# ------------------

def buildModels(tree) :
	"""
	take in an element tree object that contains an eml file
	create and store the models in the data store and returns 
	lists of the page opjects
	tree is an ElementTree object
	return 3 lists of WorldCrisisPage objects
	"""
	root = tree.getroot()
	cri_list = root.findall('crisis')
	org_list = root.findall('organization')
	per_list= root.findall('person')
	
	cList = []
	for crisis in cri_list :
		cList.append(createCrisis(crisis))
	
	oList = []
	for org in org_list :
			oList.append(createOrganization(org))
	
	pList= []
	for person in per_list :
		pList.append(createPerson(person))

	buildReferences(cList, oList, pList)
	
	return cList, oList, pList
	
	
# ------------------
# createCrisis
# ------------------

def createCrisis(elem):
	"""
	create a crisis model, including references to all child models, 
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Crisis in the datastore
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
	create a organization model, including references to all child models, 
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the organization in the datastore
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
	create a person model, including references to all child models, 
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the person in the datastore
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
	create a Date model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Date in the datastore
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
	create a CrisisInfo model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the CrisisInfo in the datastore
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
	create a OrgInfo model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the OrgInfo in the datastore
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
	create a PersonInfo model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the PersonInfo in the datastore
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
	create all the reference models for a single info instance, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the  in the datastore
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
	create a Link model, and put it in the datastore.
	etype is a string representation of the type of the link
	elem an ElementTree ElementTree
	return a key to the Link in the datastore
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
	create Reference models, of a given itype and put them in 
	it in the datastore.
	itype a string representing of the thing a reference to
	elem an ElementTree ElementTree
	return a key to the EconomicImpact in the datastore
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
	create a Location model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Location in the datastore
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
	create a HumanImpact model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the HumanImpact in the datastore
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
	create a EconomicImpact model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the EconomicImpact in the datastore
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
	create a Impact model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the Impact in the datastore
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
	create a FullAddress model, and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the FullAddress in the datastore
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
	create a contact model, including references to all child models
	and put it in the datastore.
	elem an ElementTree ElementTree
	return a key to the contact in the datastore
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
	build references to each object using the keys provided by the 
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

