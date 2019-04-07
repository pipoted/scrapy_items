# -*- coding: utf-8 -*-
import scrapy


class JdLoginSpider(scrapy.Spider):
    name = 'jd_login'
    allowed_domains = ['jd.com']
    start_urls = ['https://order.jd.com/center/list.action']
    cookies = {
        '__jdu': '582778564',
        'shshshfpa': 'ab639f2e-ecdf-3480-9a2d-3ba92e39e9c8-1551170095',
        'shshshfpb': 'a7C47tV9AqBIxImLJ6Xhk%2FQ%3D%3D',
        'areaId': '1',
        '__jda': '122270672.582778564.1550324330.1551170094.1554629390.2',
        '__jdc': '122270672',
        '__jdv': '122270672|direct|-|none|-|1554629389785',
        'PCSYCityID': '1',
        'pin': '%E8%82%96%E8%A7%8173454',
        '_tp': 'W%2B4p%2Bu%2FHoMb6JDnjnXecLFVSUFwOBlpYOx0wZLfii4A%3D',
        '_pst': '%E8%82%96%E8%A7%8173454',
        'unick': '%E8%82%96%E8%A7%8173454',
        'pinId': 'IkT4pOZjb22AjTWOg9u7_g',
        'TrackID': '1Wk9GpBTVT5aEX6bTqstJ_DZu0ebIJanqWIifhtKXL5NUb00MT9PLUwklnEBblnyBzBWFUi8i-ZbaVoOSd7OY0MOggG6xSMJOuqZByvVLsqNEXZfF-l8vhYFsK2fjjJIo',
        'ceshi3.com': '000',
        'user-key': '91d28692-50a7-40c9-8e4d-fb3116291c57',
        'cn': '0',
        'ipLoc-djd': '1-72-2799-0',
        'shshshfp': '3eac930a42d0d5f127cd14ca1fe47c3c',
        'shshshsID': 'd5296721d8a80dc348ca0e4d3ae13a5b_5_1554629627996',
        '3AB9D23F7A4B3C9B': 'Y54QSF55YNJRBKROHGWQ3CWG6N2V6OHUR3SCABHLEW3MY3TKGDNHJDIGPEXCD3WRTLALG3EJ33LI4RDZSNDF2VSYLQ',
        '__jdb': '122270672.13.582778564|2.1554629390',
        'thor': '8218B3D7CD43D23B845DC89A136BA51081A1EEF28047A6FEBE6F249A43EFF75148DB82CFC15F03C36A21515CD55A5FCDB9F92C8725679E773D57BCDB75EEDD247826139CE7CA771B48AFA45C9650E247C7F911482EB2A5DA2C927282DF13A4DC26122A0494AB9220D7C51DE0AD9B2BCBDD428D2D9E6D327F24B7E0DE2F2FA197F83F4DBE3EE4F493016E7A71EF2CB26C',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_jd)

    def parse_jd(self, response):
        with open('jd_login.html', 'wb') as fp:
            fp.write(response.body)
