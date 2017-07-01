#!/usr/bin/env python
# coding=utf-8
# Filename: Select.py
# Created by iFantastic on 2017/6/24
# Description: MySQL的测试操作

import MySQLdb

conn = MySQLdb.Connect(host='localhost', port=3306, user='root', passwd='', db='immoc', charset='utf8')

cursor = conn.cursor()

sql = 'select * from user'
cursor.execute(sql)

print cursor.rowcount

print cursor.fetchone()
print cursor.fetchmany(2)
print cursor.fetchall()

cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print 'userid=%d, username=%s' % row

cursor.close()
conn.close()