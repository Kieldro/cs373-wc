import datetime
from google.appengine.ext import *
#from google.appengine.api import users
'''
A model class describes a kind of entity.
'''


class Crisis(db.Model):
	# entity properties
	id = IntegerProperty
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True)
	location = db.StringProperty(required=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.ListProperty(db.StringProperty(required=True) )
	video = db.ListProperty(db.StringProperty(required=True) )
	network = db.ListProperty(db.StringProperty(required=True) )
	link = db.ListProperty(db.StringProperty(required=True) )
	humanImpact = db.StringProperty(required=True)
	ecoImpact = db.StringProperty(required=True)
	resources = db.StringProperty(required=True)
	waysToHelp = db.StringProperty(required=True)
	date = db.DateProperty(required=True)
	time = db.TimeProperty()
	
	orgs = db.ListProperty(IntegerProperty)
	people = db.ListProperty(IntegerProperty)

class Organization(db.Model):
	id = IntegerProperty
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True)
	location = db.StringProperty(required=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringProperty(required=True)
	video = db.StringProperty(required=True)
	network = db.StringProperty(required=True)
	link = db.StringProperty(required=True)
	history = db.StringProperty(required=True)
	contactInfo = db.StringProperty(required=True)
	
	crisis = db.ListProperty(IntegerProperty)
	people = db.ListProperty(IntegerProperty)

class Person(db.Model):
	id = IntegerProperty
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True)
	location = db.StringProperty(required=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringProperty(required=True)
	video = db.StringProperty(required=True)
	network = db.StringProperty(required=True)
	link = db.StringProperty(required=True)
	
	orgs = db.ListProperty(IntegerProperty)
	people = db.ListProperty(IntegerProperty)
	


# create an entity
c = Crisis(name="Fukushima",
			role="nulcear",
			location="Japan",
			image="NA",
			video="NA",
			network="NA",
			link="NA",
			humanImpact="great",
			ecoImpact="vast",
			resources="food",
			waysToHelp="yes",
			date="Japan")

c.date = datetime.datetime.now().date()

# store in the datastore
c.put()

training_registration_list = [users.User("Alfred.Smith@example.com"),
								users.User("jharrison@example.com"),
								users.User("budnelson@example.com")]
# GQL query to the datastore
employees_trained = db.GqlQuery("SELECT * FROM Crisis WHERE kind IN :1",
								training_registration_list)

for d in employees_trained:
	d.new_hire_training_completed = 'BOOYAKASHA'
	db.put(d)