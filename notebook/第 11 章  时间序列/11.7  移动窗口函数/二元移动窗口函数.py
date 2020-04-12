# @Version : Python3.6
# @Time    : 2018/6/16 18:47
# @Author  : zhcf1ess
# @Site    : 
# @File    : 二元移动窗口函数.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

close_px_all = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
spx_px = close_px_all['SPX']

spx_rets = spx_px.pct_change()  # 计算与之前一个值的百分比状况
# print(spx_px[:5])
# print(spx_rets[:5])

returns = close_px.pct_change()
# print(close_px[:5])
# print(returns[:5])

corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets)
# print(corr)
# corr.plot()
# plt.show()

print(returns.AAPL)
print(spx_rets)