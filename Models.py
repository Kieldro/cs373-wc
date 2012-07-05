# -*- coding: utf-8 -*-

from google.appengine.ext import db
#from google.appengine.api import users
'''
A model class describes a kind of entity.
'''



class Crisis(db.Model):
	# entity properties
	ID = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	knd = db.StringProperty(required=True)
	location = db.StringProperty(multiline=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringListProperty(required=True)
	video = db.StringListProperty(required=True)
	network = db.StringListProperty(required=True)
	link = db.StringListProperty(required=True)
	date = db.StringProperty(required=False, multiline=True)
	startDate = db.StringProperty()
	endDate = db.StringProperty()
	additional = db.StringProperty()
	humanImpact = db.StringProperty(required=True, multiline=True)
	ecoImpact = db.StringProperty(required=True, multiline=True)
	resources = db.StringProperty(required=True, multiline=True)
	waysToHelpText = db.StringListProperty(required=True)
	waysToHelpLinks = db.StringListProperty(required=True)
	orgs = db.StringListProperty()
	people = db.StringListProperty()

class Organization(db.Model):
	ID = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	knd = db.StringProperty(required=True)
	location = db.StringProperty(multiline=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringListProperty(required=True)
	video = db.StringListProperty(required=True)
	network = db.StringListProperty(required=True)
	link = db.StringListProperty(required=True)
	history = db.StringProperty(required=True, multiline=True)
	contactInfoText = db.StringListProperty(required=True)
	contactInfoLinks = db.StringListProperty(required=True)
	crises = db.StringListProperty()
	people = db.StringListProperty()

class Person(db.Model):
	ID = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	knd = db.StringProperty(required=True)
	location = db.StringProperty(multiline=True)
	state = db.StringProperty()
	city = db.StringProperty()
	country = db.StringProperty()
	image = db.StringListProperty(required=True)
	video = db.StringListProperty(required=True)
	network = db.StringListProperty(required=True)
	link = db.StringListProperty(required=True)
	crises = db.StringListProperty()
	orgs = db.StringListProperty()
	

