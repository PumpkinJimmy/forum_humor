from orm.model import Model
from orm.field import *

class ForumUser(Model):
    __tablename__ = 'forum_user'
    uid = AutoField(primary_key=True)
    uname = CharField(null=False)
    profile = ImageField()
    email = EmailField()
    gender = EnumField()
    password = PasswordField(null=False)
    signature = CharField()

class Post(Model):
    __tablename__ = 'post'
    pid = AutoField(primary_key=True)
    hot_value = IntegerField()
    title = CharField()
    content = CharField()
    post_time = DatetimeField()
    last_modified_time = DatetimeField()
    poster_uid = ForeignField(ForumUser)

class Message(Model):
    __tablename__ = 'message'
    mid = AutoField(primary_key=True)
    time_stamp = DatetimeField()
    from_uid = ForeignField(ForumUser)
    to_uid = ForeignField(ForumUser)
    content = CharField()

