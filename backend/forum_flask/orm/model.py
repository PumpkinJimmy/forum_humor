from .error import ORMError
from . import field
from .field import Field
from copy import copy
class ModelMetaClass(type):
    '''
    Meta class for Model

    Mainly works to generate meta info from model definition
    '''
    def __new__(cls, cls_name, cls_bases, cls_attrs):
        # collect fields and setup descriptors
        pk = []
        fields = []
        default = {}
        for attr_name, attr in cls_attrs.items():
            if issubclass(type(attr), Field):
                attr.name = attr_name
                fields.append(attr_name)
                if attr.primary_key:
                    pk.append(attr_name)
                if hasattr(attr, 'default'):
                    default[attr_name] = attr.default
        cls_attrs['__fields__'] = tuple(fields)
        cls_attrs['__default__'] = default

        # handle primary key
        if cls_name != 'Model' and not pk:
            raise ORMError('No primary key specified.')
        cls_attrs['__pk__'] = tuple(pk)

        # set table name
        cls_attrs.setdefault('__tablename__', cls_name)

        return super().__new__(cls, cls_name, cls_bases, cls_attrs)

class Model(metaclass=ModelMetaClass):
    @classmethod
    def get_field(cls, field_name):
        return getattr(cls, field_name)
    
    @classmethod
    def from_tuple(cls, row):
        '''
        Factory method

        build object from tuple row
        '''
        return cls(dict(zip(cls.__fields__, row)))
    
    @classmethod
    def get_key_fmtstr(cls) -> str:
        return ','.join(map(lambda pk: f'{pk}={cls.get_field(pk).get_fmt()}', cls.__pk__))

    def __init__(self, data, **kwargs):
        '''
        Basic Initialization

        More builds see factory methods
        '''
        self._data = self.__default__.copy()
        self._data.update(data)
    
    def get_data(self) -> dict:
        return self._data
    
    def get_key(self) -> dict:
        return dict(filter(lambda p: p[0] in self.__pk__, self._data.items()))
    
    def get_keyval(self) -> tuple:
        return tuple(self.get_key().values())
    
    
    
    def to_json(self) -> dict:
        return self._data
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: {self.get_data()}>'