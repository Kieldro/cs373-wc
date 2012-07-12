# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.ext.db import polymodel


# ---------------
# WorldCrisisPage
# ---------------

class WorldCrisisPage(polymodel.PolyModel):
	pass


# ---------------
# HumanImpact
# ---------------

class HumanImpact(db.Model):
	deaths = db.IntegerProperty(required=True)
	displaced = db.IntegerProperty(required=True)
	injured = db.IntegerProperty(required=True)
	missing = db.IntegerProperty(required=True)
	himpact_misc = db.TextProperty()


# ---------------
# EconomicImpact
# ---------------

class EconomicImpact(db.Model):
	amount = db.IntegerProperty(required=True)
	currency =  db.StringProperty()
	eimpact_misc = db.TextProperty()


# ---------------
# Date
# ---------------

class Date(db.Model):
	time = db.TextProperty()
	day = db.IntegerProperty(required=True)
	month = db.IntegerProperty(required=True)
	year = db.IntegerProperty(required=True)
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
	address = db.ReferenceProperty(FullAddress, required=True)


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
	url = db.LinkProperty(required=True)
	description = db.TextProperty(default=None)
	link_type = db.StringProperty(choices=["primaryImage", "image", "video", "social", "ext"], required=True)


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
	human_impact = db.ReferenceProperty(HumanImpact, required=True)
	eco_impact = db.ReferenceProperty(EconomicImpact, required=True)
	

# ---------------
# OrgInfo
# ---------------

class OrgInfo(db.Model):
	otype = db.StringProperty()
	history = db.TextProperty()
	contacts = db.ReferenceProperty(Contacts, required=True)
	location = db.ReferenceProperty(Location, required=True)


# ---------------
# CrisisInfo
# ---------------

class CrisisInfo(db.Model):
	history = db.TextProperty()
	helps = db.TextProperty()
	resources = db.TextProperty()
	ctype = db.StringProperty()
	location = db.ReferenceProperty(Location, required=True)
	impact = db.ReferenceProperty(Impact, required=True)
	date = db.ReferenceProperty(Date, required=True)


# ---------------
# PersonInfo
# ---------------

class PersonInfo(db.Model):
	ptype = db.StringProperty()
	nationality = db.StringProperty()
	biography = db.TextProperty()
	birthdate = db.ReferenceProperty(Date, required=True)
	

# ---------------
# Organization
# ---------------

class Organization(WorldCrisisPage):
	ID = db.StringProperty(required=True)
	name = db.StringProperty()
	misc = db.TextProperty()
	orginfo = db.ReferenceProperty(OrgInfo, required=True)
	reflink = db.ReferenceProperty(ReferenceLinks, required=True)
	crisisref = db.ListProperty(db.Key, required = True)
	personref = db.ListProperty(db.Key, required = True)
	

# ---------------
# Crisis
# ---------------

class Crisis(WorldCrisisPage):
	ID = db.StringProperty(required=True)
	name = db.StringProperty()
	misc = db.TextProperty()
	crisisinfo = db.ReferenceProperty(CrisisInfo, required=True)
	reflink = db.ReferenceProperty(ReferenceLinks, required=True)
	personref = db.ListProperty(db.Key, required = True)
	orgref = db.ListProperty(db.Key, required = True)
	

# ---------------
# Person
# ---------------

class Person(WorldCrisisPage):
	ID = db.StringProperty(required=True)
	name = db.StringProperty()
	misc = db.TextProperty()
	personinfo = db.ReferenceProperty(PersonInfo, required=True)
	reflink = db.ReferenceProperty(ReferenceLinks, required=True)
	crisisref = db.ListProperty(db.Key, required = True)
	orgref = db.ListProperty(db.Key, required = True)
