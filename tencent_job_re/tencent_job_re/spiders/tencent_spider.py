# -*- coding: utf-8 -*-
import scrapy


class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent_spider'
    allowed_domains = ['job.tencent.com']
    start_urls = ['http://job.tencent.com/']

    def parse(self, response):
        pass
