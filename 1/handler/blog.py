#-*- coding:utf-8 -*-


from core.base_handler import BaseHandler
from core.utility import url, authorized

from logic.user import is_admin, redirect_login

from logic.blog import get_blog, publish_blog, get_all_blogs


@url(r"/blog/(\d+)/?")
class BlogHandler(BaseHandler):
    def get(self, blog_id):
        blog = get_blog(blog_id)
        if blog:
            self.render("blog.html", Blog = blog)
        else:
            self.send_error(404)

@url(r"/admin/blog/?")
class PublishBlogHandler(BaseHandler):
    @authorized(is_admin, redirect_login)
    def get(self):
        self.render("publish_blog.html", scripts = ('blog', ))

    def post(self):
        #TODO content最大为64K,需改进
        content = self.get_argument("content", None)
        title = self.get_argument("title", None)
        result = publish_blog(title = title.encode('utf8'), content = content.encode('utf8'))
        self.write(str(result))


@url(r"/blog/?")
class BlogsHandler(BaseHandler):
    def get(self):
        count, blogs = get_all_blogs()
        self.render("blogs.html", blogs = blogs)
