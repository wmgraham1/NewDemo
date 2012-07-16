import jinja2
import os
import webapp2
from datetime import datetime
#from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import users

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

html = 'This is the more new homepage content.'

class ViewHomePage(webapp2.RequestHandler):
    def get(self):
#        user = users.get_current_user()

#        if user:

            logout = None
            login = None
            currentuser = users.get_current_user()
            if currentuser:
                  logout = users.create_logout_url('/notes/create' )
            else:
                  login = users.create_login_url('/notes/create')
            template_values = {
                'content1': html,'currentuser':currentuser, 'login':login, 'logout': logout
            }
            template = jinja_environment.get_template('stdpage_block.html')
            self.response.out.write(template.render(template_values))

#        else:
#            self.redirect(users.create_login_url(self.request.uri))
