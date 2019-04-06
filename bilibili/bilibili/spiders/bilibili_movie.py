# -*- coding: utf-8 -*-
import scrapy


class BilibiliMovieSpider(scrapy.Spider):
    name = 'bilibili_movie'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/movie/index/#area=-1&style_id=-1&year=-1&season_status=-1&order=2&st=2&sort=0&page={page}'.format(page=page) for page in range(1, 58)]

    def parse(self, response):
        pass
