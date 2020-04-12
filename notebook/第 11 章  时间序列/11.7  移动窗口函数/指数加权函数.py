# @Version : Python3.6
# @Time    : 2018/6/16 18:03
# @Author  : zhcf1ess
# @Site    : 
# @File    : 指数加权函数.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

close_px_all = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]

aapl_px = close_px.AAPL['2006':'2007']
# print(aapl_px)

ma60 = aapl_px.rolling(30, min_periods=20).mean()
# print(ma60)
ewma60 = ma60.ewm(span=30).mean()
# print(ewma60)

ewma60.plot()
ma60.plot()
plt.legend()
plt.show()
