CREATE TABLE forum_user
(
        uid serial PRIMARY KEY,
        uname VARCHAR(20) NOT NULL,
        profile BLOB,
        email CHAR(20),
        gender CHAR(1) CHECK(gender='M' OR gender= 'F'),
        password VARCHAR(20) NOT NULL,
        signature VARCHAR(50)
);

CREATE TABLE forum_group
(
        gid serial PRIMARY KEY,
        gname VARCHAR(20) NOT NULL,
        admin_uid CHAR(20) not null,
        constraint G_auid_FU foreign key(admin_uid) references forum_user(uid)
);

CREATE TABLE group_member
(
        gid CHAR(20),
        member_uid CHAR(20),
        constraint PK_FGM primary key(gid, member_uid),
        constraint G_muid_FU foreign key(member_uid) references forum_user(uid),
        constraint G_gid_FG foreign key(gid) references forum_group(gid)
);

CREATE TABLE message
(
        mid serial PRIMARY KEY,
        time_stamp TIMESTAMP NOT NULL,
        from_uid CHAR(20) NOT NULL,
        to_uid CHAR(20) NOT NULL,
        content VARCHAR(200),
        constraint M_fuid_FU foreign key(from_uid) references forum_user(uid),
        constraint M_tuid_FU foreign key(to_uid) references forum_user(uid)
);

CREATE TABLE post
(
        pid serial PRIMARY KEY,
        hot_value INTEGER CHECK(hot_value>0),
        title VARCHAR(20),
        content VARCHAR(200),
        post_time DATE,
        last_modified_time DATE,
        poster_uid CHAR(20),
        constraint P_puid_FU foreign key(poster_uid) references forum_user(uid)
);

CREATE TABLE comment
(
        cid serial PRIMARY KEY,
        ctime DATE,
        like_num INTEGER,
        content VARCHAR(200),
        commenter_uid CHAR(20),
        from_pid CHAR(20) not null,
        constraint C_cuid_FU foreign key(commenter_uid) references forum_user(uid),
        constraint C_fpid_P foreign key(from_pid) references post(pid)
);

CREATE TABLE tag
(
        tname VARCHAR(20) PRIMARY KEY,
        hot_value INTEGER CHECK(hot_value>0) default 0
);

CREATE TABLE tag_post
(
        tname VARCHAR(20) NOT NULL,
        pid CHAR(20) NOT NULL,
        PRIMARY KEY (tname, pid),
        constraint TP_tname_T foreign key(tname) references tag(tname),
        constraint TP_pid_P foreign key(pid) references post(pid)
);

CREATE TABLE tag_user
(
        tname VARCHAR(20) NOT NULL,
        uid CHAR(20) NOT NULL,
        PRIMARY KEY (tname, uid),
        constraint TU_tname_T foreign key(tname) references Tag(tname),
        constraint TU_uid_FU foreign key(uid) references forum_user(uid)
);

CREATE TABLE tag_log
(
        tname VARCHAR(20) NOT NULL,
        uid CHAR(20) NOT NULL,
        access_time DATE NOT NULL,
        PRIMARY KEY (tname, uid, access_time),
        constraint Tl_tname_T foreign key(tname) references tag(tname),
        constraint Tl_uid_FU foreign key(uid) references forum_user(uid)
);