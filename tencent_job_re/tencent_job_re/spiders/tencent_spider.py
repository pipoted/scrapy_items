# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tencent_job_re.items import TencentJobReItem


class TencentSpiderSpider(CrawlSpider):
    name = 'tencent_spider'
    allowed_domains = ['job.tencent.com']
    start_urls = ['https://job.tencent.com/position.php?keywords=&lid=0&tid=0#a']
    page_links = LinkExtractor(allow=('start=\d+'))
    rules = [Rule(page_links, callback='parse_re', follow=True)]

    def parse_re(self, response):
        trs = response.xpath('//tr[@class="odd"]') + response.xpath('//tr[@class="even"]')
        for tr in trs:
            data_dict = TencentJobReItem()
            data_dict['name'] = tr.xpath('./td/a/text()').extract()[0]
            data_dict['types'] = tr.xpath('./td[2]/text()').extract()[0]
            data_dict['nums'] = tr.xpath('./td[3]/text()').extract()[0]
            data_dict['city'] = tr.xpath('./td[4]/text()').extract()[0]

            yield data_dict
