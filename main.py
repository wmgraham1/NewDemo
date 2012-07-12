#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext.webapp.util import run_wsgi_app

import webapp2
import homepage
import pageadmin
import aboutpage
import contactpage

# Below code is what the original exercise included
#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.out.write('Hello brave new world!')

app = webapp2.WSGIApplication([
	('/', homepage.ViewHomePage),
	('/about', aboutpage.ViewAboutPage),
	('/content', pageadmin.ViewContentPage),
	('/contact', contactpage.ViewContactPage)
	],
                              debug=True)


							  


# below is the code that worked with Python (not 2.7)
#application = webapp2.WSGIApplication([
#	('/', homepage.ViewHomePage),
#	('/about', aboutpage.ViewAboutPage),
#	('/content', pageadmin.ViewContentPage)
#	],
#                              debug=True)
							  
#def main():
#    run_wsgi_app(application)

#if __name__ == '__main__':
#    main()