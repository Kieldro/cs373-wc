from google.appengine.api import search
from google.appengine.ext import db

def createDocument(name, paragraph ):
    return search.Document(
        fields=[search.TextField(name = 'name', value = name),
                search.TextField(name = 'content', value = paragraph)])

def createIndex():
	q = db.GqlQuery("SELECT * FROM WorldCrisisPage")

	index = search.Index(name='index',
                     consistency=search.Index.PER_DOCUMENT_CONSISTENT)


	for page in q:
		
		if (page.class_name() == 'Crisis'):
			content = page.crisisinfo.history + page.crisisinfo.helps + page.crisisinfo.resources
		elif (page.class_name() == 'Organization'):
			content = page.orginfo.history
		else :
			content = page.personinfo.biography
		
		index.add(createDocument(page.name, content))

def deleteDocs() :
	doc_index = search.Index('index')
	
	while True:
		document_ids = [document.doc_id for document in doc_index.list_documents(ids_only=True)]
		if not document_ids:
			break
		doc_index.remove(document_ids)
		
def searchForString(search_string):
	options = search.QueryOptions(limit = 10)  # the number of results to return)
	q = search.Query(search_string, options)

	index = search.Index(name = 'index')

	results = index.search(q)

	return results

