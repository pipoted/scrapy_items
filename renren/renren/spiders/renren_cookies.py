# -*- coding: utf-8 -*-
import scrapy


class RenrenCookiesSpider(scrapy.Spider):
    name = 'renren_cookies'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/968662672']

    cookies = {
        'anonymid': 'joe6opt4-d0oy2b',
        '_r01_': '1',
        'ick': '2efd9950-4e47-4031-93de-71e2c73d38dc',
        'first_login_flag': '1',
        'ln_uact': '15570136250',
        'ln_hurl': 'http://head.xiaonei.com/photos/0/0/men_main.gif',
        'XNESSESSIONID': 'abcgKTG86WdkI7mgyhNNw',
        'jebe_key': '963d46e8-dab7-4ec8-bb65-2a8a65d65182%7C89b3d7f637b5f78fb9f3956fc1562978%7C1554360666592%7C1%7C1554360666599',
        'depovince': 'GW',
        'JSESSIONID': 'abc5JBh9THP-t-H3BhNNw',
        'ick_login': 'aa713d74-7d8e-4834-9d7b-331f1e32b367',
        'wp_fold': '0',
        '_ga': 'GA1.2.402328653.1554365917',
        '_gid': 'GA1.2.1882945675.1554365917',
        'jebecookies': '631b67bb-dda5-4104-b4bb-15409070983d|||||',
        '_de': 'D7A8FABDDE334F652CA6A20317A7565C',
        'p': 'd6c8daab01422b12074891f61278a2682',
        't': '204aaeb7aec6fe169d721af18b8f7f712',
        'societyguester': '204aaeb7aec6fe169d721af18b8f7f712',
        'id': '968662672',
        'xnsid': '188f253a',
        'ver': '7.0',
        'loginfrom': 'null',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_home)

    def parse_home(self, response):
        with open('home.html', 'wb') as fp:
            fp.write(response.body)
