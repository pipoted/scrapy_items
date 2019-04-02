# -*- coding: utf-8 -*-
import scrapy
from bole_spider.items import BoleArticalItem


class BolezaixianSpider(scrapy.Spider):
    name = 'bolezaixian'
    allowed_domains = ['blog.jobble.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']

    def parse(self, response):
        divs = response.xpath('//div[@class="post floated-thumb"]')
        data_dict = BoleArticalItem()
        for div in divs:
            data_dict['artical_name'] = div.xpath('.//p/a/@title').extract()[0]
            data_dict['artical_url'] = div.xpath('.//p/a/@href').extract()[0]

            yield data_dict

        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]
        if next_url:
            yield scrapy.Request(next_url, self.parse)
