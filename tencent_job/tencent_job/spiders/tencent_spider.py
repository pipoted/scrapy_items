# -*- coding: utf-8 -*-
import scrapy
from tencent_job.items import TencentJobItem


class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent_spider'
    allowed_domains = ['job.tencent.com']
    start_urls = ['https://job.tencent.com/position.php?keywords=python&start={offset}#a'.format(offset=offset * 10) for offset in range(56)]
    # start_urls = ['https://job.tencent.com/position.php?keywords=python&start=0#a']

    def parse(self, response):
        trs = response.xpath('//tr[@class="odd"]') + response.xpath('//tr[@class="even"]')
        for tr in trs:
            data_dict = TencentJobItem()
            data_dict['name'] = tr.xpath('./td/a/text()').extract()[0]
            data_dict['types'] = tr.xpath('./td[2]/text()').extract()[0]
            data_dict['nums'] = tr.xpath('./td[3]/text()').extract()[0]
            data_dict['city'] = tr.xpath('./td[4]/text()').extract()[0]

            yield data_dict
