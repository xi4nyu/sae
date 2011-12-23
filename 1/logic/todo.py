#-*- coding:utf-8 -*-

from core.sql import DBHelper

def get_todo_list():
    db = DBHelper()
    count, result = db.find("SELECT text, status FROM todo")
    return result

def add_todo(text):
    db = DBHelper()
    db.insert("todo", ("text", "status"), ((text, ""),))

def del_todo(Id):
    pass

def modify_todo(Id, text, status):
    pass
