# -*- coding: utf-8 -*-

from google.appengine.ext import *
#from google.appengine.api import users
'''
A model class describes a kind of entity.
'''



class Crisis(db.Model):
	# entity properties
	ID = db.IntegerProperty(required=True)
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True)
	location = db.StringProperty(required=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringListProperty(required=True)
	video = db.StringListProperty(required=True)
	network = db.StringListProperty(required=True)
	link = db.StringListProperty(required=True)
	date = db.StringProperty(required=True)
	startDate = db.DateProperty()
	endDate = db.DateProperty()
	additional = db.StringPeoperty()
	humanImpact = db.StringProperty(required=True)
	ecoImpact = db.StringProperty(required=True)
	resources = db.StringProperty(required=True)
	waysToHelpText = db.StringListProperty(required=True)
	waysToHelpLinks = db.StringListProperty(required=True)
	orgs = db.ListProperty(int)
	people = db.ListProperty(int)

class Organization(db.Model):
	ID = IntegerProperty(require=True)
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True)
	location = db.StringProperty(required=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringListProperty(required=True)
	video = db.StringListProperty(required=True)
	network = db.StringListProperty(required=True)
	link = db.StringListProperty(required=True)
	history = db.StringProperty(required=True)
	contactInfoText = db.StringListProperty(required=True)
	contactInfoLinks = db.StringListProperty(required=True)
	crises = db.ListProperty(int)
	people = db.ListProperty(int)

class Person(db.Model):
	ID = IntegerProperty(required=True)
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True)
	location = db.StringProperty(required=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringListProperty(required=True)
	video = db.StringListProperty(required=True)
	network = db.StringListProperty(required=True)
	link = db.StringListProperty(required=True)
	crises = db.ListProperty(int)
	orgs = db.ListProperty(int)
	

