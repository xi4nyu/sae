#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import settings, urls
from tornado.web import Application
from tornado.ioloop import IOLoop


def run():
    print urls
    app = Application(urls, **settings)
    app.listen(8080)
    IOLoop.instance().start()

from core.utility import app_path

def main():
    #print app_path('handler')
    run()

if __name__ == "__main__":
    main()
