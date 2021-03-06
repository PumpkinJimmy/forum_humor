import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from .error import ORMError
from .queryset import Query
from .model import Model, ModelMetaClass

class Engine:
    pass

class Engine:
    def getconn(self):
        raise NotImplemented()

    def putconn(self, conn):
        raise NotImplemented()
    
    def select(self, conn, model, *args, **kwargs):
        raise NotImplemented()
    
    def insert(self, conn, obj: Model, *args, **kwargs):
        return NotImplemented()
    
    def delete(self, conn, *args, **kwargs):
        return NotImplemented()
    
    def update(self, conn, obj: Model, *args, **kwargs):
        return NotImplemented()

class Psycopg2Engine(Engine):
    
    @staticmethod
    def query2sql(query):
        '''
        required:
            - method
            - tablename
        optional:
            - condition
            - agg
            - orderby
            - orderby_desc
            - limit
            - offset
            - join
        '''
        if query['method'] == 'select':
            tpl = 'select {agg_str} from {tablename}'

            agg = query.get('agg')
            if agg is not None:
                agg_str = f'{agg}(*)'
            else:
                agg_str = '*'
            join = query.get('join')
            if join:
                table1 = query['tablename']
                table2 = join['join_model'].__tablename__
                tablename = f"{table1} join {table2} on {table1}.{join['field1']} = {table2}.{join['field2']}"
            else:
                tablename = query['tablename']
            tpl = tpl.format(
                tablename=tablename,
                agg_str=agg_str
            )

            condition = query.get('condition')

            if condition:
                'FIXME: not general'
                tpl += f' where {condition}'

            orderby = query.get('orderby')
            desc = query.get('orderby_desc')
            if orderby:
                tpl += f' order by {orderby} {"desc" if desc else "asc"}'

            limit = query.get('limit')
            if limit:
                tpl += f' limit {limit}'

            offset = query.get('offset')
            if offset:
                tpl += f' offset {offset}'
            print(query)
            print(tpl)
            return tpl, query.get('condition_value', ())
        else:
            raise NotImplemented()

    def __init__(self, **conf):
        self.minconn = conf.get('minconn', 1)
        self.maxconn = conf.get('maxconn', 8)
        self.conf = conf
        keys = ('dbname', 'host', 'port', 'user', 'password')
        try:
            self.dbconf = {k:conf[k] for k in keys} 
        except:
            raise ORMError(f'Need keys: {keys}')
        else:
            self.pool = ThreadedConnectionPool(self.minconn, self.maxconn, **self.dbconf)
    
    def getconn(self):
        return self.pool.getconn()
    
    def putconn(self, conn):
        self.pool.putconn(conn)
    
    def select(self, conn, model: Model, **query):
        pk = query.get('pk', None)
        if pk:
            if type(pk) != list and type(pk) != tuple:
                pk = (pk, )
            pk_query_str = ' and '.join(map(
                lambda a: f'{a}={model.get_field(a).get_fmt()}', 
                model.__pk__))
            query['condition'] = pk_query_str
            query['condition_value'] = pk
        query['method'] = 'select'
        query['tablename'] = model.__tablename__
        return Query(self, query, model)
    
    def insert(self, conn, obj: Model, *args, **kwargs):
        model = type(obj)
        curs = conn.cursor()
        data = obj.get_data()
        fmt_str = ','.join((model.get_field(a).get_fmt() for a in model.__fields__))
        print(tuple(data.values()))
        print(f'insert into {model.__tablename__} values ({fmt_str})')
        curs.execute(f'insert into {model.__tablename__} values ({fmt_str})', tuple(data.values()))
    
    def delete(self, conn, obj_or_model: Model, *args, **kwargs):
        print(type(obj_or_model))
        if issubclass(type(obj_or_model), Model):
            obj = obj_or_model
            model = type(obj)
            pk_val = obj.get_keyval()
        else:
            model = obj_or_model
            pk_val = kwargs['pk']
            if type(pk_val) != list and type(pk_val) != tuple:
                pk_val = (pk_val, )
        fmt_str = model.get_key_fmtstr()
        curs = conn.cursor()
        print(pk_val)
        print(f'delete from {model.__tablename__} where {fmt_str}')
        curs.execute(f'delete from {model.__tablename__} where {fmt_str}', pk_val)
    
    def update(self, conn, obj: Model, *args, **kwargs):
        curs = conn.cursor()
        model = type(obj)
        pk_val = obj.get_keyval()
        new = obj.get_data()
        if 'pk' in kwargs:
            pk_val = kwargs['pk']
        if 'new' in kwargs:
            new = kwargs['newl']
        fmt_where_str = ' and '.join(map(lambda pk: f'{pk}={model.get_field(pk).get_fmt()}', model.__pk__))
        fmt_new_str = ','.join(map(lambda k: f'{k}={model.get_field(k).get_fmt()}', new.keys()))
        print(f'update {model.__tablename__} set {fmt_new_str} where {fmt_where_str}')
        print(tuple(new.values()) + tuple(pk_val))
        curs.execute(
            f'update {model.__tablename__} set {fmt_new_str} where {fmt_where_str}', 
            tuple(new.values()) + tuple(pk_val)
            )
    
    def raw(self, conn, statement, value=()):
        curs = conn.cursor()
        curs.execute(statement,value)
        return curs.fetchall()