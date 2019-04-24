#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import logging as log
import random


connect = sqlite3.connect('quotescom')
cursor = connect.cursor()
rint = (random.randint(1,101),)
cursor.execute('select QUOTE from QUOTES  where id = ?',rint)
html = cursor.fetchone();
connect.close()

print(html)
print(type(html))
print(type(html[0]))


