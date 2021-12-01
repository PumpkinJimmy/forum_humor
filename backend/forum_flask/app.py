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

@app.route('/api/tag', methods=['GET', 'POST', 'PUT'])
def tag_access():
    attrs = ('tname', 'hot_value')
    keys = ('tname', )
    # Query
    if request.method == 'GET':
        '''
        {
            status: 'ok'
            rows: [row]
            key: [attr...]
        }
        '''
        conn = psycopg2.connect(**settings['database'])
        curs = conn.cursor()
        curs.execute('select * from tag')
        raw_data = curs.fetchall()
        rows = list(map(lambda t: dict(zip(attrs, t)), raw_data))
        return {
            'status': 'ok',
            'rows': rows,
            'key': ['tname']
        }
    # Insert
    elif request.method == 'POST':
        new_tag = request.get_json()
        try:
            print(f"Try insert tuple {new_tag}")
            conn = psycopg2.connect(**settings['database'])
            curs = conn.cursor()
            curs.execute(
                'insert into tag values (%(tname)s, %(hot_value)s)',
                new_tag)
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
        finally:
            conn.close()
    # Update
    elif request.method == 'PUT':
        '''
        req:{
            old_key: {data subset},
            new_value: {data}
        }
        '''
        data = request.get_json()
        new_value = data['new_value']
        old_key = data['old_key']
        vars = []
        for attr in attrs:
            vars.append(new_value.get(attr, None))
        ks = []
        for attr in keys:
            ks.append(old_key.get(attr, None))
        try:
            print(f"Try update from {old_key} to {new_value}")
            conn = psycopg2.connect(**settings['database'])
            curs = conn.cursor()
            curs.execute(
                '''
                update tag
                set tname=%s,
                hot_value=%s
                where tname=%s
                ''',
                vars + ks)
        except psycopg2.Error as e:
            print(e)
            return {
                'status': 'fail'
            }
        else:
            curs.execute('commit')
            print('Commit')
            return {
                'status': 'ok',
                'data': 'This is a put'
            }
        finally:
            conn.close()
        # return '<p>PUT not support yet</p>'
    
    else:
        return '<p>Method not support yet</p>'

@app.route('/api/tag/<tname>', methods=['DELETE'])
def tag_delete(tname):
    if request.method == 'DELETE':
        try:
            print(type(tname))
            conn = psycopg2.connect(**settings['database'])
            curs = conn.cursor()
            curs.execute(
                'delete from tag where tname=%s',
                (tname, ))
        except psycopg2.Error as e:
            print(e)
            return {
                'status': 'fail'
            }
        else:
            curs.execute('commit')
            print('Commit')
            return {
                'status': 'ok',
                'data': 'This is a delete'
            }
        finally:
            conn.close()
    # return '<p>DELETE not support yet</p>'