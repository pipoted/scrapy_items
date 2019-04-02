# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class TencentJobPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(host='localhost', port='27017')
        self.db = self.conn['scrapy']
        self.col = self.db['tencent_test']

    def process_item(self, item, spider):
        data_dict = {
            'nama': item['name'],
            'types': item['types'],
            'nums': item['nums'],
            'city': item['city'],
        }
        self.col.insert_one(data_dict)
        return item

    def __del(self):
        self.conn.close()
