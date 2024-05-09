"""
# -*- coding: utf-8 -*-
File    : app2.py
Author  : zhang 
Time    : 2024-5-9
Project : PyStu
"""

import web
import datetime
import os

urls = (
    '/', 'index',
    '/hello', 'hello',
    '/login', 'login',
    '/add', 'add',
    '/delete', 'delete',
    '/(js|css|images)/(.*)', 'static'
)

abspath = os.path.dirname(__file__)

render = web.template.render(abspath + "/templates/")

app = web.application(urls, globals())

class static:

    def GET(self, media, file):
        try:
            print(media + "/" + file)
            f = open(abspath + "/" + media + "/" + file, 'rb')
            return f.read()
        except:
            return ''

class MyData:
    def __init__(self, id, title):
        self.id = id
        self.title = title


class index:
    def GET(self):
        data = MyData(1, "洋洋")
        print(datetime.datetime.now())
        return render.index(data)

class login:
    def GET(self):
        print(datetime.datetime.now())
        return render.login()

class hello:
    def GET(self, name):
        if not name:
            name = 'world'
        return 'hello, ' + name + '!'

class add:
    def POST(self):
        i = web.input()
        print(i)
        raise web.seeother("/")

class delete:
    def GET(self):
        print(web.ctx)
        t = int(web.ctx['query'][4::])
        print(t)
        print(type(t))
        raise web.seeother('/')

if __name__ == '__main__':
    web.config.debug = True
    app.run()
