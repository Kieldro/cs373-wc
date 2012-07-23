# -*- coding: utf-8 -*-
import unittest
from Models import *
from Import import *
from Export import *
from xml.etree.ElementTree import Element, SubElement, parse, fromstring, tostring, dump
import StringIO
#from google.appengine.ext import db

headOpen = """<worldCrises>"""
headClose = """</worldCrises>"""
crisisClose = """</crisis>"""
orgClose = """</organization>"""
personClose = """</person>"""
	
crisisOpen1 = """<crisis id="test1">"""
crisisOpen2 = """<crisis id="test2">"""
crisisOpen3 = """<crisis id="test3">"""
orgOpen1 = """<organization id="test4">"""
orgOpen2 = """<organization id="test5">"""
orgOpen3 = """<organization id="test6">"""
personOpen1 = """<person id="test7">"""
personOpen2 = """<person id="test8">"""
personOpen3 = """<person id="test9">"""
	
crisisRef1 = """<crisis idref="test1"/>"""
crisisRef2 = """<crisis idref="test2"/>"""
crisisRef3 = """<crisis idref="test3"/>"""
orgRef1 = """<org idref="test4"/>"""
orgRef2 = """<org idref="test5"/>"""
orgRef3 = """<org idref="test6"/>"""
personRef1 = """<person idref="test7"/>"""
personRef2 = """<person idref="test8"/>"""
personRef3 = """<person idref="test9"/>"""
	
name1 = """<name>TESTING TESTING TESTING</name>"""
name2 = """<name>Formula</name>"""
name3 = """<name></name>"""
infoOpen = """<info>"""
infoClose = """</info>"""
help = """<help>Learn</help>"""
	
resources1 = """<resources>Money donations and food donations.</resources>"""
resources2 = """<resources/>"""
resources3 = """<resources>pick-a-dilly</resources>"""

contactOpen1 = """<contact><phone>2145977684</phone><email>callmeelasinthe@gmail.com</email>"""
				
contactOpen2 = """<contact><phone></phone><email></email>"""
contactClose = """</contact>"""
	
address1 = """<mail><address>1044 Camino La Costa</address><city>Austin</city><state>TX</state><country>USA</country><zip>78752</zip></mail>"""
				
address2 = """<mail><address>707 E. 47th St
					Unit A</address><city>Austin</city><state>TX</state><country></country><zip>78751</zip></mail>"""
			
address3 = """<mail><address></address><city></city><state></state><country></country><zip></zip></mail>"""
	
type1 = """<type>Pizza Boy</type>"""
type2 = """<type>Astroid</type>"""
type3 = """<type>Global</type>"""
	
history1 = """<history>RESEARCH ON WORLD HUNGER HISTORY</history>"""
history2 = """<history>RESEARCH ON WORLD HUNGER HISTORY</history>"""
history3 = """<history/>"""
	
timeOpen = """<time>"""
timeClose = """</time>"""
bdayOpen = """<birthdate>"""
bdayClose = """</birthdate>"""
	
