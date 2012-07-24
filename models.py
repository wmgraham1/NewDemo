import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import users

class Languages(db.Model):
  langCode = db.StringProperty()
  langCode3 = db.StringProperty()
  langName = db.StringProperty()
  
class Templates(db.Model):
  Name = db.StringProperty()
  Description = db.StringProperty()
  FileName = db.StringProperty()
  CreatedBy = db.UserProperty()
  CreatedDate = db.DateTimeProperty(auto_now_add=True)
  Status = db.StringProperty()
  StatusBy = db.UserProperty()
  StatusDate = db.DateTimeProperty()
 
class PageContent(db.Model):
  """Models an individual pagecontent block with page name, content, createdby and createddate."""
  TemplateName = db.StringProperty()
  TokenTag = db.StringProperty()
  LangCode = db.StringProperty()
  ContentText = db.StringProperty(multiline=True)
  CreatedBy = db.StringProperty()
  CreatedDate = db.DateTimeProperty(auto_now_add=True)
  UpdatedBy = db.UserProperty()
  UpdatedDate = db.DateTimeProperty()
  Status = db.StringProperty()
  StatusBy = db.UserProperty()
  StatusDate = db.DateTimeProperty()
  LangName = db.StringProperty()

  
class Notes(db.Model):
  author = db.StringProperty()
  text = db.TextProperty()
  priority = db.StringProperty()
  status = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)
  whichuser = db.UserProperty()
  
class Obj(db.Model):
  oid = db.IntegerProperty(long)
  className = db.StringProperty()
  createdDate = db.DateTimeProperty(auto_now_add=True)
  createdBy = db.UserProperty()
  updatedDate = db.DateTimeProperty(auto_now_add=True)
  updatedBy = db.UserProperty()
  status = db.IntegerProperty()  
  statusDate = db.DateTimeProperty(auto_now_add=True)
  statusBy = db.UserProperty()

#  We should use ndb but seems to have issues with jinja2
# class TokenValues(ndb.Model):
#   templateName = ndb.StringProperty()
#   langCode = ndb.StringProperty()
#   tknID = ndb.StringProperty()
#   tknValue = ndb.StringProperty()
#   date = ndb.DateTimeProperty(auto_now_add=True)
#   whichuser = ndb.UserProperty()

class TokenValues(db.Model):
  templateName = db.StringProperty()
  langCode = db.StringProperty()
  tknID = db.StringProperty()
  tknValue = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)
  whichuser = db.UserProperty()

  
#class Greeting(db.Model):
#  """Models an individual Guestbook entry with an author, content, and date."""
#  author = db.StringProperty()
#  content = db.StringProperty(multiline=True)
#  date = db.DateTimeProperty(auto_now_add=True)

