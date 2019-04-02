# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis


class TencentJobPipeline(object):
    def __init__(self):
        self.conn = redis.Redis(password='xzx199110')
        pass

    def process_item(self, item, spider):
        self.conn.set(item['name'], {
            'name': item['name'],
            'types': item['types'],
            'nums': item['nums'],
            'city': item['city'],
        })
        return item

    def __del(self):
        pass
