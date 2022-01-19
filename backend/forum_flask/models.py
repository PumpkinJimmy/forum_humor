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
    # tag_user = ManyToMany(Tag, label="Tags")

class ForumGroup(Model):
    gid = AutoField(primary_key=True, label="GID")
    gname = CharField(null=False,label='Group Name')
    admin_uid = ForeignField(ForeignField, label="Admin ID")
    # group_member = ManyToMany(ForumUser, label="Group Member")

class Post(Model):
    __tablename__ = 'post'
    pid = AutoField(primary_key=True,label="PID")
    hot_value = IntegerField(label="Hot Value")
    title = CharField(label="Title")
    content = TextField(label="Content")
    post_time = DatetimeField(label="Post Time")
    last_modified_time = DatetimeField(label="Last Modified")
    poster_uid = ForeignField(ForumUser, label="Poster UID")
    # tag_post = ManyToMany(Tag, label="Tags")

class Message(Model):
    __tablename__ = 'message'
    mid = AutoField(primary_key=True,label="MID")
    time_stamp = DatetimeField(label="Timestamp")
    from_uid = ForeignField(ForumUser,label="From UID")
    to_uid = ForeignField(ForumUser,label="To UID")
    content = TextField(label="Content")

class Comment(Model):
    __tablename__ = 'comment'
    cid = AutoField(primary_key=True,label="CID")
    ctime = DatetimeField(label="Comment Time")
    like_num = IntegerField(label="Like Number")
    content = TextField(label="Content")
    commenter_uid = ForeignField(ForumUser, label="Commenter ID")
    from_pid = ForeignField(Post, label="Reply Post ID")

class Tag(Model):
    __tablename__ = 'tag'
    tname = CharField(primary_key=True,label="Tag Name")
    hot_value = IntegerField(label="Hot Value")

class TagLog(Model):
    __tablename__ = 'tag_log'
    tname = CharField(Tag,primary_key=True)
    uid = ForeignField(ForumUser,primary_key=True)
    access_time = DatetimeField(primary_key=True)

class TagPost(Model):
    __tablename__ = 'tag_post'
    tname = ForeignField(Tag,primary_key=True)
    pid = ForeignField(Post,primary_key=True)

class TagUser(Model):
    __tablename__ = 'tag_user'
    tname = ForeignField(Tag,primary_key=True)
    uid = ForeignField(ForumUser,primary_key=True)

class TagLog(Model):
    __tablename__ = 'tag_log'
    tname = ForeignField(Tag, primary_key=True)
    uid = ForeignField(ForumUser, primary_key=True)
    access_time = DatetimeField(primary_key=True)