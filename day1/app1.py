"""
# -*- coding: utf-8 -*-
File    : app1.py.py
Author  : zhang 
Time    : 2024-5-9
Project : PyStu
"""

import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index:

    def GET(self, name):
        index_text = open('index1.html','rb').read()

        return index_text

if __name__ == '__main__':
    app.run()