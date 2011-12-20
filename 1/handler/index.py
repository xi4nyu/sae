#-*- coding:utf-8 -*-

from core.base_handler import BaseHandler
from core.utility import url

@url(r'/?')
class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html", name=u"刘立秋")
