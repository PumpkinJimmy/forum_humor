import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from .error import ORMError
from .queryset import QuerySet

class Engine:
    pass

class Engine:
    def getconn(self):
        raise NotImplemented()

    def putconn(self, conn):
        raise NotImplemented()
    
    def select(self, conn, model, *args, **kwargs):
        raise NotImplemented()

class Psycopg2Engine(Engine):
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
    
    def select(self, conn, model, *args, **kwargs):
        curs = conn.cursor()
        pk = kwargs.get('pk', None)
        if pk is None:
            curs.execute(f'select * from {model.__tablename__}')
        else:
            if type(pk) != list or type(pk) != tuple:
                pk = (pk, )
            pk_query_str = ' and '.join(map(
                lambda a: f'{a}={model.get_field(a).get_fmt()}', 
                model.__pk__))
            print(f'Auto construct SQL: select * from {model.__tablename__} where {pk_query_str}')
            curs.execute(f'select * from {model.__tablename__} where {pk_query_str}', pk)
        res = curs.fetchall()
        return QuerySet(map(model.from_tuple, res))