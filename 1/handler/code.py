#-*- coding:utf-8 -*-

from core.utility import url, FileLike
from core.base_handler import BaseHandler
from logic.code import code_to_html


@url(r"/code/?")
class CodeHandler(BaseHandler):
    def get(self):
        with open("logic/code.py") as code:
            self.render("code.html", code = code_to_html(code), styles = ("code" ,))
