from xml.etree.ElementTree import Element, SubElement
from Import import parse, buildModels

import sys, operator, Models

crisisList = []
orgList = []
personList = []


crises = Crisis.all()
for c in crises:
	crisisList.append(c)

organizations = Organization.all()
for o in organizations:
	orgList.append(o)

people = People.all()
for p in people:
	personList.append(p)

ans = buildTree(crisisList, orgList, personList)
ans.write()




