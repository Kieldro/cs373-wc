from google.appengine.ext import webapp
from google.appengine.ext.db import delete
from Models import *
from google.appengine.ext.webapp.util import run_wsgi_app
from RunExport import runExport
from RunImport import runImport, getSchemaString
from minixsv import pyxsval
from genxmlif import GenXmlIfError
from google.appengine.ext.webapp import template

import os
import StringIO

def deleteModels() :
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
		path = os.path.join(os.path.dirname(__file__), 'templates', filename)
		self.response.out.write(template.render(path, template_args))
	
class MainPage(BaseHandler):
	def get(self):
		self.render_template('index.html')
		
class AboutPage(BaseHandler):
	def get(self):
		self.render_template('about.html')
		
class CrisesPage(BaseHandler):
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE crisisinfo != NULL")
		results = q.fetch(5)
		self.render_template('crises.html', crises_list=results)
		
class PeoplePage(BaseHandler):
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE personinfo != NULL")
		results = q.fetch(5)
		self.render_template('people.html', people_list=results)
		
class OrganizationsPage(BaseHandler):
	def get(self):
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE orginfo != NULL")
		results = q.fetch(5)
		self.render_template('organizations.html', orgs_list=results)

class ImportPage(BaseHandler):
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

		deleteModels()
		try:
			runImport(xmlfile)
			self.render_template('import.html', status='success')
		except:
			self.render_template('import.html', status='error')
	
	def get(self):
		self.render_template('import.html')
		
class ExportPage(BaseHandler):
	def post(self):
		result = runExport()
		self.response.headers['Content-Type'] = 'text/xml'
		self.response.out.write(str(result))

	def get(self):
		self.render_template('export.html')
		
class EntryPage(BaseHandler) :
	def get(self):
		entry_name = self.request.get('name')
		q = db.GqlQuery("SELECT * FROM WorldCrisisPage " +
						"WHERE name = '%s'" % entry_name)
		if q.count() != 1 :
			self.render_template('_base.html')
		else:
			result=q.get()
		
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
			
			self.render_template('person_page.html', person=result,
								 images = imgs, social=socs, 
								 external = exts, videos=vids)

class MockupPage(BaseHandler):
	def get(self):
		self.render_template('mockup.html')
		
application = webapp.WSGIApplication([('/', MainPage),
									  ('/about', AboutPage),
									  ('/crises', CrisesPage),
									  ('/people', PeoplePage),
									  ('/organizations', OrganizationsPage),
									  ('/import', ImportPage),
									  ('/export', ExportPage),
									  ('/entry', EntryPage),
									  ('/mockup', MockupPage),
									  ], debug=True)
#[('/', MainPage), ('/xml/export', ExportPage),('/xml/import', ImportPage)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
