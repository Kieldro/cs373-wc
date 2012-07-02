import sys #remove this later
from Models import Crisis, Organization, Person
from xml.etree.ElementTree import Element, SubElement, parse

def buildModels(tree) :
	root = tree.getroot()
	crisesRoot = tree.find('crises')
	organizationsRoot = tree.find('organizations')
	peopleRoot = tree.find('people')
	
	crisesList = crisesRoot.getchildren()
	organizationsList = organizationsRoot.getchildren()
	peopleList = peopleRoot.getchildren()
	
	cList = []
	for crisis in crisesList :
		cList.append(createCrisis(crisis))
	
	oList = []
	for org in organizationsList :
			oList.append(createOrganization(org))
	
	pList= []
	for person in peopleList :
		pList.append(createPerson(person))
	
	return cList, oList, pList
		
def dictCommonElements(elem) :
	"""
	Builds a dict for the common elements.
	elem is the root element of a crisis, organization, or person
	returns a dict with the values of the common elements.
	"""
	d = {}
	d['ID'] = elem.attrib['id']
	d['name'] = elem.findtext('name')
	d['knd'] = elem.findtext('kind')
	
	"""
	Within <location>, there can either be:
	- <unspecific> or 
	- the set <city>, <state>, <country>, with each element optional.
	"""
	locationElem = elem.find('location')
	location_text = locationElem.findtext('unspecific')
	if location_text != None:
		d['location'] = location_text
	else :
		d['location'] = ""
		city_text = locationElem.findtext('city')
		state_text = locationElem.findtext('state')
		country_text = locationElem.findtext('country')
		if city_text != None :
			d['city'] = city_text
		else :
			d['city'] = ""
		if state_text != None :
			d['state'] = state_text
		else :
			d['state'] = ""
		if country_text != None :
			d['country'] = country_text
		else :
			d['country'] = ""
	
	# The following four can have multiple tags of the same name
	d['image'] = [str(i.text) for i in elem.findall('image')]
	d['video'] = [str(v.text) for v in elem.findall('video')]
	d['network'] = [str(n.text) for n in elem.findall('network')]
	d['link'] = [str(l.text) for l in elem.findall('link')]
	"""
	print 'START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	for k, v in d.items() :
		print '%s = %s' % (k, v)
		
	print 'END-------------------------------------------------------'
	"""
	return d
	
def createCrisis(elem) :
	"""
	Creates a Crisis instance.
	elem is the root element of a crisis (<crisis>)
	returns the crisis as an instance of Crisis
	"""
	d = dictCommonElements(elem)

	"""
	The date tag contains either:
	- <otherDiscription>
	- or the set containing <start>, <end>, and/or <additional>
	"""
	dateElem = elem.find('date')
	date_text = dateElem.findtext('otherDiscription')
	if date_text != None :
		d['date'] = date_text
	else :
		d['date'] = ""
		start_text = dateElem.findtext('start')
		end_text = dateElem.findtext('end')
		additional_text = dateElem.findtext('additional')
		if start_text != None:
			d['startDate'] = start_text
		else:
			d['startDate'] = ""
		if end_text != None:
			d['endDate'] = end_text
		else:
			d['endDate'] = ""
		if additional_text != None:
			d['additional'] = additional_text
		else:
			d['additional'] = ""


	d['humanImpact'] = elem.findtext('humanImpact')
	d['ecoImpact'] = elem.findtext('economicImpact')
	d['resources'] = elem.findtext('resourcesNeeded')
	
	waysToHelpElem = elem.find('waysToHelp')
	first_text = waysToHelpElem.text
	if first_text != None :
		text_list = [first_text, ]
	else :
		text_list = ["", ]
		
	links_list = []
	linkElems = waysToHelpElem.findall('link')
	for link in linkElems :
		links_list.append(str(link.text))	
		text_list.append(str(link.tail))		#Should I append "" if no tail?
	
	d['waysToHelpText'] = text_list
	d['waysToHelpLinks'] = links_list
	
	d['orgs'] = [str(o.text) for o in elem.findall('organizationId')]
	d['people'] = [str(p.text) for p in elem.findall('personId')]
	"""
	print 'START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	for k, v in d.items() :
		print '%s = %s' % (k, v)
		
	print 'END-------------------------------------------------------'
	"""
	c = Crisis(**d)
	return c
	
def createOrganization(elem) :
	"""
	Creates an Oragnization instance.
	elem is the root element of an organization (<organization>)
	returns the organization as an instance of Organization
	"""
	d = dictCommonElements(elem)
	d['history'] = elem.findtext('history')
	
	contactElem = elem.find('contactInfo')
	first_text = Element(contactElem).text
	if first_text != None :
		text_list = [first_text, ]
	else :
		text_list = ["", ]
	
	links_list	= []
	linkElems = Element(contactElem).findall('link')
	for link in linkElems :
		links_list.append(str(link.text))	
		text_list.append(str(link.tail))		#Should I append "" if no tail?
	
	d['contactInfoText'] = text_list
	d['contactInfoLinks'] = links_list
	
	d['crises'] = [str(c.text) for c in elem.findall('crisisId')]
	d['people'] = [str(p.text) for p in elem.findall('personId')]
	
	"""
	print 'START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	for k, v in d.items() :
		print '%s = %s' % (k, v)
		
	print 'END-------------------------------------------------------'
	"""
	o = Organization(**d)
	return o
	
def createPerson(elem) :
	"""
	Creates a Person instance.
	elem is the root element of a person (<person>)
	returns the person as an instance of Person
	"""
	d = dictCommonElements(elem)
	
	d['orgs'] = [o.text for o in elem.findall('organizationId')]
	d['crises'] = [c.text for c in elem.findall('crisisId')]
	"""
	print 'START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	for k, v in d.items() :
		print '%s = %s' % (k, v)
		
	print 'END-------------------------------------------------------'
	"""
	p = Person(**d)
	return p

if __name__ == "__main__" :
	tree = parse(sys.stdin)
	buildModels(tree)
