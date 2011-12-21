#-*- coding:utf-8 -*-

SHORT_CONTENT_LENGTH = 100

class Blog(object):

    def __init__(self, Id, title, content, create_time):
        self.Id = Id
        self.title = title
        self.content = content
        self.create_time = create_time

    @property
    def short_content(self):
        if not hasattr(self, '_short_content'):
            #TODO 处理content中有html标签的情况
            if len(self.content) < SHORT_CONTENT_LENGTH:
                self._short_content = self.content
            else:
                self._short_content = self.content[:SHORT_CONTENT_LENGTH - 3] + "..."
        return self._short_content

    @property
    def create_date(self):
        return self.create_time.date()
