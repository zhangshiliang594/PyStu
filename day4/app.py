"""
# -*- coding: utf-8 -*-
File    : app.py
Author  : zhang 
Time    : 2024-5-29
Project : PyStu
"""
from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

EXTERNAL_API_URL = '172.20.22.87:8035/esignpro/rest/account/apiAdd'

@app.route('/register', methods=['POST'])
def add_user():
    username = request.form.get('username')
    id_number = request.form.get('idNumber')
    phone_number = request.form.get('phoneNumber')

    heraders = {
        'Content-Type': 'application/json',
        'x-timevale-signature': 'c054b2215990b107b7e0abc7a9b1a3e057ec79f424a7a809e3598e59191e59e0',
        'x-timevale-project-id': '1000000'
    }

    payload = {
        'username': username,
        'id_number': id_number,
        'phone_number': phone_number
    }

    try:
        response = requests.post(EXTERNAL_API_URL, json=payload,heraders=heraders)
        response.raise_for_status()

        data = response.json()
        return jsonify(data),response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"ERROR": "Failed to connect to external service", "details": str(e)}),500

if __name__ == '__main__':
    app.run(debug=True,port=88999)