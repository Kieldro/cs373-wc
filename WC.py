from google.appengine.ext import webapp
from google.appengine.ext.db import delete, Query
from Models import *
from google.appengine.ext.webapp.util import run_wsgi_app
from RunExport import runExport
from RunImport import runImport, getSchemaString
from minixsv import pyxsval
from genxmlif import GenXmlIfError
from google.appengine.ext.webapp import template
from random import shuffle
from SearchFeature import createIndex, searchForString, deleteDocs

import os
import StringIO

def deleteModels() :
	"""
	This function deletes all entries in the datastore.
	"""
	delete(HumanImpact.all(keys_only=True))
	delete(EconomicImpact.all(keys_only=True))
	delete(Date.all(keys_only=True))
	delete(Reference.all(keys_only=True))
	delete(FullAddress.all(keys_only=True))
	delete(Contacts.all(keys_only=True))
	delete(Location.all(keys_only=True))
	delete(Link.all(keys_only=True))
	delete(ReferenceLinks.all(keys_only=True))
	delete(Impact.all(keys_only=True))
	delete(OrgInfo.all(keys_only=True))
	delete(CrisisInfo.all(keys_only=True))
	delete(PersonInfo.all(keys_only=True))
	delete(Organization.all(keys_only=True))
	delete(Crisis.all(keys_only=True))
	delete(Person.all(keys_only=True))

class BaseHandler(webapp.RequestHandler):
	def render_template(self, filename, **template_args):
		"""
		Class that handles the handling of pages. Wherever 'webapp.RequestHandler' is used, use 'BaseHandler' instead.
		self is self-explanitory.
		filename is the filename of the Django template to render.
		**template_args is all the values to pass to the template.
		"""
		path = os.path.join(os.path.dirname(__file__), 'templates', filename)
		
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage ")
		page_names = ', '.join(['"%s"'%x.name for x in q])
		
		# Queries for the four most recently updated entries for each type
		c_list=[]
		for crisis in Crisis.gql("ORDER BY last_modified DESC LIMIT 4"):
			c_list.append(crisis)
		
		o_list=[]
		for org in Organization.gql("ORDER BY last_modified DESC LIMIT 4"):
			o_list.append(org)
			
		p_list=[]
		for person in Person.gql("ORDER BY last_modified DESC LIMIT 4"):
			p_list.append(person)
		
		template_args['entries'] = page_names
		template_args['cNav'] = c_list
		template_args['oNav'] = o_list		
		template_args['pNav'] = p_list
		self.response.out.write(template.render(path, template_args))
	
class MainPage(BaseHandler):
	"""
	Class that handles the index page.
	"""
	def get(self):
		toplist = []
		for crisis in Crisis.gql("ORDER BY last_modified DESC LIMIT 4"):
			toplist.append(crisis)
		for org in Organization.gql("ORDER BY last_modified DESC LIMIT 4"):
			toplist.append(org)
		for person in Person.gql("ORDER BY last_modified DESC LIMIT 4"):
			toplist.append(person)
		shuffle(toplist)
		self.render_template('index.html', topimgs=toplist[0:4])
		
class AboutPage(BaseHandler):
	"""
	Class that handles the About Page.
	"""
	def get(self):
		self.render_template('about.html')
		
class CrisesPage(BaseHandler):
	"""
	Class that handles the Crisis listing page.
	"""
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE crisisinfo != NULL")
		results = q.fetch(5)
		self.render_template('crises.html', crises_list=results)
		
class PeoplePage(BaseHandler):
	"""
	Class that handles the People listing page.
	"""
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE personinfo != NULL")
		results = q.fetch(5)
		self.render_template('people.html', people_list=results)
		
class OrganizationsPage(BaseHandler):
	"""
	Class that handles the Organizations listing page.
	"""
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE orginfo != NULL")
		results = q.fetch(5)
		self.render_template('organizations.html', orgs_list=results)

