# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class TaobaoLoginSpider(scrapy.Spider):
    name = 'taobao_login'
    allowed_domains = ['taobao.com']
    start_urls = ['https://login.m.taobao.com/login.htm']

    def __init__(self):
        mobile_setting = {
            'deviceName': 'iPhone 6 Plus'
        }
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_setting)  # 模拟手机登录
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.set_window_size(400, 800)
        super(TaobaoLoginSpider, self).__init__()
        # dispatcher.connect(self.spider_closed, signals.spider_closed)

    # def spider_closed(self):
    #     print('spider is close')
    #     self.browser.close()

    def parse(self, response):
        print(response.url)
        print(response.body.decode())
