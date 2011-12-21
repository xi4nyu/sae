#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import settings, urls
from tornado.web import Application
from tornado.ioloop import IOLoop
from pprint import pprint


def run():
    pprint(sorted(urls))
    app = Application(urls, **settings)
    app.listen(8080)
    IOLoop.instance().start()


def main():
    run()

if __name__ == "__main__":
    main()
