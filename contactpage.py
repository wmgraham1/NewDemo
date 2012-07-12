import webapp2
from google.appengine.ext.webapp import template

contacthtml = 'This is the new contact us content.'
		
class ViewContactPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(
		template.render('page_template.html', {'content1': contacthtml}))