from google.appengine.api import search
from google.appengine.ext.db import Query

def createDocument(name, paragraph ):
    return search.Document(
        fields=[search.TextField(name = 'name', value = name),
                search.TextField(name = 'content', value = paragraph)])

def createIndex():
	q = db.GqlQuery("SELECT * FROM WorldCrisisPage")
	results = q.fetch()

	index = search.Index(name='index',
                     consistency=search.Index.PER_DOCUMENT_CONSISTENT)


	for page in results:
		
		if (page.class_name() == 'Crisis'):
			content = page.crisisinfo.history + page.crisisinfo.helps + page.crisisinfo.resources
		elif (page.class_name() == 'Organization'):
			content = page.orginfo.history
		else (page.class_name() == 'Person'):
			content = page.personinfo.biography
		
		index.add(CreateDocument(page.name, content))
	
def search(search_string):
	options = search.QueryOptions(limit = 10)  # the number of results to return)
	q = search.Query(search_string, options)

	index = search.Index(name = 'index')

	results = index.search(query)

	return results


