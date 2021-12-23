from orm.model import Model
from orm.field import *

class Tag(Model):
    __tablename__ = 'tag'
    tname = CharField(20, max_length=20, primary_key=True)
    hot_value = IntegerField()

class ForumUser(Model):
    __tablename__ = 'forum_user'
    uid = AutoField(primary_key=True)
    uname = CharField(null=False)
    profile = BlobField()
    email = CharField()
    gender = EnumField()
    password = CharField(null=False)
    signature = CharField()