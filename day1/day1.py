"""
# -*- coding: utf-8 -*-
File    : day1.py
Author  : zhang 
Time    : 2024-5-9
Project : PyStu
"""
#登录需求

def dengl():

    userlist = {"wanglin":"594liang!","ningque":"123456","aling":"123456"}
    while True:
        username = input("请输入登录账号:")
        if username in userlist.keys():
            password = input("请输入密码:")
            if password == userlist.get(username):
                print("登录成功")
                break
            else:
                print("密码错误")
        else:
            print("账号不存在")

dengl()