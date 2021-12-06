
from .error import ORMError
class Field:

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', self.__class__.__name__)
        self.allow_null = kwargs.get('null', True)
        if 'default' in kwargs:
            self.default = kwargs['default']
            if self.allow_null == False and self.default is None:
                raise ORMError('null not allowed')
        self.primary_key = kwargs.get('primary_key', False) 

    def __get__(self, instance, owner):
        if instance is not None:
            instance._data[self.name]
        else:
            return self
    
    def __set__(self, instance, value):
        instance._data[self.name] = value

    @classmethod
    def get_fmt(self):
        return '%s'
    

class CharField(Field):
    pass

class IntegerField(Field):
    @classmethod
    def get_fmt(self):
        return '%s'

class AutoField(Field):
    pass