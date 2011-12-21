#-*- coding:utf-8 -*-

from core.utility import url
from core.base_handler import BaseHandler

from logic.user import check_user

from model.result import Result


class AdminHandler(BaseHandler):
    pass

@url(r"/admin/login")
class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", scripts = ('login', 'key'))

    def post(self):
        user_name = self.get_argument("user_name")
        password = self.get_argument("password")
        if check_user(user_name, password):
            self.set_secure_cookie('user_name', user_name)
            back_uri = self.get_argument('back', '/')
            self.write(Result(True, back = back_uri).to_json())
        else:
            self.write(Result(False).to_json())



@url(r"/clear")
class ClearHandler(BaseHandler):
    def get(self):
        self.clear_all_cookies()
