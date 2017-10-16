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

# Correlation and Covariance
returns.MSFT.corr(returns.IBM)
returns.MSFT.cov(returns.IBM)
returns.corr()
returns.cov()

returns.corrwith(returns.IBM)
returns.corrwith(volume)

# Heirarchical Indexing
from pandas import Series
import numpy as np
data = Series(np.random.rand(9),
              index = [['a','a','a','b','b','b','c','c','c'], [1,2,3,1,2,3,1,2,3]])
data2 = Series(np.random.rand(10),
              index = [['a','a','a','b','b','b','c','c','d','d'], [1,2,3,1,2,3,1,2,2,3]])
data2.unstack(fill_value=np.nan).stack()

frame = DataFrame(np.arange(12).reshape(4,3),
                  index=[['a','a','b','b'], [1,2,1,2]],
                  columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame.swaplevel('key1','key2')
frame.swaplevel(0,1).sortlevel(0)
frame.sum(level='key2')
frame.sum(level='color',axis=1)

# Using Columns to set indexes
frame = DataFrame({'a':range(7),
                   'b':range(7,0,-1),
                   'c':['one','one','one','two','two','two','two'],
                   'd':[0,1,2,0,1,2,3]})
frame2 = frame.set_index(['c','d'])
frame.set_index(['c','d'], drop=False)
frame2.reset_index()

# Panel Data
pdata = pd.Panel(dict((stk, web.get_data_google(stk)) for stk in ['AAPL','GOOG','MSFT','DELL']))    # 3-dimensional
pdata=pdata.swapaxes('items','minor')
pdata.ix[:, '11/1/2016', :]
pdata.ix['Close', '11/1/2016':,:]

stacked = pdata.ix[:, '11/1/2016':, :].to_frame()
stacked.to_panel()

