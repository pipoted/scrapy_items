# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentJobReItem(scrapy.Item):
    name = scrapy.Field()
    types = scrapy.Field()
    nums = scrapy.Field()
    city = scrapy.Field()
    pass
