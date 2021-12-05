import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from .error import ORMError

class Engine:
    pass

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