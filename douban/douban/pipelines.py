# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class DoubanPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.conn['scrapy_items']
        self.col = self.db['douban_movie_test']

    def process_item(self, item, spider):
        document = {
            'name': item['name'],
            'dire': item['dire'],
            'writer': item['writer'],
            'actor': item['actor'],
            'types': item['types'],
            'area': item['area'],
            'date': item['date'],
            'desc': item['desc'],
            'score': item['score'],
        }
        self.col.insert_one(document)
        return item

    def __del__(self):
        self.conn.close()
        pass
