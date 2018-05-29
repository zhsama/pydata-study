# @Version : Python3.6
# @Time    : 2018/5/29 17:45
# @Author  : zhcf1ess
# @Site    : 
# @File    : 相关系数与协方差.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import datetime
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

# all_data = {ticker: web.get_data_yahoo(ticker)
#             for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
# price = pd.DataFrame({ticker: data['Adj   Close']
#                       for ticker, data in all_data.items()})
# volume = pd.DataFrame({ticker: data['Volume']
#                        for ticker, data in all_data.items()})
#
# print(price.pct_change())

# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2013, 1, 27)
# f = web.DataReader('F', 'google', start, end)
# print(f.ix['2010-01-04'])

# start = datetime(2015, 2, 9)
# end = datetime(2017, 5, 24)
# f = web.DataReader('F', 'iex', start, end)