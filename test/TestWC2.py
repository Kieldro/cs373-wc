# -*- coding: utf-8 -*-
import unittest
from Models import *
from Import import *
from Export import *
from xml.etree.ElementTree import Element, SubElement, parse
import StringIO
#from google.appengine.ext import db



class Success(unittest.TestCase):
	headOpen = """<worldCrises>"""
	headClose = """</worldCrises>"""
	crisisClose = """</crisis>"""
	orgClose = """</organization>"""
	personClose = """</person>"""
	
	crisis1 = """<crisis id="test1">"""
	crisis2 = """<crisis id="test2">"""
	crisis3 = """<crisis id="test3">"""
	org1 = """<organization id="test4">"""
	org2 = """<organization id="test5">"""
	org3 = """<organization id="test6">"""
	person1 = """<person id="test7">"""
	person2 = """<person id="test8">"""
	person3 = """<person id="test9">"""
	
	crisisRef1 = """<crisis idref="test1">"""
	crisisRef2 = """<crisis idref="test2">"""
	crisisRef3 = """<crisis idref="test3">"""
	orgRef1 = """<org idref="test4">"""
	orgRef2 = """<org idref="test5">"""
	orgRef3 = """<org idref="test6">"""
	personRef1 = """<person idref="test7">"""
	personRef2 = """<person idref="test8">"""
	personRef3 = """<person idref="test9">"""
	
	name1 = """<name>TESTING TESTING TESTING</name>"""
	name2 = """<name>Formula</name>"""
	name3 = """<name></name>"""
	infoOpen = """<info>"""
	infoClose = """</info>"""
	help = """<help>Learn</help>"""
	
	resources1 = """<resources>Money donations and food donations.</resources>"""
	resources2 = """<resources/>"""
	resources3 = """<resources>pick-a-dilly</resources>"""
	
	contactOpen1 = """<contact>
				<phone>2145977684</phone>
				<email>callmeelasinthe@gmail.com</email>"""
				
	contactOpen2 = """<contact>
				<phone></phone>
				<email></email>"""
	contactClose = """</contact>"""
	
	address1 = """<mail>
					<address>1044 Camino La Costa</address>
					<city>Austin</city>
					<state>TX</state>
					<country>USA</country>
					<zip>78752</zip>
				</mail>"""
				
	address2 = """<mail>
					<address>707 E. 47th St
					Unit A</address>
					<city>Austin</city>
					<state>TX</state>
					<country></country>
					<zip>78751</zip>
				</mail>"""
			
	address3 = """<mail>
					<address></address>
					<city>/city>
					<state></state>
					<country></country>
					<zip></zip>
				</mail>"""
	
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
	bio3 = """<biography>Beyonce is an American singer, songwriter, record producer and actress. Born and raised in Houston, Texas, she enrolled in various performing arts schools and was first exposed to singing and dancing competitions as a child. Knowles rose to fame in the late 1990s as the lead singer of the R&B girl group Destiny's Child, one of the world's best-selling girl groups of all time.
During the hiatus of Destiny's Child, Knowles released her debut solo album, Dangerously in Love, in 2003, which spawned two number-one singles on the Billboard Hot 100—"Crazy in Love" and "Baby Boy"—and became one of the most successful albums of that year, earning her a then record-tying five Grammy Awards. Following the disbandment of Destiny's Child in 2005, Knowles released her second solo album, B'Day, in 2006, which spawned the top 10 singles "Déjà Vu", "Irreplaceable" and "Beautiful Liar". Her third solo album I Am... Sasha Fierce (2008), spawned the hit singles "If I Were a Boy", "Single Ladies (Put a Ring on It)", "Halo" and "Sweet Dreams". The album helped Knowles earn six Grammys in 2010, breaking the record for most Grammy Awards won by a female artist in one night. Knowles' fourth solo album, 4 (2011), became her fourth consecutive number one album on the Billboard 200 as a solo artist. This made her the third artist in history to have her first four studio albums debut atop the chart.
Apart from her work in music, Knowles has also ventured into acting and designing clothes and perfumes. She made her acting debut in the musical film Carmen: A Hip Hopera (2001), prior to appearing in major films, including Austin Powers in Goldmember (2002), Dreamgirls (2006), which earned her two Golden Globe nominations, Cadillac Records (2008) and Obsessed (2009). In 2005, Knowles and her mother introduced their family's fashion line, House of Deréon, and in 2010, she released her first perfume, Heat. She has endorsed brands including, L'Oréal, Pepsi, Tommy Hilfiger, Nintendo and Vizio. In 2010, Knowles was ranked first on Forbes list of the "100 Most Powerful and Influential Musicians in the World",[4] and second on its list of the "100 Most Powerful and Influential Celebrities in the World".[5] In 2012, she was named "World's Most Beautiful Woman" by People magazine.
Knowles' work has earned her numerous awards and accolades, including 16 Grammy Awards, 11 MTV Video Music Awards, three American Music Awards, a Billboard Millennium Award, and a star on the Hollywood Walk of Fame with Destiny's Child. In 2009, Billboard named her the Top Radio Songs Artist of the 2000s decade,[6] and ranked her as the 4th overall Artist of the Decade (and as the First Female Artist of that period).[7] The Recording Industry Association of America (RIAA), also recognized Knowles as the Top Certified Artist of the 2000s.[8][9] In the US, Knowles has sold over 11.2 million albums as of May 2010,[10] and more than 30.4 million digital singles as of January 2012.[11] She has sold 75 million records worldwide, making her one of the best-selling music artists of all time.[12] Knowles appeared on VH1's 2010 list of the "100 Greatest Artists of All Time",[13] and ranked third on their "100 Greatest Women in Music" list in 2012.[14] In April 2008, Knowles married American rapper Jay-Z, and gave birth to their first child, Blue Ivy Carter, in January 2012.</biography>"""
	
	nat1 = """<nationality></nationality>"""
	nat2 = """<nationality>Unknown</nationality>"""
	nat3 = """<nationality/>"""
	
	dateMid1 = """<time>Ongoing</time>
				<day>3</day>
				<month>16</month>
				<year>-1</year>"""
				
	dateMid1 = """<time>5:53AM</time>
				<day>16</day>
				<month>8</month>
				<year>1983</year>"""
				
	dateMid1 = """<time></time>
				<day>20</day>
				<month>20</month>
				<year>20</year>"""
	
	location1 = """<loc>
				<city>All cities</city>
				<region>All regions</region>
				<country>All countries</country>
			</loc>"""
			
	location2 = """<loc>
				<city>Meknes</city>
				<region>North Africa</region>
				<country>Morocco</country>
			</loc>"""
			
	location3 = """<loc>
				<city>Paris</city>
				<region></region>
				<country>France</country>
			</loc>"""
	
	impactOpen = """<impact>"""
	impactClose = """</impact>"""
  
	humanImpactOpen1 = """<human>
					<deaths>-1</deaths>
					<displaced>-1</displaced>
					<injured>-1</injured>
					<missing>-1</missing>"""
					
	humanImpactOpen2 = """<human>
					<deaths>-1</deaths>
					<displaced>-1</displaced>
					<injured>-1</injured>
					<missing>-1</missing>"""
	
	humanImpactOpen3 = """<human>
					<deaths>-1</deaths>
					<displaced>-1</displaced>
					<injured>-1</injured>
					<missing>-1</missing>"""
	humanImpactClose = """</human>"""
			
	ecoImpactOpen1 = """<economic>
					<amount>12039847</amount>
					<currency>RESEARCH burritos</currency>"""
	ecoImpactOpen1 = """<economic>
					<amount>23</amount>
					<currency></currency>"""
	ecoImpactOpen1 = """<economic>
					<amount>0</amount>
					<currency>Yen</currency>"""
	ecoimpactClose = """</economic>"""

	misc1 = """<misc>research</misc>"""
	misc2 = """<misc>All the single ladies (7x)

Now put your hands up
Up in the club, we just broke up
I’m doing my own little thing
you Decided to dip but now you wanna trip
Cuz another brother noticed me
I’m up on him, he up on me
dont pay him any attention
cuz i cried my tears, GAVE three good years
Ya can’t be mad at me

[Chorus]
Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Don’t be mad once you see that he want it
If you liked it then you shoulda put a ring on it

wo oh ooh oh oh ooh oh oh ooh oh oh oh x2


(Chorus)Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Don’t be mad once you see that he want it
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
Don’t be mad once you see that he want it
If you liked it then you shoulda put a ring on it

woo oh ooh oh oh ooh oh oh ooh oh oh oh 2x

Don’t treat me to the things of this world
I’m not that kind of girl
Your love is what I prefer, what I deserve
Is a man that makes me, then takes me
And delivers me to a destiny, to infinity and beyond
Pull me into your arms
Say I’m the one you WANT
If you don’t, you’ll be alone
And like a ghost I’ll be gone

All the single ladies (7x)
Now put your hands up
woo oh ooh oh oh ooh oh oh ooh
oh oh oh 2x

Cuz if you liked it then you should have put a ring on it
If you liked it then you shoulda put a ring on it
Don’t be mad once you see that he want it
If you liked it then you shoulda put a ring on it woo oh ooh 2x</misc>"""
	misc3 = """<misc/>"""
		
	refOpen = """<ref>"""
	refClose = """</ref>"""

	p_imageLink = """<primaryImage>
				<site>http://stopworldhunger.webs.com</site>
				<title>World Hunger</title>
				<url>http://stopworldhunger.webs.com/hunger.jpg</url>
				<description>Starving children</description> 
			</primaryImage>"""
			
	imageLink1 = """<image>
				<site>TestImage1</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description>
			</image>"""
			
	imageLink2 = """<image>
				<site>TestImage2</site>
				<title>World Hunger</title>
				<url>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</url>
				<description>Homeless Sign</description>
			</image>"""

	imageLink3 = """<image>
				<site>TestImage3</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
			</image>"""

	videoLink1 = """<video>
				<site>TestVideo1</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description>
			</video>"""
			
	videoLink2 = """<video>
				<site>TestVideo2</site>
				<title>World Health Organization</title>
				<url></url>
				<description>World Health Organization</description>
			</video>"""

	videoLink3 = """<video>
				<site>TestVideo3</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
			</video>"""

	socialLink1 = """<social>
				<site>TestSocial1</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description>
			</social>"""
			
	socialLink2 = """<social>
				<site>TestSocial2</site>
				<title>World Health Organization</title>
				<url></url>
				<description>World Health Organization</description>
			</social>"""

	socialLink3 = """<social>
				<site>TestSocial3</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
			</social>"""


	extLink1 = """<ext>
				<site>TestSite1</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description>
			</ext>"""
			
	extLink2 = """<ext>
				<site>TestSite2</site>
				<title>World Health Organization</title>
				<url></url>
				<description>World Health Organization</description>
			</ext>"""

	extLink3 = """<ext>
				<site>TestSite3</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
			</ext>"""


# Actual tests start here
# 
	def test_date_1(self):
		date = timeOpen + dateMid1 + misc + timeClose
		root = fromString(date).getroot()
		model = createDate(root)
		elem = buildDate(modelodel)
		rootString = toString(root)
		elemString = toString(elem)
		assert(rootString == dateString)
		
	def test_date_2(self):
		date = timeOpen + dateMid2 + misc2 + timeClose
		root = fromString(date).getroot()
		model = createDate(root)
		elem = buildDate(modelodel)
		rootString = toString(root)
		elemString = toString(elem)
		assert(rootString == dateString)
		
	def test_date_3(self):
		date = bdayOpen + dateMid3 + mis3 + bdayClose
		_test(createDate, buildDate, bparem = 'birthdate')
		
	def _test(self, ctest, btest, bparam = None, cparam = None):
		root = fromString(date).getroot()
		if cparam != None:
			model = ctest(root, cparam)
		else:
			model = ctest(root)
		elem = None
		if bparam != None:
			btest(elem, model, bparam)
		else :
			elem = btest(elem, model)
		rootString = toString(root)
		elemString = toString(elem[0])
		assert(rootString == elemString)
		
	def test_success(self):
		self.assertTrue(True)
		