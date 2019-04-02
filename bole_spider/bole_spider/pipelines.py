# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BoleSpiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='xzx199110',
            database='scrapy',
            port=3306,
        )
        self.cursor = self.conn.cursor()
        sql = """
        create table if not exists scrapy_test (
          id   int primary key not null auto_increment,
          name varchar(255)    not null,
          url  varchar(255)    not null
        )        """
        self.cursor.execute(sql)
        self.conn.commit()

    def process_item(self, item, spider):
        sql = """
           insert into scrapy_test (name, url) values (%s, %s)
        """
        self.cursor.execute(sql, (item['artical_name'], item['artical_url']))
        self.conn.commit()
        return item

    def __del__(self):
        self.conn.close()
