# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.ext.db import polymodel


# ---------------
# WorldCrisisPage
# ---------------

class WorldCrisisPage(polymodel.PolyModel):
	last_modified = db.DateTimeProperty(auto_now=True) #Remove if doesn't work!


# ---------------
# HumanImpact
# ---------------

class HumanImpact(db.Model):
	
	"""Define attributes of HumanImpact."""
	
	deaths = db.StringProperty(required=True)
	displaced = db.StringProperty(required=True)
	injured = db.StringProperty(required=True)
	missing = db.StringProperty(required=True)
	himpact_misc = db.TextProperty()


# ---------------
# EconomicImpact
# ---------------

class EconomicImpact(db.Model):
	amount = db.StringProperty(required=True)
	currency =  db.StringProperty()
	eimpact_misc = db.TextProperty()


# ---------------
# Date
# ---------------

class Date(db.Model):
	time = db.TextProperty()
	day = db.StringProperty(required=True)
	month = db.StringProperty(required=True)
	year = db.StringProperty(required=True)
	time_misc = db.TextProperty()


# ---------------
# Reference
# ---------------

class Reference(db.Model):
	ref = db.ReferenceProperty(WorldCrisisPage)
	sref = db.StringProperty()
	rType = db.StringProperty(choices=["crisis", "org", "person"])
	

# ---------------
# FullAddress
# ---------------

class FullAddress(db.Model):
	address = db.StringProperty(multiline=True)
	city = db.StringProperty()
	state= db.StringProperty()
	country = db.StringProperty()
	zipcode = db.StringProperty()


# ---------------
# Contacts
# ---------------

class Contacts(db.Model):
	phone = db.StringProperty()
	email = db.StringProperty()
	address = db.ReferenceProperty(FullAddress)


# ---------------
# Location
# ---------------

class Location(db.Model):
	city = db.StringProperty()
	region = db.StringProperty()
	country = db.StringProperty()


# ---------------
#  Link
# ---------------

class Link(db.Model):
	site = db.StringProperty()
	title = db.StringProperty()
	url = db.LinkProperty()
	description = db.TextProperty(default=None)
	link_type = db.StringProperty(choices=["primaryImage", "image", "video", "social", "ext"])


# ---------------
# ReferenceLinks
# ---------------

class ReferenceLinks(db.Model):
	primaryImage = db.ReferenceProperty(Link)
	image = db.ListProperty(db.Key, required = True)
	social = db.ListProperty(db.Key, required = True)
	video = db.ListProperty(db.Key, required = True)
	ext = db.ListProperty(db.Key, required = True)
	

# ---------------
# Impact
# ---------------

class Impact(db.Model):
	human_impact = db.ReferenceProperty(HumanImpact)
	eco_impact = db.ReferenceProperty(EconomicImpact)
	

# ---------------
# OrgInfo
# ---------------

class OrgInfo(db.Model):
	otype = db.StringProperty()
	history = db.TextProperty()
	contacts = db.ReferenceProperty(Contacts)
	location = db.ReferenceProperty(Location)


# ---------------
# CrisisInfo
# ---------------

class CrisisInfo(db.Model):
	history = db.TextProperty()
	helps = db.TextProperty()
	resources = db.TextProperty()
	ctype = db.StringProperty()
	location = db.ReferenceProperty(Location)
	impact = db.ReferenceProperty(Impact)
	date = db.ReferenceProperty(Date)


# ---------------
# PersonInfo
# ---------------

class PersonInfo(db.Model):
	ptype = db.StringProperty()
	nationality = db.StringProperty()
	biography = db.TextProperty()
	birthdate = db.ReferenceProperty(Date)
	

# ---------------
# Organization
# ---------------

class Organization(WorldCrisisPage):
	ID = db.StringProperty(required=True)
	name = db.StringProperty()
	misc = db.TextProperty()
	orginfo = db.ReferenceProperty(OrgInfo)
	reflink = db.ReferenceProperty(ReferenceLinks)
	crisisref = db.ListProperty(db.Key, required = True)
	personref = db.ListProperty(db.Key, required = True)
	

# ---------------
# Crisis
# ---------------

class Crisis(WorldCrisisPage):
	ID = db.StringProperty(required=True)
	name = db.StringProperty()
	misc = db.TextProperty()
	crisisinfo = db.ReferenceProperty(CrisisInfo)
	reflink = db.ReferenceProperty(ReferenceLinks)
	personref = db.ListProperty(db.Key, required = True)
	orgref = db.ListProperty(db.Key, required = True)
	

# ---------------
# Person
# ---------------

class Person(WorldCrisisPage):
	ID = db.StringProperty(required=True)
	name = db.StringProperty()
	misc = db.TextProperty()
	personinfo = db.ReferenceProperty(PersonInfo)
	reflink = db.ReferenceProperty(ReferenceLinks)
	crisisref = db.ListProperty(db.Key, required = True)
	orgref = db.ListProperty(db.Key, required = True)
