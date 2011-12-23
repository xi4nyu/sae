#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import settings, urls
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIApplication
from wsgiref import simple_server

from werkzeug.serving import run_simple

from pprint import pprint


def run():
    pprint(sorted(urls))
    app = Application(urls, **settings)
    app.listen(8080)
    IOLoop.instance().start()

def run_wsgi():
    pprint(sorted(urls))
    app = WSGIApplication(urls, **settings)
    run_simple('localhost', 8080, app, use_reloader = True, use_debugger = True, extra_files = [])


def main():
    run()

if __name__ == "__main__":
    main()
