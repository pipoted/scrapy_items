# -*- coding: utf-8 -*-
import scrapy


class BilibiliMovieSpider(scrapy.Spider):
    name = 'bilibili_movie'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        pass
