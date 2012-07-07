# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

# The data for each type of external link
class PrimaryImageLink(db.Model):
        pi_site = db.StringProperty(required=True)
	pi_title = db.StringProperty(required=True)
	pi_url = db.LinkProperty(required=True)
	pi_description = db.TextProperty()

class ImageData(PrimaryImageLink):
        image_sites = db.StringListProperty(required=True)
	image_titles = db.StringListProperty(required=True)
 	image_urls = db.ListProperty(db.Link, required=True)
	image_descriptions = db.ListProperty(db.Text, required=True)

class VideoData(ImageData):
        video_sites = db.StringListProperty(required=True)
	video_titles = db.StringListProperty(required=True)
 	video_urls = db.ListProperty(db.Link, required=True)
	video_descriptions = db.ListProperty(db.Text, required=True)

class SocialData(VideoData):
        social_sites = db.StringListProperty(required=True)
	social_titles = db.StringListProperty(required=True)
 	social_urls = db.ListProperty(db.Link, required=True)
	social_descriptions = db.ListProperty(db.Text, required=True)

class ExternalData(SocialData):
        ext_sites = db.StringListProperty(required=True)
	ext_titles = db.StringListProperty(required=True)
 	ext_urls = db.ListProperty(db.Link, required=True)
	ext_descriptions = db.ListProperty(db.Text, required=True)

# Common Fields to all models
class CommonInfo(ExternalData):
	ID = db.StringProperty(required=True)
	name = db.StringProperty(required=True)
	misc = db.TextProperty(required=True)

# References to pages to other types
class CrisisRefs(db.Model):
	crises = db.ListProperty(item_type=db.Key, required=True)

class OrgRefs(db.Model):
	orgs = db.ListProperty(item_type=db.Key, required=True)

class PersonRefs(db.Model):
	people = db.ListProperty(item_type=db.Key, required=True)

# Breakdowns of the crisis data
class CrisisLocAndTime(CommonInfo):
	time = db.TextProperty(required=True)
	day = db.IntegerProperty(required=True)
	month = db.IntegerProperty(required=True)
	year = db.IntegerProperty(required=True)
	time_misc = db.TextProperty(required=True)
	city = db.StringProperty(required=True)
	region = db.StringProperty(required=True)
	country = db.StringProperty(required=True)

class CrisisImpact(CrisisLocAndTime):
	deaths = db.IntegerProperty(required=True)
	displaced = db.IntegerProperty(required=True)
	injured = db.IntegerProperty(required=True)
	missing = db.IntegerProperty(required=True)
	himpact_misc = db.TextProperty(required=True)
	amount = db.IntegerProperty(required=True)
	currency =  db.StringProperty(required=True)
	eimpact_misc = db.TextProperty(required=True)

# The main model declerations
class Crisis(OrgRefs, PersonRefs, CrisisImpact):
	history = db.TextProperty(required=True)
	helps = db.TextProperty(required=True)
	resources = db.TextProperty(required=True)
	ctype = db.StringProperty(required=True)

class Organization(CommonInfo, CrisisRefs, PersonRefs):
	otype = db.StringProperty(required=True)
	history = db.TextProperty(required=True)
	phone = db.PhoneNumberProperty(required=True)
	email = db.EmailProperty(required=True)
	address = db.StringProperty(required=True, multiline=True)
	city = db.StringProperty(required=True)
	state= db.StringProperty(required=True)
	country = db.StringProperty(required=True)	
	zipcode = db.StringProperty(required=True)

class Person(CommonInfo, CrisisRefs, OrgRefs):
	ptype = db.StringProperty(required=True)
	birthtime = db.TextProperty(required=True)
	birthday = db.IntegerProperty(required=True)
	birthmonth = db.IntegerProperty(required=True)
	birthyear = db.IntegerProperty(required=True)
	birthtime_misc = db.TextProperty(required=True)
	nationality = db.StringProperty(required=True)
	biography = db.TextProperty(required=True)

