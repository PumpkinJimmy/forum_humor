from flask import Flask, request, g
from flask import session
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
import models
import settings

from ml.classification import EmotionClassifier
from json_encoder import CustomJSONEncoder
import datetime
import os

engine = Psycopg2Engine(**settings.database)

db = ThreadedConnectionPool(1, 20, **settings.database)

classifier = EmotionClassifier('./ml/model/doc2vec.model', './ml/model/net_state_dict.pth')

registered_models = {
    'user': models.ForumUser,
    'post': models.Post,
    'message': models.Message,
    'comment': models.Comment,
    'tag': models.Tag,
    'tag_post': models.TagPost,
    'tag_user': models.TagUser,
    'tag_log': models.TagLog,
}

def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    app.json_encoder = CustomJSONEncoder

    class KeyConverter(BaseConverter):
        regex = r'[\w\W]+'
        def to_python(self, value):
            return tuple(value.strip('/').split('/'))
        def to_url(self, values):
            if type(values) not in (list, tuple):
                return str(values)
            return '/'.join(map(str, values))
    
    class ModelConverter(BaseConverter):
        registered_models = registered_models
        def to_python(self, model_name):
            return self.registered_models[model_name]
        
        def to_url(self, model):
            for k, v in self.registered_models.items():
                if v == model:
                    return k
    
    app.url_map.converters['key'] = KeyConverter
    app.url_map.converters['model'] = ModelConverter
    app.secret_key = os.urandom(64)

    

    @app.route('/hello/')
    def hello_forum():
        return '<p>Hello, Forum!</p>'
    
    @app.route('/api/v1/model/', methods=['GET'])
    def get_models():
        return {
            'status': 'ok',
            'models': list(registered_models.keys())
        }

    @app.route('/api/v1/model/<model:model>/', methods=['GET'])
    def get_form(model):
        return {
            'status': 'ok',
            'model_info': model.get_model_info()
        }

    @app.route('/api/v1/object/<model:model>/', methods=['GET'])
    def get_objects(model):
        session = DBSession(engine)
        if request.args.get('count_only', 'false') == 'true':
            res = session.select(model, agg='count').all()
            return {
                'status': 'ok',
                'objs': [],
                'uris': [],
                'count': int(res)
            }

        # ================================
        # FIXME: SQL Injection risk
        # ================================
        offset = request.args.get('offset')
        limit = request.args.get('limit')
        orderby = request.args.get('orderby')
        desc = True if request.args.get('desc') == 'true' else False
        
        res = session.select(model, limit=limit, offset=offset, orderby=orderby, orderby_desc=desc)

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
            'uri': url_for('get_object', model=model, pk=tuple(res.one().get_key().values())[0])
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
                'status': 'ok',
                'uri': url_for('get_object', model=model, pk=new_obj.get_keyval())
            }

    @app.route('/api/v1/object/<model:model>/<key:pk>/', methods=['PUT'])
    def update_tag(model, pk):
        '''
        req: Object
        '''
        session = DBSession(engine)
        new_obj = model(request.get_json())
        print(request.get_json())
        try:
            session.update(new_obj, pk=pk)
            session.commit()
        except psycopg2.Error as e:
            print(e)
            return {
                'status': 'fail'
            }
        else:
            return {
                'status': 'ok',
                'uri': url_for('get_object', model=model, pk=new_obj.get_keyval())
            }

    @app.route('/api/v1/object/<model:model>/<key:pk>/', methods=['DELETE'])
    def delete_tag(model, pk):
        if request.method == 'DELETE':
            session = DBSession(engine)
            session.delete(model, pk=pk)
            return {
                'status': 'ok'
            }
    
    @app.route('/api/v1/ml/infer_all/', methods=['GET'])
    def infer_all():
        session = DBSession(engine)
        posts = session.select(models.Post, condition='content is not null', limit=10).to_json()
        sentences = list(map(lambda d: d['content'], posts))
        res = [classifier.infer_emotion(sentence) for sentence in sentences]
        return {
            'status': 'ok',
            'res': res
        }
    
    @app.route('/api/v1/ml/infer_user/<string:uid>/', methods=['GET'])
    def infer_user(uid):
        from models import ForumUser, Post
        session = DBSession(engine)
        qs = session.select(ForumUser,
            join={
                'join_model': Post,
                'field1': 'uid',
                'field2': 'poster_uid'
            },
            condition=ForumUser.uid==uid
            )
        rows, fields = qs.all_raw()
        if not rows:
            return {'status': 'no available text'}
        content_idx = fields.index('content')
        res = [classifier.infer_emotion(row[content_idx]) for row in rows]
        return {
            'status': 'ok',
            'res': res
        }
    
    @app.route('/api/v1/query/user_posts/<key:pk>/')
    def query_join(pk):
        from models import ForumUser, Post
        session = DBSession(engine)
        qs = session.select(ForumUser,
            join={
                'join_model': Post,
                'field1': 'uid',
                'field2': 'poster_uid'
            },
            condition=ForumUser.uid==pk[0]
            )
        print(engine.query2sql(qs.query))
        return {
            'data': qs.all_raw(),
            'status': 'ok'
        }

    @app.route('/api/v1/query/tag_access/', methods=['GET'])
    def query_tags_access():
        session = DBSession(engine)
        return {
            'status':'ok',
            'res': session.raw('select * from tag_access_count')
        }

    @app.route('/api/v1/query/tag_access/<string:tname>/', methods=['GET'])
    def query_tag_access(tname):
        session = DBSession(engine)
        return {
            'status':'ok',
            'res': session.raw(f'select count from tag_access_count where tname=%s', (tname,))[0][0]
        }
    
    @app.route('/api/v1/log/tag_access/', methods=['GET'])
    def log_tag_access():
        tname = request.args['tname']
        uid = request.args['uid']
        log = models.TagLog({
            'tname': tname,
            'uid': uid,
            'access_time': datetime.datetime.now().timestamp()
        })
        session = DBSession(engine)
        session.insert(log)
        session.commit()
        return {
            'status': 'ok'
        }
    
    

    @app.route('/api/v1/auth/login_status/')
    def index():
        if 'username' in session:
            return {
                'status': 'ok',
                'username': session['username']
            }
        return {
            'status': 'no login'
        }

    @app.route('/api/v1/auth/login/', methods=['POST'])
    def login():
        data = request.get_json()
        session['username'] = data['username']
        return {
            'status': 'ok',
            'username': session['username']
        }

    # @app.route('/logout')
    # def logout():
    #     # remove the username from the session if it's there
    #     session.pop('username', None)
    #     return redirect(url_for('index'))

    return app

    