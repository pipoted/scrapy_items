#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree


url = 'https://www.jianshu.com/p/1828ad920ade'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}


content = requests.get(url, headers=headers).content.decode()
print(content)
