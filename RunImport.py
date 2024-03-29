# -*- coding: utf-8 -*-
from xml.etree.ElementTree import Element, SubElement, parse
from Import import buildModels
import StringIO
import sys, operator
import unicodedata

def runImport(filestring):
	""" 
	imports the contents of the xml string passed to it into the 
	datasotre. 
	filestring is a string that contains an xml instance
	"""
	xmlstring = unicodedata.normalize('NFKD', unicode(filestring)).encode('ascii', 'ignore')
	xmlstring = StringIO.StringIO(xmlstring)
	tree = parse(xmlstring)
	buildModels(tree)
	
def getSchemaString():
	"""Return a string representation of the xml schema file."""
	return """<?xml version="1.0"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

<xsd:element name="worldCrises">
	<xsd:complexType>
		<xsd:sequence>
			<xsd:element name="crisis" type="crisisType"  maxOccurs="unbounded"/>
			<xsd:element name="organization" type="organizationType"  maxOccurs="unbounded"/>
			<xsd:element name="person" type="personType"  maxOccurs="unbounded"/>
		</xsd:sequence>
	</xsd:complexType>
</xsd:element>

<xsd:complexType name = "crisisType">
	<xsd:sequence>
		<xsd:element name="name" type="xsd:normalizedString"/>
		<xsd:element name="info" type="crisisInfoType"/>
		<xsd:element name="ref" type="extLinkType"/>
		<xsd:element name="misc" type="xsd:string"/>
		<xsd:element name="org" type="referenceType" maxOccurs="unbounded"/>
		<xsd:element name="person" type="referenceType" maxOccurs="unbounded"/>
	</xsd:sequence>
	<xsd:attribute name="id" type="xsd:ID" use="required"/>
</xsd:complexType>

<xsd:complexType name="organizationType">
	<xsd:sequence>
		<xsd:element name="name" type="xsd:normalizedString"/>
		<xsd:element name="info" type="orgInfoType"/>
		<xsd:element name="ref" type="extLinkType"/>
		<xsd:element name="misc" type="xsd:string"/>
		<xsd:element name="crisis" type="referenceType" maxOccurs="unbounded"/>
		<xsd:element name="person" type="referenceType" maxOccurs="unbounded"/>
	</xsd:sequence>
	<xsd:attribute name="id" type="xsd:ID" use="required"/>
</xsd:complexType>

<xsd:complexType name="personType">  
	<xsd:sequence>
		<xsd:element name="name" type="xsd:normalizedString"/>
		<xsd:element name="info" type="personInfoType"/>
		<xsd:element name="ref" type="extLinkType"/>
		<xsd:element name="misc" type="xsd:string"/>
		<xsd:element name="crisis" type="referenceType" maxOccurs="unbounded"/>
		<xsd:element name="org" type="referenceType" maxOccurs="unbounded"/>
	</xsd:sequence>
	<xsd:attribute name="id" type="xsd:ID" use="required"/>
</xsd:complexType>

<xsd:complexType name="locationType">
	<xsd:sequence>
		<xsd:element name="city" type="xsd:normalizedString"/>
		<xsd:element name="region" type="xsd:normalizedString"/>
		<xsd:element name="country" type="xsd:normalizedString"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="dateType">
	<xsd:sequence>
		<xsd:element name="time" type="xsd:string"/>
		<xsd:element name="day" type="xsd:integer"/>
		<xsd:element name="month" type="xsd:integer"/>
		<xsd:element name="year" type="xsd:integer"/>
		<xsd:element name="misc" type="xsd:string"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="crisisInfoType">
	<xsd:sequence>
		<xsd:element name="history" type="xsd:string"/>
		<xsd:element name="help" type="xsd:string"/>
		<xsd:element name="resources" type="xsd:string"/>
		<xsd:element name="type" type="xsd:normalizedString"/>
		<xsd:element name="time" type="dateType"/>
		<xsd:element name="loc" type="locationType"/>
		<xsd:element name="impact" type="impactType"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="orgInfoType">
	<xsd:sequence>
		<xsd:element name="type" type="xsd:string"/>
		<xsd:element name="history" type="xsd:string"/>
		<xsd:element name="contact" type="contactsType"/>
		<xsd:element name="loc" type="locationType"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="personInfoType">
	<xsd:sequence>
		<xsd:element name="type" type="xsd:normalizedString"/>
		<xsd:element name="birthdate" type="dateType"/>
		<xsd:element name="nationality" type="xsd:normalizedString"/>
		<xsd:element name="biography" type="xsd:string"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="fulladdrType">
	<xsd:sequence>
		<xsd:element name="address" type="xsd:string"/>
		<xsd:element name="city" type="xsd:normalizedString"/>
		<xsd:element name="state" type="xsd:normalizedString"/>
		<xsd:element name="country" type="xsd:normalizedString"/>
		<xsd:element name="zip" type="xsd:normalizedString"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="contactsType">
	<xsd:sequence>
		<xsd:element name="phone" type="xsd:normalizedString"/>
		<xsd:element name="email" type="xsd:normalizedString"/>
		<xsd:element name="mail" type="fulladdrType"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="impactType">
	<xsd:sequence>
		<xsd:element name="human" type="humanImpType"/>
		<xsd:element name="economic" type="econImpType"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="humanImpType">
	<xsd:sequence>
		<xsd:element name="deaths" type="xsd:integer"/>
		<xsd:element name="displaced" type="xsd:integer"/>
		<xsd:element name="injured" type="xsd:integer"/>
		<xsd:element name="missing" type="xsd:integer"/>
		<xsd:element name="misc" type="xsd:string"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="econImpType">
	<xsd:sequence>
		<xsd:element name="amount" type="xsd:integer"/>
		<xsd:element name="currency" type="xsd:normalizedString"/>
		<xsd:element name="misc" type="xsd:string"/>
	</xsd:sequence>
</xsd:complexType>
   
<xsd:complexType name="extType">
	<xsd:sequence>
		<xsd:element name="site" type="xsd:normalizedString"/>
		<xsd:element name="title" type="xsd:normalizedString"/>
		<xsd:element name="url" type="xsd:token"/>
		<xsd:element name="description" type="xsd:string" minOccurs="0" maxOccurs="1" />
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="extLinkType">
	<xsd:sequence>
		<xsd:element name="primaryImage" type="extType" />
		<xsd:element name="image" type="extType" minOccurs="1" maxOccurs="unbounded"/>
		<xsd:element name="video" type="extType" minOccurs="1" maxOccurs="unbounded"/>
		<xsd:element name="social" type="extType" minOccurs="1" maxOccurs="unbounded"/>
		<xsd:element name="ext" type="extType" minOccurs="1" maxOccurs="unbounded"/>
	</xsd:sequence>
</xsd:complexType>

<xsd:complexType name="referenceType">
	<xsd:attribute name="idref" type="xsd:IDREF" use="required"/>
</xsd:complexType>

</xsd:schema>
"""
