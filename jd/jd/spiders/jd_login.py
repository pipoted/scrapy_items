# -*- coding: utf-8 -*-
import scrapy


class JdLoginSpider(scrapy.Spider):
    name = 'jd_login'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        pass
