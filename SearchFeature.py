from google.appengine.api import search
from google.appengine.ext import db

def createDocument(name, paragraph, type2, location, id2 ):
	'''Creates a document to search through'''
	return search.Document(
		doc_id = id2,
		fields=[search.TextField(name = 'name', value = name),
		search.TextField(name = 'content', value = paragraph),
		search.TextField(name = 'type', value = type2),
		search.TextField(name = 'location', value = location)])

def createIndex() :
	'''Creates the index used for search, crawls through the datastore, and populates the index.'''
	q = db.GqlQuery("SELECT * FROM WorldCrisisPage")

	index = search.Index(name='index',
                     consistency=search.Index.PER_DOCUMENT_CONSISTENT)


	for page in q:

		if (page.class_name() == 'Crisis'):
			content = page.crisisinfo.history + page.crisisinfo.helps + page.crisisinfo.resources
			type2 = page.crisisinfo.ctype
			loc = page.crisisinfo.location
			location = '%s %s %s' % (loc.city, loc.region, loc.city)
		elif (page.class_name() == 'Organization'):
			content = page.orginfo.history
			type2 = page.orginfo.otype
			loc = page.orginfo.location
			location = '%s %s %s' % (loc.city, loc.region, loc.city)
		elif (page.class_name() == 'Person' ):
			content = page.personinfo.biography
			type2 = page.personinfo.ptype
			location = page.personinfo.nationality
		else :
			raise Exception
		
		index.add(createDocument(page.name, content, type2, location, page.ID))

def deleteDocs() :
	'''Removes all documents from the index'''
	doc_index = search.Index('index')
	
	while True:
		document_ids = [document.doc_id for document in doc_index.list_documents(ids_only=True)]
		if not document_ids:
			break
		doc_index.remove(document_ids)
		
def searchForString(search_string):
	'''Search queries for the given string'''
	options = search.QueryOptions(
		returned_fields=['name'],
		snippeted_fields=['name', 'content', 'type', 'location'])

	q = search.Query(query_string=search_string, options=options)

	index = search.Index(name = 'index')

	results = index.search(q)

	return results


