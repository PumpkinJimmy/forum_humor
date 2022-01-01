from .model import Model
from .engine import Engine
from typing import List, Dict, Tuple
from .queryset import Query
        

class DBSession:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.conn = self.engine.getconn()
    
    def __del__(self):
        self.conn.commit()
        self.engine.putconn(self.conn)
    
    def get_raw_conn(self):
        return self.conn
    
    def select(self, *args, **kwargs):
        return self.engine.select(self.conn, *args, **kwargs)
            
    
    def insert(self, *args, **kwargs):
        return self.engine.insert(self.conn, *args, **kwargs)

    def update(self, *args, **kwargs):
        return self.engine.update(self.conn, *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.engine.delete(self.conn, *args, **kwargs)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()