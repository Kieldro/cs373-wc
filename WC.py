from google.appengine.ext import webapp
from google.appengine.ext.db import delete
from Models import Crisis, Organization, Person
from google.appengine.ext.webapp.util import run_wsgi_app
from RunExport import runExport
from RunImport import runImport
from minixsv import pyxsval
from genxmlif import GenXmlIfError

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<meta http-equiv="Refresh" content="1;url=staticpages/splash.html">')

class ImportPage(webapp.RequestHandler):
    def post(self):
        xmlfile = self.request.get("data")
	delete(Crisis.all(keys_only=True))
	delete(Organization.all(keys_only=True))
	delete(Person.all(keys_only=True))
	runImport(xmlfile)
	#self.response.headers['Content-Type'] = 'text/xml'
        #self.response.out.write(str(xmlfile))
        xmlschema = """<?xml version="1.0"?>
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">

<!-- User defined sub-types-->
<xs:group name="specificLocation">
	<xs:sequence>
		<xs:element name="city" type="xs:string" minOccurs="0"/>
		<xs:element name="state" type="xs:string" minOccurs="0"/>
		<xs:element name="country" type="xs:string" minOccurs="0"/>
	</xs:sequence>
</xs:group>
<xs:group name="dates">
	<xs:sequence>
		<xs:element name="start" type="xs:date"/>
		<xs:element name="end" type="xs:date" minOccurs="0"/>
		<xs:element name="additional" type="xs:string" minOccurs="0"/>
	</xs:sequence>
</xs:group>
<xs:complexType name="dateType">
	<xs:choice>
		<xs:group ref="dates"/>
		<xs:element name="otherDiscription" type="xs:string"/>
	</xs:choice>
</xs:complexType>
<xs:complexType name="locationType">
	<xs:choice>
		<xs:group ref="specificLocation"/>
		<xs:element name="unspecific" type="xs:string"/>
	</xs:choice>
</xs:complexType>
<xs:complexType name="stringAndURI" mixed="true">
	<xs:sequence>
		<xs:element name="link" type="xs:anyURI" minOccurs="0" maxOccurs="unbounded"/>
	</xs:sequence>
</xs:complexType>

<!--Shared Page Data Fields-->
<xs:group name="basicInfo">
	<xs:sequence>
		<xs:element name="name" type="xs:string"/>
		<xs:element name="kind" type="xs:string"/>
		<xs:element name="location" type="locationType"/>
	</xs:sequence>
</xs:group>
<xs:group name="externalResources">
	<xs:sequence>
		<xs:element name="image" type="xs:anyURI" maxOccurs="unbounded"/>
		<xs:element name="video" type="xs:anyURI" maxOccurs="unbounded"/>
		<xs:element name="network" type="xs:anyURI" maxOccurs="unbounded"/>
		<xs:element name="link" type="xs:anyURI" maxOccurs="unbounded"/>
	</xs:sequence>
</xs:group>

<!-- Page parent, includes general data groups -->
<xs:complexType name="datapage">
	<xs:sequence>
		<xs:group ref="basicInfo"/>
		<xs:group ref="externalResources"/>
	</xs:sequence>
	<xs:attribute name="id" type="xs:string" use="required"/>
</xs:complexType>

<!-- Actual page types, all pages extend from datapage.-->
<xs:complexType name="crisisPage">
	<xs:complexContent>
		<xs:extension base="datapage">
			<xs:sequence>
				<xs:element name="date" type="dateType"/>
				<xs:element name="humanImpact" type="xs:string"/>
				<xs:element name="economicImpact" type="xs:string"/>
				<xs:element name="resourcesNeeded" type="xs:string"/>
				<xs:element name="waysToHelp" type="stringAndURI"/>
				<xs:element name="organizationId" type="xs:positiveInteger" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="personId" type="xs:positiveInteger" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:extension>
	</xs:complexContent>
</xs:complexType>
<xs:complexType name="organizationPage">
	<xs:complexContent>
		<xs:extension base="datapage">
			<xs:sequence>
				<xs:element name="history" type="xs:string"/>
				<xs:element name="contactInfo" type="stringAndURI"/>
				<xs:element name="crisisId" type="xs:positiveInteger" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="personId" type="xs:positiveInteger" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:extension>
	</xs:complexContent>
</xs:complexType>
<xs:complexType name="personPage">
	<xs:complexContent>
		<xs:extension base="datapage">
			<xs:sequence>
				<xs:element name="crisisId" type="xs:positiveInteger" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="organizationId" type="xs:positiveInteger" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:extension>
	</xs:complexContent>
</xs:complexType>

<!--Actual instance element defined here-->
<xs:element name="data">
	<xs:complexType>
		<xs:sequence>
			<xs:element name="crises">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="crisis" type="crisisPage" minOccurs="1" maxOccurs="unbounded"/>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="organizations">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="organization" type="organizationPage" minOccurs="1" maxOccurs="unbounded"/>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="people">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="person" type="personPage" minOccurs="4" maxOccurs="unbounded"/>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
</xs:element>
</xs:schema> """
	try:
            domTreeWrapper = pyxsval.parseAndValidateString(str(xmlfile), xsdText=xmlschema)
        except pyxsval.XsvalError, errstr:
            print "Invalid xml file"
	except GenXmlIfError, errstr:
	    print errstr
	    print "Parsing aborted!"

    def get(self):
        print "hello world"

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
