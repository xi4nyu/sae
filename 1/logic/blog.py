#-*- coding:utf-8 -*-
from model.blog import Blog
from core.sql import DBHelper

TABLE_NAME = "blog"

def publish_blog(title, content):
    d = DBHelper()
    return d.insert(TABLE_NAME, ("title", "content", "is_show"), ((title, content, True),))


def get_all_blogs():
    d = DBHelper()
    count, result = d.find("SELECT id, title, content, create_time from blog")
    blogs = [Blog(ID, title, content, create_time) for ID, title, content, create_time in result]
    return count, blogs

def get_blog(blog_id):
    d = DBHelper()
    result = d.find_one("SELECT title, content, create_time from blog where id=%s", blog_id)
    if result:
        title, content, create_time = result
        b = Blog(blog_id, title, content, create_time)
        return b

