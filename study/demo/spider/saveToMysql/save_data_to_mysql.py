#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-08 20:42
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : save_data_to_mysql.py
# @IDE     : PyCharm
import pymysql

# 创建数据库
# db = pymysql.connect(host='127.0.0.1', user="root", password='9e2895fbe0df1d74', port=3306)
# cursor = db.cursor()
# print(cursor.execute('SELECT VERSION()'))
# data = cursor.fetchone()
# print('DataBase Version:', data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4')
# db.close()

# 创建数据表
# db = pymysql.connect(host='127.0.0.1', user="root", password='9e2895fbe0df1d74', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL , name VARCHAR(255) NOT NULL , age int NOT NULL , PRIMARY KEY (id))'
# data = cursor.execute(sql)
# db.close()

# 插入数据
db = pymysql.connect(host='127.0.0.1', user="root", password='9e2895fbe0df1d74', port=3306, db='spiders')
cursor = db.cursor()

user_id = '10002'
user_name = 'admin2'
user_age = 22

sql = 'INSERT INTO students (id , name, age ) values (%s,%s,%s)'

try:
    cursor.execute(sql, (user_id, user_name, user_age))
    db.commit()
except RuntimeError:
    db.rollback()

db.close()
