from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(host="remotemysql.com",
                                       user="wXy63pU5g1" ,
                                       password="qV0gRNMGRK"
                                       database="wXy63pU5g1")
        mycursor = mydb.cursor()
        mycursor.execute(
            'SELECT * FROM LoginDetails WHERE username = %s AND password = %s',
            (username, password)
        account = mycursor.fetchone
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in successfully'
            print('login successfull')
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'incorrect credentials, kindly check'
            return render_template('login.html', msg=msg)
        else:
            return render_template('login.html')


@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = 'Logged out successfully'
    return render_template('login.html', msg=msg, name=name, id=id)


@app.route('/register', methods=['GET', 'POST'])
def register
        )