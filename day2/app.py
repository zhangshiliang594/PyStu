"""
# -*- coding: utf-8 -*-
File    : app.py.py
Author  : zhang 
Time    : 2024-5-27
Project : PyStu
"""

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from mysql.connector import Error
import bcrypt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

# 连接数据库配置
def create_conn():
    return mysql.connector.connect(
        host = '192.168.22.100',
        port = '3306',
        user = 'root',
        password = 'Timevale#123`',
        database = 'mywebapp_test'
    )

@app.route('/')
def home():
    if 'username' in session:
        return f"hello, {session['username']}! <a href='{url_for('logout')}'>Logout</a>"
    return redirect(url_for('logout'))


def hash_password(password):
    """哈希给定的密码"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form.get('eamil')

        hashed_password = hash_password(password)

        try:
            conn = create_conn()
            cursor = conn.cursor()
            query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, hashed_password, email))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('login'))
        except Error as e:
            print("Error while connecting to MySql", e)
            return "An error occurred, please try again later."
    return render_template('register.html')


def verify_password(stored_password_hash, provided_password):
    """验证提供的密码是否与存储的哈希密码匹配"""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password_hash.encode('utf-8'))


# 登录逻辑中使用verify_password函数
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = create_conn()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            print(user)
            cursor.close()
            conn.close()

            if user and verify_password(user['password'], password):  # 验证密码
                session['username'] = username
                return redirect(url_for('welcome'))
            else:
                return "Invalid username or password."
        except Error as e:
            print("Error while connecting to MySQL", e)
            return "An error occurred, please try again later."

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    username = session.get('username')  # 获取session中的用户名
    if not username:
        # 如果用户未登录，则重定向到登录页面或其他适当页面
        return redirect(url_for('login'))
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)