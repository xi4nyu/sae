#-*- coding:utf-8 -*-

"""
    author:         llq<llq17501@gmail.com>
    status:         1 normal
                    2 complete
                    3 delete
"""
from core.sql import DBHelper

from model.todo import Todo



def get_todo_list():
    db = DBHelper()
    count, result = db.find("SELECT id, text, status FROM todo")
    return [dict(Id = Id, text = text, status = status) for Id, text, status in result]

def add_todo(text):
    print "todo"
    db = DBHelper()
    db.insert("todo", ("text", "status"), ((text, 1),))

def del_todo(Id):
    pass

def modify_todo(Id, text, status):
    pass
