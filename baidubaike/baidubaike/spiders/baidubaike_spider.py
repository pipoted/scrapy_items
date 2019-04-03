# -*- coding: utf-8 -*-
import scrapy


class BaidubaikeSpiderSpider(scrapy.Spider):
    name = 'baidubaike_spider'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['http://baike.baidu.com/']

    def parse(self, response):
        pass
