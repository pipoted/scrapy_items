# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from bole_spider.items import BoleArticalItem


class BolezaixianSpider(scrapy.Spider):
    name = 'bolezaixian'
    allowed_domains = ['blog.jobble.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        with open('bole.html', 'w') as savefile:
            pagedata = response.body.decode('utf-8', 'ignore')
            savefile.write(pagedata)


            tree = etree.HTML(pagedata)
            divs = tree.xpath('//div[@class="post floated-thumb"]')

            for div in divs:
                data_dict = BoleArticalItem()
                name = div.xpath('./div[@class="post-meta"]/p/a[@class="archive-title"]/@title')[0].strip()
                url = div.xpath('./div[@class="post-meta"]/p/a[@class="archive-title"]/@href')[0].strip()
                data_dict['artical_name'] = name
                data_dict['artical_url'] = url

                yield data_dict
