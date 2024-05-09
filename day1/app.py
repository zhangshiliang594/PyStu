"""
# -*- coding: utf-8 -*-
File    : app.py.py
Author  : zhang 
Time    : 2024-5-9
Project : PyStu
"""

import web

urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())

class hello:

    def GET(self, name):
        if  not name:
            name = 'world'

        return 'hello, ' + name + '!'

if __name__ == '__main__':
    app.run()