import jinja2
import os
import webapp2
from datetime import datetime
#from google.appengine.api import users
from google.appengine.ext import db

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

html = 'This is the more new homepage content.'

class ViewHomePage(webapp2.RequestHandler):
    def get(self):
#        user = users.get_current_user()

#        if user:
			template_values = {
				'content1': html
			}
			template = jinja_environment.get_template('stdpage_block.html')
			self.response.out.write(template.render(template_values))

#        else:
#            self.redirect(users.create_login_url(self.request.uri))
