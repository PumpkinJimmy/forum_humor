copy forum_user from 'ForumUser.csv' with csv headers;
copy post from 'Post.csv' with csv headers;
copy message from 'Message.csv' with csv headers;

/* -- for train_db_post.csv
copy post(content, pid, hot_value, title, poster_uid, post_time, last_modified_time) 
from '/home/omm/project/train_post.csv' 
with csv header;
* /