bio1 = """<biography></biography>"""
bio2 = """<biography/>"""
bio3 = """<biography>Apart from her work in music, Knowles has also ventured into acting and designing clothes and perfumes. She made her acting debut in the musical film Carmen: A Hip Hopera (2001), prior to appearing in major films, including Austin Powers in Goldmember (2002), Dreamgirls (2006), which earned her two Golden Globe nominations, Cadillac Records (2008) and Obsessed (2009). In 2005, Knowles and her mother introduced their familys fashion line, House of Deron, and in 2010, she released her first perfume, Heat. She has endorsed brands including, LOral, Pepsi, Tommy Hilfiger, Nintendo and Vizio. In 2010, Knowles was ranked first on Forbes list of the 100 Most Powerful and Influential Musicians in the World,[4] and second on its list of the 100 Most Powerful and Influential Celebrities in the World.[5] In 2012, she was named Worl's Most Beautiful Woman by People magazine.
Knowles work has earned her numerous awards and accolades, including 16 Grammy Awards, 11 MTV Video Music Awards, three American Music Awards, a Billboard Millennium Award, and a star on the Hollywood Walk of Fame with Destinys Child. In 2009, Billboard named her the Top Radio Songs Artist of the 2000s decade,[6] and ranked her as the 4th overall Artist of the Decade (and as the First Female Artist of that period).[7] The Recording Industry Association of America (RIAA), also recognized Knowles as the Top Certified Artist of the 2000s.[8][9] In the US, Knowles has sold over 11.2 million albums as of May 2010,[10] and more than 30.4 million digital singles as of January 2012.[11] She has sold 75 million records worldwide, making her one of the best-selling music artists of all time.[12] Knowles appeared on VHSs 2010 list of the 100 Greatest Artists of All Time,[13] and ranked third on their 100 Greatest Women in Music list in 2012.[14] In April 2008, Knowles married American rapper Jay-Z, and gave birth to their first child, Blue Ivy Carter, in January 2012.</biography>"""
	
nat1 = """<nationality></nationality>"""
nat2 = """<nationality>Unknown</nationality>"""
nat3 = """<nationality/>"""
	
dateMid1 = """<time>Ongoing</time><day>3</day><month>16</month><year>-1</year>"""
				
dateMid2 = """<time>5:53AM</time><day>16</day><month>8</month><year>1983</year>"""
				
dateMid3 = """<time></time><day>20</day><month>20</month><year>20</year>"""
	
location1 = """<loc><city>All cities</city><region>All regions</region><country>All countries</country></loc>"""
			
location2 = """<loc><city>Meknes</city><region>North Africa</region><country>Morocco</country></loc>"""
			
location3 = """<loc><city>Paris</city><region></region><country>France</country></loc>"""
	
impactOpen = """<impact>"""
impactClose = """</impact>"""
  
humanImpactOpen1 = """<human><deaths>-1</deaths><displaced>-1</displaced><injured>-1</injured><missing>-1</missing>"""
					
humanImpactOpen2 = """<human><deaths>-1</deaths><displaced>-1</displaced><injured>-1</injured><missing>-1</missing>"""
	
humanImpactOpen3 = """<human><deaths>-1</deaths><displaced>-1</displaced><injured>-1</injured><missing>-1</missing>"""
humanImpactClose = """</human>"""
			
ecoImpactOpen1 = """<economic><amount>12039847</amount><currency>RESEARCH burritos</currency>"""
ecoImpactOpen2 = """<economic><amount>23</amount><currency></currency>"""
ecoImpactOpen3 = """<economic><amount>0</amount><currency>Yen</currency>"""
ecoImpactClose = """</economic>"""
	
misc1 = """<misc>research</misc>"""
misc2 = """<misc>All the single ladies (7x)

Now put your hands up
Up in the club, we just broke up
Im doing my own little thing
you Decided to dip but now you wanna trip
Cuz another brother noticed me
Im up on him, he up on me
dont pay him any attention
cuz i cried my tears, GAVE three good years
Ya cant be mad at me

[Chorus]
Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Dont be mad once you see that he want it
If you liked it then you shoulda put a ring on it

wo oh ooh oh oh ooh oh oh ooh oh oh oh x2


(Chorus)Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Dont be mad once you see that he want it
If you liked it then you shoulda put a ring on it


I got gloss on my lips, a man on my hips
hold me tighter than my Dereon jeans
acting up, drink in my cup
I couldnt care less what you think
I need no permission, did I mention
Dont pay him any attention
Cuz you had your turn
But now you gonna learn
What it really feels like to miss me

(Chorus)

Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Dont be mad once you see that he want it
If you liked it then you shoulda put a ring on it

woo oh ooh oh oh ooh oh oh ooh oh oh oh 2x

Dont treat me to the things of this world
Im not that kind of girl
Your love is what I prefer, what I deserve
Is a man that makes me, then takes me
And delivers me to a destiny, to infinity and beyond
Pull me into your arms
Say Im the one you WANT
If you dont, youll be alone
And like a ghost Ill be gone

All the single ladies (7x)
Now put your hands up
woo oh ooh oh oh ooh oh oh ooh
oh oh oh 2x

Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Dont be mad once you see that he want it
If you liked it then you shoulda put a ring on it woo oh ooh 2x</misc>"""
misc3 = """<misc/>"""
		
