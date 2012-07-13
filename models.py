import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

class PageContent(db.Model):
  """Models an individual pagecontent block with page name, content, createdby and createddate."""
  pagename = db.StringProperty()
  textContent = db.StringProperty(multiline=True)
  createdby = db.StringProperty()
  createddate = db.DateTimeProperty(auto_now_add=True)
  
class Notes(db.Model):
  author = db.StringProperty()
  text = db.StringProperty(multiline=True)
  priority = db.StringProperty()
  status = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)

  
#class Greeting(db.Model):
#  """Models an individual Guestbook entry with an author, content, and date."""
#  author = db.StringProperty()
#  content = db.StringProperty(multiline=True)
#  date = db.DateTimeProperty(auto_now_add=True)

