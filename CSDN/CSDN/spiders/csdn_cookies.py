# -*- coding: utf-8 -*-
import scrapy


class CsdnCookiesSpider(scrapy.Spider):
    name = 'csdn_cookies'
    allowed_domains = ['www.csdn.net']
    start_urls = ['https://my.csdn.net/my/mycsdn']

    cookies = {
        'uuid_tt_dd': '10_19293749450-1532423364703-346846',
        'smidV2': '20180816165946ee794a154832ce24c49e1a412bc3b0a000d29d87f092612a0',
        '_ga': 'GA1.2.521141775.1541674991',
        'UM_distinctid': '166f7c648a41ad-097c124168439d-1e396652-13c680-166f7c648a5282',
        'dc_session_id': '10_1544167850677.479857',
        'ARK_ID': 'JS75a9773184ed4c59a9049036f855ffc475a9',
        'UN': 'qq_36940418',
        'Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac': '1788*1*PC_VC!5744*1*qq_36940418!6525*1*10_19293749450-1532423364703-346846',
        'c-login-auto': '19',
        'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac': '1554300542,1554301261,1554310820,1554367625',
        'UserName': 'qq_36940418',
        'UserInfo': '227f138c4964426482c2837ff558fab0',
        'UserToken': '227f138c4964426482c2837ff558fab0',
        'UserNick': 'qq_36940418',
        'AU': '31C',
        'BT': '1554372993791',
        'SESSION': '7083a889-e509-410a-9210-c3ccfab490d2',
        'ci_session': 'a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22fd18a42924aca7fd6bd0a8f772d4cfee%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22106.39.149.35%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_14_3%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F72.0.3626.121+Safari%2F537.3%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1554373069%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22userInfo%22%3Bs%3A11%3A%22qq_36940418%22%3B%7Da77b916cbc390aa8eb0291835fbd39f7',
        'Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac': '1554373070',
        'dc_tos': 'ppflxq',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_home)

    def parse_home(self, response):
        with open('home_csdn.html', 'wb') as fp:
            fp.write(response.body)
