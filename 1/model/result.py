#-*- coding:utf-8 -*-
import json

class Result(object):
    def __init__(self, success, **kwargs):
        self.success = success
        self.data = kwargs

    def to_json(self):
        return json.dumps(dict(success = self.success, data = self.data))
