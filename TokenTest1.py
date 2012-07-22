import jinja2
import os
import webapp2
import logging
from datetime import datetime
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import users

from models import TokenValues
from models import Languages

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class TknBaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))


class TknStep1Page(TknBaseHandler):

    def get(self):
        tokens = TokenValues.all()
        countmap={}
        for token in tokens:
            logging.info('QQQ: token: %s' % token.langCode)
            if token.langCode in countmap:
                    countmap[token.langCode]=countmap[token.langCode]+1
            else:
                    countmap[token.langCode]=1
        #tokens = TokenValues.query()
        if self.request.get('langCode'):
            langCode=self.request.get('langCode')
            #tokens = TokenValues.query(TokenValues.langCode == langCode)
            tokens = tokens.filter('langCode =', langCode)
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/tokens' )
        else:
              login = users.create_login_url('/tokens/create')
        self.render_template('TknStep1.html', {'countmap':countmap, 'tokens': tokens,'currentuser':currentuser, 'login':login, 'logout': logout})

class TknMainPage(TknBaseHandler):

    def get(self):
        tokens = TokenValues.all()
        #tokens = TokenValues.query()
        if self.request.get('langCode'):
            langCode=self.request.get('langCode')
            #tokens = TokenValues.query(TokenValues.langCode == langCode)
            tokens = tokens.filter('langCode =', langCode)
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/tokens' )
        else:
              login = users.create_login_url('/tokens/create')
        self.render_template('TknList.html', {'tokens': tokens,'currentuser':currentuser, 'login':login, 'logout': logout})


class CreateTkn(TknBaseHandler):

    def post(self):
        n = TokenValues(templateName=self.request.get('templateName'),
                  langCode=self.request.get('langCode'),
                  tknID=self.request.get('tknID'),
                  tknValue=self.request.get('tknValue')
                  , whichuser=users.get_current_user()
                  )

        n.put()
        return webapp2.redirect('/tokens')

    def get(self):
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/tokens' )
        else:
              login = users.create_login_url('/tokens/create')
        self.render_template('TknCreate.html', {'currentuser':currentuser, 'login':login, 'logout': logout})


class EditTkn(TknBaseHandler):

    def post(self, token_id):
        iden = int(token_id)
        token = db.get(db.Key.from_path('TokenValues', iden))
        currentuser = users.get_current_user()
        if currentuser != token.whichuser and not users.is_current_user_admin():
            self.abort(403)
            return
        token.templateName = self.request.get('templateName')
        token.langCode = self.request.get('langCode')
        token.tknID = self.request.get('tknID')
        token.tknValue = self.request.get('tknValue')
        token.date = datetime.now()
        token.put()
        return webapp2.redirect('/tokens')

    def get(self, token_id):
        iden = int(token_id)
        token = db.get(db.Key.from_path('TokenValues', iden))
        currentuser = users.get_current_user()
        if currentuser != token.whichuser and not users.is_current_user_admin():
            self.abort(403)
            return
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/tokens' )
        else:
              login = users.create_login_url('/tokens')
        self.render_template('TknEdit.html', {'token': token,'currentuser':currentuser, 'login':login, 'logout': logout})


class DeleteTkn(TknBaseHandler):

    def get(self, token_id):
        iden = int(token_id)
        token = db.get(db.Key.from_path('TokenValues', iden))
        currentuser = users.get_current_user()
        if currentuser != token.whichuser and not users.is_current_user_admin():
            self.abort(403)
            return
        db.delete(token)
        return webapp2.redirect('/tokens')
