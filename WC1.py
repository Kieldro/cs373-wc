from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
	def get(self):
	self.response.out.write('<meta http-equiv="Refresh" content="1;url=http://jwilke-cs373-wc.appspot.com/staticpages/splash.html">')

application = webapp.WSGIApplication([ ('/', MainPage) ], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
