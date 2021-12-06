from flask import Flask, request, g
import flask
from flask_cors import CORS
import json
import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from orm.engine import Psycopg2Engine
from orm.session import DBSession
from models import Tag
import settings




engine = Psycopg2Engine(**settings.database)

db = ThreadedConnectionPool(1, 20, **settings.database)

def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    @app.route('/hello')
    def hello_forum():
        return '<p>Hello, Forum!</p>'

    @app.route('/api/tag', methods=['GET'])
    def get_tags():
        '''
        {
            status: String
            rows: Array
            pks: Array
        }
        '''
        session = DBSession(engine)
        res = session.select(Tag)
        # FIXME: No URI Provided
        return {
            'status': 'testing',
            'rows': res.to_json()
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
        session = DBSession(engine)
        res = session.select(Tag, pk=tname)
        return {
            'status': 'testing',
            'row': res.one().to_json()
        }
        # attrs = ('tname', 'hot_value')
        # keys = ('tname', )
        
        # conn = db.getconn()
        # curs = conn.cursor()

        # curs.execute('select * from tag where tname=%s', [tname])
        # raw_data = curs.fetchall()

        # db.putconn(conn)

        # row = dict(zip(attrs, raw_data[0]))
        # pk = raw_data[0][0]
        # # uri = flask.url_for('get_tag', tname=raw_data[0][0])
        # return {
        #     'status': 'ok',
        #     'row': row,
        #     'pk': pk
        #     # 'uri': uri
        # }

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