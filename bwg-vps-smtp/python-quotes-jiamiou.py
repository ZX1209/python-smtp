#!/usr/bin/python3
# -*- coding: utf-8 -*-
# /home/gl/python-smtp

import requests
from bs4 import BeautifulSoup
import sqlite3
import logging as log
from string import Template

quoteTemplate = """
<body style="margin-bottom: 60px;">
<div class="quote" style="padding: 10px;margin-bottom: 30px;border: 1px solid #333333;border-radius: 5px;box-shadow: 2px 2px 3px #333333;"itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">
$quote
</span>
<br />
<span>by 
<small class="author" style="font-weight: bold;color: #3677E8;"itemprop="author">
$author
</small>
</span>
</div>
</body>
"""

s = Template(quoteTemplate)


log.basicConfig(format='%(levelname)s: %(message)s\n',level=log.INFO)

connect = sqlite3.connect('quotescom')
cursor = connect.cursor()
# cursor.execute('''CREATE TABLE QUOTES(ID INTEGER PRIMARY KEY NOT NULL,QUOTE VARCHAR(2000));''')

# 
for i in range(0,72):
    response = requests.get('https://www.juzimi.com/writer/%E9%98%BF%E5%B0%94%E8%B4%9D%C2%B7%E5%8A%A0%E7%BC%AA?page='+str(i))
    html = response.text
    soup = BeautifulSoup(html,features="html.parser")
    quotes = soup.select('div.views-field-phpcode-1 a[title="查看本句"]')


    for quote in quotes:
        ts = s.substitute(quote=quote.text,author='阿尔贝·加缪')
        cursor.execute("insert into QUOTES(QUOTE) values(?)", (ts,))
    connect.commit()

    log.info(str(i)+' success')

connect.close()
log.info('finished')