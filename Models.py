# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class WorldCrisisPage(polymodel.PolyModel):
	pass

class HumanImpact(db.Model):
	deaths = db.IntegerProperty()
	displaced = db.IntegerProperty()
	injured = db.IntegerProperty()
	missing = db.IntegerProperty()
	himpact_misc = db.TextProperty()

class EconomicImpact(db.Model):
	amount = db.IntegerProperty()
	currency =  db.StringProperty()
	eimpact_misc = db.TextProperty()

class Date(db.Model):
	time = db.TextProperty()
	day = db.IntegerProperty()
	month = db.IntegerProperty()
	year = db.IntegerProperty()
	time_misc = db.TextProperty()

class Reference(db.Model):
	ref = db.ReferenceProperty(WorldCrisisPage)
	sref = db.StringProperty()
	rType = db.StringProperty(choices=["crisis", "org", "person"])
	
class FullAddress(db.Model):
	address = db.StringProperty(multiline=True)
	city = db.StringProperty()
	state= db.StringProperty()
	country = db.StringProperty()
	zipcode = db.StringProperty()

class Contacts(db.Model):
	phone = db.StringProperty()
	email = db.StringProperty()
	address = db.ReferenceProperty(FullAddress, )

class Location(db.Model):
	city = db.StringProperty()
	region = db.StringProperty()
	country = db.StringProperty()

class Link(db.Model):
	site = db.StringProperty()
	title = db.StringProperty()
	url = db.LinkProperty()
	description = db.TextProperty(default="")
	link_type = db.StringProperty(choices=["primary_image", "image", "video", "social", "ext"], )

class ReferenceLinks(db.Model):
	primary_image = db.ReferenceProperty(Link)
	image = db.ListProperty(db.Key, )
	social = db.ListProperty(db.Key, )
	video = db.ListProperty(db.Key, )
	ext = db.ListProperty(db.Key, )
	
class Impact(db.Model):
	human_impact = db.ReferenceProperty(HumanImpact, )
	eco_impact = db.ReferenceProperty(EconomicImpact, )
	
class OrgInfo(db.Model):
	otype = db.StringProperty()
	history = db.TextProperty()
	contacts = db.ReferenceProperty(Contacts, )
	location = db.ReferenceProperty(Location, )

class CrisisInfo(db.Model):
	history = db.TextProperty()
	helps = db.TextProperty()
	resources = db.TextProperty()
	ctype = db.StringProperty()
	location = db.ReferenceProperty(Location, )
	impact = db.ReferenceProperty(Impact, )
	date = db.ReferenceProperty(Date, )

class PersonInfo(db.Model):
	ptype = db.StringProperty()
	nationality = db.StringProperty()
	biography = db.TextProperty()
	birthdate = db.ReferenceProperty(Date, )
	
class Organization(WorldCrisisPage):
	ID = db.StringProperty()
	name = db.StringProperty()
	misc = db.TextProperty()
	orginfo = db.ReferenceProperty(OrgInfo, )
	reflink = db.ReferenceProperty(ReferenceLinks, )
	crisisref = db.ListProperty(db.Key, )
	personref = db.ListProperty(db.Key, )
	
class Crisis(WorldCrisisPage):
	ID = db.StringProperty()
	name = db.StringProperty()
	misc = db.TextProperty()
	crisisinfo = db.ReferenceProperty(CrisisInfo, )
	reflink = db.ReferenceProperty(ReferenceLinks, )
	personref = db.ListProperty(db.Key, )
	orgref = db.ListProperty(db.Key, )
	
class Person(WorldCrisisPage):
	ID = db.StringProperty()
	name = db.StringProperty()
	misc = db.TextProperty()
	personinfo = db.ReferenceProperty(PersonInfo, )
	reflink = db.ReferenceProperty(ReferenceLinks, )
	crisisref = db.ListProperty(db.Key, )
	orgref = db.ListProperty(db.Key, )
