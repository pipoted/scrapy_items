# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from baidubaike.items import BaidubaikeItem


class BaidubaikeSpiderSpider(CrawlSpider):
    name = 'baidubaike_spider'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E7%A4%BE%E4%BC%9A%E5%8F%82%E4%B8%8E/6550778']
    page_links = LinkExtractor(allow=('/item/.*?'))
    rules = [Rule(page_links, callback='parse_baike', follow=True)]

    def parse_baike(self, response):
        data = BaidubaikeItem()
        data['key'] = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').extract()[0]
        data['desc'] = ''.join(response.xpath('//div[@class="lemma-summary"]/div/text()').extract())
        data['url'] = response.url

        yield data

