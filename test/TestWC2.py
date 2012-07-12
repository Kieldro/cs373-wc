# -*- coding: utf-8 -*-
import unittest
from Models import *
from Import import *
from Export import *
from xml.etree.ElementTree import Element, SubElement, parse
import StringIO
#from google.appengine.ext import db



class Success(unittest.TestCase):

  
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
	misc2 = """<misc>single Ladies

All the single ladies (7x)

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

	crisisRef1 = """<crisis idref="CA"/>"""
	crisisRef2 = """<crisis idref="CB"/>"""
	crisisRef3 = """<crisis idref="CC"/>"""
	orgRef1 = """<organization idref="OA"/>"""
	orgRef2 = """<organization idref="OB"/>"""
	orgRef3 = """<organization idref="OC"/>"""
	personRef1 = """<person idref="PA"/>"""
	personRef2 = """<person idref="PB"/>"""
	personRef3 = """<person idref="PC"/>"""
		
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


	filestring = '''<?xml version="1.0" ?> 
<worldCrises>
	<crisis id="worldhunger">
		<name>World Hunger</name>
		<info>
			<history>RESEARCH ON WORLD HUNGER HISTORY</history>
			<help>Learn</help>
			<resources>Money donations and food donations.</resources>
			<type>Global, Biological</type>
			<time>
				<time>Ongoing</time>
				<day>-1</day>
				<month>-1</month>
				<year>-1</year>
				<misc>Ongoing</misc>
			</time>
			<loc>
				<city>All cities</city>
				<region>All regions</region>
				<country>All countries</country>
			</loc>
			<impact>
				<human>
					<deaths>-1</deaths>
					<displaced>-1</displaced>
					<injured>-1</injured>
					<missing>-1</missing>
					<misc>1 in 7 people go to bed hungry.</misc>
				</human>
				<economic>
					<amount>-1</amount>
					<currency>RESEARCH burritos</currency>
					<misc>In the developing world</misc>
				</economic>
			</impact>
		</info>
		<ref>
			<primaryImage>
				<site>http://stopworldhunger.webs.com</site>
				<title>World Hunger</title>
				<url>http://stopworldhunger.webs.com/hunger.jpg</url>
				<description>Starving children</description> 
			</primaryImage>
			<image>
				<site>http://viroquafood.coop</site>
				<title>Stop World Hunger</title>
				<url>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</url>
				<description>Homeless Sign</description> 
			</image>
			<video>
				<site>http://www.youtube.com</site>
				<title>World hunger - A Billion for a Billion </title>
				<url>http://www.youtube.com/watch?v=6jSBW0BOPqM</url>
				<description>World hunger - A Billion for a Billion </description> <!-- OPTIONAL -->
			</video>
			<video>
				<site>http://www.youtube.com</site>
				<title>World Hunger PSA </title>
				<url>http://www.youtube.com/watch?v=0W2Ic5hV28w</url>
				<description>World Hunger PSA</description>
			</video>
			<social>
				<site>http://www.facebook.com</site>
				<title>World Hunger Relief</title>
				<url>http://www.facebook.com/WorldHungerRelief</url>
				<description>World Hunger Relief</description> 
			</social>
			<social>
				<site>https://twitter.com</site>
				<title>World Food Day </title>
				<url>https://twitter.com/#!/FAOWFD</url>
				<description>World Food Day</description> 
			</social>
			<ext>
				<site>http://www.who.int</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description>
			</ext>
			<ext>
				<site>http://www.worldhunger.org/</site>
				<title>http://www.worldhunger.org/</title>
				<url>http://www.worldhunger.org/</url>
				<description>http://www.worldhunger.org/</description> 
			</ext>
			<ext>
				<site>http://www.freedomfromhunger.org/</site>
				<title>http://www.freedomfromhunger.org/</title>
				<url>http://www.freedomfromhunger.org/</url>
				<description>http://www.freedomfromhunger.org/</description> 
			</ext>
		</ref>
		<misc>RESEARCH</misc>
		<org idref="WHO"/>
		<person idref="Chan"/>
	</crisis>
	
	<organization id="WHO">
		<name>World Health Organization</name>
		<info>
			<type>Global, Biological</type>
			<history>RESEARCH ON WORLD HUNGER HISTORY</history>
			<contact>
				<phone></phone>
				<email></email>
				<mail>
					<address></address>
					<city></city>
					<state></state>
					<country></country>
					<zip></zip>
				</mail>
			</contact>
			<loc>
				<city>All cities</city>
				<region>All regions</region>
				<country>All countries</country>
			</loc>
		</info>
		<ref>
			<primaryImage>
				<site>http://stopworldhunger.webs.com</site>
				<title>World Hunger</title>
				<url>http://stopworldhunger.webs.com/hunger.jpg</url>
				<description>Starving children</description> 
			</primaryImage>
			<image>
				<site>http://viroquafood.coop</site>
				<title>Stop World Hunger</title>
				<url>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</url>
				<description>Homeless Sign</description> 
			</image>
			<video>
				<site>http://www.youtube.com</site>
				<title>World hunger - A Billion for a Billion </title>
				<url>http://www.youtube.com/watch?v=6jSBW0BOPqM</url>
				<description>World hunger - A Billion for a Billion </description> <!-- OPTIONAL -->
			</video>
			<video>
				<site>http://www.youtube.com</site>
				<title>World Hunger PSA </title>
				<url>http://www.youtube.com/watch?v=0W2Ic5hV28w</url>
				<description>World Hunger PSA</description> 
			</video>
			<social>
				<site>http://www.facebook.com</site>
				<title>World Hunger Relief</title>
				<url>http://www.facebook.com/WorldHungerRelief</url>
				<description>World Hunger Relief</description> 
			</social>
			<social>
				<site>https://twitter.com</site>
				<title>World Food Day </title>
				<url>https://twitter.com/#!/FAOWFD</url>
				<description>World Food Day</description> 
			</social>
			<ext>
				<site>http://www.who.int</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description> 
			</ext>
			<ext>
				<site>http://www.worldhunger.org/</site>
				<title>http://www.worldhunger.org/</title>
				<url>http://www.worldhunger.org/</url>
				<description>http://www.worldhunger.org/</description> 
			</ext>
			<ext>
				<site>http://www.freedomfromhunger.org/</site>
				<title>http://www.freedomfromhunger.org/</title>
				<url>http://www.freedomfromhunger.org/</url>
				<description>http://www.freedomfromhunger.org/</description> 
			</ext>
		</ref>
		<misc>RESEARCH</misc>
		<crisis idref="WHO"/>
		<person idref="Chan"/>
	</organization>
	
	<person id="Chan">
		<name>World Health Organization</name>
		<info>
			<type>Global, Biological</type>
			<birthdate>
				<time>Ongoing</time>
				<day>-1</day>
				<month>-1</month>
				<year>-1</year>
				<misc>Ongoing</misc>
			</birthdate>
			<nationality></nationality>
			<biography></biography>	
			
		</info>
		<ref>
			<primaryImage>
				<site>http://stopworldhunger.webs.com</site>
				<title>World Hunger</title>
				<url>http://stopworldhunger.webs.com/hunger.jpg</url>
				<description>Starving children</description> <!-- OPTIONAL -->
			</primaryImage>
			<image>
				<site>http://viroquafood.coop</site>
				<title>Stop World Hunger</title>
				<url>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</url>
				<description>Homeless Sign</description> <!-- OPTIONAL -->
			</image>
			<video>
				<site>http://www.youtube.com</site>
				<title>World hunger - A Billion for a Billion </title>
				<url>http://www.youtube.com/watch?v=6jSBW0BOPqM</url>
				<description>World hunger - A Billion for a Billion </description> <!-- OPTIONAL -->
			</video>
			<video>
				<site>http://www.youtube.com</site>
				<title>World Hunger PSA </title>
				<url>http://www.youtube.com/watch?v=0W2Ic5hV28w</url>
				<description>World Hunger PSA</description> <!-- OPTIONAL -->
			</video>
			<social>
				<site>http://www.facebook.com</site>
				<title>World Hunger Relief</title>
				<url>http://www.facebook.com/WorldHungerRelief</url>
				<description>World Hunger Relief</description> <!-- OPTIONAL -->
			</social>
			<social>
				<site>https://twitter.com</site>
				<title>World Food Day </title>
				<url>https://twitter.com/#!/FAOWFD</url>
				<description>World Food Day</description> <!-- OPTIONAL -->
			</social>
			<ext>
				<site>http://www.who.int</site>
				<title>World Health Organization</title>
				<url>http://www.who.int/en</url>
				<description>World Health Organization</description> <!-- OPTIONAL -->
			</ext>
			<ext>
				<site>http://www.worldhunger.org/</site>
				<title>http://www.worldhunger.org/</title>
				<url>http://www.worldhunger.org/</url>
				<description>http://www.worldhunger.org/</description> <!-- OPTIONAL -->
			</ext>
			<ext>
				<site>http://www.freedomfromhunger.org/</site>
				<title>http://www.freedomfromhunger.org/</title>
				<url>http://www.freedomfromhunger.org/</url>
				<description>http://www.freedomfromhunger.org/</description> <!-- OPTIONAL -->
			</ext>
		</ref>
		<misc>RESEARCH</misc>
		<crisis idref="worldhunger"/>
		<org idref="WHO"/>
	</person>
</worldCrises>'''

	def test_success(self):
		self.assertTrue(True)
	
	# import tests
	
	def test_import(self):
		xmlstring = StringIO.StringIO(filestring)
		tree = parse(xmlstring)
		
		buildModels(tree)
		self.assertTrue(True)