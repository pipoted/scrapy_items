# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    name = scrapy.Field()
    dire = scrapy.Field()
    writer = scrapy.Field()
    actor = scrapy.Field()
    types = scrapy.Field()
    area = scrapy.Field()
    lan = scrapy.Field()
    date = scrapy.Field()
    len = scrapy.Field()
    desc = scrapy.Field()
    score = scrapy.Field()
    pass
