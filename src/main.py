import os
import urllib

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

	
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers.add_header("X-Custom", "CCC")	
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))
		
class XSSPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers.add_header("X-Custom", "CCC")	
        template = JINJA_ENVIRONMENT.get_template('xss.html')
        self.response.write(template.render({}))
		
class CORSPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers.add_header("X-Custom", "CCC")	
        template = JINJA_ENVIRONMENT.get_template('cors.html')
        self.response.write(template.render({}))
		
class TutorialPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers.add_header("X-Custom", "CCC")	
        template = JINJA_ENVIRONMENT.get_template('tutorial.html')
        self.response.write(template.render({}))
		
application = webapp2.WSGIApplication([
	('/', MainPage),
	('/xss', XSSPage),
	('/cors', CORSPage),
	('/tutorial', TutorialPage)], debug=True)