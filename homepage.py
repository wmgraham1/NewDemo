import os
import webapp2

import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

homehtml = 'This is the more new homepage content.'
	
class ViewHomePage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'content1': homehtml
        }

        template = jinja_environment.get_template('page_template.html')
        self.response.out.write(template.render(template_values))

