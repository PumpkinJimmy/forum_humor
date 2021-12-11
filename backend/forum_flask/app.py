from flask import Flask, request, g
import flask
from flask.helpers import url_for
from flask_cors import CORS
import json
import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from werkzeug.routing import BaseConverter
from orm.model import ModelMetaClass

from orm.engine import Psycopg2Engine
from orm.session import DBSession
from models import Tag, ForumUser
import settings




engine = Psycopg2Engine(**settings.database)

db = ThreadedConnectionPool(1, 20, **settings.database)

def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    class KeyConverter(BaseConverter):
        regex = r'[\w\W]+'
        def to_python(self, value):
            return tuple(value.strip('/').split('/'))
        def to_url(self, values):
            return '/'.join(map(str, values))
    
    class ModelConverter(BaseConverter):
        registered_models = {
            'tag': Tag,
            'user': ForumUser
        }
        def to_python(self, model_name):
            return self.registered_models[model_name]
        
        def to_url(self, model):
            for k, v in self.registered_models.items():
                if v == model:
                    return k
    
    app.url_map.converters['key'] = KeyConverter
    app.url_map.converters['model'] = ModelConverter

    @app.route('/object/<model:m>/<key:pk>/')
    def generic_view(m, pk):
        print(m)
        print(pk)
        # print(flask.url_for('generic_view', m=Tag, pk=pk))
        return '<p>Test Works</p>'

    @app.route('/hello/')
    def hello_forum():
        return '<p>Hello, Forum!</p>'

    @app.route('/api/v1/object/<model:model>/', methods=['GET'])
    def get_objects(model):

        session = DBSession(engine)
        res = session.select(model)
        uris = [
            url_for('get_object', model=model, pk=tuple(obj.get_key().values())) 
            for obj in res.all()
        ]
        return {
            'status': 'ok',
            'objs': res.to_json(),
            'uris': uris
        }

    @app.route('/api/v1/object/<model:model>/<key:pk>/', methods=['GET'])
    def get_object(model, pk):

        session = DBSession(engine)
        res = session.select(model, pk=pk)
        return {
            'status': 'ok',
            'obj': res.one().to_json(),
            'uri': url_for('get_object', model=model, pk=res.one().get_key().values())
        }
        
    @app.route('/api/v1/object/<model:model>/', methods=['POST'])
    def create_tag(model):
        '''
        req: Object
        '''
        new_obj = model(request.get_json())
        try:
            print(f"Try insert tuple {new_obj}")
            session = DBSession(engine)
            session.insert(new_obj)
            session.commit()
        except psycopg2.Error as e:
            print(e)
            return {
                'status': 'fail'
            }
        else:
            return {
                'status': 'ok'
            }

    @app.route('/api/v1/object/<model:model>/<key:pk>/', methods=['PUT'])
    def update_tag(model, pk):
        '''
        req: Object
        '''
        session = DBSession(engine)
        new_value = model(request.get_json())
        try:
            session.update(new_value, pk=pk)
            session.commit()
        except psycopg2.Error as e:
            print(e)
            return {
                'status': 'fail'
            }
        else:
            return {
                'status': 'ok'
            }

    @app.route('/api/v1/object/<model:model>/<key:pk>/', methods=['DELETE'])
    def delete_tag(model, pk):
        if request.method == 'DELETE':
            session = DBSession(engine)
            session.delete(model, pk=pk)
            return {
                'status': 'ok'
            }
    
    @app.route('/api/v1/form/<model:model>/', methods=['GET'])
    def get_for_listview(model):
        raise NotImplemented()
        return {
            'status': 'ok',
            'layout': model.__fields__
        }

    return app

    