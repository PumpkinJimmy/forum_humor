import psycopg2
from psycopg2.pool import ThreadedConnectionPool

class Engine:
    pass

class ORMError(Exception): pass

class Engine:
    def getconn(self):
        raise NotImplemented()

    def putconn(self, conn):
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


class QuerySet:
    pass
        

class DBSession:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.conn = self.engine.getconn()
    
    def __del__(self):
        self.engine.putconn(self.conn)
    
    def get_raw_conn(self):
        return self.conn
    
    def select(model, *cond) -> QuerySet:
        pass
    
    def insert(self, *cond):
        pass

    def update(self, *cond):
        pass

    def delete(self, *cond):
        pass

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

