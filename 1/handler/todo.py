#-*- coding:utf-8 -*-

from core.utility import url
from core.base_handler import BaseHandler

from logic.todo import get_todo_list, add_todo, del_todo, modify_todo
from json import dumps



NAME = "todo"
@url("(?i)/todo/?")
class TodoHandler(BaseHandler):
    def get(self):
        self.render("todo.html", scripts = ("key", "dialog", "todo",), styles = ("todo", "dialog"))

@url("(?i)/todo/list/?")
class GetTodoHandler(BaseHandler):
    def get(self):
        ls = get_todo_list()
        re = dumps({"result":ls})
        self.write(re)


@url("(?i)/todo/add/?")
class AddHandler(BaseHandler):
    def post(self):
        text=self.get_argument("text")
        add_todo(text)
        self.write({"result":get_todo_list()})


@url("(?i)/todo/del/?")
class DeleteHandler(BaseHandler):
    def post(self):
        id=self.get_argument("id",None)
        if not id:
            return
        del_todo(id)
        self.write({"result":get_todo_list()})


@url("(?i)/todo/modify/?")
class ModifyHandler(BaseHandler):
    def post(self):
        id=self.get_argument("id")
        if not id:
            return 
        id=int(id)
        text=self.get_argument("text",None)
        status=self.get_argument("status",None)
        modify_todo(id, text, status)
        self.write({"result":get_todo_list()})