refOpen = """<ref>"""
refClose = """</ref>"""

p_imageLink = """<primaryImage><site>http://stopworldhunger.webs.com</site><title>World Hunger</title><url>http://stopworldhunger.webs.com/hunger.jpg</url><description>Starving children</description></primaryImage>"""
			
imageLink1 = """<image><site>TestImage1</site><title>World Health Organization</title><url>http://www.who.int/en</url><description>World Health Organization</description></image>"""
			
imageLink2 = """<image><site>TestImage2</site><title>World Hunger</title><url>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</url><description>Homeless Sign</description></image>"""

imageLink3 = """<image><site>TestImage3</site><title>World Health Organization</title><url>http://www.who.int/en</url></image>"""

videoLink1 = """<video><site>TestVideo1</site><title>World Health Organization</title><url>http://www.who.int/en</url><description>World Health Organization</description></video>"""
			
videoLink2 = """<video><site>TestVideo2</site><title>World Health Organization</title><url>http://www.google.com/</url><description>World Health Organization</description></video>"""

videoLink3 = """<video><site>TestVideo3</site><title>World Health Organization</title><url>http://www.who.int/en</url></video>"""

socialLink1 = """<social><site>TestSocial1</site><title>World Health Organization</title><url>http://www.who.int/en</url><description>World Health Organization</description></social>"""
			
socialLink2 = """<social><site>TestSocial2</site><title>World Health Organization</title><url>http://www.google.com/</url><description>World Health Organization</description></social>"""

socialLink3 = """<social><site>TestSocial3</site><title>World Health Organization</title><url>http://www.who.int/en</url></social>"""


extLink1 = """<ext><site>TestSite1</site><title>World Health Organization</title><url>http://www.who.int/en</url><description>World Health Organization</description></ext>"""
			
extLink2 = """<ext><site>TestSite2</site><title>World Health Organization</title><url>http://www.google.com/</url><description>World Health Organization</description></ext>"""

extLink3 = """<ext><site>TestSite3</site><title>World Health Organization</title><url>http://www.who.int/en</url></ext>"""


cDate1 = timeOpen + dateMid1 + misc1 + timeClose
cDate2 = timeOpen + dateMid2 + misc2 + timeClose
cDate3 = bdayOpen + dateMid3 + misc3 + bdayClose

himpact1 = humanImpactOpen1 + misc1 + humanImpactClose
himpact2 = humanImpactOpen2 + misc2 + humanImpactClose
himpact3 = humanImpactOpen3 + misc3 + humanImpactClose

eimpact1 = ecoImpactOpen1 + misc1 + ecoImpactClose
eimpact2 = ecoImpactOpen2 + misc2 + ecoImpactClose
eimpact3 = ecoImpactOpen3 + misc3 + ecoImpactClose

impact1 = impactOpen + himpact1 + eimpact3 + impactClose
impact2 = impactOpen + himpact2 + eimpact2 + impactClose
impact3 = impactOpen + himpact3 + eimpact1 + impactClose

cInfo1 = infoOpen + history1 + help + resources1 + type3 + cDate2 + location1 + impact1 + infoClose
cInfo2 = infoOpen + history2 + help + resources2 + type1 + cDate1 + location2 + impact2 + infoClose
cInfo3 = infoOpen + history3 + help + resources3 + type2 + cDate1 + location3 + impact3 + infoClose

