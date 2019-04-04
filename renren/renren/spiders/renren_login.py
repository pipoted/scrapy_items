# -*- coding: utf-8 -*-
import scrapy


class RenrenLoginSpider(scrapy.Spider):
    name = 'renren_login'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response, formdata={
            'email': '15570136250',
            'password': 'xzx199110',
        }, callback=self.parse_page)

    def parse_page(self, response):
        url = 'http://www.renren.com/968662672'
        yield scrapy.Request(url, callback=self.parse_home_page)

    def parse_home_page(self, response):
        with open('home.html', 'w') as fp:
            fp.write(response.body)
