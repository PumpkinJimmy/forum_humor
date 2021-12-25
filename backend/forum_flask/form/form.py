from orm.field import Field
from orm.model import Model
from .field import FormField

class FormMetaClass(type):
    def __new__(cls, cls_name, cls_bases, cls_attrs):
        model = cls_attrs['model']
        pk = model.__pk__
        fields = model.__fields__
        default = model.__default__
        form_fields = {}
        for fn in fields:
            f = model.get_field(fn)
            form_fields[f.name] = f.__fieldtype__
        for attr_name, attr in cls_attrs.items():
            if issubclass(type(attr), FormField):
                attr.name = attr_name
                form_fields[attr_name] = attr.__fieldtype__
        cls_attrs['__fields__'] = form_fields
        cls_attrs['__default__'] = default
        cls_attrs['__pk__'] = pk

        form_class = super().__new__(cls, cls_name, cls_bases, cls_attrs)
        model.__form__ = form_class

        return form_class
        

class Form(metaclass=FormMetaClass):
    model = Model
    @classmethod
    def get_form(cls):
        return {
            'fields': cls.__fields__,
            'pk': cls.__pk__,
            'default': cls.__default__
        }