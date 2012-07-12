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
			self.response.out.write("Validation aborted!")
			self.render_template('import.html', status='error')
			return
		except GenXmlIfError, errstr:
			self.response.out.write("Parsing aborted!")
			self.render_template('import.html', status='error')
			return
		except:
			self.response.out.write("XML file does not conform to the schema.")
			self.render_template('import.html', status='error')
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
		#TODO: change this to be dynamic later!
		self.render_template('person_page.html')

application = webapp.WSGIApplication([('/', MainPage),
									  ('/about', AboutPage),
									  ('/crises', CrisesPage),
									  ('/people', PeoplePage),
									  ('/organizations', OrganizationsPage),
									  ('/import', ImportPage),
									  ('/export', ExportPage),
									  ('/entry', EntryPage),
									  ], debug=True)
#[('/', MainPage), ('/xml/export', ExportPage),('/xml/import', ImportPage)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
