# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    title = scrapy.Field()
    pub_time = scrapy.Field()
    word_age = scrapy.Field()
    view_count = scrapy.Field()
    comment_count = scrapy.Field()
    like_count = scrapy.Field()
    url = scrapy.Field()
    pass
