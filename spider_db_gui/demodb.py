#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:44:04 2018

@author: ailike
"""

from mysql import connector as mysqlconn
conn = mysqlconn.connect(host='127.0.0.1', user='root', password='madeakua', database='demo_db', use_unicode=True)
cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['4', 'Jim'])
print(cursor.rowcount)
conn.commit()
cursor.close()
##
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('3',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

