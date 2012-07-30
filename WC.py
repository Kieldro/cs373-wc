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
from math import ceil

import os
import re
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

def generatePagenavs(page, num_pages) :
		pagenav_list = []
		
		if page==1 :
			pagenav_list.append('<li class="disabled"><a>&laquo</a></li>')
		else :
			pagenav_list.append('<li><a href="/crises?p=%s">&laquo</a></li>' % (page-1))
		
		# If there are less than 5 pages, just display all.
		if num_pages <= 5 :
			for p in range(1,num_pages+1) :
				if p == page :
					pagenav_list.append('<li class="active"><a href="/crises?p=%s">%s</a></li>' %(p, p))
				else:
					pagenav_list.append('<li><a href="/crises?p=%s">%s</a></li>' % (p,p))
		# If we can, display 5 at a time with page in the middle:  [<<][p-2][p-1][p][p+1][p+2][>>]
		elif page+2 <= num_pages :
			for p in range(page-2, page+3):
				if p == page :
					pagenav_list.append('<li class="active"><a href="/crises?p=%s">%s</a></li>' % (p,p))
				else:
					pagenav_list.append('<li><a href="/crises?p=%s">%s</a></li>' % (p,p))
		# If we get here, just display the last 5 pages, current page doesn't have to be in the middle
		else :
			for p in range(num_pages-4, num_pages+1) :
				if p == page :
					pagenav_list.append('<li class="active"><a href="/crises?p=%s">%s</a></li>' % (p,p))
				else:
					pagenav_list.append('<li><a href="/crises?p=%s">%s</a></li>' % (p,p))
					
		if page==num_pages :
			pagenav_list.append('<li class="disabled"><a>&raquo</a></li>')
		else :
			pagenav_list.append('<li><a href="/crises?p=%s">&raquo</a></li>' % (page+1))
			
		return pagenav_list
	
	
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
		self.render_template('index.html', first=toplist[0], topimgs=toplist[1:4])
		
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
		pstring = self.request.get('p')
		if pstring == '' :
			page = 1
		else :
			try:
				page = int(pstring)
			except:
				self.render_template('_base.html')
				return
		
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE crisisinfo != NULL")
		num_pages = int(ceil(q.count()/4))
		results = q.fetch(offset=(page-1)*4, limit=4)
		self.render_template('crises.html', crises_list=results, pagenav=generatePagenavs(page, num_pages))
		
class PeoplePage(BaseHandler):
	"""
	Class that handles the People listing page.
	"""
	def get(self):
		pstring = self.request.get('p')
		if pstring == '' :
			page = 1
		else :
			try:
				page = int(pstring)
			except:
				self.render_template('_base.html')
				return

		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE personinfo != NULL")
		num_pages = int(ceil(q.count()/4))
		results = q.fetch(offset=(page-1)*4, limit=4)
		self.render_template('people.html', people_list=results, pagenav=generatePagenavs(page, num_pages))
		
class OrganizationsPage(BaseHandler):
	"""
	Class that handles the Organizations listing page.
	"""
	def get(self):
		pstring = self.request.get('p')
		if pstring == '' :
			page = 1
		else :
			try:
				page = int(pstring)
			except:
				self.render_template('_base.html')
				return
				
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE orginfo != NULL")
		num_pages = int(ceil(q.count()/4))
		results = q.fetch(offset=(page-1)*4, limit=4)
		self.render_template('organizations.html', orgs_list=results, pagenav=generatePagenavs(page, num_pages))

class ImportPage(BaseHandler):
	"""
	Class that handles the Import page. 
	On GET, the page is generated.
	On POST, the xml given by the user is validated. If it passes, it is added to the models.
	"""
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage ORDER by name")
		self.render_template('import.html', pages=q)

	def post(self):
		xmlfile = self.request.get("data")
		xmlschema = getSchemaString()
		
		# validate XML instance
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

		#try:
		runImport(xmlfile)
		#except Exception, e:
		#	self.render_template('import.html', status='error', message=e.args)
		#	return

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
				#vids.append(Link.get(key))
				v = Link.get(key)
				if re.search("youtube", v.url):
					if re.search("embed", v.url):
						vids.append('<iframe width="560" height="315" src="%s?wmode=transparent" frameborder="0" allowfullscreen></iframe>' % v.url)
					else :
						vsearch = re.search("v=((.)*)(&)?", v.url)
						vids.append(vids.append('<iframe width="560" height="315" src="http://www.youtube.com/embed/%s?wmode=transparent" frameborder="0" allowfullscreen></iframe>'% vsearch.group(1)))
				else :
					vids.append('<a href="%s">%s</a>' % (v.url, v.url))
			
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
		mode = self.request.get('type')
		if (mode == 'e'):
			x = searchForString("'"+name+"'")
			self.render_template('search.html', term=name, results=x)
		elif (mode == 'k'):
			andterms = re.sub(" ", " AND ", name)
			orterms =  re.sub(" ", " OR ", name)
			r = searchForString(andterms)
			s = searchForString(orterms)
			x = set(r)
			y = set(s)
			y = y - x
			self.render_template('search.html', term=andterms, term2=orterms, results=x, results2=y)

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
