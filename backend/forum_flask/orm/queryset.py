from typing import List, Dict, Tuple

from .error import ORMError
from .model import Model

class Query:
    'FIXME: count/orderby等函数是inplace操作,不符合通常的语义'


    def __init__(self, engine, query, model):
        self.__data = []
        self.engine = engine
        self.query = query
        self.query_applied = False
        self.model = model
    
    def filter(self,**kwargs):
        raise NotImplemented()
    
    def count(self):
        if self.qs is None:
            raise ORMError('QuerySet count: No query')
        self.query_applied = False
        self.query['agg'] = 'count'
        return self
    
    def orderby(self, col, desc=False):
        if self.qs is None:
            raise ORMError('QuerySet orderby: No query')
        self.query_applied = False
        self.query['orderby'] = col
        self.query['orderby_desc'] = desc
        return self
    
    def paginate(self, offset=0, limit=None):
        if self.qs is None:
            raise ORMError('QuerySet paginate: No query')
        self.query['limit'] = limit
        self.query['offset'] = offset
        return self
        
    def one(self) -> Model:
        if self.query_applied:
            return self.__data[0]
        else:
            raise NotImplemented()
    
    def all(self) -> List[Model]:
        if self.query_applied:
            return self.__data
        else:
            conn = self.engine.getconn()
            curs = conn.cursor()
            statement, value = self.engine.query2sql(self.query)
            curs.execute(statement, *value)
            self.__data = curs.fetchall()
            self.engine.putconn(conn)
            self.query_applied = True
            if self.query.get('agg'):
                return self.__data[0][0]
            else:
                return list(map(self.model.from_tuple, self.__data))

    
    def to_json(self):
        return list(map(lambda t: self.model.from_tuple(t).to_json(), self.all()))
    
    