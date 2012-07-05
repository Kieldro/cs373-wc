import unittest
import StringIO
from Import import *
from Models import *

crisis_1 = '''
<crisis id="1">
		<name>World Hunger</name>
		<kind>Global, Biological</kind>
		<location>
			<unspecific>All countries and cities</unspecific>
		</location>
		<image>http://stopworldhunger.webs.com/hunger.jpg</image>
		<image>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</image>
		<video>http://www.youtube.com/watch?v=6jSBW0BOPqM</video>
		<video>http://www.youtube.com/watch?v=0W2Ic5hV28w</video>
		<network>http://www.facebook.com/WorldHungerRelief</network>
		<network>https://twitter.com/#!/FAOWFD</network>
		<link>http://www.who.int/en/</link>
		<link>http://www.worldhunger.org/</link>
		<link>http://www.freedomfromhunger.org/</link>
		<date>
			<otherDiscription>Ongoing.</otherDiscription>
		</date>
		<humanImpact>1 in 7 people go to bed hungry. More than 4.5 million children under the age of 5 will die from hunger related causes this year. Death from malnutirition. 25,000 people die daily. 925 million hungry people in 2010.</humanImpact>
		<economicImpact>In the developing world, more than 1.4 billion people live below the international poverty line, earning less than $1.25 per day. Among this group of poor people, many have problems obtaining adequate, nutritious food for themselves and their families. As a result, 1.02 billion people in the world are undernourished. They consume less than the minimum amount of calories for sound health and growth. In 2006, more than 36 million died of hunger or diseases due to deficiencies in micronutrients.</economicImpact>
		<resourcesNeeded>Money donations and food donations.</resourcesNeeded>
		<waysToHelp>Learn and spread awareness about world hunger: <link>http://www.worldhunger.org/learn.htm</link> Donate to the cause. There are many organaztions available, here's one for example: <link>https://www.freedomfromhunger.org/help/online.php?origin=ggHP</link></waysToHelp>
		<organizationId>5</organizationId>
		<personId>9</personId>
	</crisis>
	'''
crisis_2 = """<crisis id="2">
		<name>Fukushima Daiichi Nuclear Disaster</name>
		<kind>Nuclear meltdown and release of radioactive materials</kind>
		<location>
			<city>Okuma</city>
			<state>Fukushima</state>
			<country>Japan</country>
		</location>
		<image>http://upload.wikimedia.org/wikipedia/commons/d/d7/NIT_Combined_Flights_Ground_Measurements_30Mar_03Apr2011_results.jpg</image>
		<image>http://upload.wikimedia.org/wikipedia/commons/1/16/Fukushima_I_by_Digital_Globe_crop.jpg</image>
		<video>http://www.youtube.com/watch?v=PqQWpo_AsF8</video>
		<video>http://www.youtube.com/watch?v=44hv-4C2yXI</video>
		<video>http://www.youtube.com/watch?v=1rdWyrtX0cU</video>
		<network>http://www.facebook.com/pages/Japanese-reaction-to-Fukushima-Daiichi-nuclear-disaster/245496545477108</network>
		<link>http://fukushimaupdate.com/</link>
		<date>
			<start>2011-03-11</start>
		</date>
		<humanImpact>~573</humanImpact>
		<economicImpact>unknown</economicImpact>
		<resourcesNeeded>food</resourcesNeeded>
		<waysToHelp></waysToHelp>
		<organizationId>6</organizationId>
		<personId>10</personId>
	</crisis>
	"""
crisis_3 = """<crisis id="3">
		<name>2011 Tohoku Earthquake and Tsunami</name>
		<kind>Natural Disaster</kind>
		<location>
			<country>Japan</country>
		</location>
		<image>http://upload.wikimedia.org/wikipedia/commons/5/5a/Shindomap_2011-03-11_Tohoku_earthquake.png</image>
		<image>http://upload.wikimedia.org/wikipedia/commons/b/b9/Carried_train_in_Ishinomaki_Line_.JPG</image>
		<image>http://www.flickr.com/photos/ifrc/5542584560/</image>
		<image>http://www.flickr.com/photos/ifrc/5587996898/</image>
		<video>http://www.youtube.com/watch?v=6ZJ3-tbkhA4</video>
		<video>http://www.youtube.com/watch?v=oriVz1xE3wQ</video>
		<video>http://www.youtube.com/watch?v=tNgDKyznXkI</video>
		<network></network>
		<link>http://en.wikipedia.org/wiki/2011_Tohoku_earthquake_and_tsunami</link>
		<link>http://www.jrc.or.jp/eq-japan2011/index.html</link>
		<date>
			<start>2011-03-11</start>
			<additional>05:46 UTC</additional>
		</date>
		<humanImpact>15,861 deaths, 6,107 injured, 3,018 missing</humanImpact>
		<economicImpact>Reconstruction needed for over a million buildings
		Reactor Meltdown at the Fukushima Daiichi Nuclear Power Plant
		Costs of damage possibly exceeding 25 trillion Yen ($300 billion)</economicImpact>
		<resourcesNeeded>Food and medical supplies, temporary housing</resourcesNeeded>
		<waysToHelp>Monetary donations directly to the Japanese Red Cross, or through your national Red Cross/Red Crescent society</waysToHelp>
		<organizationId>7</organizationId>
		<personId>10</personId>
	</crisis>
	"""