refs1 = refOpen + p_imageLink + imageLink1 + videoLink1 + socialLink1 + extLink1 + refClose
refs2 = refOpen + p_imageLink + imageLink1 + imageLink2 + videoLink1 + videoLink2 + socialLink1 + socialLink2 + extLink1 + extLink2 + refClose
refs3 = refOpen + p_imageLink + imageLink1 + imageLink2 + imageLink3 + videoLink1 + videoLink2 + videoLink3 + socialLink1 + socialLink2 + socialLink3 + extLink1 + extLink2 + extLink3 + refClose
refs4 = refOpen + p_imageLink + imageLink1 + imageLink2 + imageLink3 + videoLink3 + socialLink1 + socialLink3 + extLink2 + refClose

crisis1 = crisisOpen3 + name2 + cInfo1 + refs2 + misc3 + orgRef1 + personRef2 + crisisClose
crisis2 = crisisOpen2 + name1 + cInfo3 + refs4 + misc2 + orgRef1 + orgRef2 + personRef2 + personRef3 + crisisClose
crisis3 = crisisOpen1 + name3 + cInfo2 + refs3 + misc2 + orgRef3 + personRef1 + crisisClose
crisis4 = crisisOpen1 + name2 + cInfo1 + refs1 + misc1 + orgRef1 + orgRef2 + orgRef3 + personRef2 + personRef3 + personRef1 + crisisClose

contact1 = contactOpen1 + address3 + contactClose
contact2 = contactOpen2 + address2 + contactClose
contact3 = contactOpen1 + address1 + contactClose

oInfo1 = infoOpen + type1 + history2 + contact3 + location3 + infoClose
oInfo2 = infoOpen + type2 + history3 + contact1 + location2 + infoClose
oInfo3 = infoOpen + type3 + history1 + contact2 + location1 + infoClose

pInfo1 = infoOpen + type1 + cDate3 + nat1 + bio3 + infoClose
pInfo2 = infoOpen + type2 + cDate3 + nat2 + bio1 + infoClose
pInfo3 = infoOpen + type3 + cDate3 + nat3 + bio2 + infoClose

org1 = orgOpen3 + name2 + oInfo1 + refs2 + misc3 + crisisRef1 + personRef2 + orgClose
org2 = orgOpen2 + name1 + oInfo3 + refs4 + misc2 + crisisRef1 + crisisRef2 + personRef2 + personRef3 + orgClose
org3 = orgOpen1 + name3 + oInfo2 + refs3 + misc2 + crisisRef3 + personRef1 + orgClose
org4 = orgOpen1 + name2 + oInfo1 + refs1 + misc1 + crisisRef1 + crisisRef2 + crisisRef3 + personRef2 + personRef3 + personRef1 + orgClose

person1 = personOpen3 + name2 + pInfo1 + refs2 + misc3 + crisisRef1 + orgRef2 + personClose
person2 = personOpen2 + name1 + pInfo3 + refs4 + misc2 + crisisRef1 + crisisRef2 + orgRef2 + orgRef3 + personClose
person3 = personOpen1 + name3 + pInfo2 + refs3 + misc2 + crisisRef3 + orgRef1 + personClose
person4 = personOpen1 + name2 + pInfo1 + refs1 + misc1 + crisisRef1 + crisisRef2 + crisisRef3 + orgRef2 + orgRef3 + orgRef1 + personClose


# Actual tests start here
class TestWC2(unittest.TestCase):
	
# -----------
# test_person
# -----------

	def test_person1(self):
		root = fromstring(person1)
		model = createPerson(root)
		elem = Element('person')
		buildPersonPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	

	def test_person2(self):
		root = fromstring(person2)
		model = createPerson(root)
		elem = Element('person')
		buildPersonPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	
		
	def test_person3(self):
		root = fromstring(person3)
		model = createPerson(root)
		elem = Element('person')
		buildPersonPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	
		
	def test_person4(self):
		root = fromstring(person4)
		model = createPerson(root)
		elem = Element('person')
		buildPersonPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	
	
