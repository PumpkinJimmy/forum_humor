CREATE TABLE ForumUser
(
        uid CHAR(20) PRIMARY KEY,
        uname VARCHAR(20) NOT NULL,
        profile BLOB,
        email CHAR(20),
        gender CHAR(1) CHECK(gender='M' OR gender= 'F'),
        password VARCHAR(20) NOT NULL,
        signature VARCHAR(50)
);

CREATE TABLE ForumGroupLeader
(
        gid CHAR(20) PRIMARY KEY,
        admin_uid CHAR(20),
        constraint G_auid_FU foreign key(admin_uid) references ForumUser(uid)
);

CREATE TABLE ForumGroupMember
(
        gid CHAR(20) PRIMARY KEY,
        member_uid CHAR(20),
        constraint G_muid_FU foreign key(member_uid) references ForumUser(uid)
);

CREATE TABLE Message
(
        time_stamp DATE NOT NULL,
        from_uid CHAR(20) NOT NULL,
        to_uid CHAR(20) NOT NULL,
        content VARCHAR(200),
        PRIMARY KEY (time_stamp, from_uid, to_uid),
        constraint M_fuid_FU foreign key(from_uid) references ForumUser(uid),
        constraint M_tuid_FU foreign key(to_uid) references ForumUser(uid)
);

CREATE TABLE Post
(
        pid CHAR(20) PRIMARY KEY,
        hot_value INTEGER CHECK(hot_value>0),
        title VARCHAR(20),
        content VARCHAR(200),
        post_time DATE,
        last_modified_time DATE,
        poster_uid CHAR(20),
        constraint P_puid_FU foreign key(poster_uid) references ForumUser(uid)
);

CREATE TABLE Comment
(
        cid CHAR(20) PRIMARY KEY,
        ctime DATE,
        like_num INTEGER,
        content VARCHAR(200),
        commenter_uid CHAR(20),
        from_pid CHAR(20),
        constraint C_cuid_FU foreign key(commenter_uid) references ForumUser(uid),
        constraint C_fpid_P foreign key(from_pid) references Post(pid)
);

CREATE TABLE Tag
(
        tname VARCHAR(20) PRIMARY KEY,
        hot_value INTEGER CHECK(hot_value>0)
);

CREATE TABLE TagofPost
(
        tname VARCHAR(20) NOT NULL,
        pid CHAR(20) NOT NULL,
        PRIMARY KEY (tname, pid),
        constraint TP_tname_T foreign key(tname) references Tag(tname),
        constraint TP_pid_P foreign key(pid) references Post(pid)
);

CREATE TABLE TagofUser
(
        tname VARCHAR(20) NOT NULL,
        uid CHAR(20) NOT NULL,
        PRIMARY KEY (tname, uid),
        constraint TU_tname_T foreign key(tname) references Tag(tname),
        constraint TU_uid_FU foreign key(uid) references ForumUser(uid)
);

CREATE TABLE Tag_log
(
        tname VARCHAR(20) NOT NULL,
        uid CHAR(20) NOT NULL,
        access_time DATE NOT NULL,
        PRIMARY KEY (tname, uid, access_time),
        constraint Tl_tname_T foreign key(tname) references Tag(tname),
        constraint Tl_uid_FU foreign key(uid) references ForumUser(uid)
);