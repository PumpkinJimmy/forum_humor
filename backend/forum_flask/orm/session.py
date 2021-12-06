from .model import Model
from .engine import Engine
from typing import List, Dict, Tuple
from .queryset import QuerySet
        

class DBSession:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.conn = self.engine.getconn()
    
    def __del__(self):
        self.engine.putconn(self.conn)
    
    def get_raw_conn(self):
        return self.conn
    
    def select(self, model: Model, *args, **kwargs) -> QuerySet:
        return self.engine.select(self.conn, model, *args, **kwargs)
            
    
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