# -----------
# test_org
# -----------

	def test_org1(self):
		root = fromstring(org1)
		model = createOrganization(root)
		elem = Element('organization')
		buildOrgPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	
		
	def test_org2(self):
		root = fromstring(org2)
		model = createOrganization(root)
		elem = Element('organization')
		buildOrgPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	
		
	def test_org3(self):
		root = fromstring(org3)
		model = createOrganization(root)
		elem = Element('organization')
		buildOrgPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	
		
	def test_org4(self):
		root = fromstring(org4)
		model = createOrganization(root)
		elem = Element('organization')
		buildOrgPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)	

# ------------	
# test_personInfo
# ------------

	def test_personInfo1(self):
		root = fromstring(pInfo1)
		model = createPersonInfo(root)
		elem = Element('test')
		buildPersonInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_personInfo2(self):
		root = fromstring(pInfo2)
		model = createPersonInfo(root)
		elem = Element('test')
		buildPersonInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_personInfo3(self):
		root = fromstring(pInfo3)
		model = createPersonInfo(root)
		elem = Element('test')
		buildPersonInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
	
# ------------	
# test_orgInfo
# ------------

	def test_orgInfo1(self):
		root = fromstring(oInfo1)
		model = createOrgInfo(root)
		elem = Element('test')
		buildOrgInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_orgInfo2(self):
		root = fromstring(oInfo2)
		model = createOrgInfo(root)
		elem = Element('test')
		buildOrgInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_orgInfo3(self):
		root = fromstring(oInfo3)
		model = createOrgInfo(root)
		elem = Element('test')
		buildOrgInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
# -------------
# test_contact
# -------------

	def test_contact1(self):
		root = fromstring(contact1)
		model = createContacts(root)
		elem = Element('test')
		buildContact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

	def test_contact2(self):
		root = fromstring(contact2)
		model = createContacts(root)
		elem = Element('test')
		buildContact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_contact3(self):
		root = fromstring(contact3)
		model = createContacts(root)
		elem = Element('test')
		buildContact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
	
# -------------
# test_address
# -------------

	def test_address1(self):
		root = fromstring(address1)
		model = createFullAddress(root)
		elem = Element('test')
		buildAddress(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_address2(self):
		root = fromstring(address2)
		model = createFullAddress(root)
		elem = Element('test')
		buildAddress(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

	def test_address3(self):
		root = fromstring(address3)
		model = createFullAddress(root)
		elem = Element('test')
		buildAddress(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

# -----------
# test_crisis
# -----------

	def test_crisis1(self):
		root = fromstring(crisis1)
		model = createCrisis(root)
		elem = Element('crisis')
		buildCrisisPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)
		
	def test_crisis2(self):
		root = fromstring(crisis2)
		model = createCrisis(root)
		elem = Element('crisis')
		buildCrisisPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)

	def test_crisis3(self):
		root = fromstring(crisis3)
		model = createCrisis(root)
		elem = Element('crisis')
		buildCrisisPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)
		
	def test_crisis4(self):
		root = fromstring(crisis4)
		model = createCrisis(root)
		elem = Element('crisis')
		buildCrisisPage(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)

# -------------------
# test_external_links
# -------------------

	def test_external_links1(self):
		root = fromstring(refs1)
		model = createRefLinks(root)
		elem = Element('test')
		buildExternalRefs(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_external_links2(self):
		root = fromstring(refs2)
		model = createRefLinks(root)
		elem = Element('test')
		buildExternalRefs(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_external_links3(self):
		root = fromstring(refs3)
		model = createRefLinks(root)
		elem = Element('test')
		buildExternalRefs(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_external_links4(self):
		root = fromstring(refs4)
		model = createRefLinks(root)
		elem = Element('test')
		buildExternalRefs(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

# ------------	
# test_link
# ------------

	def test_link1(self):
		root = fromstring(p_imageLink)
		model = createLink('primaryImage', root)
		elem = Element('primaryImage')
		buildLink(elem, model.site, model.title, model.url, model.description)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)
		
	def test_link2(self):
		root = fromstring(imageLink1)
		model = createLink('image', root)
		elem = Element('image')
		buildLink(elem, model.site, model.title, model.url, model.description)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)
		
	def test_link3(self):
		root = fromstring(videoLink1)
		model = createLink('video', root)
		elem = Element('video')
		buildLink(elem, model.site, model.title, model.url, model.description)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)
		
	def test_link4(self):
		root = fromstring(socialLink1)
		model = createLink('social', root)
		elem = Element('social')
		buildLink(elem, model.site, model.title, model.url, model.description)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)
		
	def test_link5(self):
		root = fromstring(extLink1)
		model = createLink('ext', root)
		elem = Element('ext')
		buildLink(elem, model.site, model.title, model.url, model.description)
		rootstring = tostring(root)
		elemstring = tostring(elem)
		self.assert_(rootstring == elemstring)

