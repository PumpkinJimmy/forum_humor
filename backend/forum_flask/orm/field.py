
from .error import ORMError
class Field:
    __fieldtype__ = 'unknown'

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', self.__class__.__name__)
        self.allow_null = kwargs.get('null', True)
        if self.allow_null == False \
            and 'default' in kwargs \
                and kwargs['default'] is None:
            raise ORMError('null not allowed')
        self.default = kwargs.get('default', None)
        self.primary_key = kwargs.get('primary_key', False) 
        self.label = kwargs.get('label', '')

    def __get__(self, instance, owner):
        if instance is not None:
            instance._data[self.name]
        else:
            return self
    
    def __set__(self, instance, value):
        instance._data[self.name] = value
    
    def get_info(self):
        res = {
            'type': self.__fieldtype__,
            'label': getattr(self, 'label', self.name)
        }
        if hasattr(self, 'default'):
            res['default'] = self.default
        return res

    @classmethod
    def get_fmt(self):
        return '%s'

    
    

class CharField(Field):
    __fieldtype__ = 'char'

class IntegerField(Field):
    __fieldtype__ = 'integer'
    @classmethod
    def get_fmt(self):
        return '%s'

class AutoField(Field):
    __fieldtype__ = 'auto'

class BlobField(Field):
    __fieldtype__ = 'blob'

class EnumField(Field):
    __fieldtype__ = 'enum'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.options = kwargs.get('options', ())
    def get_info(self):
        res = super().get_info()
        res['options'] = self.options
        return res

class DatetimeField(Field):
    __fieldtype__ = 'datetime'
    @classmethod
    def get_fmt(lcs):
        return 'to_timestamp(%s)'

class ForeignField(Field):
    __fieldtype__ = 'foreign'

class ManyToManyField(Field):
    __fieldtype__ = 'many_to_many'


class ImageField(BlobField):
    __fieldtype__ = 'image'

class EmailField(CharField):
    __fieldtype__ = 'email'

class PasswordField(CharField):
    __fieldtype__ = 'password'

class TextField(Field):
    __fieldtype__ = 'text'