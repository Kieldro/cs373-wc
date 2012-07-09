# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

class Organization(db.Model):
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)
	
class Crisis(db.Model):
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)
	
class Person(db.Model):
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)

class OrgInfo(db.Model):
	otype = db.StringProperty(required=True)
	history = db.TextProperty(required=True)

class CrisisInfo(db.Model):
	history = db.TextProperty(required=True)
	helps = db.TextProperty(required=True)
	resources = db.TextProperty(required=True)
	ctype = db.StringProperty(required=True)

class PersonInfo(db.Model):
	ptype = db.StringProperty(required=True)
	nationality = db.StringProperty(required=True)
	biography = db.TextProperty(required=True)
	
class Contacts(db.Model):
	phone = db.PhoneNumberProperty(required=True)
	email = db.EmailProperty(required=True)

class FullAddress(db.Model):
	address = db.StringProperty(required=True, multiline=True)
	city = db.StringProperty(required=True)
	state= db.StringProperty(required=True)
	country = db.StringProperty(required=True)
	zipcode = db.StringProperty(required=True)
	
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
	ref = db.ReferenceProperty(required=True)
	rType = db.StringProperty(required=True,choices=["crisis", "organization", "person"])
