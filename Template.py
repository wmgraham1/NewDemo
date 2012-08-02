import jinja2
import os
import webapp2
from datetime import datetime
from google.appengine.ext import db
from google.appengine.api import users

from models import Templates

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

class TemplateBaseHandler(webapp2.RequestHandler):

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


class TemplateList(TemplateBaseHandler):

    def get(self):
        templates = Templates.all()
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/templates' )
        else:
              login = users.create_login_url('/templates/create')
        self.render_template('TemplateList.html', {'templates': templates,'currentuser':currentuser, 'login':login, 'logout': logout})


class TemplateCreate(TemplateBaseHandler):

    def post(self):
        #logging.error('QQQ: templatecreate POST')
        n = Templates(Name=self.request.get('Name')
                  , TemplateType=self.request.get('TemplateType')
                  , FileName=self.request.get('FileName')
                  , Description=self.request.get('Description')
                  , Status=self.request.get('Status')
                  #, CreatedBy=users.get_current_user()
                  #, StatusBy=users.get_current_user()
                  #, StatusDate=datetime.now() # datetime.datetime.utcnow() - datetime.timedelta(hours = 5) for East Coast United States
                  )
        #logging.error('QQQ: templatecreate before put')
        n.put()
        #logging.error('QQQ: templatecreate after put')
        return webapp2.redirect('/templates')

    def get(self):
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/templates' )
        else:
              login = users.create_login_url('/templates/create')
        self.render_template('TemplateCreate.html', {'currentuser':currentuser, 'login':login, 'logout': logout})


class TemplateEdit(TemplateBaseHandler):

    def post(self, template_id):
        iden = int(template_id)
        template = db.get(db.Key.from_path('Templates', iden))
        currentuser = users.get_current_user()
        if currentuser != template.CreatedBy and not users.is_current_user_admin():
            self.abort(403)
            return
        template.Name = self.request.get('Name')
        template.FileName = self.request.get('FileName')
        template.Description = self.request.get('Description')
        template.put()
        return webapp2.redirect('/templates')

    def get(self, template_id):
        iden = int(template_id)
        template = db.get(db.Key.from_path('Templates', iden))
        currentuser = users.get_current_user()
        if currentuser != template.CreatedBy and not users.is_current_user_admin():
            self.abort(403)
            return
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/templates' )
        else:
              login = users.create_login_url('/templates')
        self.render_template('TemplateEdit.html', {'template': template,'currentuser':currentuser, 'login':login, 'logout': logout})


class TemplateDelete(TemplateBaseHandler):

    def get(self, template_id):
        iden = int(template_id)
        template = db.get(db.Key.from_path('Templates', iden))
        currentuser = users.get_current_user()
        if currentuser != template.CreatedBy and not users.is_current_user_admin():
            self.abort(403)
            return
        db.delete(template)
        return webapp2.redirect('/templates')
