from . import engine
class QuerySet:
    pass
        

class DBSession:
    def __init__(self, engine: engine.Engine):
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