#-*- coding:utf-8 -*-

from setting import LOGIN_URL
from core.sql import DBHelper
from md5 import md5

def check_user_name(user_name):
    if not user_name:
        return False, False
    x = DBHelper()
    result = x.find_one("SELECT is_admin FROM user WHERE user_name=%s", user_name)
    if result:
        is_user = True
        is_admin = result
    else:
        is_user = False
        is_admin = False

    return is_user, is_admin


def check_user(user_name, password):
    if not (user_name and password):
        return False
    x = DBHelper()
    result = x.find_one("SELECT password FROM user WHERE user_name=%s", user_name)
    return result and result[0] == md5(password).hexdigest()



def _check_handler(request_handler):
    user_name = request_handler.get_secure_cookie("user_name")
    return check_user_name(user_name)


def is_login(request_handler, *args, **kwargs):
    return _check_handler(request_handler)[0]

def is_admin(request_handler, *args, **kwargs):
    return _check_handler(request_handler)[1]

def redirect_login(request_handler, *args, **kwargs):
    uri = request_handler.request.uri
    request_handler.redirect(LOGIN_URL.format(uri))

