import webapp2
from google.appengine.ext.webapp import template

abouthtml = 'This is the new about us content.'
		
class ViewAboutPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(
		template.render('page_template.html', {'content1': abouthtml}))