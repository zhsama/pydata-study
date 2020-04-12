# @Version : Python3.6
# @Time    : 2018/6/16 21:44
# @Author  : zhcf1ess
# @Site    : 
# @File    : 用户定义的移动窗口函数.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import percentileofscore

close_px_all = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
spx_px = close_px_all['SPX']
returns = close_px.pct_change()

score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
# print(result)
result.plot()
plt.show()