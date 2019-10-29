#!/usr/bin/python 
# -*- coding: UTF-8 -*- 

import MySQLdb as mysql
import sys

class get_image():
    def __init__(self):
        insert_db(self)
        select_img(self)
# mysql连接
conn = mysql.connect(host='localhost', user='root', passwd='123456', db='test db')

def insert_db(self):
    try:
        # 读取图片文件
        fp = open(r"G:\Downloan Image\00bz.png",errors='ignore')
        img = fp.read()
        fp.close()
    except IOError as e:
        print(
        "Error %d %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    try:

        cursor = conn.cursor()
        # 注意使用Binary()函数来指定存储的是二进制
        cursor.execute("INSERT INTO images (DATA) VALUES (%s)"%img)
        # 如果数据库没有设置自动提交，这里要提交一下
        conn.commit()
        cursor.close()
        # 关闭数据库连接
        conn.close()
    except mysql.Error as e:
        print(
        "Error %d %s" % (e.args[0], e.args[1]))
        sys.exit(1)

def select_img(self):
    cursor = conn.cursor()
    cursor.execute("select * from images where a.inageid = 6")
    cursor.fetchall()
    cursor.close()

if __name__ == '__main__':
    get_image()