import jinja2
import os
import webapp2
from datetime import datetime
from google.appengine.ext import db

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

#jinja_environment = jinja2.Environment(autoescape=True,
#    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

html = 'This is more new about us content.'

class ViewAboutPage(webapp2.RequestHandler):
    def get(self):
        iden = int(1)
        note = db.get(db.Key.from_path('Notes', iden))
        template_values = {
            'content1': note.text
        }
        template = jinja_environment.get_template('stdpage_block.html')
        self.response.out.write(template.render(template_values))
		
#	def get(self):
#        self.render_template('create.html', {'content1': 'This is more new about us content.'})
