#-*- coding:utf-8 -*-

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def render(self, *args, **kwargs):
        if 'scripts' not in kwargs:
            kwargs['scripts'] = ()
        if 'styles' not in kwargs:
            kwargs['styles'] = ()
        super(BaseHandler, self).render(*args, **kwargs)
