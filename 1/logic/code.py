#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tokenize import tokenize, COMMENT, NAME, STRING, OP, NUMBER
from tornado.escape import xhtml_escape

def code_to_html(file_obj):
    code_parse = CodeParse()
    return list_to_html(code_parse(file_obj))




def f(x):
    snippet, t = x
    return ''.join(('<span class="', t, '">', xhtml_escape(snippet), '</span>'))


def list_to_html(lst):
    """
        author:         llq<llq17501@gmail.com>
        args:
            lst             ((codesnippet, type), ...)
    """
    return ''.join(map(f, lst))

PythonKeywords = set(('and', 'del', 'from', 'not', 'while',
            'as', 'elif', 'global', 'or', '','with',
            'assert', 'else', 'if', 'pass', 'yield',
            'break', 'except', 'import', 'print',
            'class', 'exec', 'in', 'raise',
            'continue', 'finally', 'is', 'return',
            'def', 'for', 'lambda', 'try'))

StyleClass = {
            COMMENT:"comment",
            STRING:"string",
            OP:"operator",
            NUMBER:"number"
        }

class CodeParse:
    def __init__(self):
        self._result = []

    def tokenize(self, type_num, snippet, begin, end, line):
        if hasattr(self, 'prev_end'):
            begin_line, begin_column = begin
            end_line, end_column = self.prev_end
            if begin_line != end_line:
                end_column = 0
            if begin_column != end_column:
                self._result[-1][0].append(' ' * (begin_column - end_column))
        if snippet:
            type_name = StyleClass.get(type_num, "normal")

            if type_num == NAME and snippet in PythonKeywords:
                type_name = "keyword"

            if self._result and type_name == self._result[-1][1]:
                self._result[-1][0].append(snippet)
            else:
                self._result.append(([snippet], type_name))
        self.prev_end = end

    def __call__(self, file_obj):
        tokenize(file_obj.readline, self.tokenize)
        return self.result

    @property
    def result(self):
        return [(''.join(snippet), tp) for snippet, tp in self._result]



def main():
    with open('code.py') as code:
        print code_to_html(code)



if __name__ == "__main__":
    main()
