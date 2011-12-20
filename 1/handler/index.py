#-*- coding:utf-8 -*-

from core.base_handler import BaseHandler
from core.utility import url, get_urls, get_files

@url(r'/?')
class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html", name=u"刘立秋")
 

