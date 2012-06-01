#-*- coding:utf-8 -*-

from tornado.web import RequestHandler
import json

class BaseHandler(RequestHandler):
    def render(self, *args, **kwargs):
        if 'scripts' not in kwargs:
            kwargs['scripts'] = ()
        if 'styles' not in kwargs:
            kwargs['styles'] = ()
        super(BaseHandler, self).render(*args, **kwargs)

    def json(self, value):
        json = value.to_json() if hasattr(value, "to_json") else json.dumps(value)
        self.write(json)
