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
	
	return cList, oList, pList
	
def createCrisis(elem):
	d = {}
	#d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['misc'] = elem.findtext('misc')
	d['crisisinfo'] = createCrisisInfo(elem.find('info'))
	d['reflink'] = createRefLinks(elem.find('ref'))

	personrefs = createReferences('person', elem)
	d['personref'] = personrefs[0]
	orgrefs = createReferences('org', elem)
	d['orgref'] = orgrefs[0]
	
	c = Crisis(**d)
	for personref in personrefs :
		c.personref = personref

	for orgref in orgrefs:
		c.orgref = orgref

	c.put()
	return c
		
def createOrganization(elem):
	d = {}
	#d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['misc'] = elem.findtext('misc')
	d['orginfo'] = createOrgInfo(elem.find('info'))
	d['reflink'] = createRefLinks(elem.find('ref'))

	crisisrefs = createReferences('crisis', elem)
	d['crisisref'] = crisisrefs[0]
	personrefs = createReferences('person', elem)
	d['personref'] = personrefs[0]
	
	o = Organization(**d)
	for crisisref in crisisrefs:
		o.crisisref = crisisref

	for personref in personrefs :
		o.personref = personref

	o.put()
	return o
	
def createPerson(elem):
	d = {}
	#d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['misc'] = elem.findtext('misc')
	d['personinfo'] = createPersonInfo(elem.find('info'))
	d['reflink'] = createRefLinks(elem.find('ref'))

	crisisrefs = createReferences('crisis', elem)
	d['crisisref'] = crisisrefs[0]
	orgrefs = createReferences('org', elem)
	d['orgref'] = orgrefs[0]
	
	p = Person(**d)
	for crisisref in crisisrefs:
		p.crisisref = crisisref

	for orgref in orgrefs:
		p.orgref = orgref

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
		image_list.append(createLink('image', image))
	d['image'] = image_list[0]
	
	videos = elem.findall('video')
	video_list = []
	for video in videos :
		video_list.append(createLink('video', video))
	d['video'] = video_list[0]
	
	socials = elem.findall('social')
	social_list = []
	for social in socials :
		social_list.append(createLink('social', social))
	d['social'] = social_list[0]
	
	exts = elem.findall('ext')
	ext_list = []
	for ext in exts :
		ext_list.append(createLink('ext', ext))
	d['ext'] = ext_list[0]
	
	rl = ReferenceLinks(**d)

	for image in image_list :
		rl.image = image
	
	for video in video_list :
		rl.video = video
	
	for social in social_list :
		rl.social = social
	
	for ext in ext_list:
		rl.ext = ext
	
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
		ref_list.append(r)

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
