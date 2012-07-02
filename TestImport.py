import unittest
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
			<otherDiscription>
				Ongoing.
			</otherDiscription>
		</date>
		<humanImpact>1 in 7 people go to bed hungry. More than 4.5 million children under the age of 5 will die from hunger related causes this year. Death from malnutirition. 25,000 people die daily. 925 million hungry people in 2010.</humanImpact>
		<economicImpact>In the developing world, more than 1.4 billion people currently live below the international poverty line, earning less than $1.25 per day. Among this group of poor people, many have problems obtaining adequate, nutritious food for themselves and their families. As a result, 1.02 billion people in the developing world are undernourished. They consume less than the minimum amount of calories essential for sound health and growth. In 2006, more than 36 million died of hunger or diseases due to deficiencies in micronutrients.</economicImpact>
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
	<crisis id="3">
		<name>2011 Tōhoku Earthquake and Tsunami</name>
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
	
	def test_dictCommonElements_1(self) :
		tree = parse(crisis_1)
		d = dictCommonElements(tree)
		self.assert_(d['id'] == '1')
		self.assert_(d['name'] == 'World Hunger')
		self.assert_(d['kind'] == 'Global, Biological')
		self.assert_(d['location'] == 'All countries and cities')
		self.assert_(d['state'] == '')
		self.assert_(d['city'] == '')
		self.assert_(d['country'] == '')
		self.assert_(d['image'] == ['http://stopworldhunger.webs.com/hunger.jpg','http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=6jSBW0BOPqM', 'http://www.youtube.com/watch?v=0W2Ic5hV28w'])
		self.assert_(d['network'] == ['http://www.facebook.com/WorldHungerRelief', 'https://twitter.com/#!/FAOWFD'])
		self.assert_(d['link'] == ['http://www.who.int/en/', 'http://www.worldhunger.org/', 'http://www.freedomfromhunger.org/'])
		self.assert_(d['date'] == '''
				Ongoing.
			''')
		self.assert_(d['startDate'] == ''])
		self.assert_(d['endDate'] == '' )
		self.assert_(d['additional'] == '' )
		self.assert_(d['humanImpact'] == '1 in 7 people go to bed hungry. More than 4.5 million children under the age of 5 will die from hunger related causes this year. Death from malnutirition. 25,000 people die daily. 925 million hungry people in 2010.')
		self.assert_(d['ecoImpact'] == 'In the developing world, more than 1.4 billion people currently live below the international poverty line, earning less than $1.25 per day. Among this group of poor people, many have problems obtaining adequate, nutritious food for themselves and their families. As a result, 1.02 billion people in the developing world are undernourished. They consume less than the minimum amount of calories essential for sound health and growth. In 2006, more than 36 million died of hunger or diseases due to deficiencies in micronutrients.')
		self.assert_(d['resources'] == 'Money donations and food donations.')
		self.assert_(d['waysToHelpText'] ==['Learn and spread awareness about world hunger: ', " Donate to the cause. There are many organaztions available, here's one for example: ",  ])
		self.assert_(d['waysToHelpLinks'] == ['http://www.worldhunger.org/learn.htm', 'https://www.freedomfromhunger.org/help/online.php?origin=ggHP'])
		self.assert_(d['orgs'] == ['5'])
		self.assert_(d['people'] == ['9'])
	"""
	def test_dictCommonElements_2 (self) :
		tree = parse(crisis_2)
		d = dictCommonElements(tree)
		self.assert_(d['id'] == '2')
		self.assert_(d['name'] == 
		self.assert_(d['kind'] ==
		self.assert_(d['location'] ==
		self.assert_(d['state'] ==
		self.assert_(d['city'] ==
		self.assert_(d['country'] ==
		self.assert_(d['image'] ==
		self.assert_(d['video'] ==
		self.assert_(d['network'] ==
		self.assert_(d['link'] ==
		self.assert_(d['date'] ==
		self.assert_(d['startDate'] ==
		self.assert_(d['endDate'] ==
		self.assert_(d['additional'] ==
		self.assert_(d['humanImpact'] ==
		self.assert_(d['ecoImpact'] ==
		self.assert_(d['resources'] ==
		self.assert_(d['waysToHelpText'] ==
		self.assert_(d['waysToHelpLinks'] ==
		self.assert_(d['orgs'] ==
		self.assert_(d['people'] ==

	def test_dictCommonElements_2 (self) :
		self.assert_(d['id'] == '2')
		self.assert_(d['name'] == 
		self.assert_(d['kind'] == 'Nuclear meltdown and release of radioactive materials')
		self.assert_(d['location'] == 
		self.assert_(d['state'] ==
		self.assert_(d['city'] =='Okuma'
		self.assert_(d['country'] == 
		self.assert_(d['image'] ==
		self.assert_(d['video'] ==
		self.assert_(d['network'] ==
		self.assert_(d['link'] ==
		self.assert_(d['date'] ==
		self.assert_(d['startDate'] ==
		self.assert_(d['endDate'] ==
		self.assert_(d['additional'] ==
		self.assert_(d['humanImpact'] ==
		self.assert_(d['ecoImpact'] ==
		self.assert_(d['resources'] ==
		self.assert_(d['waysToHelpText'] ==
		self.assert_(d['waysToHelpLinks'] ==
		self.assert_(d['orgs'] ==
		self.assert_(d['people'] ==
		"""
