from google.appengine.ext import webapp
from google.appengine.ext.db import delete
from Models import Crisis, Organization, Person
from google.appengine.ext.webapp.util import run_wsgi_app
from RunExport import runExport
from RunImport import runImport
from minixsv import pyxsval
from genxmlif import GenXmlIfError

import StringIO

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<meta http-equiv="Refresh" content="1;url=staticpages/splash.html">')

class ImportPage(webapp.RequestHandler):
    def post(self):
        xmlfile = self.request.get("data")
	delete(Crisis.all(keys_only=True))
	delete(Organization.all(keys_only=True))
	delete(Person.all(keys_only=True))
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

application = webapp.WSGIApplication([('/', MainPage), ('/xml/export', ExportPage), ('/xml/import', ImportPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
