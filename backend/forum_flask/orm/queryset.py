from typing import List, Dict, Tuple
from .model import Model

class QuerySet:
    def __init__(self, *args, **kwargs):
        self.__data = list(*args, **kwargs)
        
    def one(self) -> Model:
        return self.__data[0]
    
    def all(self) -> List[Model]:
        return self.__data
    
    def to_json(self):
        return list(map(lambda m: m.to_json(), self.all()))