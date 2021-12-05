from .field import Field
class ModelMetaClass(type):
    def __new__(cls, cls_name, cls_bases, cls_attrs):
        # collect fields
        cls_attrs['__fields__'] = []
        for attr_name, attr in cls_attrs.items():
            if issubclass(type(attr), Field):
                cls_attrs['__fields__'].append(attr_name)

        # set table name
        cls_attrs.setdefault('__tablename__', cls_name)

        return super().__new__(cls, cls_name, cls_bases, cls_attrs)

class Model(metaclass=ModelMetaClass):
    @classmethod
    def get_field(cls, field_name):
        return getattr(cls, field_name)