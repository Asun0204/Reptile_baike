#!/usr/bin/env python
# coding=utf-8
# Filename: test_update.py
# Created by iFantastic on 2017/6/24
# Description:

import MySQLdb

conn = MySQLdb.Connect(host='localhost', port=3306, user='root', passwd='', db='immoc', charset='utf8')
cursor = conn.cursor()
sql_insert = "insert into user(userid, username) values(10, 'name10')"
sql_update = "update user set username='name9' WHERE userid=9"
sql_delete = "delete FROM USER WHERE userid<3"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount

    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()