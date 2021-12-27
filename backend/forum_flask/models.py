from orm.model import Model
from orm.field import *

class ForumUser(Model):
    __tablename__ = 'forum_user'
    uid = AutoField(primary_key=True,label="UID")
    uname = CharField(null=False, label="User Name")
    profile = ImageField(label="Profile")
    email = EmailField(label="Email")
    gender = EnumField(label="Gender", options=('M', 'F'))
    password = PasswordField(null=False,label="Password")
    signature = CharField(label="Signature")

class Post(Model):
    __tablename__ = 'post'
    pid = AutoField(primary_key=True,label="PID")
    hot_value = IntegerField(label="Hot Value")
    title = CharField(label="Title")
    content = CharField(label="Content")
    post_time = DatetimeField(label="Post Time")
    last_modified_time = DatetimeField(label="Last Modified")
    poster_uid = ForeignField(ForumUser, label="Poster UID")

class Message(Model):
    __tablename__ = 'message'
    mid = AutoField(primary_key=True,label="MID")
    time_stamp = DatetimeField(label="Timestamp")
    from_uid = ForeignField(ForumUser,label="From UID")
    to_uid = ForeignField(ForumUser,label="To UID")
    content = CharField(label="Content")

