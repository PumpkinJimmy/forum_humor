from orm.model import Model
from orm.field import *

class Tag(Model):
    __tablename__ = 'tag'
    tname = CharField(20, max_length=20, primary_key=True)
    hot_value = IntegerField()
