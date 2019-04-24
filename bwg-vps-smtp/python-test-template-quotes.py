#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fire
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
ts = s.substitute(quote='test quote',author='test author')


