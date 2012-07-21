import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
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
  pagename = db.StringProperty()
  textContent = db.StringProperty(multiline=True)
  createdby = db.StringProperty()
  createddate = db.DateTimeProperty(auto_now_add=True)
  
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

