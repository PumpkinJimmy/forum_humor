from orm.model import Model
from orm.field import *

class Tag(Model):
    __tablename__ = 'tag'
    tname = CharField(20, max_length=20, primary_key=True)
    hot_value = IntegerField()

class ForumUser(Model):
    __tablename__ = 'forum_user'
    uid = IntegerField(primary_key=True)
    uname = CharField()
    email = CharField()
    gender = CharField()
    password = CharField(null=False)
    signature = CharField()