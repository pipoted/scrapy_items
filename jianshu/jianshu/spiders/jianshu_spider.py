#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from jianshu.items import JianshuItem


class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['https://www.jianshu.com/p/1828ad920ade']
    page_links = LinkExtractor(allow=('/p/.*?'))
    rules = [Rule(page_links, callback='parse_jianshu', follow=True)]

    def parse_jianshu(self, response):
        data = JianshuItem()
        data['title'] = ''.join(response.xpath('//h1[@class="title"]/text()').extract())
        data['pub_time'] = ''.join(response.xpath('//span[@class="publish-time"]/text()').extract())
        data['word_age'] = ''.join(response.xpath('//span[@class="wordage"]/text()').extract()).replace('字数', '').strip()
        data['view_count'] = ''.join(response.xpath('//span[@class="views-count"]/text()').extract()).replace('阅读', '').strip()
        data['comment_count'] = ''.join(response.xpath('//span[@class="comments-count"]/text()').extract()).replace('评论', '').strip()
        data['like_count'] = ''.join(response.xpath('//span[@class="comments-count"]/text()').extract()).replace('喜欢', '').strip()
        data['url'] = response.url

        yield data
