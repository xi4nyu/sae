#-*- coding:utf-8 -*-
from os import listdir
from os.path import splitext, dirname, abspath, join as path_join
from fnmatch import fnmatch
from inspect import getmembers, isclass
from core.base_handler import BaseHandler

class FileLike:
    def __init__(self, content, split = '\n'):
        self.content = content
        self.index = 0
        self.split = split
    def __next__(self):
        if self.index == len(self.content):
            raise StopIteration
        old_index = self.index
        new_line = self.content.find(self.split, old_index)
        if new_line > 0:
            self.index = new_line + len(self.split)
        else:
            self.index = len(self.content)
        return self.content[old_index:self.index]
    
    def readline(self):
        return self.__next__()


def get_files(path, file_filter):
    return (splitext(n)[0] for n in listdir(path) if file_filter(n))


def get_members(path, member_filter):
    file_filter = lambda f:all((not f.startswith("__"), fnmatch(f, "*.py")))
    modules = [getattr(__import__(".".join((path, file_name))), file_name) for file_name in get_files(path, file_filter)]
    return ((k, v) for module in modules for k, v in getmembers(module) if member_filter(k, v))


def get_urls():
    member_filter = lambda k, v:isclass(v) and issubclass(v, BaseHandler) and hasurl(v)
    return [(geturl(v), v) for k, v in get_members('handler', member_filter)]


def app_path(dir_name):
    return abspath(path_join(dirname(__file__), '..', dir_name))


def url(path):
    def wrap(cls):
        cls._url = path
        return cls
    return wrap


def hasurl(cls):
    return hasattr(cls, '_url')


def geturl(cls):
    return cls._url


def authorized(check, fail_handler):
    def wrap(handler):
        def authorized_handler(self, *args, **kwargs):
            if check(self, *args, **kwargs):
                handler(self, *args, **kwargs)
            else:
                fail_handler(self, *args, **kwargs)
        return authorized_handler
    return wrap
