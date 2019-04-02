# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TencentJobPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            user='root',
            port=3306,
            password='xzx199110',
            database='scrapy',
        )
        self.cursor = self.conn.cursor()
        sql = '''
        create table if not exists tencent_test (
        id int primary key not null auto_increment,
        name varchar(255) not null,
        types varchar(255) not null,
        nums varchar(255) not null,
        city varchar(255) not null
        )
        '''
        self.cursor.execute(sql)
        self.conn.commit()

    def process_item(self, item, spider):
        sql = '''
        insert into tencent_test (name, types, nums, city) values (%s, %s, %s, %s)
        '''
        self.cursor.execute(sql, (item['name'], item['types'], item['nums'], item['city']))
        self.conn.commit()
        return item

    def __del(self):
        self.conn.close()
