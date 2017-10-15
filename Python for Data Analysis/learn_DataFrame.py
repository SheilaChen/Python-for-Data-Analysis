#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:31:39 2017

Examples from the Book Python for Data Analysis, on Data Frames

@author: xuehuachen
"""

from pandas import DataFrame
import pandas as pd
import pandas.io.data as web

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_google(ticker)

price = DataFrame({tic: data['Close'] for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})

returns = price.pct_change()