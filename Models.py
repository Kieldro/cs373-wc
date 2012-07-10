# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class WorldCrisisPage(polymodel.PolyModel):
	pass

class HumanImpact(db.Model):
	deaths = db.IntegerProperty(required=True)
	displaced = db.IntegerProperty(required=True)
	injured = db.IntegerProperty(required=True)
	missing = db.IntegerProperty(required=True)
	himpact_misc = db.TextProperty(required=True)

class EconomicImpact(db.Model):
	amount = db.IntegerProperty(required=True)
	currency =  db.StringProperty(required=True)
	eimpact_misc = db.TextProperty(required=True)

class Date(db.Model):
	time = db.TextProperty(required=True)
	day = db.IntegerProperty(required=True)
	month = db.IntegerProperty(required=True)
	year = db.IntegerProperty(required=True)
	time_misc = db.TextProperty(required=True)

class Reference(db.Model):
	ref = db.ReferenceProperty(WorldCrisisPage)
	sref = db.StringProperty(required=True)
	rType = db.StringProperty(required=True,choices=["crisis", "org", "person"])
	
class FullAddress(db.Model):
	address = db.StringProperty(required=True, multiline=True)
	city = db.StringProperty(required=True)
	state= db.StringProperty(required=True)
	country = db.StringProperty(required=True)
	zipcode = db.StringProperty(required=True)

class Contacts(db.Model):
	phone = db.PhoneNumberProperty(required=True)
	email = db.EmailProperty(required=True)
	address = db.ReferenceProperty(FullAddress, required=True)

class Location(db.Model):
	city = db.StringProperty(required=True)
	region = db.StringProperty(required=True)
	country = db.StringProperty(required=True)

class Link(db.Model):
	site = db.StringProperty(required=True)
	title = db.StringProperty(required=True)
	url = db.LinkProperty(required=True)
	description = db.TextProperty(required=True, default="")
	link_type = db.StringProperty(choices=["primary_image", "image", "video", "social", "ext"], required=True)


class ReferenceLinks(db.Model):
	primary_image = db.ReferenceProperty(Link, collection_name="pimage")
	image = db.ReferenceProperty(Link, collection_name="image")
	social = db.ReferenceProperty(Link, collection_name="social")
	video = db.ReferenceProperty(Link, collection_name="video")
	ext = db.ReferenceProperty(Link, collection_name="ext")
	
class Impact(db.Model):
	human_impact = db.ReferenceProperty(HumanImpact, required=True)
	eco_impact = db.ReferenceProperty(EconomicImpact, required=True)
	
class OrgInfo(db.Model):
	otype = db.StringProperty(required=True)
	history = db.TextProperty(required=True)
	contacts = db.ReferenceProperty(Contacts, required=True)
	location = db.ReferenceProperty(Location, required=True)

class CrisisInfo(db.Model):
	history = db.TextProperty(required=True)
	helps = db.TextProperty(required=True)
	resources = db.TextProperty(required=True)
	ctype = db.StringProperty(required=True)
	location = db.ReferenceProperty(Location, required=True)
	impact = db.ReferenceProperty(Impact, required=True)
	date = db.ReferenceProperty(Date, required=True)

class PersonInfo(db.Model):
	ptype = db.StringProperty(required=True)
	nationality = db.StringProperty(required=True)
	biography = db.TextProperty(required=True)
	birthdate = db.ReferenceProperty(Date, required=True)
	
class Organization(WorldCrisisPage):
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)
	orginfo = db.ReferenceProperty(OrgInfo, required=True)
	reflink = db.ReferenceProperty(ReferenceLinks, required=True)
	crisisref = db.ReferenceProperty(Reference, collection_name="org_criref", required = True)
	personref = db.ReferenceProperty(Reference, collection_name="org_perref", required = True)
	
class Crisis(WorldCrisisPage):
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)
	crisisinfo = db.ReferenceProperty(CrisisInfo, required=True)
	reflink = db.ReferenceProperty(ReferenceLinks, required=True)
	personref = db.ReferenceProperty(Reference, collection_name="cri_perref", required = True)
	orgref = db.ReferenceProperty(Reference, collection_name="cri_orgref", required = True)
	
class Person(WorldCrisisPage):
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)
	personinfo = db.ReferenceProperty(PersonInfo, required=True)
	reflink = db.ReferenceProperty(ReferenceLinks, required=True)
	crisisref = db.ReferenceProperty(Reference, collection_name="per_criref", required = True)
	orgref = db.ReferenceProperty(Reference, collection_name="per_orgref", required = True)
