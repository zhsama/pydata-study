# @Version : Python3.6
# @Time    : 2018/6/16 17:37
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

close_px_all = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
# print(close_px_all)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
# print(close_px)

# print(close_px.AAPL.plot())
# close_px.AAPL.rolling(250).mean().plot()
# close_px.rolling(60).mean().plot(logy=True)
# plt.show()

appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
expanding_mean = appl_std250.rolling(250).mean()
expanding_mean1 = appl_std250.expanding().mean()
# appl_std250.plot()
expanding_mean.plot()
expanding_mean1.plot()
plt.show()
print(expanding_mean)
print(expanding_mean1)
# print(close_px.rolling('20D').mean())