# ------------	
# test_crisisInfo
# ------------

	def test_crisisInfo1(self):
		root = fromstring(cInfo1)
		model = createCrisisInfo(root)
		elem = Element('test')
		buildCrisisInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

	def test_crisisInfo2(self):
		root = fromstring(cInfo2)
		model = createCrisisInfo(root)
		elem = Element('test')
		buildCrisisInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

	def test_crisisInfo3(self):
		root = fromstring(cInfo3)
		model = createCrisisInfo(root)
		elem = Element('test')
		buildCrisisInfo(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

# ------------	
# test_location
# ------------

	def test_location1(self):
		root = fromstring(location1)
		model = createLocationInfo(root)
		elem = Element('test')
		buildLocation(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_location2(self):
		root = fromstring(location2)
		model = createLocationInfo(root)
		elem = Element('test')
		buildLocation(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_location3(self):
		root = fromstring(location3)
		model = createLocationInfo(root)
		elem = Element('test')
		buildLocation(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
# ----------------
# test_humanimpact
# ----------------

	def test_himpact1(self):
		root = fromstring(himpact1)
		model = createHumanImpact(root)
		elem = Element('test')
		buildHumanImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_himpact2(self):
		root = fromstring(himpact2)
		model = createHumanImpact(root)
		elem = Element('test')
		buildHumanImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_himpact3(self):
		root = fromstring(himpact3)
		model = createHumanImpact(root)
		elem = Element('test')
		buildHumanImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
# ----------------
# test_impact
# ---------------
		
	def test_impact1(self) :
		root = fromstring(impact1)
		model = createImpact(root)
		elem = Element('test')
		buildImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_impact2(self) :
		root = fromstring(impact2)
		model = createImpact(root)
		elem = Element('test')
		buildImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_impact3(self) :
		root = fromstring(impact3)
		model = createImpact(root)
		elem = Element('test')
		buildImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
		
# -------------------
# test_economicimpact
# -------------------
	def test_eimpact1(self):
		root = fromstring(eimpact1)
		model = createEconomicImpact(root)
		elem = Element('test')
		buildEconomicImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_eimpact2(self):
		root = fromstring(eimpact2)
		model = createEconomicImpact(root)
		elem = Element('test')
		buildEconomicImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_eimpact3(self):
		root = fromstring(eimpact3)
		model = createEconomicImpact(root)
		elem = Element('test')
		buildEconomicImpact(elem, model)
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
	
	
# ------------	
# test_date
# ------------

	def test_date1(self):
		root = fromstring(cDate1)
		model = createDate(root)
		elem = Element('test')
		buildDate(elem, model, 'time')
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)

	def test_date2(self):
		root = fromstring(cDate2)
		model = createDate(root)
		elem = Element('test')
		buildDate(elem, model, 'time')
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
	def test_date3(self):
		root = fromstring(cDate3)
		model = createDate(root)
		elem = Element('test')
		buildDate(elem, model, 'birthdate')
		rootstring = tostring(root)
		elemstring = tostring(elem[0])
		self.assert_(rootstring == elemstring)
		
#unittest.main()