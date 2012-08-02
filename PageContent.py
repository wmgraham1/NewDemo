import jinja2
import os
import webapp2
import logging
from datetime import datetime
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import users
from webapp2_extras import sessions
from google.appengine.api import memcache

from models import PageContents
from models import Languages

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

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



class PageContentList(BaseHandler):

    def get(self):
        languages = memcache.get("languages")
        if languages is not None:
           logging.info("get languages from memcache.")
        else:
           languages = Languages.all()
           logging.info("Can not get languages from memcache.")
           if not memcache.add("languages", languages, 10):
               logging.info("Memcache set failed.")

        if self.request.get('langCode'):
            langCode=self.request.get('langCode')
            self.session['langCode'] = langCode
        else:
            langCode = self.session.get('langCode')
        if not langCode:
            self.session['langCode'] = 'en'

        LangName = 'no language'
        for language in languages:
            if language.langCode == langCode:
                langName = language.langName

#        q = db.GqlQuery("SELECT * FROM PageContents " + 
#                "WHERE langCode = :1 " +
#                "ORDER BY TemplateName ASC",
#                "en")
#        pagecontents = q.fetch(999)
		pagecontents = PageContents.all()
 
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/pagecontents' )
        else:
              login = users.create_login_url('/pagecontents/create')
#        self.render_template('PageContentList.html', {'pagecontents': pagecontents, 'LangName':LangName, 'currentuser':currentuser, 'login':login, 'logout': logout})
        self.render_template('PageContentList.html', {'pagecontents': pagecontents, 'currentuser':currentuser, 'login':login, 'logout': logout})


class PageContentCreate(BaseHandler):

    def post(self):
        #TemplateName = 'about-us'
        #LangCode = 'en'
        #TokenTag = 'content1'
        #text = 'about-us'
        #Status = 'Published'
        CreatedBy = users.get_current_user()
        #StatusBy = users.get_current_user()
	
        n = PageContents(TemplateName=self.request.get('TemplateName'),
                LangCode=self.request.get('LangCode'),
                TokenTag=self.request.get('TokenTag'),
                ContentText=self.request.get('ContentText'),
                Status='Published',
                CreatedBy=CreatedBy,
                StatusBy=CreatedBy
                )

        n.put()

        q = db.GqlQuery("SELECT * FROM PageContents " + 
                "WHERE LangCode = :1 " +
                "ORDER BY TemplateName ASC",
                "en")
        pagecontents = q.fetch(999)
#		pagecontents = PageContents.all()
 
        logout = None
        login = None
        currentuser = users.get_current_user()
        if currentuser:
              logout = users.create_logout_url('/pagecontents' )
        else:
              login = users.create_login_url('/pagecontents/create')
        self.render_template('PageContentList.html', {'pagecontents': pagecontents, 'currentuser':currentuser, 'login':login, 'logout': logout})

        #return webapp2.redirect('/pagecontents/')

    def get(self):
        self.render_template('PageContentCreate.html', {})


class PageContentEdit(BaseHandler):

    def post(self, pagecontent_id):
        iden = int(pagecontent_id)
        PageContent = db.get(db.Key.from_path('PageContents', iden))
        PageContent.TemplateName = self.request.get('author')
        PageContent.LangCode = self.request.get('LangCode')
        PageContent.TokenTag = self.request.get('TokenTag')
        PageContent.ContentText = self.request.get('ContentText')
        #PageContent.Status = self.request.get('Status')
        PageContent.put()
        return webapp2.redirect('/')

    def get(self, pagecontent_id):
        iden = int(pagecontent_id)
        PageContent = db.get(db.Key.from_path('PageContents', iden))
        self.render_template('PageContentEdit.html', {'PageContent': PageContent})


class PageContentDelete(BaseHandler):

    def get(self, pagecontent_id):
        iden = int(pagecontent_id)
        PageContent = db.get(db.Key.from_path('PageContents', iden))
        db.delete(PageContent)
        return webapp2.redirect('/pagecontents')
