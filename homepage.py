import jinja2
import os
import webapp2
from datetime import datetime
#from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import users
from webapp2_extras import sessions

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

html = 'This is the more new homepage content.'



class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()


class ViewHomePage(BaseHandler):
    def get(self):
#        user = users.get_current_user()

#        if user:
            self.session['foo'] = 'Kun'

            logout = None
            login = None
            currentuser = users.get_current_user()
            if currentuser:
                  logout = users.create_logout_url('/' )
            else:
                  login = users.create_login_url('/')
            template_values = {
                'content1': html,'currentuser':currentuser, 'login':login, 'logout': logout
            }
            template = jinja_environment.get_template('stdpage_block.html')
            self.response.out.write(template.render(template_values))

#        else:
#            self.redirect(users.create_login_url(self.request.uri))
