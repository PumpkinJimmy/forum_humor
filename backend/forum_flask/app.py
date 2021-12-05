from flask import Flask, request, g
import flask
from flask_cors import CORS
import json
import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from orm import Psycopg2Engine, DBSession
from models import Tag


settings = {
    'database':{
        'dbname': 'test_forum',
        'host': '192.168.56.104',
        'port': 5432,
        'user': 'win',
        'password': 'Hsp;t1xX'
    }
}

engine = Psycopg2Engine(**settings['database'])

db = ThreadedConnectionPool(1, 20, **settings['database'])

def create_app():
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

    @app.route('/api/tag', methods=['GET'])
    def get_tags():
        '''
        {
            status: String
            rows: Array
            pks: Array
        }
        '''

        attrs = ('tname', 'hot_value')
        keys = ('tname', )
        
        session = DBSession(engine)
        conn = session.get_raw_conn()

        curs = conn.cursor()
        curs.execute('select * from tag')
        raw_data = curs.fetchall()

        rows = list(map(lambda t: dict(zip(attrs, t)), raw_data))
        # uris = list(map(lambda t: flask.url_for('get_tag', tname=t[0], _external=True), raw_data))
        pks = list(map(lambda t: t[0], raw_data))
        return {
            'status': 'ok',
            'rows': rows,
            'pks': pks
            # 'uris': uris
        }

    @app.route('/api/tag/<tname>', methods=['GET'])
    def get_tag(tname):
        '''
        {
            status: String,
            row: Object,
            pk: String
        }
        '''
        attrs = ('tname', 'hot_value')
        keys = ('tname', )
        
        conn = db.getconn()
        curs = conn.cursor()

        curs.execute('select * from tag where tname=%s', [tname])
        raw_data = curs.fetchall()

        db.putconn(conn)

        row = dict(zip(attrs, raw_data[0]))
        pk = raw_data[0][0]
        # uri = flask.url_for('get_tag', tname=raw_data[0][0])
        return {
            'status': 'ok',
            'row': row,
            'pk': pk
            # 'uri': uri
        }

    @app.route('/api/tag', methods=['POST'])
    def create_tag():
        '''
        req: Object
        '''
        new_tag = request.get_json()
        try:
            print(f"Try insert tuple {new_tag}")
            session = DBSession(engine)
            conn = session.get_raw_conn()
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
            curs.execute('commit')
            print('Commit')
            return {
                'status': 'ok',
                'data': 'This is a post'
            }

    @app.route('/api/tag/<tname>', methods=['PUT'])
    def update_tag(tname):
        '''
        req: Object
        '''
        attrs = ('tname', 'hot_value')
        new_value = request.get_json()
        vars = []
        for attr in attrs:
            vars.append(new_value.get(attr, None))
        try:
            print(f"Try update {tname} to {new_value}")
            conn = db.getconn()
            curs = conn.cursor()
            curs.execute(
                '''
                update tag
                set tname=%s,
                hot_value=%s
                where tname=%s
                ''',
                vars + [tname])
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
            db.putconn(conn)

    @app.route('/api/tag/<tname>', methods=['DELETE'])
    def delete_tag(tname):
        if request.method == 'DELETE':
            try:
                print(type(tname))
                conn = db.getconn()
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
                db.putconn(conn)

    return app