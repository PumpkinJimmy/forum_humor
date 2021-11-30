from flask import Flask, request
from flask_cors import CORS
import psycopg2

settings = {
    'database':{
        'dbname': 'test_forum',
        'host': '192.168.56.104',
        'port': 5432,
        'user': 'win',
        'password': 'Hsp;t1xX'
    }
}

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/hello')
def hello_forum():
    return '<p>Hello, Forum!</p>'

@app.route('/api/forum_user', methods=['GET', 'PUT', 'DELETE'])
def forum_user_access():
    if request.method == 'GET':
        attrs = ('uid', 'uname', 'email', 'gender', 'password', 'signature')
        conn = psycopg2.connect(**settings['database'])
        curs = conn.cursor()
        curs.execute('select * from forum_user')
        raw_data = curs.fetchall()
        data = list(map(lambda t: dict(zip(attrs, t)), raw_data))
        return {
            'status': 'ok',
            'data': data
        }
    else:
        return '<p>Method not support yes</p>'

@app.route('/api/tag', methods=['GET', 'PUT', 'DELETE'])
def tag_access():
    if request.method == 'GET':
        attrs = ('tname', 'hot_value')
        conn = psycopg2.connect(**settings['database'])
        curs = conn.cursor()
        curs.execute('select * from tag')
        raw_data = curs.fetchall()
        data = list(map(lambda t: dict(zip(attrs, t)), raw_data))
        return {
            'status': 'ok',
            'data': data
        }
    else:
        return '<p>Method not support yet</p>'