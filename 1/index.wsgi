#-*- coding:utf-8 -*-
import sae
import tornado.wsgi

from main import urls, settings

app = tornado.wsgi.WSGIApplication(urls)
application = sae.create_wsgi_app(app)
