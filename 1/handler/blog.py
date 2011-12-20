#-*- coding:utf-8 -*-


from core.base_handler import BaseHandler
from core.utility import url

from logic.blog import get_blog


@url(r"/blog/(\w+)/?")
class BlogHandler(BaseHandler):
    def get(self, blog_id):
        self.render("blog.html", Blog = get_blog(blog_id))

@url(r"/blog/?")
class PublishBlogHandler(BaseHandler):
    def get(self):
        self.render("publish_blog.html", scripts = ('blog', ))

    def post(self):
        print self.get_argument("content", None)
        print self.get_argument("title", None)
        self.write("test")