class TestImport(unittest.TestCase) :

	def test_buildModels(self) :
		self.assert_(True == True)
		
# ------------------
# dictCommonElements
# ------------------
	def test_dictCommonElements_1(self) :
		xml_in = StringIO.StringIO(crisis_1)
		tree = parse(xml_in)
		d = dictCommonElements(tree.getroot())
		self.assert_(d['ID'] == '1')
		self.assert_(d['name'] == 'World Hunger')
		self.assert_(d['knd'] == 'Global, Biological')
		self.assert_(d['location'] == 'All countries and cities')
		self.assert_(d['image'] == ['http://stopworldhunger.webs.com/hunger.jpg','http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=6jSBW0BOPqM', 'http://www.youtube.com/watch?v=0W2Ic5hV28w'])
		self.assert_(d['network'] == ['http://www.facebook.com/WorldHungerRelief', 'https://twitter.com/#!/FAOWFD'])
		self.assert_(d['link'] == ['http://www.who.int/en/', 'http://www.worldhunger.org/', 'http://www.freedomfromhunger.org/'])

	def test_dictCommonElements_2 (self) :
		xml_in = StringIO.StringIO(crisis_2)
		tree = parse(xml_in)
		d = dictCommonElements(tree.getroot())
		self.assert_(d['ID'] == '2')
		self.assert_(d['name'] == 'Fukushima Daiichi Nuclear Disaster')
		self.assert_(d['knd'] == 'Nuclear meltdown and release of radioactive materials')
		self.assert_(d['location'] == '')
		self.assert_(d['state'] == 'Fukushima')
		self.assert_(d['city'] =='Okuma')
		self.assert_(d['country'] == 'Japan')
		self.assert_(d['image'] == ['http://upload.wikimedia.org/wikipedia/commons/d/d7/NIT_Combined_Flights_Ground_Measurements_30Mar_03Apr2011_results.jpg', 'http://upload.wikimedia.org/wikipedia/commons/1/16/Fukushima_I_by_Digital_Globe_crop.jpg'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=PqQWpo_AsF8', 'http://www.youtube.com/watch?v=44hv-4C2yXI', 'http://www.youtube.com/watch?v=1rdWyrtX0cU'])
		self.assert_(d['network'] == ['http://www.facebook.com/pages/Japanese-reaction-to-Fukushima-Daiichi-nuclear-disaster/245496545477108'])
		self.assert_(d['link'] == ['http://fukushimaupdate.com/'])
		
	def test_dictCommonElements_3 (self) :
		xml_in = StringIO.StringIO(crisis_3)
		tree = parse(xml_in)
		d = dictCommonElements(tree.getroot())
		self.assert_(d['ID'] == '3')
		self.assert_(d['name'] == '2011 Tohoku Earthquake and Tsunami')
		self.assert_(d['knd'] == 'Natural Disaster')
		self.assert_(d['location'] == '')
		self.assert_(d['state'] == '')
		self.assert_(d['city'] == '')
		self.assert_(d['country'] == 'Japan')
		self.assert_(d['image'] == ['http://upload.wikimedia.org/wikipedia/commons/5/5a/Shindomap_2011-03-11_Tohoku_earthquake.png', 'http://upload.wikimedia.org/wikipedia/commons/b/b9/Carried_train_in_Ishinomaki_Line_.JPG', 'http://www.flickr.com/photos/ifrc/5542584560/', 'http://www.flickr.com/photos/ifrc/5587996898/'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=6ZJ3-tbkhA4', 'http://www.youtube.com/watch?v=oriVz1xE3wQ', 'http://www.youtube.com/watch?v=tNgDKyznXkI'])
		self.assert_(d['network'] == ['None'])
		self.assert_(d['link'] == ['http://en.wikipedia.org/wiki/2011_Tohoku_earthquake_and_tsunami', 'http://www.jrc.or.jp/eq-japan2011/index.html'])
		
# ------------
# createCrisis
# ------------
	def test_createCrisis_1 (self) :
		xml_in = StringIO.StringIO(crisis_1)
		tree = parse(xml_in)
		c = createCrisis(tree.getroot())
		self.assert_(c.ID == '1')
		self.assert_(c.name == 'World Hunger')
		self.assert_(c.knd == 'Global, Biological')
		self.assert_(c.location == 'All countries and cities')
		self.assert_(c.image == ['http://stopworldhunger.webs.com/hunger.jpg','http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg'])
		self.assert_(c.video == ['http://www.youtube.com/watch?v=6jSBW0BOPqM', 'http://www.youtube.com/watch?v=0W2Ic5hV28w'])
		self.assert_(c.link == ['http://www.who.int/en/', 'http://www.worldhunger.org/', 'http://www.freedomfromhunger.org/'])
		self.assert_(c.date == 'Ongoing.')
		self.assert_(c.humanImpact == '1 in 7 people go to bed hungry. More than 4.5 million children under the age of 5 will die from hunger related causes this year. Death from malnutirition. 25,000 people die daily. 925 million hungry people in 2010.')
		self.assert_(c.ecoImpact == 'In the developing world, more than 1.4 billion people live below the international poverty line, earning less than $1.25 per day. Among this group of poor people, many have problems obtaining adequate, nutritious food for themselves and their families. As a result, 1.02 billion people in the world are undernourished. They consume less than the minimum amount of calories for sound health and growth. In 2006, more than 36 million died of hunger or diseases due to deficiencies in micronutrients.')
		self.assert_(c.resources == 'Money donations and food donations.')
		self.assert_(c.waysToHelpText == ['Learn and spread awareness about world hunger: ', " Donate to the cause. There are many organaztions available, here's one for example: ", 'None'])
		self.assert_(c.waysToHelpLinks == ['http://www.worldhunger.org/learn.htm', 'https://www.freedomfromhunger.org/help/online.php?origin=ggHP'])
		self.assert_(c.orgs == ['5'])
		self.assert_(c.people == ['9'])
		
	def test_createCrisis_2 (self) :
		xml_in = StringIO.StringIO(crisis_2)
		tree = parse(xml_in)
		c = createCrisis(tree.getroot())
		self.assert_(c.ID == '2')
		self.assert_(c.name == 'Fukushima Daiichi Nuclear Disaster')
		self.assert_(c.knd == 'Nuclear meltdown and release of radioactive materials')
		self.assert_(c.location == '')
		self.assert_(c.city == 'Okuma')
		self.assert_(c.state == 'Fukushima')
		self.assert_(c.country == 'Japan')
		self.assert_(c.image == ['http://upload.wikimedia.org/wikipedia/commons/d/d7/NIT_Combined_Flights_Ground_Measurements_30Mar_03Apr2011_results.jpg', 'http://upload.wikimedia.org/wikipedia/commons/1/16/Fukushima_I_by_Digital_Globe_crop.jpg'])
		self.assert_(c.video == ['http://www.youtube.com/watch?v=PqQWpo_AsF8', 'http://www.youtube.com/watch?v=44hv-4C2yXI', 'http://www.youtube.com/watch?v=1rdWyrtX0cU'])
		self.assert_(c.date == '')
		self.assert_(c.startDate == '2011-03-11')
		self.assert_(c.endDate == '')
		self.assert_(c.additional == '')
		self.assert_(c.humanImpact == '~573')
		self.assert_(c.ecoImpact == 'unknown')
		self.assert_(c.resources == 'food')
		self.assert_(c.waysToHelpText == [''] )
		self.assert_(c.waysToHelpLinks == [] )
		self.assert_(c.orgs == ['6'])
		self.assert_(c.people == ['10'])
		
	def test_createCrisis_3 (self) :
		xml_in = StringIO.StringIO(crisis_3)
		tree = parse(xml_in)
		c = createCrisis(tree.getroot())
		self.assert_(c.ID == '3')
		self.assert_(c.name == '2011 Tohoku Earthquake and Tsunami')
		self.assert_(c.knd == 'Natural Disaster')
		self.assert_(c.location == '')
		self.assert_(c.city == '')
		self.assert_(c.state == '')
		self.assert_(c.country == 'Japan')
		self.assert_(c.image == ['http://upload.wikimedia.org/wikipedia/commons/5/5a/Shindomap_2011-03-11_Tohoku_earthquake.png', 'http://upload.wikimedia.org/wikipedia/commons/b/b9/Carried_train_in_Ishinomaki_Line_.JPG', 'http://www.flickr.com/photos/ifrc/5542584560/', 'http://www.flickr.com/photos/ifrc/5587996898/'])
		self.assert_(c.video == ['http://www.youtube.com/watch?v=6ZJ3-tbkhA4', 'http://www.youtube.com/watch?v=oriVz1xE3wQ', 'http://www.youtube.com/watch?v=tNgDKyznXkI'])
		self.assert_(c.date == '')
		self.assert_(c.startDate == '2011-03-11')
		self.assert_(c.endDate == '')
		self.assert_(c.additional == '05:46 UTC')
		self.assert_(c.humanImpact == '15,861 deaths, 6,107 injured, 3,018 missing')
		self.assert_(c.ecoImpact == """Reconstruction needed for over a million buildings
		Reactor Meltdown at the Fukushima Daiichi Nuclear Power Plant
		Costs of damage possibly exceeding 25 trillion Yen ($300 billion)""")
		self.assert_(c.resources == 'Food and medical supplies, temporary housing')
		self.assert_(c.waysToHelpText == ['Monetary donations directly to the Japanese Red Cross, or through your national Red Cross/Red Crescent society'])
		self.assert_(c.waysToHelpLinks == [])
		self.assert_(c.orgs == ['7'])
		self.assert_(c.people == ['10'])

