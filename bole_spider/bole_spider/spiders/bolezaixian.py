# -*- coding: utf-8 -*-
import scrapy
from bole_spider.items import BoleArticalItem


class BolezaixianSpider(scrapy.Spider):
    name = 'bolezaixian'
    allowed_domains = ['blog.jobble.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/{page}/'.format(page=page) for page in range(1, 500)]

    def parse(self, response):
        divs = response.xpath('//div[@class="post floated-thumb"]')
        data_dict = BoleArticalItem()
        for div in divs:
            data_dict['artical_name'] = div.xpath('.//p/a/@title').extract()[0]
            data_dict['artical_url'] = div.xpath('.//p/a/@href').extract()[0]

            yield data_dict
