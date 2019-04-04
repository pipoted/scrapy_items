# -*- coding: utf-8 -*-
import scrapy


class CsdnCookiesSpider(scrapy.Spider):
    name = 'csdn_cookies'
    allowed_domains = ['www.csdn.net']
    start_urls = ['http://www.csdn.net/']

    def parse(self, response):
        pass