class ImportPage(BaseHandler):
	"""
	Class that handles the Import page. 
	On GET, the page is generated.
	On POST, the xml given by the user is validated. If it passes, it is added to the models.
	"""
	def get(self):
		self.render_template('import.html')

	def post(self):
		xmlfile = self.request.get("data")
		xmlschema = getSchemaString()
		try:
			# call validator
			elementTreeWrapper = pyxsval.parseAndValidateXmlInputString (xmlfile, xsdText=str(xmlschema), verbose=0)
			#elementtree object after validation
			elemTree = elementTreeWrapper.getTree()
		except pyxsval.XsvalError, errstr:
			s= "Validation aborted! XML does not conform to the schema."
			self.render_template('import.html', status='error', message=s)
			return
		except GenXmlIfError, errstr:
			s = "Parsing aborted! Could not parse the XML. Check the syntax of your file."
			self.render_template('import.html', status='error', message=s)
			return

		merge = self.request.get("mergebox")
		if (merge != "merge") :
			deleteModels()

		try:
			runImport(xmlfile)
		except:
			self.render_template('import.html', status='error')
			return

		try:
			deleteDocs()
		except Exception, e:
			self.render_template('import.html', status='error', message="DELETE DOCS "+e.args)
			
		try:
			createIndex()
			self.render_template('import.html', status='success', message="Everything's OKAY!")
		except Exception, e:
			self.render_template('import.html', status='error', message=e.args)
		
class ExportPage(BaseHandler):
	"""
	Class that handles the Export page.
	"""
	def post(self):
		result = runExport()
		self.response.headers['Content-Type'] = 'text/xml'
		self.response.out.write(str(result))

	def get(self):
		self.render_template('export.html')
		
class EntryPage(BaseHandler) :
	"""
	Class that handles rendering an entry in the datastore.
	"""
	def get(self):
		entry_name = self.request.get('name')
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE name = '%s'" % entry_name)
		if q.count() != 1 :
			self.render_template('_base.html')
		else:
			result=q.get()
			
			# -Obtaining external reference links common to all pages- #
			references = result.reflink
			
			socialKey_list = references.social
			socs = []
			for key in socialKey_list:
				socs.append(Link.get(key))
			
			extKey_list = references.ext
			exts = []
			for key in extKey_list:
				exts.append(Link.get(key))
			
			imageKey_list = references.image
			imgs = []
			for key in imageKey_list :
				imgs.append(Link.get(key))
			
			videoKey_list = references.video
			vids = []
			for key in videoKey_list:
				vids.append(Link.get(key))
			
			# ----Page specific Stuff----#
			class_string = result.class_name()
			if class_string == 'Crisis':
				o_refs = []
				for key in result.orgref:
					o_refs.append(Reference.get(key))
				p_refs = []
				for key in result.personref:
					p_refs.append(Reference.get(key))
				
				self.render_template('crisis_page.html', crisis=result,
									 images=imgs, social=socs,
									 external=exts, videos=vids,
									 orefs=o_refs, prefs=p_refs)
									 
			elif class_string == 'Organization':
				c_refs = []
				for key in result.crisisref:
					c_refs.append(Reference.get(key))
				p_refs = []
				for key in result.personref:
					p_refs.append(Reference.get(key))
				
				self.render_template('organization_page.html', org=result,
									 images=imgs, social=socs, 
									 external=exts, videos=vids,
									 crefs=c_refs, prefs=p_refs)
				
			elif class_string == 'Person':
				c_refs = []
				for key in result.crisisref:
					c_refs.append(Reference.get(key))
				o_refs = []
				for key in result.orgref:
					o_refs.append(Reference.get(key))
					
				self.render_template('person_page.html', person=result,
									 images=imgs, social=socs, 
									 external=exts, videos=vids,
									 orefs=o_refs, crefs=c_refs)
									 
			else :	#Should never reach here, but just in case...
				self.render_template('_base.html')

class SearchPage(BaseHandler) :
	"""
	Class that handles searching and the displaying of search results.
	"""
	def get(self) :
		name = self.request.get('name')
		"""r = []
		for result in searchForString(name):
			r.append(result.fields[0].value)"""
		r = searchForString(name)
			
		self.render_template('search.html', term=name, results=r)

		"""q = db.GqlQuery("SELECT * FROM WorldCrisisPage WHERE name = '%s'" % name)
		if q.count() > 0 :
			r = q
		else :
			r = []
		# q is iterable by itself, no need to call .fetch if default arguments are okay
		self.render_template('search.html', term=name, results=r)
"""

application = webapp.WSGIApplication([('/', MainPage),
									  ('/about', AboutPage),
									  ('/crises', CrisesPage),
									  ('/people', PeoplePage),
									  ('/organizations', OrganizationsPage),
									  ('/import', ImportPage),
									  ('/export', ExportPage),
									  ('/entry', EntryPage),
									  ('/search', SearchPage),
									  ], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
