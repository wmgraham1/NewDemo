import os
import webapp2

import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

contacthtml = 'This is the more new contact us content.'	
	
class ViewContactPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'content1': contacthtml
        }

        template = jinja_environment.get_template('page_template.html')
        self.response.out.write(template.render(template_values))


#import webapp2
#from google.appengine.ext.webapp import template
		
#class ViewContactPage(webapp2.RequestHandler):
#  def get(self):
#    self.response.out.write(
#		template.render('page_template.html', {'content1': contacthtml}))