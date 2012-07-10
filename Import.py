# -*- coding: utf-8 -*-
from Models import *
from xml.etree.ElementTree import Element, SubElement

def buildModels(tree) :
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

def createCrisis(elem):
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
		
def createOrganization(elem):
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
	
def createPerson(elem):
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
	
def createDate(elem) :
	d = {}
	d['time'] = elem.findtext('time')
	d['day'] = int(elem.findtext('day'))
	d['month'] = int(elem.findtext('month'))
	d['year'] = int(elem.findtext('year'))
	d['time_misc'] = elem.findtext('misc')
	
	de = Date(**d)
	de.put()
	return de
	
def createCrisisInfo(elem):
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
	
def createOrgInfo(elem):
	d = {}
	d['otype'] = elem.findtext('type')
	d['history'] = elem.findtext('history')	
	
	d['location'] = createLocationInfo(elem.find('loc'))
	d['contacts'] = createContacts(elem.find('contact'))
	
	oi = OrgInfo(**d)
	oi.put()
	return oi
	
def createPersonInfo(elem):
	d = {}
	d['biography'] = elem.findtext('biography')
	d['nationality'] = elem.findtext('nationality')
	d['ptype'] = elem.findtext('type')

	d['birthdate'] = createDate(elem.find('birthdate'))
	
	pi = PersonInfo(**d)
	pi.put()
	return pi
	
def createRefLinks(elem) :
	d = {}
	d['primary_image'] = createLink('primary_image', elem.find('primaryImage'))
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
	
	
def createLink(etype, elem) :
	d = {}
	d['site'] = elem.findtext('site')
	d['title'] = elem.findtext('title')
	d['url'] = elem.findtext('url')
	desc = elem.findtext('description')
	if(desc) :
		d['description'] = desc
	
	d['link_type'] = etype
	
	l = Link(**d)
	l.put()
	return l


def createReferences(itype, elem) :
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
	
def createLocationInfo(elem) :
	d = {}
	d['city'] = elem.findtext('city')
	d['region'] = elem.findtext('region')
	d['country'] = elem.findtext('country')
	
	l = Location(**d)
	l.put()
	return l
	
	
def createHumanImpact(elem) :
	d = {}
	d['deaths'] = int(elem.findtext('deaths'))
	d['displaced'] = int(elem.findtext('displaced'))
	d['injured'] = int(elem.findtext('injured'))
	d['missing'] = int(elem.findtext('missing'))
	d['himpact_misc'] = elem.findtext('misc')
	
	hi = HumanImpact(**d)
	hi.put()
	return hi
	
def createEconomicImpact(elem) :
	d = {}
	d['amount'] = int(elem.findtext('amount'))
	d['currency'] = elem.findtext('currency')
	d['eimpact_misc'] = elem.findtext('misc')
	
	ei = EconomicImpact(**d)
	ei.put()
	return ei
	
def createImpact(elem) :
	d = {}
	d['human_impact'] = createHumanImpact(elem.find('human'))
	d['eco_impact'] = createEconomicImpact(elem.find('economic'))
	
	i = Impact(**d)
	i.put()
	return i
	
def createFullAddress(elem) :
	d = {}
	d['address'] = elem.findtext('address')
	d['city'] = elem.findtext('city')
	d['state'] = elem.findtext('state')
	d['country'] = elem.findtext('country')
	d['zipcode'] = elem.findtext('zip')
	
	fa = FullAddress(**d)
	fa.put()
	return fa
	
def createContacts(elem) :
	d = {}
	d['phone'] = elem.findtext('phone')
	d['email'] = elem.findtext('email')
	d['address'] = createFullAddress(elem.find('mail'))
	
	c = Contacts(**d)
	c.put()
	return c


def buildReferences(cList, oList, pList) :
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

