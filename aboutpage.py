import os
import webapp2

import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class ViewAboutPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'content1': 'This is more new about us content.'
        }

        template = jinja_environment.get_template('page_template.html')
        self.response.out.write(template.render(template_values))


#import webapp2
#from google.appengine.ext.webapp import template

#abouthtml = 'This is the new about us content.'
		
#class ViewAboutPage(webapp2.RequestHandler):
#  def get(self):
#    self.response.out.write(
#		template.render('page_template.html', {'content1': abouthtml}))