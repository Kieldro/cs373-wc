import unittest
from test import test_support
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


class TestImport(unittest.TestCase) :

	def test_buildModels(self) :
		self.assert_(True == True)
	
	def test_dictCommonElements(self) :
		tree = parse(crisis_1)
		d = dictCommonElements(tree)
		self.assert_(d['id'] == '1')
		
