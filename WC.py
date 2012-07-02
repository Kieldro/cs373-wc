from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<meta http-equiv="Refresh" content="1;url=staticpages/splash.html">')

class ImportPage(webapp.RequestHandler):
    def post(self):
        xmlfile = self.request.get("data")
        """xmlschema = open('/staticfiles/WC1.xsd', 'r')
	try:
            domTreeWrapper = pyxsval.parseAndValidate(xmlfile, xsdFile=xmlschema)
        except pyxsval.XsvalError, errstr:
            print errstr
            print "Invalid xml file"
        except GenXmlIfError, errstr:
            print errstr
            print "Parsing aborted!" """
	self.response.headers['Content-Type'] = 'text/xml'
	self.response.out.write(str(xmlfile))

    def get(self):
        self.response.out.write('Hello import')

class ExportPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('hello world')

application = webapp.WSGIApplication([('/', MainPage), ('/xml/export', ExportPage), ('/xml/import', ImportPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
