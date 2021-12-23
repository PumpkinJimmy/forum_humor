CREATE INDEX ForumUser_email_index ON ForumUser (email);
CREATE INDEX ForumUser_gender_index ON ForumUser (gender);

CREATE INDEX ForumGroup_admin_uid_index ON ForumGroup (admin_uid);

CREATE INDEX Post_hot_value_index ON Post (hot_value);
CREATE INDEX Post_title_index ON Post (title);
CREATE INDEX Post_post_time_index ON Post (post_time);
CREATE INDEX Post_poster_uid_index ON Post (poster_uid);

CREATE INDEX Comment_ctime_index ON Comment (ctime);
CREATE INDEX Comment_like_num_index ON Comment (like_num);
CREATE INDEX Comment_commenter_uid_index ON Comment (commenter_uid);
CREATE INDEX Comment_from_pid_index ON Comment (from_pid);

CREATE INDEX Tag_hot_value_index ON Tag (hot_value);

CREATE OR REPLACE FUNCTION tri_insertTU_func() RETURNS TRIGGER AS 
$$ 
DECLARE 
BEGIN
        INSERT INTO Tag_log VALUES(NEW.tname, NEW.uid, now());
        RETURN NEW; 
END
$$ LANGUAGE PLPGSQL;

CREATE OR REPLACE FUNCTION tri_insertTP_func() RETURNS TRIGGER AS 
$$ 
DECLARE 
BEGIN
        INSERT INTO Tag_log
                select NEW.tname, poster_uid, now()
                from Post
                where NEW.pid = pid;
        RETURN NEW;
END
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER InsertTU
AFTER INSERT OR UPDATE ON TagofUser
FOR EACH ROW
EXECUTE PROCEDURE tri_insertTU_func();

CREATE TRIGGER InsertTP
AFTER INSERT OR UPDATE ON TagofPost
FOR EACH ROW
EXECUTE PROCEDURE tri_insertTP_func();