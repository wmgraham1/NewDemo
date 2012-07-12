import webapp2
from google.appengine.ext.webapp import template

homehtml = 'This is the new homepage content.'

class ViewHomePage(webapp2.RequestHandler):
  def get(self):
	self.response.out.write(
		template.render('page_template.html', {'content1': homehtml}))


