import webapp2
from google.appengine.ext import db

Class PageContent(db.Model):
  pagename = db.StringProperty()
  textContent = db.StringProperty()
  
