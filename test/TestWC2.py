import unittest
from Models import *
from Import import *
from xml.etree.ElementTree import Element, SubElement, parse
import StringIO
#from google.appengine.ext import db



class Success(unittest.TestCase):
	def test_success(self):
		self.assertTrue(True)
	
	# import tests
	
	def test_import(self):
		xmlstring = StringIO.StringIO(filestring)
		tree = parse(xmlstring)
		
		buildModels(tree)
		self.assertTrue(True)



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