#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:13:53 2017

@author: xuehuachen
"""

import pandas as pd
df = pd.read_csv('ch06/ex1.csv', header=1, index_col='message')
#df.dropna(how='all', inplace=True)
#df.dropna(how='all', axis=1, inplace=True)
pd.read_table('ch06/ex1.csv', sep=',', header=1)

import sys
df.to_csv(sys.stdout, sep='|')
df.to_csv(sys.stdout, sep='|', header=False)

# HTML
from lxml.html import parse
from urllib2 import urlopen
parsed = parse(urlopen('https://finance.yahoo.com/quote/AAPL/options?p=AAPL'))
doc = parsed.getroot()

links = doc.findall('.//a')
lnk = links[28]
lnk.get('href')
lnk.text_content()

urls = [lnk.get('href') for lnk in doc.findall('.//a')]

tables = doc.findall('.//table')
calls = tables[0]
puts = tables[1]
rows = calls.findall('.//tr')

def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]

_unpack(rows[1], kind='th')