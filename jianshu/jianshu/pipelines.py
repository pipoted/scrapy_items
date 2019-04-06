# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class JianshuPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.conn['scrapy_items']
        self.col = self.db['jianshu_test']

    def process_item(self, item, spider):
        document = {
            'title': item['title'],
            'pub_time': item['pub_time'],
            'word_age': item['word_age'],
            'view_count': item['view_count'],
            'comment_count': item['comment_count'],
            'like_count': item['like_count'],
            'url': item['url'],
        }
        self.col.insert_one(document)
        return item

    def __del__(self):
        self.conn.close()
        pass
