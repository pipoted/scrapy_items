# -*- coding: utf-8 -*-
import scrapy


class CsdnCookiesSpider(scrapy.Spider):
    name = 'csdn_cookies'
    allowed_domains = ['www.csdn.net']
    start_urls = ['https://edu.csdn.net/mycollege']

    cookies = {
        'uuid_tt_dd': '10_19293749450-1532423364703-346846',
        'smidV2': '20180816165946ee794a154832ce24c49e1a412bc3b0a000d29d87f092612a0',
        '_ga': 'GA1.2.521141775.1541674991',
        'UM_distinctid': '166f7c648a41ad-097c124168439d-1e396652-13c680-166f7c648a5282',
        'dc_session_id': '10_1544167850677.479857',
        'ARK_ID': 'JS75a9773184ed4c59a9049036f855ffc475a9',
        'UN': 'qq_36940418',
        'ADHOC_MEMBERSHIP_CLIENT_ID1.0': '039131f8-e367-e1df-7000-620aa52c081b',
        'Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac': '1788*1*PC_VC!5744*1*qq_36940418!6525*1*10_19293749450-1532423364703-346846',
        'c-login-auto': '19',
        'TY_SESSION_ID': '41a81609-aa64-4764-b6f9-6c8a4238d952',
        'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac': '1554300542,1554301261,1554310820,1554367625',
        'SESSION': 'f09ccf38-7ff7-496b-9aa1-b233caa4ad8e',
        'Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac': '1554369267',
        'dc_tos': 'ppfj07',
        'UserName': 'qq_36940418',
        'UserInfo': '4650fe97893343d4833b5ef5d530c727',
        'UserToken': '4650fe97893343d4833b5ef5d530c727',
        'UserNick': 'qq_36940418',
        'AU': '31C',
        'BT': '1554369299202',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_home)

    def parse_home(self, response):
        with open('home_csdn.html', 'wb') as fp:
            fp.write(response.body)
