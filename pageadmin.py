import webapp2
from google.appengine.ext.webapp import template
#from google.appengine.ext.db import djangoforms

#import models

#class PageContentForm(djangoforms.ModelForm):
#  class Meta:
#    model = models.PageContent


#contenthtml = str(PageContentForm())
contenthtml = 'This is the new content admin content.'

class ViewContentPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(
		template.render('page_template.html', {'content1': contenthtml}))
