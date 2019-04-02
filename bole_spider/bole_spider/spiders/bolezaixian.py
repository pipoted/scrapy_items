# -*- coding: utf-8 -*-
import scrapy
from bole_spider.items import BoleArticalItem


class BolezaixianSpider(scrapy.Spider):
    name = 'bolezaixian'
    page = 1
    allowed_domains = ['blog.jobble.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']

    def parse(self, response):
        divs = response.xpath('//div[@class="post floated-thumb"]')
        data_dict = BoleArticalItem()
        for div in divs:
            data_dict['artical_name'] = div.xpath('.//p/a/@title').extract()[0]
            data_dict['artical_url'] = div.xpath('.//p/a/@href').extract()[0]

            yield data_dict

        if self.page < 564:
            self.page += 1

            next_url = 'http://blog.jobbole.com/all-posts/page/' + str(self.page) + '/'
            yield scrapy.Request(next_url, self.parse)
