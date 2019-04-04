# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from douban.items import DoubanItem


class DoubanMovieSpider(CrawlSpider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/30164448/']
    page_links = LinkExtractor(allow=('/subject/\d+/[^\w]'))
    rules = [Rule(page_links, callback='parse_douban', follow=True)]

    def parse_douban(self, response):
        data = DoubanItem()
        info = response.xpath(
            '//div[@class="subject clearfix"]/div[@id="info"]')
        data['name'] = ''.join(response.xpath(
            '//div[@id="content"]/h1//text()').extract()).strip().replace('\n', '')
        data['dire'] = ''.join(info.xpath(
            './span[1]/span[@class="attrs"]/a/text()').extract())
        data['writer'] = ''.join(info.xpath('./span[2]//text()').extract()[2:])
        data['actor'] = ''.join(info.xpath('./span[3]//text()').extract()[2:])
        data['types'] = '/'.join(info.xpath(
            './span[@property="v:genre"]/text()').extract())
        data['area'] = ''.join(info.re('制片国家/地区:</span>(.*?)<br>')).strip()
        data['date'] = '/'.join(info.xpath(
            './span[@property="v:initialReleaseDate"]/text()').extract())
        data['desc'] = ''.join(response.xpath(
            '//div[@class="indent"]/span//text()').extract()).replace('\n', '')
        data['score'] = ''.join(response.xpath('//strong[@class="ll rating_num"]/text()').extract()) + '/' + ''.join(response.xpath(
            '//a[@class="rating_people"]/span/text()').extract())

        yield data
