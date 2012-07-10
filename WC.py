from google.appengine.ext import webapp
from google.appengine.ext.db import delete
from Models import *
from google.appengine.ext.webapp.util import run_wsgi_app
from RunExport import runExport
from RunImport import runImport
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
		self.render_template('crises.html')
		
class PeoplePage(BaseHandler):
	def get(self):
		self.render_template('people.html')
		
class OrganizationsPage(BaseHandler):
	def get(self):
		self.render_template('organizations.html')
"""
class ImportPage(webapp.RequestHandler):
	def post(self):
		xmlfile = self.request.get("data")
		deleteModels()
		runImport(xmlfile)
		try:
			runImport(xmlfile)
			self.response.out.write('<meta http-equiv="Refresh" content="1;url=/staticpages/port.html">')
		except:
			self.response.out.write("XML file does not conform to the schema.")

	def get(self):
		print "XML file does not conform to the schema."
		
class ExportPage(webapp.RequestHandler):
	def get(self):
		result = runExport()
		self.response.headers['Content-Type'] = 'text/xml'
		self.response.out.write(str(result))
"""

application = webapp.WSGIApplication([('/', MainPage),
									  ('/about', AboutPage),
									  ('/crises', CrisesPage),
									  ('/people', PeoplePage),
									  ('/organizations', OrganizationsPage)
									  ], debug=True)
#[('/', MainPage), ('/xml/export', ExportPage),('/xml/import', ImportPage)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
