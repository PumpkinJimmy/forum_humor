import numpy as np
import pandas as pd
import random
import string
import time
import datetime

G = ['M', 'F']
startuid, enduid = 1, 10000
startgid, endgid = 1, 10000
GroupSizemin, GroupSizemax = 25, 100
# start_time, end_time = datetime.datetime.now() + datetime.timedelta(days = -100), datetime.datetime.now()
start_time, end_time = datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days = 100)
MessageNum = 100000
startpid, endpid = 1, 10000
startcid, endcid = 1, 100000

def rand_str(num):
    alphabet = string.ascii_letters + string.digits
    characters = random.sample(alphabet, num)
    return ''.join(characters)

def rand_date():
    a1 = tuple(start_time.timetuple()[0:9])    #设置开始日期时间元组
    a2 = tuple(end_time.timetuple()[0:9])   #设置结束日期时间元组
    start = time.mktime(a1)    #生成开始时间戳
    end = time.mktime(a2)      #生成结束时间戳
    t = random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)          #将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d %H:%M:%S",date_touple)   #将时间元组转成格式化字符串（2020-04-11 16:33:21）
    return date


def rand_ForumUser():
    with open('random_Data\\ForumUser.csv', 'w+', encoding='utf-8') as f:
        f.write('uid,uname,profile,email,gender,password,signature\n')
        for uid in range(startuid, enduid):
            uname = rand_str(random.randint(1, 20))
            email = rand_str(10) + "@123.com"
            gender = G[random.randint(0, 1)]
            password = rand_str(random.randint(8, 20))
            f.write(str(uid) + ',' + uname + ',' + ',' + email + ',' + gender + ',' + password + ',' + '\n')


def rand_ForumGroup():
    with open('random_Data\\ForumGroupLeader.csv', 'w+', encoding='utf-8') as fL:
        with open('random_Data\\ForumGroupMember.csv', 'w+', encoding='utf-8') as fM:
            fL.write('gid,admin_uid\n')
            fM.write('gid,member_uid\n')
            for gid in range(startgid, endgid):
                admin_uid = random.randint(startuid, enduid)
                fL.write(str(gid) + ',' + str(admin_uid) + '\n')
                for counter in range(random.randint(GroupSizemin, GroupSizemax)):
                    member_uid = random.randint(startuid, enduid)
                    while member_uid == admin_uid:
                        member_uid = random.randint(startuid, enduid)
                    fM.write(str(gid) + ',' + str(member_uid) + '\n')


def rand_Message():
    with open('random_Data\\Message.csv', 'w+', encoding='utf-8') as f:
        f.write('time_stamp,from_uid,to_uid,content\n')
        for counter in range(MessageNum):
            time_stamp = rand_date()
            from_uid = random.randint(startuid, enduid)
            to_uid = random.randint(startuid, enduid)
            f.write(time_stamp + ',' + str(from_uid) + ',' + str(to_uid) + ',' + '\n')


def rand_Post():
    with open('random_Data\\Post.csv', 'w+', encoding='utf-8') as f:
        f.write('pid,hot_value,title,content,post_time,last_modified_time,poster_uid\n')
        for pid in range(startpid, endpid):
            hot_value = random.randint(1, 2147483647)
            post_time = last_modified_time = rand_date()
            poster_uid = random.randint(startuid, enduid)
            f.write(str(pid) + ',' + str(hot_value) + ',' + ',' + ',' + post_time + ',' + last_modified_time + ',' + str(poster_uid) + '\n')


def rand_Comment():
    with open('random_Data\\Comment.csv', 'w+', encoding='utf-8') as f:
        f.write('cid,ctime,like_num,content,commenter_uid,from_pid\n')
        for cid in range(startcid, endcid):
            ctime = rand_date()
            like_num = random.randint(1, 2147483647)
            commenter_uid = random.randint(startuid, enduid)
            from_pid = random.randint(startpid, endpid)
            f.write(str(cid) + ',' + ctime + ',' + str(like_num) + ',' + ',' + str(commenter_uid) + ',' + str(from_pid) + '\n')


if __name__ == "__main__":
    # rand_ForumUser()
    # rand_ForumGroup()
    # rand_Message()
    # rand_Post()
    # rand_Comment()