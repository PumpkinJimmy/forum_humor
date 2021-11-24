from flask import Flask
from flask import render_template
import sqlite3
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/hello')
def hello_world():
    return '<p>Hello, Flask!</p>'

@app.route('/view')
def view():
    conn = sqlite3.connect('test_user')
    curs = conn.cursor()
    curs.execute('select * from user')
    users = curs.fetchall()

    return render_template('view.html', users=users)

@app.route('/api/allusers')
def allusers():
    conn = sqlite3.connect('test_user.dat')
    curs = conn.cursor()
    curs.execute('select * from user')
    users = curs.fetchall()
    headers = ('uid', 'name', 'humor', 'tag')
    users = list(map(lambda tp: dict(zip(headers, tp)), users))
    return {
        'ok': True,
        'users': users
    }