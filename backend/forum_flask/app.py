from flask import Flask, request
from flask_cors import CORS
import json
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

@app.route('/api/tag', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tag_access():
    attrs = ('tname', 'hot_value')
    # Query
    if request.method == 'GET':
        conn = psycopg2.connect(**settings['database'])
        curs = conn.cursor()
        curs.execute('select * from tag')
        raw_data = curs.fetchall()
        data = list(map(lambda t: dict(zip(attrs, t)), raw_data))
        return {
            'status': 'ok',
            'data': data
        }
    # Insert
    elif request.method == 'POST':
        
        new_tag = json.loads(request.data)
        t = []
        for attr in attrs:
            t.append(new_tag.get(attr, None))
        try:
            print(f"Try insert tuple {t}")
            conn = psycopg2.connect(**settings['database'])
            curs = conn.cursor()
            curs.execute(
                'insert into tag values (%s, %s)',
                t)
        except psycopg2.Error as e:
            print(e)
            return {
                'status': 'fail'
            }
        else:
            # curs.execute('select * from tag')
            # print(curs.fetchall())
            # curs.execute('rollback')
            # print('Rollback')
            curs.execute('commit')
            print('Commit')
            return {
                'status': 'ok',
                'data': 'This is a post'
            }
    # Update
    elif request.method == 'PUT':
        return '<p>Update not support yet</p>'
    elif request.method == 'DELETE':
        return '<p>DELETE not support yet</p>'
    else:
        return '<p>Method not support yet</p>'